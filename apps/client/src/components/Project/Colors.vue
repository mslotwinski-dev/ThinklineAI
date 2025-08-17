<template>
  <div class="container">
    <div
      class="color"
      v-for="color in colors"
      :key="color"
      :style="{ background: color }"
      :class="{ isopen: isopen || color == selected_color }"
      @click="selectColor(color)"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { useProjectsStore } from '@/store/projects'
import { Project } from '@/types/project'

export default defineComponent({
  props: {
    project: {
      type: Object as () => Project,
      required: true,
    },
  },
  data() {
    return {
      isopen: false,
      selected_color: '',
      colors: [
        '#2e4057',
        '#00647d',
        '#34abc0',
        '#007f46',
        '#52a121',
        '#e1a038',
        '#a50034',
        '#62477a',
        '#826577',
      ],
    }
  },
  mounted() {
    if (this.project.color) {
      this.selected_color = this.project.color
    } else {
      this.selected_color = this.colors[0]
      useProjectsStore().set_color(this.project, this.colors[0])
    }
  },
  methods: {
    selectColor(color: string) {
      this.selected_color = color
      useProjectsStore().set_color(this.project, color)
      this.isopen = !this.isopen
    },
  },
})
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  padding: 10px;
}

.color {
  width: 0px;
  height: 30px;
  border: 1px solid #ccc;
  border-radius: 50%;
  display: inline-block;
  opacity: 0;
  cursor: pointer;
  transform: scale(0);
  margin: 0;
  transition: opacity 0.35s ease, width 0.35s ease, margin 0.35s ease,
    transform 0.35s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.isopen {
  opacity: 1;
  width: 30px;
  margin: 5px;
  transform: scale(1);
}
</style>
