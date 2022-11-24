<template>
  <div class="mx-3">
    <!-- 이미지 노출 - 민혁 -->
    <img 
      v-if="userImage"
      :src="require(`./../../../final-pjt-back/media/${userImage}`)" alt="profile_icon">
<!-- <img 
      v-if="!userImage"
      :src="firstImage" alt="profile_icon"> -->
    <!-- 민혁 추가 부분 -->
    <div>
      <div>
        <label class="profile-label" for="image_input"><b>여기</b></label>
        <span>를 누르고 사용할 프로필 사진을 선택하세요.</span>
      </div>
      <input 
        @change="getProfileImage" 
        type="file"
        id="image_input" 
        style="visibility:hidden;"
      >
      <button
         @click="changeProfileImage"
          class='rounded' 
          style="color: white; border:none; background:#4589ef; width:20%;"
      >
        변경하기
      </button>

    </div>
    <!-- 민혁 추가 부분 -->

    <h2 v-if="userData" style="color: #00ABB3;">{{ userData.username }}</h2><br>
    <LikeMovieList :userData="userData"/><br>
    <MyReviewList :userData="userData" @deleteReview="getProfile"/>
  </div>
</template>

<script>
import axios from 'axios'
import LikeMovieList from '@/components/LikeMovieList'
import MyReviewList from '@/components/MyReviewList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    LikeMovieList,
    MyReviewList,
  },
  data() {
    return {
      userData: null,
      userImage: 'profiles/facebook.png', // 11.24 추가
    }
  },
  created() {
    this.getProfile()
    // this.showProfileImage() // 11.24
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.username}/`
      })
        .then((res) => {
          // console.log(res.data)
          this.userData = res.data
          // console.log(this.userData)
        })
        .then(() => {
          this.showProfileImage()
        })

        .catch((err) => {
          console.log(err)
        })
    },
    getProfileImage() {
      // console.log(event.target.files)
      this.userImage = event.target.files
      // console.log(this.userImage)
    },
    // 프로필 이미지 변경
    changeProfileImage() {
      // 이미지를 선택하지 않았을 경우 경고창
      // if (this.userImage === null) {
      //   alert('변경할 프로필 사진을 선택하세요.')
      // } else {
        const payload = {
          userImage: this.userImage,
          userId: this.userData.userid
        }
        console.log(this.userImage)
       
        this.$store.dispatch('changeProfileImage', payload)
      //   this.userImage = null
      // }
    },
    showProfileImage() {
      // DB에 저장된 이미지를 보여줌
      // this.$store.dispatch('showProfileImage')
      console.log(this.userData)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/show_image/${this.userData.userid}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.userImage = res.data
          console.log(this.userImage)
  
        })
        // .catch((err) => {
        //   if (err.response.status === 404) {
        //     this.similarMovies = null
        //   }
        // })
    }
  }
  
}
</script>

<style>

</style>

