<template>
  <div class="container-lg mx-3">

    <div class="container-lg row justify-content-evenly pb-5">
      <!-- 프로필 이미지 -->
      <img v-if="!userImage" class="profile-img col-4"
        src="https://www.seekpng.com/png/detail/514-5147412_default-avatar-icon.png" alt="profile_icon">
      <img v-if="userImage" class="profile-img col-4"
        :src="require(`./../../../final-pjt-back/media/${userImage}`)" alt="profile_icon">
      <!-- 내용 -->
      <div class="col-7">
        <h1 v-if="userData" style="color: #00ABB3;">{{ userData.username }}</h1>
        <label
          for="image_input"
          class="btn btn-primary mb-2 me-1"
          style="color: #00ABB3; background-color: white; border: white;" 
        >프로필 편집</label>
        <input
          v-show="false"
          @change="getProfileImage" 
          type="file"
          id="image_input" 
        >
        <button
          @click="changeProfileImage"
          class="btn btn-primary mb-2"
          style="color: #00ABB3; background-color: white; border: white;" 
        >편집 완료</button>
      </div>
    </div>

    <hr>
    
    <div class="container-lg py-5">
      <LikeMovieList :userData="userData"/><br><br>
      <MyReviewList :userData="userData" @deleteReview="getProfile"/>
    </div>
  </div>
  
    <!-- <div>
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
      >변경하기</button>
    </div> -->
    <!-- 민혁 추가 부분 -->


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
      userImage: 'profiles/default.png', // 11.24 추가
      showvalue: false,
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
          console.log(res)
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
    getProfileImage(event) {
      console.log(event.target.files)
      this.userImage = event.target.files
      this.showvalue = !this.showvalue
      // console.log(this.userImage)
    },
    // 프로필 이미지 변경
    changeProfileImage() {
      // 이미지를 선택하지 않았을 경우 경고창
      if (this.userImage === null) {
        alert('변경할 프로필 사진을 선택하세요.')
      } else {
        const payload = {
          userImage: this.userImage,
          userId: this.userData.userid
        }
        this.$store.dispatch('changeProfileImage', payload)
      }
      console.log(this.userImage)
      this.showvalue = !this.showvalue
       
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
.profile-img {
  width: 350px;
  border-radius: 100%;
  border-image-slice: 100;
}
</style>

