import { Injectable, Inject } from '@nestjs/common'
import type { AxiosInstance } from 'axios'
import { Project } from './project.types'

@Injectable()
export class ProjectService {
  constructor(@Inject('AI_CORE_CLIENT') private readonly http: AxiosInstance) {}

  private async template<T>(link: string, body: Project): Promise<T> {
    const response = await this.http.post<T>('/project/' + link, body, {
      headers: { 'Content-Type': 'application/json' },
    })
    return response.data
  }

  async generateField<K extends keyof Project>(
    project: Project,
    field: K
  ): Promise<Project> {
    type FieldType = Project[K]

    const result = await this.template<FieldType | { [key in K]: FieldType }>(
      field as string,
      project
    )

    const value =
      result && typeof result === 'object' && field in result
        ? (result as Record<K, FieldType>)[field]
        : result

    return { ...project, [field]: value } as Project
  }
}
