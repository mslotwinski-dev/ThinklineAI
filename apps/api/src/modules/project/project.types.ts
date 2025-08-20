export interface UseCase {
  name: string
  actor: string
  goal: string
  flow: string[]
  exceptions?: string[]
}

export interface Project {
  ID: string
  name: string
  description: string
  tech_stack: string[]
  difficulty: number
  tags: string[]
  estimated_time: number

  // <-- AI GENERATED -->

  color?: string

  // <-- PODSTAWY -->

  summary?: string
  long_desc?: string
  target?: string
  inspirations?: string[]
  notes: string

  // <-- FUNCTIONS -->

  basic_functions?: string
  extensions?: string
  integrations?: string
  roadmap?: string
  interface?: string

  // <-- TECHNOLOGY -->

  stack?: string
  tools?: string
  architecture?: string
  deployment?: string

  // <-- SOFTWARE -->

  usecases?: UseCase[]
  patterns?: string
  testing?: string
  scalability?: string

  // <-- BUSINESS -->

  monetization?: string
  market?: string
  social_impact?: string

  // <-- SECURITY -->

  threats?: string
  monitoring?: string
  data_security?: string
  access?: string

  // <-- LEARNED -->

  acquired_skills?: string
  further_development?: string
}
