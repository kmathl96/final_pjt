<template>
  <div id="app">
    <nav class="navbar fixed-top navbar-expand-lg navbar-info bg-info">
      <router-link class="navbar-brand" to="/" ><img src="../src/assets/crown.png" width="30" height="30" alt="" loading="lazy"></router-link>
      <div>
        <ul class="d-flex justify-content-end m-0" style="list-style:none;">
          <li class="nav-item">
            <router-link class="nav-link text-white" v-if="isLoggedIn" to="/community"><i class="fas fa-edit"></i></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-white" v-if="!isLoggedIn" to="/signup"><i class="fas fa-user-plus"></i></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-white" v-if="!isLoggedIn" to="/login"><i class="fas fa-sign-in-alt"></i></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-white" v-if="isLoggedIn" @click.native="logout" to="/logout"><i class="fas fa-sign-out-alt"></i></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-white" v-if="isLoggedIn" to="/movierecommend"><i class="fas fa-video"></i></router-link>
          </li>
          <li class="nav-item">
            <button @click="darkThemeSwitch" class="btn" :class="{'text-dark': this.darkmode, 'text-white': !this.darkmode}"><i class="fas fa-moon"></i></button>
          </li>
          <!-- <li class="nav-item dropdown">
            <div  class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-toggle="dropdown"></div>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <div class="dropdown-item" @click="darkmode(true)"><i class="fas fa-moon"></i></div>
              <div class="dropdown-item" @click="darkmode(false)"><i class="fas fa-sun"></i></div>
            </div>
          </li> -->
        </ul>
      </div>
    </nav>
<!-- <p v-for="genre in genre_list" :key="genre.id" >{{gcinputt(genre.id)}}</p> -->
    <div class="p-5 m-5">
      <router-view
        @loginsubmit="login"
        @signupsubmit="signup"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL= 'http://localhost:8000'

export default {
  name: 'App',
  data() {
    return{
      isLoggedIn: false,
      genre_list: [],
      genrecountlist: [],
      genrecountInfo :{
        username: '',
        genre: '',
        sum_rate: 0,
        count: 0
      },
      darkmode: false,
    }
  },
 methods: {
    setCookie(key){
      this.$cookies.set('auth-token',key)
      this.isLoggedIn=true
    },
    signup(signupInfo) {
      const API_SIGNUP_URL = API_BASE_URL + '/rest_auth/signup/'
      // const GC_INPUT_URL = API_BASE_URL + '/movies/gcinput/'
      axios.post(API_SIGNUP_URL, signupInfo)
        .then(res => { 
          this.setCookie(res.data.key)
          // axios.post(GC_INPUT_URL)
          this.$router.push('/')
        })
        .catch(err => {
          console.error(err)
        })
    },
    login(loginInfo) {
      const API_LOGIN_URL = API_BASE_URL + '/rest_auth/login/'
      axios.post(API_LOGIN_URL, loginInfo)  
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push('/')
        })
        .catch(err => {
          console.error(err)
        })
    },
    logout(){
      const API_LOGOUT_URL = API_BASE_URL + '/rest_auth/logout/'
      const config ={
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(API_LOGOUT_URL, {}, config) 
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
    },
    // fetchGenreList() {
    //   const API_GENRE_LIST_URL = API_BASE_URL + '/movies/genreinput/'
    //   const config = {}
    //   this.$axios.get(API_GENRE_LIST_URL, config)
    //     .then(res => {
    //       this.genre_list = res.data
    //     })
    //     .catch(err => {
    //       console.error(err)
    //     })
    // },
    // gcinput(signupInfo) {
    //   this.genrecountInfo.user=this.
    // } 
  //     gcinputt(genre) {
  //       this.genrecountInfo.genre = this.genre
  //       this.genrecountInfo.id
  //       this.sum_rate= 0
  //       this.count= 0

  //       this.genrecountlist.push(this.genrecountInfo)
  // },

    // --------다크모드------
    addDarkTheme() {
      const darkThemeLinkEl = document.createElement("link");
      darkThemeLinkEl.setAttribute("rel", "stylesheet");
      darkThemeLinkEl.setAttribute("href", "/css/darktheme.css");
      darkThemeLinkEl.setAttribute("id", "dark-theme-style");

      const docHead = document.querySelector("head");
      docHead.append(darkThemeLinkEl);
    },
    removeDarkTheme() {
      const darkThemeLinkEl = document.querySelector("#dark-theme-style");
      const parentNode = darkThemeLinkEl.parentNode;
      parentNode.removeChild(darkThemeLinkEl);
    },
    darkThemeSwitch() {
      const darkThemeLinkEl = document.querySelector("#dark-theme-style");
      if (!darkThemeLinkEl) {
        this.addDarkTheme()
        this.darkmode = true
      } else {
        this.removeDarkTheme()
        this.darkmode = false
      }
    },
  },
  created() {
    // this.fetchGenreList()
    if (this.$cookies.isKey('auth-token')){
      this.isLoggedIn=true
    }
}}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  columns: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>