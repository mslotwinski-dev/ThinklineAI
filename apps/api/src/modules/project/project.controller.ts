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

  @Post('basic_functions')
  basic_functions(@Body() body: Project) {
    return this.projectService.basic_functions(body)
  }

  @Post('extensions')
  extensions(@Body() body: Project) {
    return this.projectService.extensions(body)
  }

  @Post('integrations')
  integrations(@Body() body: Project) {
    return this.projectService.integrations(body)
  }

  @Post('roadmap')
  roadmap(@Body() body: Project) {
    return this.projectService.roadmap(body)
  }

  @Post('interface')
  interface(@Body() body: Project) {
    return this.projectService.interface(body)
  }

  @Post('stack')
  stack(@Body() body: Project) {
    return this.projectService.stack(body)
  }

  @Post('tools')
  tools(@Body() body: Project) {
    return this.projectService.tools(body)
  }

  @Post('architecture')
  architecture(@Body() body: Project) {
    return this.projectService.architecture(body)
  }

  @Post('deployment')
  deployment(@Body() body: Project) {
    return this.projectService.deployment(body)
  }

  @Post('usecases')
  usecases(@Body() body: Project) {
    return this.projectService.usecases(body)
  }

  @Post('patterns')
  patterns(@Body() body: Project) {
    return this.projectService.patterns(body)
  }

  @Post('testing')
  testing(@Body() body: Project) {
    return this.projectService.testing(body)
  }

  @Post('scalability')
  scalability(@Body() body: Project) {
    return this.projectService.scalability(body)
  }

  @Post('monetization')
  monetization(@Body() body: Project) {
    return this.projectService.monetization(body)
  }

  @Post('market')
  market(@Body() body: Project) {
    return this.projectService.market(body)
  }

  @Post('social_impact')
  socialImpact(@Body() body: Project) {
    return this.projectService.social_impact(body)
  }

  @Post('threats')
  threats(@Body() body: Project) {
    return this.projectService.threats(body)
  }

  @Post('monitoring')
  monitoring(@Body() body: Project) {
    return this.projectService.monitoring(body)
  }

  @Post('data_security')
  dataSecurity(@Body() body: Project) {
    return this.projectService.data_security(body)
  }

  @Post('access')
  access(@Body() body: Project) {
    return this.projectService.access(body)
  }

  @Post('acquired_skills')
  acquiredSkills(@Body() body: Project) {
    return this.projectService.acquired_skills(body)
  }

  @Post('further_development')
  furtherDevelopment(@Body() body: Project) {
    return this.projectService.further_development(body)
  }
}
