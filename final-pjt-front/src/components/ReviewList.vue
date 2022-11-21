<template>
  <div>
    <ReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
      @deleteReview="deleteReview"
    />
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  props: {
    reviews: Array,
  },
  methods: {
    deleteReview() {
      this.$emit('deleteReview')
    }
  }
}
</script>

<style>

</style>