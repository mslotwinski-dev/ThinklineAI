import { defineStore } from 'pinia'
import { notify } from '@kyvg/vue3-notification'

import { Project } from '@/types/project'

export const useProjectsStore = defineStore('projects', {
  state: () => ({
    projects: [] as Project[],
  }),

  actions: {
    loadFromLocalStorage() {
      const stored = localStorage.getItem('projects')
      if (stored) {
        try {
          this.projects = JSON.parse(stored)
        } catch (e) {
          notify({
            title: 'Błąd',
            text: 'Błąd przy odczycie projects z localStorage:' + e,
            type: 'error',
          })
        }
      }
    },

    addProject(project: Project) {
      this.loadFromLocalStorage()

      this.projects.push(project)
      this.saveToLocalStorage()

      notify({
        title: 'Sukces',
        text: 'Projekt został dodany.',
        type: 'success',
      })
    },

    removeProject(project: Project) {
      this.loadFromLocalStorage()

      this.projects = this.projects.filter(
        (p) => p.description != project.description
      )

      console.log(this.projects)
      this.saveToLocalStorage()

      notify({
        title: 'Sukces',
        text: 'Projekt został usunięty.',
        type: 'success',
      })
    },

    saveToLocalStorage() {
      localStorage.setItem('projects', JSON.stringify(this.projects))
    },

    read() {
      this.loadFromLocalStorage()
      return this.projects
    },
  },
})
