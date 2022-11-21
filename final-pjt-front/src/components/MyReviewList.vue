<template>
  <div>
    <h4>내가 쓴 리뷰</h4>
    <MyReviewListItem
      v-for="myReview in myReviews"
      :key="myReview.pk"
      :myReview="myReview"
      @deleteReview="deleteReview"
    />
  </div>
</template>

<script>
import MyReviewListItem from '@/components/MyReviewListItem'

export default {
  name: 'MyReviewList',
  components: {
    MyReviewListItem
  },
  props: {
    myReviews: Array,
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