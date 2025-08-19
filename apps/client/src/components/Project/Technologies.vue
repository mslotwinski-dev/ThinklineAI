<template>
  <Body>
    <Column class="grow">
      <Section :color="project.color" :head="$t('project.sections.stack')">
        <Box :size="250" :content="project.stack" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.tools')">
        <Box :size="200" :content="project.tools" />
      </Section>
    </Column>

    <Column>
      <Section
        :color="project.color"
        :head="$t('project.sections.architecture')"
      >
        <Box :size="350" :content="project.architecture" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.deployment')">
        <Box :size="150" :content="project.deployment" />
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
