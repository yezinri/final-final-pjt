<template>
  <div>
    <div class="container" style="width: 400px; backgrount-color: white;">
      <h1 class="text-center" style="color: #00ABB3;">Sign Up</h1><br>
      <hr class="mx-auto" style="color: #00ABB3;">
      <div class="mx-auto" style="width: 300px;">
        
        <form @submit.prevent="signUp">
          <div class="mb-3">
            <label for="username" class="form-label">username</label>
            <input type="text" class="form-control" id="username" v-model="username">
          </div>
          <div class="mb-3">
            <label for="password1" class="form-label">Password</label>
            <input type="password" class="form-control" id="password1" v-model="password1">
          </div>
          <div class="mb-3">
            <label for="password2" class="form-label">Password confirmation</label>
            <input type="password" class="form-control" id="password2" v-model="password2">
          </div><br>
          <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-primary" style="background-color: #00ABB3; border: #00ABB3;">Sign Up</button>
          </div>
        </form>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>

</style>