<template>
  <div class="p404">
    <p>{{ $t('p404.title') }}</p>
    <div>{{ $t('p404.desc') }}</div>
    <div class="icon">
      <ic icon="bomb" />
    </div>
    <div class="buttons">
      <div class="buttoncont">
        {{ $t('p404.gotoprojects') }}
        <router-link to="/projects">
          <button>{{ $t('p404.link') }}</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({})
</script>

<style lang="scss" scoped>
.p404 {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: calc(85vh - 110px);
  p {
    font-size: 25px;
  }

  .icon {
    color: $gold;
    font-size: 100px;
    padding: 20px;
  }
}

.buttoncont {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px 0;
}

.buttons {
  display: flex;
  gap: 20px;
}

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
}
</style>
