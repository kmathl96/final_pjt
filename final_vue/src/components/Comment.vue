<template>
  <div>
    <h1>Comments</h1>
    <!-- Create Comment -->
    <input v-model="commentInfo.content" type="text" placeholder="댓글 작성">
    <button @click="createComment" class="btn btn-info">작성</button>
    <!-- Comment list -->
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">comment</th>
          <th scope="col">User</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(comment, index) in comment_list" :key="comment.id" > 
          <th scope="row">{{ index+1 }}</th>
          <td>{{ comment.content }}
            <button class="badge badge-danger m-1" data-toggle="modal" :data-target="'#update'+comment.id">수정</button>
            <div class="modal fade" :id="'update'+comment.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Update Comment</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <input type="text" v-model="updateCommentInfo.content">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" data-dismiss="modal" @click="updateData(comment)">Save changes</button>
                  </div>
                </div>
              </div>
            </div>
            <span @click="deleteData(comment)" class="badge badge-danger m-1">삭제</span>
            </td>
          <td>{{ comment.user.username }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
const API_BASE_URL = 'http://localhost:8000'
export default {
  name: 'Comment',
  data() {
    return {
      commentInfo: {
        content: '',
      },
      updateCommentInfo: {
        content: '',
      },
      comment_list: [],
      params: this.$route.params.review_pk,
    }
  },
  methods: {
    createComment() {
      const API_COMMENT_CREATE_URL = API_BASE_URL + `/community/${this.params}/create_comment/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.post(API_COMMENT_CREATE_URL, this.commentInfo, config)
        .then(() => {
          this.fetchCommentList()
          this.updateCommentInfo.content = ''
        })
        .catch(err => {
          console.error(err)
        })
    },
    fetchCommentList() {
      const API_COMMENT_LIST_URL = API_BASE_URL + `/community/${this.params}/comment_list/`
      const config = {}
      this.$axios.get(API_COMMENT_LIST_URL,config)
        .then(res => {
          this.comment_list = res.data
        })
        .catch(err => {
          console.error(err)
        })
    },
    deleteData(comment) {
      const DeleteUrl = API_BASE_URL+ `/community/${this.params}/${comment.id}/delete/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.post(DeleteUrl, null, config)
        .then(() => {
          console.log(comment)
          this.fetchCommentList()
        })
    },
    // fetchComment() {
    //   const API_REVIEW_URL = API_BASE_URL + `/community/${this.params}`
    //   const config = {}
    //   this.$axios.get(API_REVIEW_URL, config)
    //     .then(res => {
    //       this.reviewInfo.title = res.data.title
    //       this.reviewInfo.content = res.data.content
    //     })
    //     .catch(err => {
    //       console.error(err)
    //     })
    // },
    updateData(comment) {
      const API_UPDATE_URL = API_BASE_URL + `/community/${this.params}/${comment.id}/update/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.patch(API_UPDATE_URL, this.updateCommentInfo, config)
        .then(() => {
          this.fetchCommentList()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.fetchCommentList()
  },
}
</script>

<style>

</style>