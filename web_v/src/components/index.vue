<template>
  <div>
  <div class="fd-button">
           <button class="fd-button" @click="go">我想对你说</button>
           
         </div>   
    <div class="fd-back">
          <button class="fd-back" @click="back">说吧</button>
          
         </div>  
    <router-view></router-view>   
  </div>
</template>

<script>
import router from '../router';
export default {
  name: 'index',
  data (){
    return {
     
    }
  },
  methods: { 
    go: function () {
      router.push({name: 'send_sms'});
    },
    back: function () {
      router.push({path: '/group'});
    }
 }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style type="text/css">
   .fd-button{
      z-index: 2;
     position:absolute;
     width: 150px;
  height:   50px;
    background: rgba(0, 0, 0, 0);
  top: 70%;
  left: 20%;
  border:none;
   font-size: large;
  font-weight:bold;
} 
  .fd-back{
      z-index: 2;
     position:absolute;
     width: 150px;
  height:   50px;
    background: rgba(0, 0, 0, 0);
  top: 80%;
  left: 40%;
  border:none;
  font-size: large;
  font-weight:bold;
} 

</style>  

