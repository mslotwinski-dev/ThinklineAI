import { HttpException, HttpStatus, Injectable, Inject } from '@nestjs/common'
import type { AxiosInstance } from 'axios'
import * as generateTypes from './generate.types'

function randomString(length = 12) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  let result = ''

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * chars.length)
    result += chars[randomIndex]
  }

  return result
}

@Injectable()
export class GenerateService {
  constructor(@Inject('AI_CORE_CLIENT') private readonly http: AxiosInstance) {}

  async generate(
    body: generateTypes.GenerateData
  ): Promise<generateTypes.Project[]> {
    try {
      const response = await this.http.post<generateTypes.GenerateResponse>(
        '/generate',
        body,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      )

      const ideas = response.data.ideas

      for (const idea of ideas) {
        idea.ID = randomString()
      }

      return ideas
    } catch (error) {
      throw new HttpException(
        `Failed to communicate with AI service: ${error instanceof Error ? error.message : 'Unknown error'}`,
        HttpStatus.BAD_GATEWAY
      )
    }
  }

  async regenerate(
    body: generateTypes.GenerateData
  ): Promise<generateTypes.Project[]> {
    try {
      const response = await this.http.post<generateTypes.GenerateResponse>(
        '/regenerate',
        body,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      )

      return response.data.ideas
    } catch (error) {
      throw new HttpException(
        `Failed to communicate with AI service: ${error instanceof Error ? error.message : 'Unknown error'}`,
        HttpStatus.BAD_GATEWAY
      )
    }
  }
}
