<template>
  <Body>
    <Column class="grow">
      <Section
        :color="project.color"
        :head="$t('project.sections.basic_functions')"
        @submit.prevent="req('basic_functions')"
      >
        <Box :size="200" :content="project.basic_functions" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.extensions')"
        @submit.prevent="req('extensions')"
      >
        <Box :size="200" :content="project.extensions" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.integrations')"
        @submit.prevent="req('integrations')"
      >
        <Box :size="100" :content="project.integrations" />
      </Section>
    </Column>

    <Column>
      <Section
        :color="project.color"
        :head="$t('project.sections.roadmap')"
        @submit.prevent="req('roadmap')"
      >
        <Box :size="450" :content="project.roadmap" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.interface')"
        @submit.prevent="req('interface')"
      >
        <Box :size="100" :content="project.interface" />
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

import { useProjectsStore } from '@/store/projects'
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
  },
  data() {
    return {
      service: new RequestService(this.project),
    }
  },
  emits: ['reload'],
  methods: {
    req(str: string) {
      this.service.request(str).then((project) => {
        if (project) {
          useProjectsStore().update_project(project.ID, project)
          this.$emit('reload', project)
        }
      })
    },
  },
})
</script>
