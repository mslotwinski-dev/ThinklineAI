<template>
  <div v-if="array.length > 0">
    <div class="box centered" v-for="(usecase, index) in array" :key="index">
      <div class="flex">
        <div class="name">{{ usecase.name }}</div>
        <div class="actor">
          <div class="small">{{ $t('project.usecases.actor') }}</div>
          {{ usecase.actor }}
        </div>
        <div class="goal">
          <div class="small">
            {{ $t('project.usecases.goal') }}
          </div>
          {{ usecase.goal }}
        </div>
      </div>

      <div class="flex">
        <ol class="flow">
          <li v-for="(step, index) in usecase.flow" :key="index">
            {{ step }}
          </li>
        </ol>
      </div>
    </div>
  </div>
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
import { UseCase } from '@/types/project'

export default defineComponent({
  props: {
    array: {
      type: Array as () => UseCase[],
      default: () => [
        // {
        //   name: 'Otworzenie gry',
        //   actor: 'Gracz',
        //   goal: 'Rozpoczęcie nowej gry',
        //   flow: [
        //     'Uruchomienie aplikacji',
        //     'Utworzenie nowego zapisu',
        //     'Wybór poziomu trudności',
        //     'Rozpoczęcie rozgrywki',
        //   ],
        // },
      ],
    },
  },
})
</script>

<style lang="scss" scoped>
.box {
  padding: 12px;
  border-radius: 10px;
  height: 150px;
  // overflow-y: scroll;
  background: $dark;
  margin-top: 12px;
  flex-grow: 1;
  font-size: 14.5px;
  display: flex;
  gap: 20px;
}

.flex {
  display: flex;
  flex-direction: column;
  justify-content: center;
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

.name {
  font-weight: 500;
  text-transform: uppercase;
}

.actor,
.exceptions,
.goal {
  margin-top: 5px;
}

ol {
  padding: 0;
  margin: 0;
  border-left: 3px solid $main2;

  li {
    margin-left: 40px;
    margin-bottom: 9px;
  }
}

.small {
  font-size: 11px;
  margin-top: 5px;
  color: $dark_gray;
}
</style>
