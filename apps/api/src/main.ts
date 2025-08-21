import { NestFactory } from '@nestjs/core'
import { ValidationPipe } from '@nestjs/common'
import * as dotenv from 'dotenv'

import { AppModule } from './app.module'
import { AIFilter } from './filters/ai-filter'

async function bootstrap() {
  const app = await NestFactory.create(AppModule)

  dotenv.config()

  app.enableCors({
    origin: [process.env.CLIENT_URL, process.env.AI_CORE_URL],
    credentials: true,
  })

  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
    })
  )

  app.useGlobalFilters(new AIFilter())

  const port = process.env.PORT || 5000

  await app.listen(port)
}

bootstrap().catch((err) => {
  console.error('Bootstrap failed', err)
})
