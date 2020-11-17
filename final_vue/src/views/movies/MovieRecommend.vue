<template>
  <div>
 
    <h1/>
      <h2></h2>
    <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">

      <div class="carousel-inner">
          <div class="carousel-item" :class="{active: index==0}" v-for="(random,index) in allrandom" :key=random.id style="height:300px width:50%">
          <h2>오늘은 {{random.title}} 어떄요?</h2>
          <!-- <div v-if="index==0"> -->
            <!-- <div class="carousel-item" :class="{active: index==0}"> -->
            <img :src="random.poster_path" class=" w-20" alt="...">
            
            
            <!-- </div> -->
          <!-- </div> -->
          <!-- <div v-else> -->
            <!-- <div class="carousel-item">
            <img :src="random.poster_path" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random.title}}</h5>
            </div>
            </div> -->
          <!-- </div> -->



        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
</template>

<script>
const API_BASE_URL= 'http://localhost:8000'
export default {
  name: 'MovieRecommend',
  data() {
    return{
      allrandom:[]
    }
  },
  methods: {
    fetchALLR() {
      const API_ALLRANDOM_URL = API_BASE_URL + '/movies/recommend_random/'
      const config = {}
      this.$axios.get(API_ALLRANDOM_URL, config)
        .then(res => {
          this.allrandom = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },

  },
  created() {
    this.fetchALLR()
  },
}
</script>

<style>

</style>