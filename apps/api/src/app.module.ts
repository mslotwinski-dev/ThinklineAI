import { Module } from '@nestjs/common'

import { AppController } from './app.controller'
import { AppService } from './app.service'

import { GenerateModule } from './modules/generate/generate.module'
import { ProjectModule } from './modules/project/project.module'

@Module({
  imports: [GenerateModule, ProjectModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
