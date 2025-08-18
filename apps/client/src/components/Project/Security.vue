<template>
  <div class="global-project-page">
    <div class="column grow">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.threats')" />
          <div class="box centered h400">A</div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.monitoring')" />
          <div class="box centered h100">A</div>
        </div>
      </div>
    </div>
    <div class="column between">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.data_security')" />
          <div class="box centered h300">A</div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.access')" />
          <div class="box centered h150">A</div>
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
