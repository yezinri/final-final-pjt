<template>
  <div class="mx-2">
    <div class="row row-cols-3 row-cols-xl-6 g-4">
      <SelectionListItem
        v-for="randomMovie in randomMovies"
        :key="randomMovie.pk"
        :randomMovie="randomMovie.fields"
      />
    </div><br>
    <div class="d-flex justify-content-center sticky-bottom">
      <button class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3; height: 70px; width: 350px; box-shadow: 0 4px 4px -2px black;" @click="goHome">영화 추천받으러 가기</button>
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