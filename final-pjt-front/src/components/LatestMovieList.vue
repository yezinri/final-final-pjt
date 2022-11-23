<template>
  <div class="mx-3">
    <h4 class="mb-4">최신 영화</h4>
    <div class="hover-container g-4">
      <LatestMovieListItem
        v-for="latestMovie in latestMovies"
        :key="latestMovie.id"
        :latestMovie="latestMovie"
        class="item"
      />
    </div>
  </div>
</template>

<script>
import LatestMovieListItem from '@/components/LatestMovieListItem'

export default {
  name: 'LatestMovieList',
  components: {
    LatestMovieListItem,
  },
  computed: {
    latestMovies() {
      return this.$store.state.latestMovies
    }
  }
}
</script>

<style>
.hover-container {
  display: flex;
  padding: 0px;
}

.item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
  margin-left: 2px;
  margin-right: 2px;
}

.hover-container:focus-within .item,
.hover-container:hover .item {
  transform: translateX(-25%);
}

.item:focus ~ .item,
.item:hover ~ .item {
  transform: translateX(25%);
}

.hover-container .item:focus,
.hover-container .item:hover {
  transform: scale(1.5);
  z-index: 1;
}

.item img {
  display: block;
  max-width: 100%;
}
</style>