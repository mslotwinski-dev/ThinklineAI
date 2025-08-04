export interface GenerateData {
  language: string
  level: number
  tags: string[]
  locale: string
  topic: number
}

export interface Project {
  name: string
  description: string
  tech_stack: string[]
  difficulty: number
  tags: string[]
  estimated_time: number
}

export interface GenerateResponse {
  ideas: Project[]
}
