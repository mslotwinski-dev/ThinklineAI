import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Generate from '../views/Generate.vue'
import Projects from '../views/Projects.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: Home,
  },
  {
    path: '/generate',
    component: Generate,
  },
  {
    path: '/projects',
    component: Projects,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
