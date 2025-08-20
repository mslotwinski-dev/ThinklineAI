import { Body, Controller, Param, Post, HttpException } from '@nestjs/common'
import { ProjectService } from './project.service'
import type { Project } from './project.types'

const fields: (keyof Project)[] = [
  'summary',
  'long_desc',
  'target',
  'inspirations',
  'notes',

  'basic_functions',
  'extensions',
  'integrations',
  'roadmap',
  'interface',

  'stack',
  'tools',
  'architecture',
  'deployment',

  'usecases',
  'patterns',
  'testing',
  'scalability',

  'monetization',
  'market',
  'social_impact',

  'threats',
  'monitoring',
  'data_security',
  'access',

  'acquired_skills',
  'further_development',
]

@Controller('project')
export class ProjectController {
  constructor(private readonly projectService: ProjectService) {}

  @Post(':field')
  async generateField(
    @Param('field') field: keyof Project,
    @Body() body: Project
  ): Promise<Project> {
    if (!fields.includes(field)) {
      throw new HttpException(`Nieznane pole: ${String(field)}`, 400)
    }

    return await this.projectService.generateField(body, field)
  }
}
