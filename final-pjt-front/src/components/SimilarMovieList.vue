<template>
  <div>
    <h3>비슷한 영화</h3>
    <SimilarMovieListItem
      v-for="similarMovie in similarMovies"
      :key="similarMovie.id"
      :similarMovie="similarMovie"
    />
  </div>
</template>

<script>
import SimilarMovieListItem from '@/components/SimilarMovieListItem'

export default {
  name: 'SimilarMovieList',
  components: {
    SimilarMovieListItem,
  },
  props: {
    similarMovies: Array,
  },
  computed: {
  },
  data() {
    return {

    }
  },
  methods: {
  }
}
</script>

<style>

</style>