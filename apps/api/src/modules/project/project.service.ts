import { Injectable, Inject } from '@nestjs/common'
import type { AxiosInstance } from 'axios'
import { Project } from './project.types'

@Injectable()
export class ProjectService {
  constructor(@Inject('AI_CORE_CLIENT') private readonly http: AxiosInstance) {}

  async template<T>(link: string, body: Project): Promise<T> {
    await this.http.post('/project/summary', body)

    const response = await this.http.post<T>('/' + link, body, {
      headers: {
        'Content-Type': 'application/json',
      },
    })

    return response.data
  }

  async summary(project: Project): Promise<Project> {
    return {
      ...project,
      summary: await this.template<string>('summary', project),
    }
  }

  async description(project: Project): Promise<Project> {
    return {
      ...project,
      long_desc: await this.template<string>('long_desc', project),
    }
  }

  async inspirations(project: Project): Promise<Project> {
    return {
      ...project,
      inspirations: await this.template<string[]>('inspirations', project),
    }
  }

  async target(project: Project): Promise<Project> {
    return {
      ...project,
      target: await this.template<string>('target', project),
    }
  }

  async notes(project: Project): Promise<Project> {
    return {
      ...project,
      notes: await this.template<string>('notes', project),
    }
  }
}
