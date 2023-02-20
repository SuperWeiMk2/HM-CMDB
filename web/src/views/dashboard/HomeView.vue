<template>
  <div class="home-view">
    <div class="welcome-text">欢迎使用 HM CMDB</div>
    <div class="version-text">v1.0.0</div>
    <div class="left-img">
      <img src="../../assets/image/undraw_left-img.svg" alt="" style="width: 100%;height: 100%;">
    </div>
    <div class="right-img">
      <img src="../../assets/image/undraw_right-img.svg" alt="" style="width: 100%;height: 100%;">
    </div>
  </div>
</template>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.welcome-text {
  font-size: 20pt;
}

.version-text {
  margin-top: 10px;
  font-size: 16pt;
}

.left-img {
  width: 200px;
  height: 150px;
  position: absolute;
  left: 20px;
  bottom: 0;
}

.right-img {
  width: 200px;
  height: 150px;
  position: absolute;
  right: 20px;
  bottom: 0;
}
</style>