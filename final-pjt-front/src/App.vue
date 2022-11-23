<template>
  <div id="app" :style="{ backgroundImage: 'linear-gradient(to bottom, rgba(0, 0, 0, 0.6) 10%, rgba(0, 0, 0, 0.7) 25%, rgba(0, 0, 0, 0.8) 50%, rgba(0, 0, 0, 0.9) 75%, rgba(0, 0, 0, 1) 100%), url(' + backdroppath + ')', backgroundSize: 'cover' }">
    <nav class="navbar navbar-expand navbar-dark mb-4">
      <div class="container-fluid px-4 py-2">
        <router-link class="navbar-brand fs-2" style="color: #00ABB3;" :to="{ name: 'movie' }">whyisitreal</router-link>
        <div class="navbar-nav">
          <router-link v-if="!isLogin" class="nav-link" :to="{ name: 'signup' }">Signup</router-link>
          <router-link v-if="!isLogin" class="nav-link" :to="{ name: 'login' }">Login</router-link>
          <span class="nav-link" v-if="isLogin" @click="logOut">Logout</span>
          <router-link v-if="isLogin" class="nav-link fw-bold" style="color: #00ABB3;" :to="{ name: 'profile', params: { username: userName } }">{{ userName }}</router-link>
          <form class="d-flex ms-2" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" @keyup="searchMovie">
          </form>
        </div>
      </div>
    </nav>

    <div class="container-lg" style="min-height: 100%;">
      <router-view id="fade"/>
    </div>

    <footer class="text-center pb-2">
      <hr>
      <p>copyright@whyisitreal</p>
      <p class="fw-b" style="color: #00ABB3;">whyisitreal</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      // userName: this.$store.state.userName,
      // searchword: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userName() {
      return this.$store.state.userName
    },
    movieNow() {
      return this.$store.state.movieNow
    },
    backdroppath() {
      return 'https://image.tmdb.org/t/p/original' + this.$store.state.backdropPath
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
      // this.$router.push({ name: 'movie' })
    },
    searchMovie(event) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/search/${event.target.value}/`,
      })
        .then((res) => {
          if (this.$route.path !== '/search') {
            this.$router.push({ name: 'search' })
          }
          this.$store.commit('SEARCH_MOVIE', [res.data, event.target.value])
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
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
  height: 100%;
  /* background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.6) 10%,
    rgba(0, 0, 0, 0.7) 25%,
    rgba(0, 0, 0, 0.8) 50%,
    rgba(0, 0, 0, 0.9) 75%,
    rgba(0, 0, 0, 1) 100%
  ), url(https://image.tmdb.org/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg);
  background-size: cover; */
}

#fade {
  animation: fadein 5s ease 3s;
  -webkit-animation: fadein 3s; /* Safari and Chrome */
}

@keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@-webkit-keyframes fadein { /* Safari and Chrome */
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
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
  color: black
}
</style>
