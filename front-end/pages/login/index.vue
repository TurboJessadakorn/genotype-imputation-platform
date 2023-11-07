<template>
    <section class="bg-gray-50">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <div class="w-full flex justify-center">
                        <img class="w-56 h-56" src="NBT-circle.png">
                    </div>
                    <h1 class="text-xl text-cyan-700 font-bold leading-tight tracking-tight md:text-2xl text-center">
                        Genotype Imputation Platform
                    </h1>
                    <form class="space-y-4 md:space-y-6" action="#">
                        <button @click="keycloak()" type="submit" class="w-full text-white bg-cyan-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Login</button>
                        <p class="text-sm font-light text-gray-500">
                            Don't have an account yet? <a href="https://accounts.nbt.or.th" target="_blank" class="font-medium text-primary-600 hover:underline">Sign up</a>
                        </p>
                    </form>
                    
                </div>
            </div> 
        </div>
    </section>
</template>

<script>
export default {
    layout:'empty',
    methods: {
        async keycloak() {
            // alert('Test')
            try{
                let auth0 = await this.$auth.loginWith('keycloak')
                console.log(auth0)
            }catch (err){
                console.log(err)
            }
        }
    },
    
}
</script>