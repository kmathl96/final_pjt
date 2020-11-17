<template>
  <div class="container">
    <!-- <MovieListItem :movie_list="movie_list"/> -->
    <div class="card-deck justify-content-center">
      <div v-for="movie in movie_list.slice(start,end)" :key="movie.id" class="col-sm-6 col-lg-4 col-xl-3  p-2 row">
        <div class="card mx-3">
          <img :src="movie.poster_path" class="card-img-top" alt="..." data-toggle="modal" :data-target="'#movie'+movie.id">
          <div class="card-body">
            <h5 class="card-title text-dark">{{ movie.title }}</h5>
            <div class="modal fade" :id="'movie'+movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <img :src="movie.backdrop_path" alt="" class="movieImg img-fluid">
                    <h3>{{movie.vote_average}}</h3>
                    <small>{{movie.overview}}</small>
                    <!-- <small v-for="genre in movie.genres" :key="genre.id"> </small> -->
                    <hr>
                    <p>예고편</p>
                    <MovieTrailer :movie_title="movie.title"/>
                    <hr>
                    <Rating :movie_pk="movie.id"/>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="btn-cover d-flex justify-content-center align-items-center">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn btn btn-info m-2">
        <i class="fas fa-angle-left"></i>
      </button>
      <span class="page-count m-0"><h4>{{ pageNum + 1 }} / 86</h4></span>
      <button :disabled="pageNum >= 86" @click="nextPage" class="page-btn btn btn-info m-2">
        <i class="fas fa-angle-right"></i>
      </button>
    </div> 
  </div>

</template>
<script>
import Rating from '../../components/Rating.vue'
import MovieTrailer from '../../components/MovieTrailer.vue'
const API_BASE_URL = 'http://localhost:8000'

export default {

  name: 'MovieListView',
  data() {
    return {
      movie_list: [],
      pageNum: 0,
      pageSIze: 10,
      start: 0,
      end: 12,
    }
  },
  components:{
    Rating,
    MovieTrailer,
  },
  methods: {
    fetchMovieList() {
      const API_MOVIE_LIST_URL = API_BASE_URL + '/movies/'
      const config = {}
      this.$axios.get(API_MOVIE_LIST_URL, config)
        .then(res => {
          this.movie_list = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
    nextPage () {
      this.pageNum += 1
      this.start+=12
      this.end+=12
    },
    prevPage () {
      this.pageNum -= 1
      this.start-=12
      this.end-=12
    }
  },
  created() {
    this.fetchMovieList()
  },
  computed: {
    pageCount () {
        let  page = Math.floor((this.movie_list.length-1) / this.pageSize) + 1
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize
      const end = start + this.pageSize
      console.log(this.movie_list.slice(start, end))
      return this.movie_list.slice(start, end)
    }
  }
}
</script>

<style>
</style>