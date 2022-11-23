<template>
  <div>
    <form @submit.prevent="updateReview">
      <!-- <label class="fs-3 mb-2" for="content">Review Update</label> -->
      <div class="d-flex flex-row">
        <input class="form-control me-1" type="text" id="content" v-model.trim="content">
        <input class="btn btn-primary" style="background-color: #00ABB3; border: #00ABB3;" type="submit" value="수정 완료">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewUpdateForm',
  data() {
    return {
      content: this.beforeReview.content,
    }
  },
  props: {
    beforeReview: Object,
  },
  methods: {
    updateReview() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요')
        return 
      } 

      axios({
        method: 'put',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/${this.beforeReview.id}/`,
        data: { content },
        headers: {
          Authorization: `Token ${ this.$store.state.token }`,
        }
      })
        .then((res) => {
          console.log('실행')
          this.$emit('updateReview')
          console.log(res)
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