<template>
  <div class="container">
    <div class="title">
      {{ $t('generate.title') }}
      <span class="gold">
        <ic icon="wand-magic-sparkles" />
      </span>
    </div>
    <Form />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Form from '@/components/Generate/Form.vue'

export default defineComponent({
  data() {
    return {}
  },
  components: {
    Form,
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
  height: calc(85vh - 110px);
}

.title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.gold {
  color: $gold;
}
</style>
