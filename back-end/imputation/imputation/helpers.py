from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import json, urllib
from django.conf import settings

KAFKA_BOOTSTRAP_SERVERS = settings.KAFKA_BOOTSTRAP_SERVERS
KAFKA_SCHEMA_REGISTRY = settings.KAFKA_SCHEMA_REGISTRY
TOPIC=settings.TOPIC

def messageRun(user_id, project_id, input, valueSet):
    try:
        topic = TOPIC

        def delivery_report(err, msg):
            """ Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush(). """
            if err is not None:
                print('Message delivery failed: {}'.format(err))
            else:
                print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

        conf = {
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
            "on_delivery": delivery_report,
            "schema.registry.url": KAFKA_SCHEMA_REGISTRY
        }

        print(KAFKA_SCHEMA_REGISTRY)
        def getSchema(urls):           
            with urllib.request.urlopen(f'{urls}/latest/schema/') as url:
                schema = json.loads(url.read().decode())
            return json.dumps(schema)
        
        value_schema = avro.loads(getSchema(f'{KAFKA_SCHEMA_REGISTRY}/subjects/{topic}-value/versions'))
        key_schema = avro.loads(getSchema(f'{KAFKA_SCHEMA_REGISTRY}/subjects/{topic}-key/versions'))
        avroProducer = AvroProducer(conf, default_key_schema=key_schema, default_value_schema=value_schema)

            
        
        keySet = {
            'projectId': str(project_id),
            'userId': str(user_id),
            # 'runId': str(uuID),
            'priority': 'LOW',
            'sampleIds': [],
        } 

        # valueSet['input'] = f's3://{settings.MINIO_STORAGE_MEDIA_BUCKET_NAME}/{user_id}/{project_id}/input'
        valueSet['input'] = f's3://{settings.MINIO_STORAGE_MEDIA_BUCKET_NAME}/{input}/input'
        # valueSet = {
        #     'input': f's3://imputation/{user_id}/{project_id}/input',
        #     'inputtype' : 'bedbimfam',
        #     'mafvalue': 0.30,
        #     'buildversion': 'hg38'
        # }
            
        print('Topic ##########################')
        print('test')
        print('keySet #########################')
        print(keySet)
        print('valueSet #######################')
        print(valueSet)
        avroProducer.produce(topic=TOPIC, key=keySet, value=valueSet)
        avroProducer.poll(0)
        avroProducer.flush()
        return None

    except Exception as e:
        return str(e)