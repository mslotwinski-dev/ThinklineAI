<template>
  <Body>
    <Column class="grow">
      <Section :color="project.color" :head="$t('project.sections.usecases')">
        <UseCases :array="project.usecases" />
      </Section>
    </Column>

    <Column>
      <Section :color="project.color" :head="$t('project.sections.patterns')">
        <Box :size="200" :content="project.patterns" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.testing')">
        <Box :size="150" :content="project.testing" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.scalability')"
      >
        <Box :size="150" :content="project.scalability" />
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
import UseCases from '@/components/Project/ProjectElements/UseCases.vue'

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
    UseCases,
  },
})
</script>
