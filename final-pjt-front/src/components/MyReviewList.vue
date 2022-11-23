<template>
  <div>
    <h4 v-if="userData.username == userName">내가 쓴 리뷰</h4>
    <h4 v-if="userData.username !== userName"><span style="color: #00ABB3;">{{ userData?.username }}</span>님이 쓴 리뷰</h4>
    <MyReviewListItem
      v-for="myReview in userData.my_reviews"
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
    userData: Object,
  },
  data() {
    return {
      userName: this.$store.state.userName,
    }
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