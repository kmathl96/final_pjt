<template>
  <div v-if="movie" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
      <iframe 
      class="embed-responsive-item" 
      :src="videoUrl" 
      allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieTrailerDetail',
    props: {
        trailer:{ 
            type: Object,
        },
    },
    computed: {
        videoUrl() {
            const videoId = this.trailer.id.videoId
            return `https://www.youtube.com/embed/${videoId}`  
        },
    }
}
</script>

<style scoped>
div.container {
  text-align: center;
}
</style>