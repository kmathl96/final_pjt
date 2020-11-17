<template>
  <div>
    <h1 class="m-3">로그인</h1>
    <div class="m-2">
      <p>아이디</p>
      <input v-model="loginInfo.username" type="text" class="form-control"/>
    </div>
    <div class="m-2">
      <p>비밀번호</p>
      <input v-model="loginInfo.password" type="password" class="form-control"/>
    </div>
    <br><br>
    <router-link to="/signup">아직 회원이 아니시라면?</router-link><br><br>
    <button @click="LoginSubmit" class="btn btn-info">확인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      loginInfo: {
        username: '',
        password: ''
      },
    }
  },
 methods: {
    LoginSubmit() {
      this.$emit('loginsubmit', this.loginInfo)
    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')){
      this.$router.push('/')
    }
  },
}
</script>

<style>

</style>