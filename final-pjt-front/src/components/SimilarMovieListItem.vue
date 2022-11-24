<template>
  <div>
    <div>
      <router-link :to="{ name: 'detail', params: { movie_id: similarMovie.id } }">
        <div class="swiper-slide">
          <img :src="movieSrc" class="card-img-top" :alt="similarMovie.title">
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SimilarMovieListItem',
  props: {
    similarMovie: Array,
  },
  computed: {
    movieSrc() {
      const movieSrc = `https://image.tmdb.org/t/p/original/${this.similarMovie.poster_path}`
      return movieSrc
    }
  },
}
</script>

<style>

</style>