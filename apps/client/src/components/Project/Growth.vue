<template>
  <div class="global-project-page">
    <div class="column grow">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.acquired_skills')" />
          <div class="box centered h200">A</div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div
            class="header"
            v-html="$t('project.sections.further_development')"
          />
          <div class="box centered h200">A</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Project } from '@/types/project'
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    project: {
      type: Object as () => Project,
      required: true,
    },
  },
})
</script>

<style lang="scss" scoped></style>
