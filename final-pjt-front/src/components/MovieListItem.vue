<template>
  <div>
    <h5>{{ movie.title }}</h5>
    <p>{{ movie.id }}</p>
    <router-link :to="{ name: 'detail', params: { id: movie.id } }">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>