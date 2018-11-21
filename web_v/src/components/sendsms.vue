<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    
  </div>
</template>

<script>

export default {
  name: 'sendsms',
  data () {
    return {
      msg: 'sendsms'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
      z-index: 2;
     position:absolute;
     width: 50px;
  height:   50px;
    background: rgba(0, 0, 0, 0);
  top: 20%;
  left: 20%;
  border:none;
}
</style>
