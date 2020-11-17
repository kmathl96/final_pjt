<template>
  <div>
    
    <h1>회원가입</h1>
    <p>아이디</p>
    <input v-model='signupInfo.username' type="text" class="form-control">
    <p>비밀번호</p>
    <input v-model='signupInfo.password1' type="password" class="form-control">
    <p>비밀번호 확인</p>
    <input v-model='signupInfo.password2' type="password" class="form-control">
    <br>
    <!-- <p v-for="genre in genre_list" :key="genre.id" >{{gcinputt(genre)}}</p> -->
    <button @click="SignupSubmit" class="btn btn-info">signup</button>
  </div>
</template>

<script>
// const API_BASE_URL = 'http://localhost:8000'
export default {
  name: 'SignupView',
  data() {
    return{
      signupInfo : {
        username: '',
        password1: '',
        password2: '',
      },
      // genre_list: [],
      // genrecountlist: [],
      // genrecountInfo :{
      //   username: '',
      //   genre: '',
      //   sum_rate: 0,
      //   count: 0
      // }
  }
},
methods:{
  SignupSubmit() {
    if(this.signupInfo.password1==this.signupInfo.password2){
    this.$emit('signupsubmit',this.signupInfo)
    // this.genrecountlist.push({username:this.signupInfo.username})
    //  this.$emit('signupsubmit',this.genrecountlist)
    }
    else {
      alert("비밀번호를 일치시켜주세요")
      }
    },
  // fetchGenreList() {
  //     const API_GENRE_LIST_URL = API_BASE_URL + '/movies/genreinput/'
  //     const config = {}
  //     this.$axios.get(API_GENRE_LIST_URL, config)
  //       .then(res => {
  //         this.genre_list = res.data
  //       })
  //       .catch(err => {
  //         console.error(err)
  //       })
  //   },
  // gcinputt(genre) {
  //   this.genrecountInfo.genre = this.genre.id
  //   this.genre= genre.id
  //   this.sum_rate= 0
  //   this.count= 0

  //   this.genrecountlist.push(this.genrecountInfo)
  // },
  },
  // created() {
  //   this.fetchGenreList()
  // },

}
</script>

<style>

</style>