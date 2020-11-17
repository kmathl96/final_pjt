<template>
  <div>
    <div class="card text-left">
      <h5 class="card-header text-dark">{{ review.title }}</h5>
      <div class="card-body">
        <h5 class="card-title text-dark">{{ review.content }}</h5>
        <p class="card-text text-dark">{{ review.user.username }}</p>
        <small class="text-secondary">{{ review.created_at }}</small>
        <small class="text-secondary">{{ review.updated_at }}</small>
        <div>
          <router-link to="update" tag="button" class="btn btn-success m-2">수정하기</router-link>
          <button @click="deleteData()" class="btn btn-danger m-2">삭제하기</button>
        </div>
      </div>
    </div>
    <Comment/>
  </div>
</template>

<script>
import Comment from '@/components/Comment.vue'
const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'ReviewDetail',
  components: {
    Comment,
  },
  data() {
    return {
      review: [],
      params: this.$route.params.review_pk,
    }
  },
  methods: {
    fetchReview() {
      const API_REVIEW_URL = API_BASE_URL + `/community/${this.params}`
      const config={}
      this.$axios.get(API_REVIEW_URL,config)
        .then(res => {
          this.review = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
    deleteData() {
      const DeleteUrl = API_BASE_URL+ `/community/${this.params}/delete/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.post(DeleteUrl, null, config)
        .then(()=>{
          this.$router.push( {
            path:'/community'
          })
        })
    }
  },
  created() {
    this.fetchReview()
  },
  computed: {
    update() {
      const updateurl = `/community/${this.params}/update`
      return updateurl  
    },
  }
}
</script>

<style>

</style>