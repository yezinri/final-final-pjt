<template>
  <div>
    <h4 class="mb-4" v-if="userData.username == userName">내가 좋아요한 영화</h4>
    <h4 class="mb-4" v-if="userData.username !== userName"><span style="color: #00ABB3;">{{ userData.username }}</span>님이 좋아요한 영화</h4>
    <div class="row row-cols-3 row-cols-xl-6 g-4">
    <LikeMovieListItem
      v-for="likeMovie in userData.like_movies"
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
  data() {
    return {
      userName: this.$store.state.userName,
    }
  },
  props: {
    userData: Object,
  },
}
</script>

<style>

</style>