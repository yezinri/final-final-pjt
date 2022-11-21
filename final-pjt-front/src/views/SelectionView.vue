<template>
  <div>
    <h3 class="text-center">재밌게 봤던 영화를 선택하세요</h3><br>
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