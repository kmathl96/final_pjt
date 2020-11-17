<template>
  <div>
    <h1>자유게시판</h1>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Title</th>
          <th scope="col">User</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(review, index) in review_list" :key="review.id" @click="goDetail(review)"> 
          <th scope="row">{{ index+1 }}</th>
          <td>{{ review.title }}</td>
          <td>{{ review.user.username }}</td>
        </tr>
      </tbody>
      <router-link to="/community/create" tag="button" :review_list=review_list>게시글 작성</router-link>
    </table>
  </div>
</template>

<script>

const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'ReviewMovList',
  data() {
    return {
      review_list: [],
    }
  },
  methods: {
    fetchReviewList() {
      const API_REVIEW_LIST_URL = API_BASE_URL+'/community/'
      const config={}
      this.$axios.get(API_REVIEW_LIST_URL,config)
        .then(res => {
          this.review_list = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
    goDetail(review) {
      // this.$emit('selected-review', review.id)
      this.$router.push(`/community/${review.id}/`)
    },
  },
  created() {
    this.fetchReviewList()
  },
}
</script>

<style>
</style>