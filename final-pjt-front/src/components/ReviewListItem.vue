<template>
  <div class="my-3">
    <div class="card">
      <div class="card-body d-flex flex-row justify-content-between">
        <div>
          <h5 class="card-title">
            <router-link style="text-decoration: none; color: #00ABB3;" :to="{ name: 'profile', params: { username: review.username } }">
              {{ review.username }}</router-link>
          </h5>
          <p v-if="!toggleStatus" class="card-text text-secondary">{{ review.content }}</p>
          <ReviewUpdateForm v-if="toggleStatus" :beforeReview="review" @updateReview="updateReview" />
        </div>
        <div class="d-flex align-items-center">
          <div v-if="userId !== review.user">
            <button
              :id="'like-btn-' + review.id"
              v-if="!isLike" @click="reviewLike"
              class="btn btn-primary me-1" style="background-color: #00ABB3; border: #00ABB3;">좋아요</button>
            <button 
              :id="'like-btn-' + review.id"
              v-if="isLike" @click="reviewLike"
              class="btn btn-primary me-1" style="background-color: #00ABB3; border: #00ABB3;">좋아요 취소</button>
          </div>
          <button id="updateBtn" v-if="userId == review.user" class="btn btn-primary me-1" style="background-color: #00ABB3; border: #00ABB3;" @click="toggleOnOff">수정</button>
          <button v-if="userId == review.user" class="btn btn-primary" style="background-color: #00ABB3; border: #00ABB3;" @click="deleteReview">삭제</button>
        </div>
      </div>
      <!-- <star-rating v-model="rating" :increment=0.5 animate=true></star-rating> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewUpdateForm from '@/components/ReviewUpdateForm'
// import StarRating from 'vue-star-rating'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  // components: {
  //   StarRating
  // },
  data() {
    return {
      userId: null,
      toggleStatus: false,
      // rating: 0,
    }
  },
  components: {
    ReviewUpdateForm,
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
    },
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/${this.review.id}`,
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
    updateReview() {
      this.toggleOnOff()
      console.log('에밋 성공')
      this.$emit('updateReview')
    },
    toggleOnOff() {
      const updateBtn = document.querySelector('#updateBtn')

      if (!this.toggleStatus) {
        updateBtn.innerText = '수정 취소'
      } else {
        updateBtn.innerText = '수정'
        // this.$refs.updateRequest.updateReview('')
      }

      this.toggleStatus = !this.toggleStatus
    },
    reviewLike() {
      if (this.isLogin) {
        axios({
          method: 'post',
          url: `${API_URL}/movies/${this.$route.params.movie_id}/reviews/${this.review.id}/likes/`,
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
      } else {
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'login' })
      }
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