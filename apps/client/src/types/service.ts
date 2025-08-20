import { notify } from '@kyvg/vue3-notification'
import ax, { AxiosInstance } from 'axios'

import axios from '@/config/axios'
import { Project } from './project'

export class RequestService {
  project: Project
  http: AxiosInstance
  constructor(_project: Project) {
    this.project = _project
    this.http = axios
  }

  async request(path: string): Promise<Project | null> {
    try {
      const response = await this.http.post<Project>(
        `/project/${path}`,
        this.project,
        {
          headers: { 'Content-Type': 'application/json' },
        }
      )

      this.project = response.data
      return response.data
    } catch (error) {
      let message = 'Unknown error'

      if (ax.isAxiosError(error)) {
        message = error.response?.data?.message ?? error.message
      } else if (error instanceof Error) {
        message = error.message
      }

      notify({
        title: 'Błąd przy aktualizacji projektu',
        text: message,
        type: 'error',
      })
    }

    return null
  }
}
