<template>
  <div>
    <h1>SelectionList</h1>
    <SelectionListItem
      v-for="randomMovie in randomMovies"
      :key="randomMovie.id"
      :randomMovie="randomMovie.fields"
    />
  </div>
</template>

<script>
import SelectionListItem from '@/components/SelectionListItem'

export default {
  name: 'SelectionList',
  components: {
    SelectionListItem,
  },
  computed: {
    randomMovies() {
      console.log(this.$store.state.randomMovies)
      return this.$store.state.randomMovies
    }
  }
  
}
</script>

<style>

</style>