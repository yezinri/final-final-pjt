<template>
  <div class="mx-2">
    <div class="row row-cols-3 row-cols-xl-6 g-4">
      <SelectionListItem
        v-for="randomMovie in randomMovies"
        :key="randomMovie.pk"
        :randomMovie="randomMovie.fields"
      />
    </div><br>
    <div class="d-flex justify-content-center">
      <button class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3;" @click="goHome">SAVE</button>
    </div>
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
  },
  methods: {
    goHome() {
      this.$router.push({ name: 'movie' })
    }
  }
  
}
</script>

<style>

</style>