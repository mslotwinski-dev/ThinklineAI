<template>
  <Loading v-if="loading" />
  <Body>
    <Column class="grow">
      <Section
        :color="project.color"
        :head="$t('project.sections.threats')"
        @submit.prevent="req('threats')"
      >
        <Box :size="400" :content="project.threats" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.monitoring')"
        @submit.prevent="req('monitoring')"
      >
        <Box :size="100" :content="project.monitoring" />
      </Section>
    </Column>

    <Column>
      <Section
        :color="project.color"
        :head="$t('project.sections.data_security')"
        @submit.prevent="req('data_security')"
      >
        <Box :size="300" :content="project.data_security" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.access')"
        @submit.prevent="req('access')"
      >
        <Box :size="150" :content="project.access" />
      </Section>
    </Column>
  </Body>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import Body from '@/components/Project/ProjectElements/Body.vue'
import Column from '@/components/Project/ProjectElements/Column.vue'
import Section from '@/components/Project/ProjectElements/Section.vue'
import Box from '@/components/Project/ProjectElements/Box.vue'
import Loading from '@/components/Project/ProjectElements/Loading.vue'

import { Project } from '@/types/project'
import { RequestService } from '@/types/service'

export default defineComponent({
  props: {
    project: {
      type: Object as () => Project,
      required: true,
    },
  },
  components: {
    Body,
    Column,
    Section,
    Box,
    Loading,
  },
  data() {
    return {
      loading: false,
      service: new RequestService(this.project),
    }
  },
  emits: ['reload'],
  methods: {
    req(str: string) {
      this.loading = true
      this.service.request(str).then((project) => {
        if (project) {
          this.$emit('reload', project)
          this.loading = false
        }
      })
    },
  },
})
</script>
