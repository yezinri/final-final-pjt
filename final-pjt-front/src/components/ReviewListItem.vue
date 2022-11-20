<template>
  <div>
    <span><router-link :to="{ name: 'profile', params: { username: review.username } }">{{ review.username }}</router-link></span>
    <span> : {{ review.content }}</span>
    <button @click="deleteReview">삭제</button>
    <button
      :id="'like-btn-' + review.id"
      v-if="!isLike" @click="reviewLike">좋아요</button>
    <button 
      :id="'like-btn-' + review.id"
      v-if="isLike" @click="reviewLike">좋아요 취소</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  data() {
    return {
      userId: null,
    }
  },
  compunted: {
  },
  props: {
    review: Object,
  },
  created() {
    this.getId()
  },
  computed: {
    isLike: {
      get() {
        // console.log(this.review)
        return this.review.like_users?.includes(this.userId)
      },
      set() {

      }
    }
  },
  methods: {
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/${this.review.id}`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)  
          this.$emit('deleteReview')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    reviewLike() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/${this.review.id}/likes/`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          console.log(res)
          const likeBtn = document.querySelector(`#like-btn-${this.review.id}`);

          if (res.data.is_like === true) {
            likeBtn.innerText = '좋아요 취소'
          } else {
            likeBtn.innerText = '좋아요'
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getId() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
            Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          this.userId = res.data.pk
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