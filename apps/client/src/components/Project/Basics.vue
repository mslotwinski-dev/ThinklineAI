<template>
  <div class="global-project-page">
    <div class="column grow">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />
        <div>
          <div class="header" v-html="$t('project.sections.summary')" />
          <div class="box centered h100"></div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />

        <div>
          <div class="header" v-html="$t('project.sections.description')" />

          <div class="box centered h200">A</div>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />

        <div>
          <div class="header" v-html="$t('project.sections.target')" />
          <div class="box centered h150">A</div>
        </div>
      </div>
    </div>
    <div class="column">
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />

        <div>
          <div class="header" v-html="$t('project.sections.inspiration')" />

          <ul>
            <li>Projekt 1</li>
            <li>Projekt 2</li>
            <li>Projekt 3</li>
            <li>Projekt 4</li>
          </ul>
        </div>
      </div>
      <div class="section">
        <span class="bar" :style="{ background: project.color || '#2e4057' }" />

        <div>
          <div class="header" v-html="$t('project.sections.notes')" />

          <div class="box centered h300">A</div>
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
