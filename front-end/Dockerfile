# Dockerfile
FROM node:18.16.0-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project to the container
COPY . .

# Build the Nuxt.js application
RUN npm run build

# Expose the port on which the application will run
EXPOSE 4000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=4000

# Set the command to run the application
# CMD [ "npm", "start" ]
