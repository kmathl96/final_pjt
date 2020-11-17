<template>
  <div>
    <h1>Review update</h1>
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
    <button @click="updateReview" class="btn btn-primary">수정</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL = 'http://localhost:8000'
export default {
  name:'ReviewUpdate',
  data() {
    return {
      params: this.$route.params.review_pk,
      reviewInfo: {
        title: '',
        content: '',
      },
    }
  },
  methods: {
    fetchReview() {
      const API_REVIEW_URL = API_BASE_URL + `/community/${this.params}`
      const config = {}
      this.$axios.get(API_REVIEW_URL, config)
        .then(res => {
          this.reviewInfo.title = res.data.title
          this.reviewInfo.content = res.data.content
        })
        .catch(err => {
          console.error(err)
        })
    },
    updateReview() {
      const API_UPDATE_URL = API_BASE_URL + `/community/${this.params}/update/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.patch(API_UPDATE_URL, this.reviewInfo, config)
        .then(res => {
          console.log(res)
          this.$router.push(`/community/${this.params}`)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.fetchReview()
  },
}
</script>

<style>

</style>