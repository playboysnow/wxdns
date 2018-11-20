<template>
  <div class="fd-say">
           <button class="fd-say" @click="go">日常</button>
           <router-view/>
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
      router.push({name: 'query'});
    }
 }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style type="text/css">
   .fd-say{
     
     position:relative;
     width: 50px;
  height:   50px;
    background: rgba(0, 0, 0, 0);
  top: 70%;
  left: 30%;
  border:none;
} 
</style>  

