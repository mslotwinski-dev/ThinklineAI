import { Controller, Post, Body } from '@nestjs/common'
import type { Project } from './project.types'
import { ProjectService } from './project.service'

@Controller('project')
export class ProjectController {
  constructor(private readonly projectService: ProjectService) {}

  @Post('summary')
  summary(@Body() body: Project) {
    return this.projectService.summary(body)
  }

  @Post('description')
  description(@Body() body: Project) {
    return this.projectService.description(body)
  }

  @Post('inspirations')
  inspirations(@Body() body: Project) {
    return this.projectService.inspirations(body)
  }

  @Post('target')
  target(@Body() body: Project) {
    return this.projectService.target(body)
  }

  @Post('notes')
  notes(@Body() body: Project) {
    return this.projectService.notes(body)
  }
}
