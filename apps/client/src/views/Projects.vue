<template>
  <div class="container" v-if="projects.length > 0">
    <div class="title">
      {{ $t('projects.hello') }}
      <span class="gold">
        <ic icon="diagram-project" />
      </span>
    </div>
    <p>
      {{ $t('projects.description') }}
    </p>

    <div class="projects">
      <div
        class="project-container"
        v-for="project in projects"
        :key="project.id"
      >
        <div class="project" @click="$router.push('/projects/' + project.ID)">
          <div class="name" v-html="project.name"></div>
          <div class="tags">
            <div
              v-for="tag in project.tags.filter((n) => n).slice(0, 3)"
              :key="tag"
              class="tag"
              v-html="tag"
            />
          </div>
        </div>
        <div class="buttons">
          <div @click="HandleRemove(project)">
            <ic icon="remove" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="empty">
    <p>{{ $t('projects.empty') }}</p>
    <div>{{ $t('projects.addmore') }}</div>
    <div class="icon">
      <ic icon="sailboat" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { useProjectsStore } from '@/store/projects'
import { Project } from '@/types/project'

export default defineComponent({
  data() {
    return {
      projects: useProjectsStore().read(),
    }
  },
  methods: {
    // HandleSave(project: Project) {
    //   useProjectsStore().addProject(project)
    // },
    HandleRemove(project: Project) {
      useProjectsStore().removeProject(project)
      this.projects = useProjectsStore().read()
    },
  },
})
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  min-height: calc(85vh - 110px);
}

.title {
  text-align: center;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  .gold {
    color: $gold;
  }
}

.project {
  display: flex;
  align-items: center;
  width: 1000px;
  padding: 5px 10px;
  border-radius: 10px;
  background: $dark;
  justify-content: space-between;
  cursor: pointer;
  .name {
    font-size: 16px;
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
    margin-top: 0.5rem;

    .tag {
      background-color: $violet;
      border-radius: 4px;
      padding: 0.25rem 0.5rem;
      margin-right: 0.5rem;
      margin-bottom: 0.5rem;
    }
  }
}

.project-container {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 1rem;
}

.buttons {
  display: flex;
  gap: 10px;

  div {
    cursor: pointer;
    font-size: 25px;
    color: $rose;
  }
}

.empty {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: calc(85vh - 110px);
  font-size: 20px;
  p {
    font-size: 25px;
  }

  .icon {
    color: $main;
    font-size: 100px;
    padding: 20px;
  }
}
</style>
