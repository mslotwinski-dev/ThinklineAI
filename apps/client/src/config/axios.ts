import axios from 'axios'

const instance = axios.create({
  withCredentials: true,
  baseURL: process.env.API_URL || 'http://localhost:5000/',
})

export default instance
