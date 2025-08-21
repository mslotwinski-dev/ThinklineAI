import { Module } from '@nestjs/common'
import { ConfigModule } from '@nestjs/config'

import { AppController } from './app.controller'
import { AppService } from './app.service'

import { GenerateModule } from './modules/generate/generate.module'
import { ProjectModule } from './modules/project/project.module'

@Module({
  imports: [
    GenerateModule,
    ProjectModule,
    ConfigModule.forRoot({
      isGlobal: true,
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
