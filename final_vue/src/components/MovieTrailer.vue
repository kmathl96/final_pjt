<template>
    <div class="container" v-if="isLoaded">
      <!-- <h3>{{trailer[0].id.videoId}}</h3> -->
      <!-- <div class="embed-responsive embed-responsive-16by9"> -->
      <iframe 
        class="embed-responsive-item" 
        :src="videoUrl" 
        allowfullscreen>
      </iframe>
    <!-- </div> -->
  </div>
</template>

<script>
import axios from 'axios'
// import MovieTrailerDetail from './MovieTrailerDetail.vue'
const YOUTUBE_API_KEY = "AIzaSyC3mbNAFEM4uW57IdbzoNHldNGlsGephVU"
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieTrailer',
  data() {
    return {
      trailer: [],
      isLoaded: false
    }
  },
  // components:{MovieTrailerDetail},
  props: {
    movie_title: {
        type: String,
    },
  },
  methods: {
    getTrailer() {
      const config = {
        params: {
          key: YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.movie_title+ 'official trailer',
        },
      }
      axios.get(YOUTUBE_API_URL,config)
      .then(res => {
        this.trailer = res.data.items
        this.isLoaded= true
        // console.log(this.trailer,"여기")
      })
      .catch(err => {
        console.error(err)
      })
    },
  },
  computed: {
      videoUrl() {
          const videoId = this.trailer[0].id.videoId
          return `https://www.youtube.com/embed/${videoId}`  
      },
  },
  created() {
    this.getTrailer()
  },
}
</script>

<style>

</style>