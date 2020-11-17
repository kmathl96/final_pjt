import Vue from 'vue'
import VueRouter from 'vue-router'

import ReviewList from '../views/community/ReviewList.vue'
import ReviewCreate from '../views/community/ReviewCreate.vue'
import ReviewDetail from '../views/community/ReviewDetail.vue'
import ReviewUpdate from '../views/community/ReviewUpdate.vue'

import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import MovieList from '../views/movies/MovieListView.vue'
import MovieRecommend from '../views/movies/MovieRecommend.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/community',
    name: 'ReviewList',
    component: ReviewList
  },
  {
    path: '/community/create',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: `/community/:review_pk`,
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: `/community/:review_pk/update`,
    name: 'ReviewUpdate',
    component: ReviewUpdate
  },
  
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/',
    name: 'MovieListView',
    component: MovieList
  },
  {
    path: '/movierecommend',
    name: 'MovieRecommend',
    component: MovieRecommend
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
