<template>
  <div>
    <h1>Selection View</h1>
    <SelectionList/>
  </div>
</template>


<script>
import SelectionList from '@/components/SelectionList'

export default {
  name: 'SelectionView',
  components: {
    SelectionList,
  },
  data() {
    return {
    }
  },
  created() {
    console.log('created')
    this.randomMovies()
  },
  methods: {
    randomMovies() {
      console.log('methods')
      this.$store.dispatch('randomMovies')
    }
  }
}

</script>

<style>

</style>