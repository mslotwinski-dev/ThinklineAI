import axios from 'axios'

export const AiCoreProvider = {
  provide: 'AI_CORE_CLIENT',
  useFactory: () => {
    return axios.create({
      baseURL: /* process.env.AI_CORE_URL  || */ 'http://localhost:8000',
    })
  },
}
