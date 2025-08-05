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
    <Success v-if="state == 2 && projects.length >= 1" :projects="projects" />
    <Error v-if="state == 3" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from '@/config/axios'

import Form from '@/components/Generate/Form.vue'
import Wait from '@/components/Generate/Wait.vue'
import Success from '@/components/Generate/Success.vue'
import Error from '@/components/Generate/Error.vue'

export default defineComponent({
  data() {
    return {
      state: 0, // 0: initial, 1: loading, 2: success, 3: error
      projects: [],
    }
  },
  components: {
    Form,
    Wait,
    Success,
    Error,
  },
  methods: {
    handleGenerate(data: {
      language: string
      topic: number
      tags: string[]
      level: number
    }) {
      this.state = 1

      axios
        .post('/generate', {
          language: data.language,
          topic: data.topic,
          tags: data.tags,
          level: data.level,
          locale: localStorage.getItem('locale') || 'en',
        })
        .then((response) => {
          if (response.data.length == 0) {
            this.state = 3
            return
          }

          this.projects = response.data
          this.state = 2
        })
        .catch((error) => {
          console.error(error)
          // this.$toast.error(this.$t('generate.error'))
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
