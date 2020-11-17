<template>
  <div>
    <h1>Review Create</h1>
    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1">Title</span>
      </div>
      <input v-model="reviewInfo.title" type="text" class="form-control">
    </div>
    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1">Content</span>
      </div>
      <input v-model="reviewInfo.content" type="text" class="form-control">
    </div>
    <button @click="createReview" class="btn btn-primary">Create</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'ReviewCreate',
  data() {
    return {
      reviewInfo: {
        title: '',
        content: '',
      },
    }
  },
  methods: {
    createReview() {
      const API_CREATE_URL = API_BASE_URL + '/community/create/' 
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(API_CREATE_URL, this.reviewInfo, config)
        .then(res => {
          console.log(res)
          this.$router.push('/community')
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style>

</style>