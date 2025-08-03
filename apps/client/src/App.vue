<template>
  <nav>
    <img src="@/assets/logo.png" />
    Polistats
  </nav>
  <router-view />
</template>

<style lang="scss">
nav {
  img {
    width: 50px;
    height: 50px;
    margin-right: 10px;
  }
  color: #fff;
  background-color: $main;
  border-radius: 10px;
  font-size: 20px;
  display: flex;
  align-items: center;
  padding: 5px;
}

.map path,
.map g,
.map svg {
  stroke-width: 0.37379283;
  stroke: #ddd;
  stroke-linecap: round;
}
</style>
