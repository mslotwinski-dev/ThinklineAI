<template>
  <div class="header" :style="{ background: project.color || '#2e4057' }">
    <div class="namecont">
      <div class="name">{{ project.name }}</div>
      <Colors :project="project" @click="reloadProject" />
    </div>
    <div class="desc">{{ project.description }}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Colors from '@/components/Project/Colors.vue'
import { Project } from '@/types/project'

export default defineComponent({
  components: {
    Colors,
  },
  props: {
    project: {
      type: Object as () => Project,
      required: true,
    },
  },
  methods: {
    reloadProject() {
      this.$emit('reload')
    },
  },
})
</script>

<style lang="scss" scoped>
.header {
  height: 150px;

  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 20px;
}

.namecont {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.name {
  font-size: 26px;
  text-transform: uppercase;
  font-weight: 500;
  padding: 10px 0;
}
</style>
