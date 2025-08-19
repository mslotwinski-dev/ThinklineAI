<template>
  <Body>
    <Column class="grow">
      <Section
        :color="project.color"
        :head="$t('project.sections.basicfunctions')"
      >
        <Box :size="200" :content="project.basicfunctions" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.extensions')">
        <Box :size="200" :content="project.extensions" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.integrations')"
      >
        <Box :size="100" :content="project.integrations" />
      </Section>
    </Column>

    <Column>
      <Section :color="project.color" :head="$t('project.sections.roadmap')">
        <Box :size="450" :content="project.roadmap" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.interface')">
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
