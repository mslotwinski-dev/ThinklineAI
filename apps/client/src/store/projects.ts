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

      this.projects = this.projects.filter((p) => p.ID != project.ID)

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

    // <-- AI -->

    set_color(project: Project, color: string) {
      this.loadFromLocalStorage()

      const p = this.projects.find((p) => p.ID === project.ID)
      if (p) {
        p.color = color
      }

      this.saveToLocalStorage()
    },

    update_project(id: string, newProject: Project) {
      this.loadFromLocalStorage()

      const index = this.projects.findIndex((p) => p.ID === id)
      if (index !== -1) {
        this.projects[index] = newProject
      }

      this.saveToLocalStorage()
    },
  },
})
