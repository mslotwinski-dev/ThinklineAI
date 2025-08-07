<template>
  <div class="container">
    <div class="title" v-html="$t('generate.error')" />
    <div>Error: {{ error }}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    error: {
      type: String,
      required: true,
    },
  },
  mounted() {
    // document.title = 'Error - Thinkline AI'
  },
})
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  min-height: calc(85vh - 110px);
}

.title {
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 1rem;
  padding: 10px;
  background: $rose;
  border-radius: 10px;
}

.gold {
  color: $gold;
}
</style>
