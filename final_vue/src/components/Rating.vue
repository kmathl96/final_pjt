<template>
  <div>
    <h1>Rating</h1>
    <select v-model="ratingInfo.rate">
      <option disabled value="">Please select one</option>
      <option value=1>☆</option>
      <option value=2>★</option>
      <option value=3>★☆</option>
      <option value=4>★★</option>
      <option value=5>★★☆</option>
      <option value=6>★★★</option>
      <option value=7>★★★☆</option>
      <option value=8>★★★★</option>
      <option value=9>★★★★☆</option>
      <option value=10>★★★★★</option>
    </select>
    <input v-model="ratingInfo.content" type="text" placeholder="한줄평 남기기">
    <button @click="createRating" class="btn btn-info">작성</button>
    <table class="table">

      <tbody>
         <tr v-for="rating in rating_list" :key="rating.id" > 
         
          <td>{{rating.rate}}</td>
          <td>{{rating.content}}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'Rating',
  data() {
    return {
      ratingInfo: {
        rate: '',
        content: '',
      },
      rating_list:[]
    }
  },
  props: {
    movie_pk: {
      type: Number,
    },
  },
  methods: {
    createRating() {
      const API_RATING_CREATE_URL = API_BASE_URL + `/movies/${this.movie_pk}/rate/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.post(API_RATING_CREATE_URL, this.ratingInfo, config)
        .then(() => {
          console.log(this.ratingInfo)
          this.fetchRatingList()
        })
        .catch(err => {
          console.error(err)
          
        })
    },
    fetchRatingList() {
      const API_RATING_LIST_URL = API_BASE_URL + `/movies/${this.movie_pk}/rating_list/`
      const config = {}
      this.$axios.get(API_RATING_LIST_URL,config)
        .then(res => {
          this.rating_list = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
  created() {
    this.fetchRatingList()
  },
}
</script>
<style>