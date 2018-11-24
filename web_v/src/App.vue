<template>
    <div class="homepage-hero-module">
      <router-view></router-view>
      <div class="video-container">
        <div :style="fixStyle" class="filter"></div>
        <video :style="fixStyle" autoplay loop class="fillWidth" v-on:canplay="canplay">
          <source src="../static/mz.mp4" type="video/mp4"/>
        浏览器不支持 video 标签，建议升级浏览器。
        </video>
          <div  class="poster hidden" v-if="!vedioCanPlay">
            <img :style="fixStyle" src="../static/basic.jpg" alt="">
      </div>
    </div>
  </div>  
</div>
</template>

<script>

import router from './router';
export default {
  name: 'app',
   data() {
      return {
        vedioCanPlay: true,
        fixStyle: ''
      }
    },
  created () {
        router.push({name: 'index'});
    },
  methods: { 
    canplay() {
        this.vedioCanPlay = true
      },
    
    goto: function () {
      router.push({name: 'index'});
    }
 },
 mounted: function() {
      window.onresize = () => {
        const windowWidth = document.body.clientWidth
        const windowHeight = document.body.clientHeight
        const windowAspectRatio = windowHeight / windowWidth
        let videoWidth
        let videoHeight
        if (windowAspectRatio < 0.5625) {
          videoWidth = windowWidth
          videoHeight = videoWidth * 0.5625
          this.fixStyle = {
            height: windowWidth * 0.5625 + 'px',
            width: windowWidth + 'px',
            'margin-bottom': (windowHeight - videoHeight) / 2 + 'px',
            'margin-left': 'initial'
          }
        } else {
          videoHeight = windowHeight
          videoWidth = videoHeight / 0.5625
          this.fixStyle = {
            height: windowHeight + 'px',
            width: windowHeight / 0.5625 + 'px',
            'margin-left': (windowWidth - videoWidth) / 2 + 'px',
            'margin-bottom': 'initial'
          }
        }
      }
      window.onresize()
    }
}
</script>



<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.homepage-hero-module,
  .video-container {
    position: relative;
    height: 100vh;
    overflow: hidden;
  }

  .video-container .poster img,
  .video-container video {
    z-index: 0;
    position: absolute;
  }

  .video-container .filter {
    z-index: 1;
    position: absolute;
    background: rgba(0, 0, 0, 0.4);
  }
</style>
