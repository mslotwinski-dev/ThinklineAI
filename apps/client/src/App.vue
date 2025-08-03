<template>
  <div>
    <Navbar />

    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Navbar from '@/components/Shared/Navbar.vue'

export default defineComponent({
  components: {
    Navbar,
  },
})
</script>

<style lang="scss">
@import '@/styles/index.scss';
</style>
