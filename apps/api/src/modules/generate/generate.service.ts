import { Injectable } from '@nestjs/common'
import axios from 'axios'
import * as generateTypes from './generate.types'

@Injectable()
export class GenerateService {
  async generate(
    body: generateTypes.GenerateData
  ): Promise<generateTypes.Project[]> {
    try {
      const response = await axios.post<generateTypes.GenerateResponse>(
        'http://localhost:8000/generate',
        body,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      )

      return response.data.ideas
    } catch (error) {
      if (error instanceof Error) {
        console.error('Error calling AI service:', error.message)
      } else {
        console.error('Unknown error calling AI service:', error)
      }
      console.log('Error:', error)
    }
    return []
  }
}
