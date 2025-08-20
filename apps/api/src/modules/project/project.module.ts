import { Module } from '@nestjs/common'
import { ProjectController } from './project.controller'
import { ProjectService } from './project.service'
import { AiCoreProvider } from '../../providers/AI'

@Module({
  controllers: [ProjectController],
  providers: [ProjectService, AiCoreProvider],
})
export class ProjectModule {}
