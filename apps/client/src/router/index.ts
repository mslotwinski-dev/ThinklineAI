import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Generate from '../views/Generate.vue'
import Projects from '../views/Projects.vue'
import Project from '../views/Project.vue'
import ProjectNotFound from '../views/ProjectNotFound.vue'

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
  {
    path: '/projects/:id',
    component: Project,
  },
  {
    path: '/P404',
    component: ProjectNotFound,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
