<template>
  <div>
    <div class="container" style="width: 400px; backgrount-color: white;">
      <h2 class="text-center" style="color: #00ABB3;">Login</h2>
      <hr class="mx-auto" style="width: 50px; border: 0; height: 5px; background: #00ABB3;">
      <div class="mx-auto" style="width: 250px;">
        
        <form @submit.prevent="logIn">
          <div class="mb-3">
            <label for="username" class="form-label">username</label>
            <input type="text" class="form-control" id="username" v-model="username">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" v-model="password">
          </div><br>
          <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-primary" style="background-color: #00ABB3; border: #00ABB3;">Login</button>
          </div>
        </form>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
  }
}
</script>

<style>

</style>