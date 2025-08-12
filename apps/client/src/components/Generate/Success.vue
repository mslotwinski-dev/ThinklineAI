<template>
  <div class="title">
    {{ $t('generate.success') }}
    <span class="gold">
      <ic icon="truck-fast" />
    </span>
  </div>
  <div class="desc">
    {{ $t('generate.success_description') }}
  </div>

  <div class="buttons">
    <div class="buttoncont">
      <div>{{ $t('generate.lfse') }}</div>

      <button @click="regenerateProjects">
        {{ $t('generate.regenerate') }}
      </button>
    </div>

    <div class="buttoncont">
      <div>{{ $t('generate.done') }}</div>
      <button :disabled="!counter" @click="$router.push('/projects')">
        {{ $t('generate.projects') }}
      </button>
    </div>
  </div>

  <div class="project-list">
    <Project
      v-for="(project, index) in projects"
      :key="index"
      :project="project"
      @added="counter++"
      @removed="counter--"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Project from './Project.vue'

export default defineComponent({
  props: {
    projects: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      counter: 0,
    }
  },
  components: {
    Project,
  },
  methods: {
    regenerateProjects() {
      this.$emit('regenerate')
    },
  },
})
</script>

<style lang="scss" scoped>
button {
  border-radius: 8px;
  border: none;
  color: $light;
  font-size: 16px;
  max-width: 300px;
  padding: 10px;
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

.title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  .gold {
    color: $gold;
    &:after {
      content: '';
    }
  }
}

.buttoncont {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px 0;
  margin-top: 20px;
}

.buttons {
  display: flex;
  gap: 20px;
  padding: 5px;
}

.project-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
