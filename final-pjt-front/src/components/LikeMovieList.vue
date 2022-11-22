<template>
  <div>
    <h4 class="mb-4">내가 좋아요한 영화</h4>
    <div class="row row-cols-3 row-cols-xl-6 g-4">
    <LikeMovieListItem
      v-for="likeMovie in likeMovies"
      :key="likeMovie.pk"
      :likeMovie="likeMovie"
    />
    </div>
  </div>
</template>

<script>
import LikeMovieListItem from '@/components/LikeMovieListItem'

export default {
  name: 'LikeMovieList',
  components: {
    LikeMovieListItem,
  },
  props: {
    likeMovies: Array,
  },
}
</script>

<style>

</style>