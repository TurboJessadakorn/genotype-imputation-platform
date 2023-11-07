export default async function ({ $axios, redirect, app }) {
    try {
      const email = app.$auth.user.email;
      const response = await $axios.get(`/useremail/${email}`)
      const userData = response.data
  
      if (userData.role === 'admin') {
  
      } else {
        redirect('/unauthorized')
      }
    } catch (error) {
      console.log(error)
    }
  }