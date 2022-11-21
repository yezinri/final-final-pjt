<template>
  <div>
    <div class="my-3">
      <div class="card">
        <div class="card-body d-flex flex-row justify-content-between">
          <div>
            <h5 class="card-title">
              <router-link v-if="movieTitle" style="text-decoration: none; color: #00ABB3;" :to="{ name: 'detail', params: { movie_id: myReview.movie_id } }">
                {{ movieTitle }}</router-link>
            </h5>
            <p class="card-text text-secondary">{{ myReview.content }}</p>
          </div>
          <div class="d-flex align-items-center">
            <button class="btn btn-primary" style="background-color: #00ABB3; border: #00ABB3;" @click="deleteReview">삭제</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyReviewListItem',
  props: {
    myReview: Object,
  },
  data() {
    return {
      movieTitle: null,
    }
  },
  created() {
    this.getMovieTitle()
  },
  methods: {
    getMovieTitle() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.myReview.movie_id}?api_key=a10047aa70542f33ac2138abb4e13bb7&language=ko-KR`
      })
        .then((res) => {
          // console.log(res.data.title)
          this.movieTitle = res.data.title
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.myReview.movie_id}/reviews/${this.myReview.id}`,
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
  }

}
</script>

<style>

</style>