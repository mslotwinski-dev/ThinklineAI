<template>
  <Body>
    <Column class="grow">
      <Section :color="project.color" :head="$t('project.sections.threats')">
        <Box :size="400" :content="project.threats" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.monitoring')">
        <Box :size="100" :content="project.monitoring" />
      </Section>
    </Column>

    <Column>
      <Section
        :color="project.color"
        :head="$t('project.sections.data_security')"
      >
        <Box :size="300" :content="project.data_security" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.access')">
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
