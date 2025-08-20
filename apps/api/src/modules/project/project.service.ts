import { Injectable, Inject } from '@nestjs/common'
import type { AxiosInstance } from 'axios'
import { Project, UseCase } from './project.types'

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

  async basicfunctions(project: Project): Promise<Project> {
    return {
      ...project,
      basicfunctions: await this.template<string>('basicfunctions', project),
    }
  }

  async extensions(project: Project): Promise<Project> {
    return {
      ...project,
      extensions: await this.template<string>('extensions', project),
    }
  }

  async integrations(project: Project): Promise<Project> {
    return {
      ...project,
      integrations: await this.template<string>('integrations', project),
    }
  }

  async roadmap(project: Project): Promise<Project> {
    return {
      ...project,
      roadmap: await this.template<string>('roadmap', project),
    }
  }

  async interface(project: Project): Promise<Project> {
    return {
      ...project,
      interface: await this.template<string>('interface', project),
    }
  }

  async stack(project: Project): Promise<Project> {
    return {
      ...project,
      stack: await this.template<string>('stack', project),
    }
  }

  async tools(project: Project): Promise<Project> {
    return {
      ...project,
      tools: await this.template<string>('tools', project),
    }
  }

  async architecture(project: Project): Promise<Project> {
    return {
      ...project,
      architecture: await this.template<string>('architecture', project),
    }
  }

  async deployment(project: Project): Promise<Project> {
    return {
      ...project,
      deployment: await this.template<string>('deployment', project),
    }
  }

  async usecases(project: Project): Promise<Project> {
    return {
      ...project,
      usecases: await this.template<UseCase[]>('usecases', project),
    }
  }

  async patterns(project: Project): Promise<Project> {
    return {
      ...project,
      patterns: await this.template<string>('patterns', project),
    }
  }

  async testing(project: Project): Promise<Project> {
    return {
      ...project,
      testing: await this.template<string>('testing', project),
    }
  }

  async scalability(project: Project): Promise<Project> {
    return {
      ...project,
      scalability: await this.template<string>('scalability', project),
    }
  }

  async monetization(project: Project): Promise<Project> {
    return {
      ...project,
      monetization: await this.template<string>('monetization', project),
    }
  }

  async market(project: Project): Promise<Project> {
    return {
      ...project,
      market: await this.template<string>('market', project),
    }
  }

  async social_impact(project: Project): Promise<Project> {
    return {
      ...project,
      social_impact: await this.template<string>('social_impact', project),
    }
  }

  async threats(project: Project): Promise<Project> {
    return {
      ...project,
      threats: await this.template<string>('threats', project),
    }
  }

  async monitoring(project: Project): Promise<Project> {
    return {
      ...project,
      monitoring: await this.template<string>('monitoring', project),
    }
  }

  async data_security(project: Project): Promise<Project> {
    return {
      ...project,
      data_security: await this.template<string>('data_security', project),
    }
  }

  async access(project: Project): Promise<Project> {
    return {
      ...project,
      access: await this.template<string>('access', project),
    }
  }

  async acquired_skills(project: Project): Promise<Project> {
    return {
      ...project,
      acquired_skills: await this.template<string>('acquired_skills', project),
    }
  }

  async further_development(project: Project): Promise<Project> {
    return {
      ...project,
      further_development: await this.template<string>(
        'further_development',
        project
      ),
    }
  }
}
