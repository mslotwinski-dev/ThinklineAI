<template>
  <div class="container" v-if="display">
    <Header :project="project" @reload="reloadProject" />

    <div class="tabs">
      <div
        v-for="(key, index) in [
          'project.buttons.basics',
          'project.buttons.functionalities',
          'project.buttons.technologies',
          'project.buttons.software',
          'project.buttons.business',
          'project.buttons.security',
          'project.buttons.growth',
        ]"
        :key="index"
        @click="mode = index"
        :class="{ active: mode === index }"
      >
        <ic :icon="icons[index]" />
        <span>{{ $t(key) }}</span>
      </div>
    </div>

    <section>
      <Basics v-if="mode == 0" :project="project" />
      <Functionalities v-if="mode == 1" :project="project" />
      <Technologies v-if="mode == 2" :project="project" />
      <Software v-if="mode == 3" :project="project" />
      <Business v-if="mode == 4" :project="project" />
      <Security v-if="mode == 5" :project="project" />
      <Growth v-if="mode == 6" :project="project" />
    </section>
  </div>
  <div class="container" v-else>
    <Loading />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { useProjectsStore } from '@/store/projects'
import { Project } from '@/types/project'

import Loading from '@/components/Generate/Wait.vue'
import Header from '@/components/Project/Header.vue'
import Basics from '@/components/Project/Basics.vue'
import Functionalities from '@/components/Project/Functionalities.vue'
import Technologies from '@/components/Project/Technologies.vue'
import Software from '@/components/Project/Software.vue'
import Business from '@/components/Project/Business.vue'
import Security from '@/components/Project/Security.vue'
import Growth from '@/components/Project/Growth.vue'

export default defineComponent({
  data() {
    // I18N

    this.$t('project.buttons.basics')
    this.$t('project.buttons.functionalities')
    this.$t('project.buttons.technologies')
    this.$t('project.buttons.software')
    this.$t('project.buttons.business')
    this.$t('project.buttons.security')
    this.$t('project.buttons.growth')

    return {
      display: false,
      mode: 0,
      project: {} as Project,

      icons: [
        'file',
        'diagram-project',
        'code',
        'folder-open',
        'coins',
        'file-shield',
        'graduation-cap',
      ],
    }
  },
  components: {
    Header,
    Loading,
    Basics,
    Functionalities,
    Technologies,
    Software,
    Business,
    Security,
    Growth,
  },
  methods: {
    reloadProject() {
      this.display = false
      const project = useProjectsStore()
        .read()
        .find((p) => p.ID === this.$route.params.id)
      if (project) {
        this.project = project
        this.display = true
      } else {
        this.$router.push('/P404')
      }
    },
  },
  mounted() {
    this.reloadProject()
  },
})
</script>

<style lang="scss" scoped>
.container {
  width: 1200px;
  margin: 20px auto;
  border-radius: 20px 20px 0 0;
  overflow: hidden;
}

.tabs {
  background: $dark;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  overflow: hidden;
  margin-bottom: 20px;

  div {
    background: $dark;
    flex-grow: 1;
    text-align: center;
    cursor: pointer;
    padding: 10px;
    transition: 0.2s all;
    border-left: 2px solid #242f33;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    gap: 8px;

    span {
      font-size: 15px;
    }

    &:hover {
      filter: brightness(0.9);
    }
  }

  .active {
    background: #202a2d;
  }
}
</style>

<style lang="scss">
.global-project-page {
  display: flex;
  gap: 30px;

  .column {
    display: flex;
    flex-direction: column;
    gap: 30px;
    min-width: 400px;
    &.grow {
      flex-grow: 1;
    }

    &.between {
      justify-content: space-between;
    }
  }

  .header {
    font-size: 20px;
    font-weight: 500;
    text-transform: uppercase;
  }

  .section {
    .bar {
      content: '';
      display: block;
      background: red;
      border-radius: 10px;
      width: 5px;
    }

    & > div {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }
    flex-grow: 1;
    display: flex;
    gap: 15px;
  }

  .box {
    padding: 12px;
    border-radius: 10px;
    height: 200px;
    // overflow-y: scroll;
    background: $dark;
    margin-top: 12px;
    flex-grow: 1;

    &.h50 {
      height: 50px;
    }

    &.h100 {
      height: 100px;
    }
    &.h150 {
      height: 150px;
    }
    &.h200 {
      height: 200px;
    }
    &.h250 {
      height: 250px;
    }
    &.h300 {
      height: 300px;
    }
    &.h350 {
      height: 350px;
    }
    &.h400 {
      height: 400px;
    }
    &.h450 {
      height: 450px;
    }
    &.h500 {
      height: 500px;
    }
  }

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
}
</style>
