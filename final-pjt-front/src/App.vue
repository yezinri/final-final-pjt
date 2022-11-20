<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'movie' }">Home</router-link> |
      <router-link :to="{ name: 'profile', params: { username: userName } }">Profile</router-link> |
      <router-link :to="{ name: 'signup' }">Signup</router-link> |
      <router-link v-if="!isLogin" :to="{ name: 'login' }">Login | </router-link>  
      <router-link :to="{ name: 'selection' }">Selection</router-link> |
      <button v-if="isLogin" @click="logOut">Logout</button>
    </nav>
    <router-view/>
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
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
