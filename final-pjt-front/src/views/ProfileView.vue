<template>
  <div>
    <h1>ProfileView</h1>
    <h2 v-if="userData">{{ userData.username }}</h2>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      userData: null,
    }
  },
  created() {
    this.getProfile()
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`
      })
        .then((res) => {
          // console.log(res.data)
          this.userData = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
  
}
</script>

<style>

</style>

