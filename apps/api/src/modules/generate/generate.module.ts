import { Module } from '@nestjs/common'
import { GenerateController } from './generate.controller'
import { GenerateService } from './generate.service'
import { AiCoreProvider } from '../../providers/AI'

@Module({
  controllers: [GenerateController],
  providers: [GenerateService, AiCoreProvider],
})
export class GenerateModule {}
