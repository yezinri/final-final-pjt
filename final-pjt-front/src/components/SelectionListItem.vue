<template>
  <div>
    <div>
      <h5 v-if="randomMovie">{{ randomMovie.title }}</h5>
      <p v-if="randomMovie">{{ randomMovie.movie_id }}</p>
      <p v-if="randomMovie">{{ randomMovie.genre_ids }}</p>
      <p v-if="randomMovie">{{ randomMovie.poster_path }}</p>
    <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SelectionListItem',
  props: {
    randomMovie: Object,
  },
  computed: {

  },
  methods: {
      
    },
  }
</script>

<style>

</style>