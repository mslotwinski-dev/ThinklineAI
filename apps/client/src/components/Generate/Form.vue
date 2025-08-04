<template>
  <form class="box" @submit.prevent="generate">
    <p class="desc">
      {{ $t('generate.description') }}
      <span class="color">
        <ic icon="mug-hot" />
      </span>
    </p>
    <div class="fields">
      <div class="field A">
        <label for="language" v-html="$t('generate.language')" />
        <input
          type="text"
          v-model="language"
          autocomplete="off"
          placeholder="JavaScript, Python, etc."
        />
        <label for="level" v-html="$t('generate.level')" />
        <select v-model="level" @change="level = $event.target.value">
          <option value="0" v-html="$t('levels.beginner')" />
          <option value="1" v-html="$t('levels.intermediate')" />
          <option value="2" v-html="$t('levels.advanced')" />
        </select>

        <label for="topic" v-html="$t('generate.topic')" />
        <select
          v-model="topic"
          id="topic"
          @change="topic = $event.target.value"
        >
          <option value="0" v-html="$t('generate.topics.web')" />
          <option value="1" v-html="$t('generate.topics.desktop')" />
          <option value="2" v-html="$t('generate.topics.mobile')" />
          <option value="3" v-html="$t('generate.topics.games')" />
          <option value="4" v-html="$t('generate.topics.ai')" />
          <option value="5" v-html="$t('generate.topics.data')" />
          <option value="6" v-html="$t('generate.topics.security')" />
          <option value="7" v-html="$t('generate.topics.electronics')" />
          <option value="8" v-html="$t('generate.topics.telecom')" />
          <option value="9" v-html="$t('generate.topics.physics')" />
          <option value="10" v-html="$t('generate.topics.others')" />
        </select>
      </div>
      <div class="field">
        <label for="language" v-html="$t('generate.tags')" />
        <input
          type="text"
          v-model="tags[0]"
          :placeholder="$t(`generate.placeholders.tag.A`)"
          autocomplete="off"
        />
        <input
          type="text"
          v-model="tags[1]"
          :placeholder="$t(`generate.placeholders.tag.B`)"
          autocomplete="off"
        />
        <input
          type="text"
          v-model="tags[2]"
          :placeholder="$t(`generate.placeholders.tag.C`)"
          autocomplete="off"
        />
        <input
          type="text"
          v-model="tags[3]"
          :placeholder="$t(`generate.placeholders.tag.D`)"
          autocomplete="off"
        />
      </div>
    </div>
    <button v-html="$t('generate.button')" />
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import axios from '@/config/axios'

export default defineComponent({
  data() {
    return {
      language: '',
      tags: ['', '', ''],
      level: 0,
      topic: 0,
    }
  },
  methods: {
    generate() {
      axios
        .post('/generate', {
          language: this.language,
          topic: this.topic,
          tags: this.tags,
          level: this.level,
          locale: localStorage.getItem('locale') || 'en',
        })
        .then((response) => {
          if (response.data.success) {
            console.log('Generation successful:', response.data)
            // this.$router.push({
            //   name: 'GenerateResult',
            //   params: { id: response.data.id },
            // })
          } else {
            // this.$toast.error(this.$t('generate.error'))
          }
        })
        .catch((error) => {
          console.error(error)
          // this.$toast.error(this.$t('generate.error'))
        })
    },
  },
})
</script>

<style lang="scss" scoped>
.box {
  background-color: $dark;
  margin: 10px;
  padding: 20px;
  width: 100%;
  max-width: 1000px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 0 10px $violet;
}

.desc {
  margin-bottom: 30px;
}

input,
select,
button {
  width: 100%;
  padding: 7px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  background-color: $black;
  color: $light;
  font-size: 14px;
}

input:focus,
select:focus {
  box-shadow: 0 0 10px $violet;
}

button {
  max-width: 300px;
  padding: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  background: $violet;
  margin-top: 20px;

  &:hover {
    filter: brightness(1.1);
    transform: translateY(-2px);
  }
}

.field {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 400px;
  &.A {
    width: 330px;
  }
}

.fields {
  display: flex;
  justify-content: space-evenly;
  width: 100%;
}

label {
  font-size: 12px;
}

.color {
  color: $main;
}
</style>
