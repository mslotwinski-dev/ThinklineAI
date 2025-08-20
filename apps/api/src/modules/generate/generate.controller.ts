import { Controller, Post, Body } from '@nestjs/common'
import { GenerateService } from './generate.service'
import type { GenerateData, Project } from './generate.types'

@Controller('generate')
export class GenerateController {
  constructor(private readonly generateService: GenerateService) {}

  @Post()
  generate(@Body() body: GenerateData): Promise<Project[]> {
    return this.generateService.generate(body)
  }

  @Post('regenerate')
  regenerate(@Body() body: GenerateData): Promise<Project[]> {
    return this.generateService.regenerate(body)
  }
}
