<template>
  <div class="column">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style lang="scss" scoped>
.column {
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 400px;
  &.grow {
    flex-grow: 1;
  }

  &.between {
    justify-content: space-between;
  }
}
</style>
