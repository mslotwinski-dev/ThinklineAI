<template>
  <div>
    <Navbar />
    <notifications position="bottom left" width="400px" />
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
  mounted() {
    document.title = 'Thinkline AI'
  },
})
</script>

<style lang="scss">
@import '@/styles/index.scss';
</style>
