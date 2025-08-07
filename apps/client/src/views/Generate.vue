<template>
  <div class="container">
    <div class="title" v-if="state == 0">
      {{ $t('generate.title') }}
      <span class="gold">
        <ic icon="wand-magic-sparkles" />
      </span>
    </div>
    <Form @generate="handleGenerate" v-if="state == 0" />
    <Wait v-if="state == 1" />
    <Success
      v-if="state == 2 && projects.length >= 1"
      :projects="projects"
      @regenerate="handleRegenerate"
    />
    <Error v-if="state == 3 && error" :error="error" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from '@/config/axios'

import { Project, GenerateData } from '@/types/project'

import Form from '@/components/Generate/Form.vue'
import Wait from '@/components/Generate/Wait.vue'
import Success from '@/components/Generate/Success.vue'
import Error from '@/components/Generate/Error.vue'

export default defineComponent({
  data() {
    return {
      state: 0, // 0: initial, 1: loading, 2: success, 3: error
      projects: [] as Project[],
      error: null as string | null,
      generateData: {} as GenerateData,
    }
  },
  components: {
    Form,
    Wait,
    Success,
    Error,
  },
  methods: {
    handleGenerate(data: GenerateData) {
      this.state = 1

      const generatedata = {
        language: data.language,
        topic: data.topic,
        tags: data.tags,
        level: data.level,
        locale: localStorage.getItem('locale') || 'en',
      }

      this.generateData = generatedata

      axios
        .post('/generate', generatedata)
        .then((response) => {
          if (response.data.length == 0) {
            this.state = 3
            return
          }

          this.projects = response.data
          this.state = 2
        })
        .catch((error) => {
          this.error = error.response.data.message
          this.state = 3
        })
    },
    handleRegenerate() {
      this.state = 1
      const prev = []
      for (const project of this.projects) {
        prev.push(`${project.name}: ${project.description}`)
      }

      const generatedata: GenerateData = {
        ...this.generateData,
        previous_projects: prev,
      }

      axios
        .post('/generate/regenerate', generatedata)
        .then((response) => {
          if (response.data.length == 0) {
            this.state = 3
            return
          }

          this.projects = response.data
          this.state = 2
        })
        .catch((error) => {
          this.error = error.response.data.message
          this.state = 3
        })
    },
  },
})
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  min-height: calc(85vh - 110px);
}

.title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.gold {
  color: $gold;
}
</style>
