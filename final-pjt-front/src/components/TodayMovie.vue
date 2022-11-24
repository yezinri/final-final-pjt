<template>
  <div class="mx-3">
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <div class="row justify-content-center">
            <div class="col-9">
              <h5><span class="fs-bold" style="color: #00ABB3;">{{ userName }}</span>님 안녕하세요</h5>
              <h4 class="mb-4">오늘 <span style="color: #00ABB3;">{{ todayMovie.title }}</span> 한편 어떠세요?</h4>
            </div>
          </div>
          <router-link style='text-decoration: none;' :to="{ name: 'detail', params: { movie_id: todayMovie.movie_id } }">
            <div class="row justify-content-center">
              <img class="col-3 mt-0 g-4" style="height: 10%" :src="todayMovieSrc" :alt="todayMovie.title">
              <div class="col-6 mt-auto">
                <p class="fw-lighter word">{{ todayMovie.overview }}</p>
              </div>
            </div>
          </router-link>
        </div>
        <div class="carousel-item" data-bs-interval="10000">
          <div class="row justify-content-center">
            <div class="col-9">
              <h4 class="mb-4">이런 영화도 있어요!</h4>
            </div>
          </div>
          <router-link style='text-decoration: none;' :to="{ name: 'detail', params: { movie_id: todayMovie.movie_id } }">
            <div class="row justify-content-center">
              <img class="col-3 mt-0 g-4" style="height: 10%" :src="worstMovieSrc" :alt="worstMovie.title">
              <div class="col-6 mt-auto">
                <p class="fw-lighter word">{{ worstMovie.overview }}</p>
              </div>
            </div>
          </router-link>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
  
</template>

<script>
export default {
  name: 'TodayMovie',
  data() {
    return {
      userName: this.$store.state.userName,
    }
  },
  computed: {
    todayMovie() {
      return this.$store.state.todayMovie
    },
    worstMovie() {
      return this.$store.state.worstMovie
    },
    todayMovieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.todayMovie.poster_path}`
      return movieSrc
    },
    worstMovieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.worstMovie.poster_path}`
      return movieSrc
    },
    todaybackdroppath() {
      return 'https://image.tmdb.org/t/p/original' + this.$store.state.todayMovie.backdrop_path
    },
    worstbackdroppath() {
      return 'https://image.tmdb.org/t/p/original' + this.$store.state.worstMovie.backdrop_path
    },
  },

}
</script>

<style>
.word {
    color: white;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: normal;
    text-align: left;
    word-wrap: break-word;
    display: -webkit-box;
    -webkit-line-clamp: 3 ;
    -webkit-box-orient: vertical;
}
</style>