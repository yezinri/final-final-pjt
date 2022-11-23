<template>
  <div class="mx-3">
    <h4 class="mb-4"><span style="color: #00ABB3;">{{ searchWord }}</span>에 대한 검색 결과입니다</h4>
    <div class="row row-cols-3 row-cols-xl-6 g-4">
      <SearchMovieListItem
        v-for="searchMovie in searchMovies"
        :key="searchMovie.id"
        :searchMovie="searchMovie"
      />
    </div>
  </div>
</template>

<script>
import SearchMovieListItem from '@/components/SearchMovieListItem'

export default {
  name: 'SearchMovieList',
  components: {
    SearchMovieListItem,
  },
  computed: {
    searchMovies () {
      // console.log(this.$store.state.searchMovies)
      return this.$store.state.searchMovies
    },
    searchWord () {
      return this.$store.state.searchWord
    }
  },
}
</script>

<style>

</style>