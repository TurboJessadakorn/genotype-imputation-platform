<template>
    <section class="bg-gray-50">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 sm:px-12 items-center">
                    <div class="flex justify-center">
                        <font-awesome-icon :icon="['fasr', 'circle-xmark']" size="2xl" color="#b91c1c"/>
                    </div>
                    <div class="space-y-2">
                        <h1 class="text-xl text-red-700 font-bold leading-tight tracking-tight md:text-2xl text-center">
                        Access denied
                         </h1>
                        <h1 class="text-md text-center">
                            To access this page you need to have an approval of the admin first
                        </h1>
                    </div>
                    <div class="flex justify-center">
                        <NuxtLink to="/" class="text-white bg-red-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-md text-sm px-8 py-2.5 text-center">
                            <span class="flex-1">Go To Homepage</span>
                        </NuxtLink>
                    </div>
                </div>
            </div> 
        </div>
    </section>
</template>
   
<script>
export default {
    middleware:'auth',
    layout:'empty'
}
</script>
   
   