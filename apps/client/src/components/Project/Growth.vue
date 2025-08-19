<template>
  <Body>
    <Column class="grow">
      <Section
        :color="project.color"
        :head="$t('project.sections.acquired_skills')"
      >
        <Box :size="200" :content="project.acquired_skills" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.further_development')"
      >
        <Box :size="200" :content="project.further_development" />
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

import { Project } from '@/types/project'

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
})
</script>
