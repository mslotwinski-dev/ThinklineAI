<template>
  <div class="global-project-page">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style lang="scss" scoped>
.global-project-page {
  display: flex;
  gap: 30px;
}
</style>
