import axios from 'axios'

const instance = axios.create({
  withCredentials: true,
  baseURL:
    process.env.VUE_APP_API_URL ||
    (process.env.NODE_ENV === 'production'
      ? 'https://api.thinklineai.eu'
      : 'http://localhost:5125/'),
})

export default instance
