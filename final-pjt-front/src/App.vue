<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark mb-4">
      <div class="container-fluid px-4 py-2">
        <router-link class="navbar-brand fs-2" style="color: #00ABB3;" :to="{ name: 'movie' }">whyisitreal</router-link>
        <div class="navbar-nav">
          <router-link v-if="isLogin" class="nav-link" :to="{ name: 'profile', params: { username: userName } }">Profile</router-link>
          <router-link v-if="!isLogin" class="nav-link" :to="{ name: 'signup' }">Signup</router-link>
          <router-link v-if="!isLogin" class="nav-link" :to="{ name: 'login' }">Login</router-link>
          <router-link class="nav-link" :to="{ name: 'selection' }">Selection</router-link>
          <span class="nav-link" v-if="isLogin" @click="logOut">Logout</span>
        </div>
      </div>
    </nav>

    <div class="container">
      <router-view/>
    </div>

    <footer class="text-center pt-5">
      <hr>
      <p>copyright@whyisitreal</p>
      <p class="fw-b" style="color: #00ABB3;">whyisitreal</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  // data() {
  //   return {
  //     userName: this.$store.state.userName
  //   }
  // },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userName() {
      return this.$store.state.userName
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
      // this.$router.push({ name: 'movie' })
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');

#app {
  font-family: 'Noto Sans KR', sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: white;
  background-color: #212529;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #00ABB3;
}

.nav-link:hover  {
  color: #00ABB3;
}

.nav-link:focus  {
  color: #00ABB3;
}

.nav-link:active  {
  color: #00ABB3;
}
</style>
