<template>
  <Body>
    <Column class="grow">
      <Section :color="project.color" :head="$t('project.sections.summary')">
        <Box :size="100" :content="project.summary" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.description')"
      >
        <Box :size="400" :content="project.long_desc" />
      </Section>
    </Column>

    <Column>
      <Section
        :color="project.color"
        :head="$t('project.sections.inspiration')"
      >
        <List :array="project.inspirations" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.target')">
        <Box :size="100" :content="project.target" />
      </Section>

      <Section :color="project.color" :head="$t('project.sections.notes')">
        <Box :size="150" :content="project.notes" />
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
import List from '@/components/Project/ProjectElements/List.vue'

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
    List,
  },
})
</script>
