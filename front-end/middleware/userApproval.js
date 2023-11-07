export default async function ({ $axios, redirect, app, store }) {
  try {
    const email = app.$auth.user.email;
    const response = await $axios.get(`/useremail/${email}`)
    const userData = response.data
    store.dispatch('setUserId', userData.user_id);
    if (userData.approval === 'approved') {
      store.dispatch('setUserId', userData.user_id);
    } else {
      redirect('/unauthorized')
    }
  } catch (error) {
    console.log(error)
  }
}