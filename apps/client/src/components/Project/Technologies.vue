<template>
  <div class="global-project-page">
    <div class="column grow">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.stack')" />
          <div class="box centered h250">A</div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.tools')" />
          <div class="box centered h200">A</div>
        </div>
      </div>
    </div>
    <div class="column between">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.architecture')" />
          <div class="box centered h350">A</div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.deployment')" />
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
