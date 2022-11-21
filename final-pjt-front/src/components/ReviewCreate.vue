<template>
  <div>
    <form @submit.prevent="createReview">
      <label class="fs-3 mb-2" for="content">Review</label>
      <div class="d-flex flex-row">
        <textarea class="form-control me-1" type="text" id="content" v-model.trim="content" placeholder="리뷰를 작성하세요"></textarea>
        <input class="btn btn-primary" style="background-color: #00ABB3; border: #00ABB3;" type="submit" value="작성">
      </div>
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
          url: `${API_URL}/movies/${this.$route.params.movie_id}/reviewcreate/`,
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