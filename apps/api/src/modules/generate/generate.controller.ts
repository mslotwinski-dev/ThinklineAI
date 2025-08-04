import { Controller, Post, Body } from '@nestjs/common'
import { GenerateService } from './generate.service'
import * as generateTypes from './generate.types'

@Controller('generate')
export class GenerateController {
  constructor(private readonly generateService: GenerateService) {}

  @Post()
  async generate(
    @Body() body: generateTypes.GenerateData
  ): Promise<generateTypes.Project[]> {
    const projects = await this.generateService.generate(body)
    return projects
  }
}
