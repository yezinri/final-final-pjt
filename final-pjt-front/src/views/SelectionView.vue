<template>
  <div>
    <h3 class="text-center mb-5">
      <span style="color: #00ABB3;">{{ userName }}</span>님이 재밌게 본 영화를 골라주세요
    </h3>
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
  created() {
    this.randomMovies()
  },
  computed: {
    userName() {
      return this.$store.state.userName
    }
  },
  methods: {
    randomMovies() {
      this.$store.dispatch('randomMovies')
    }
  }
}

</script>

<style>

</style>