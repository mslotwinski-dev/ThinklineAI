<template>
  <Body>
    <Column class="grow">
      <Section
        :color="project.color"
        :head="$t('project.sections.monetization')"
      >
        <Box :size="500" :content="project.monetization" />
      </Section>
    </Column>

    <Column>
      <Section :color="project.color" :head="$t('project.sections.market')">
        <Box :size="300" :content="project.market" />
      </Section>

      <Section
        :color="project.color"
        :head="$t('project.sections.social_impact')"
      >
        <Box :size="150" :content="project.social_impact" />
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
