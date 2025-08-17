<template>
  <div class="container" v-if="display">
    <Header :project="project" @reload="reloadProject" />

    <div class="tabs">
      <div
        v-for="(button, index) in buttons"
        :key="index"
        @click="mode = index"
        :class="{ active: mode === index }"
      >
        <ic :icon="icons[index]" />
        <span>{{ button }}</span>
      </div>
    </div>

    <section>
      <Basics v-if="mode == 0" />
      <Functionalities v-if="mode == 1" />
      <Technologies v-if="mode == 2" />
      <Software v-if="mode == 3" />
      <Business v-if="mode == 4" />
      <Security v-if="mode == 5" />
      <Notes v-if="mode == 6" />
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
import Notes from '@/components/Project/Notes.vue'

export default defineComponent({
  data() {
    return {
      display: false,
      mode: 0,
      project: {} as Project,
      buttons: [
        'Basics',
        'Functionalities',
        'Technologies',
        'Software',
        'Business',
        'Security',
        'Notes',
      ],
      icons: [
        'file',
        'diagram-project',
        'code',
        'folder-open',
        'coins',
        'file-shield',
        'pen-clip',
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
    Notes,
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
  margin-bottom: 30px;

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
  flex-direction: column;
  gap: 30px;

  .header {
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 12px;
    text-transform: uppercase;
  }

  .box {
    padding: 12px;
    border-radius: 10px;
    height: 200px;
    // overflow-y: scroll;
    background: $dark;

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
    &.h400 {
      height: 400px;
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
