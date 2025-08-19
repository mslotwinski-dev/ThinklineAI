<template>
  <div class="section">
    <span class="bar" :style="{ background: color }" />
    <div>
      <div class="header" v-html="head" />

      <slot />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    color: {
      type: String,
      default: '#2e4057',
    },
    head: {
      type: String,
      default: '',
    },
  },
})
</script>

<style lang="scss" scoped>
.section {
  .bar {
    content: '';
    display: block;
    background: red;
    border-radius: 10px;
    width: 5px;
    flex-shrink: 0;
  }

  & > div {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }
  flex-grow: 1;
  display: flex;
  gap: 15px;
}

.header {
  font-size: 20px;
  font-weight: 500;
  text-transform: uppercase;
}
</style>
