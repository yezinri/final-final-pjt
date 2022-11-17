<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'movie' }">Home</router-link> |
      <router-link :to="{ name: 'signup' }">Signup</router-link> |
      <router-link :to="{ name: 'login' }">Login</router-link> |
      <button v-if="isLogin" @click="logOut">Logout</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
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
