<template>
  <div class="box centered" :style="{ height: size + 'px' }">
    <span v-if="content">
      {{ content }}
    </span>

    <form class="none" v-else>
      <div class="nocont">
        {{ $t('project.content.none') }} <ic icon="carrot" />
      </div>
      <div class="generate">{{ $t('project.content.generate') }}</div>
      <button>{{ $t('project.content.button') }}</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    size: {
      type: Number,
      default: 200,
    },
    content: {
      type: String,
      default: '',
    },
  },
})
</script>

<style lang="scss" scoped>
.box {
  padding: 12px;
  border-radius: 10px;
  height: 200px;
  // overflow-y: scroll;
  background: $dark;
  margin-top: 12px;
  flex-grow: 1;
  font-size: 14.5px;
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
