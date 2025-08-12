<template>
  <div class="item" :class="{ saved }" @click="HandleSave()">
    <div class="name">{{ project.name }}</div>
    <p>{{ project.description }}</p>
    <div class="stack">
      <span v-html="$t('project.tech_stack')" />
      <div
        v-for="(tag, tagIndex) in project.tech_stack.filter((n) => n)"
        :key="tagIndex"
        v-html="tag"
      />
    </div>
    <div class="tags">
      <span v-html="$t('project.tags')" />
      <div
        v-for="(tag, tagIndex) in project.tags.filter((n) => n)"
        :key="tagIndex"
        v-html="tag"
      />
    </div>
    <div class="estimated">
      <span v-html="$t('project.estimated_time')" />
      {{ project.estimated_time }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Project } from '@/types/project'
import { useProjectsStore } from '@/store/projects'

export default defineComponent({
  props: {
    project: {
      type: Object as () => Project,
      required: true,
    },
  },
  emits: ['added', 'removed'],
  data() {
    return {
      saved: false,
    }
  },
  methods: {
    HandleSave() {
      this.saved = !this.saved
      if (this.saved) {
        useProjectsStore().addProject(this.project)
        this.$emit('added', this.project)
      } else {
        useProjectsStore().removeProject(this.project)
        this.$emit('removed', this.project)
      }
    },
  },
})
</script>

<style lang="scss" scoped>
.item {
  padding: 20px;
  width: 1000px;
  margin: 10px auto;
  background-color: $dark;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 0;
  transition: 0.2s all;
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

b {
  font-weight: 500;
}

.saved {
  box-shadow: 0 0 10px $violet;
}
</style>
