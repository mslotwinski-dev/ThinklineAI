import {
  ExceptionFilter,
  Catch,
  ArgumentsHost,
  HttpException,
  HttpStatus,
} from '@nestjs/common'

import type { Response } from 'express'

@Catch()
export class AIFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp()
    const response = ctx.getResponse<Response>()

    const status =
      exception instanceof HttpException
        ? exception.getStatus()
        : HttpStatus.BAD_GATEWAY

    const message =
      exception instanceof HttpException
        ? exception.getResponse()
        : `Failed to communicate with AI service: ${
            exception instanceof Error ? exception.message : 'Unknown error'
          }`

    response.status(status).json({ statusCode: status, message })
  }
}
