<template>
  <div>
    <h4 class="mb-4">비슷한 영화</h4>
    <div class="hover-container g-4">
      <SimilarMovieListItem
        v-for="similarMovie in similarMovies"
        :key="similarMovie.id"
        :similarMovie="similarMovie"
        class="item"
      />
    </div>
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