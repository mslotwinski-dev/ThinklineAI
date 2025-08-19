<template>
  <ul v-if="array.length > 0">
    <li v-for="(content, index) in array" :key="index">
      {{ content }}
    </li>
  </ul>
  <form class="none" v-else>
    <div class="nocont">
      {{ $t('project.content.none') }} <ic icon="carrot" />
    </div>
    <div class="generate">{{ $t('project.content.generate') }}</div>
    <button>{{ $t('project.content.button') }}</button>
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    array: {
      type: Array,
      default: () => [],
    },
  },
})
</script>

<style lang="scss" scoped>
ul {
  list-style: none;
  padding: 0;

  li {
    padding: 8px 12px;
    background: $dark;
    transition: 0.2s all;
    border-radius: 10px;
    margin: 10px 0;

    &:hover {
      background: darken($dark, 5%);
    }
  }
}

.none {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 5px;

  .nocont {
    font-weight: 500;
    font-size: 17px;
  }

  button {
    border-radius: 8px;
    border: none;
    color: $light;
    font-size: 16px;
    max-width: 300px;
    padding: 5px 10px;
    cursor: pointer;
    transition: all 0.3s ease;
    background: $main2;
    color: $light;
    margin: 10px 0;

    &:hover {
      filter: brightness(1.1);
      transform: translateY(-2px);
    }

    &:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      filter: none;
      transform: none;
    }
  }
}
</style>
