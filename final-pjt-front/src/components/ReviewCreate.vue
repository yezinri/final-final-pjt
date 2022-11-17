<template>
  <div>
    <h3>리뷰 작성</h3>
    <form @submit.prevent="createReview">
      <label for="content">리뷰 : </label>
      <textarea type="text" id="content" v-model.trim="content"></textarea>
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewCreate',
  data() {
    return {
      content: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    createReview() {
      if (this.isLogin) {
        const content = this.content
        if (!content) {
          alert('내용을 입력해주세요')
          return 
        } 
  
        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.$route.params.id}/reviewcreate/`,
          data: { content },
          headers: {
            Authorization: `Token ${ this.$store.state.token }`
          }
        })
          .then((res) => {
            console.log(res)
            this.$emit('createReview')
            this.content = null
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>

</style>