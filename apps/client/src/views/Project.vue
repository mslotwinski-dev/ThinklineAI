<template>
  <div>
    {{ project }}
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useProjectsStore } from '@/store/projects'
import { Project } from '@/types/project'

export default defineComponent({
  data() {
    return {
      project: {} as Project,
    }
  },
  mounted() {
    const project = useProjectsStore()
      .read()
      .find((p) => p.ID === this.$route.params.id)

    if (project) {
      this.project = project
    } else {
      this.$router.push('/P404')
    }
  },
})
</script>

<style lang="scss" scoped></style>
