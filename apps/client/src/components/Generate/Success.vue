<template>
  <div class="project-list">
    <div v-for="(project, index) in projects" :key="index" class="item">
      <div class="name">{{ project.name }}</div>
      <p>{{ project.description }}</p>
      <div class="stack">
        <span v-html="$t('project.tech_stack')" />
        <div
          v-for="(tag, tagIndex) in project.tech_stack"
          :key="tagIndex"
          v-html="tag"
        />
      </div>
      <div class="tags">
        <span v-html="$t('project.tags')" />
        <div
          v-for="(tag, tagIndex) in project.tags"
          :key="tagIndex"
          v-html="tag"
        />
      </div>
      <div class="estimated">
        <span v-html="$t('project.estimated_time')" />
        {{ project.estimated_time }}
      </div>
      <div class="buttons">
        <div class="save">
          <ic icon="bookmark" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    projects: {
      type: Array,
      required: true,
    },
  },
})
</script>

<style lang="scss" scoped>
.item {
  padding: 20px;
  max-width: 1000px;
  margin: 10px auto;
  background-color: $dark;
  border-radius: 10px;
}

.name {
  font-size: 20px;
  font-weight: 500;
}

span {
  margin-right: 10px;
  &:after {
    content: ':';
  }
}

.stack,
.tags {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 5px;
  font-size: 14px;
  margin: 15px 0;
  div {
    padding: 5px 10px;
    background-color: $violet;
    border-radius: 5px;
  }
}

.tags div {
  background-color: $rose;
}

.estimated {
  font-size: 14px;
}

.save {
  cursor: pointer;
  background: $violet;
  font-size: 20px;
  padding: 5px;
  border-radius: 5px;
}

.buttons {
  position: absolute;
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
  bottom: 20px;
  right: 20px;
  gap: 15px;
}
</style>
