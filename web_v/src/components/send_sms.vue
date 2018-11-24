<template>   
  <div class="hello" >
    <el-form :inline="true" :model="formInline" class="demo-form-inline" >
    <el-form-item label="类型">
    <el-select v-model="formInline.region" placeholder="选择类型">
      <el-option label="短信" value="短信"></el-option>
      <el-option label="说吧" value="说吧"></el-option>
    </el-select>
    </el-form-item>
    <el-form-item label="手机号">
    <el-input v-model="formInline.remobile" placeholder="收件人手机号" clearable></el-input>
  </el-form-item>
   <el-form-item label="手机号">
    <el-input v-model="formInline.sendmobile" placeholder="本人手机号，用于接收回复" clearable></el-input>
  </el-form-item>
    <el-form-item>
    <el-button type="primary" @click="onSubmit">送信</el-button>
    </el-form-item>
</el-form>
  <el-input label="内容" v-model="input" placeholder="请输入内容,不包含特殊字符" clearable></el-input>
<div class="input">
  <el-input label="内容" type="textarea" autosize  v-model="textarea" placeholder="请输入内容，不允许特殊字符，不超过1340个字"  clearable></el-input>
  </div>
</div>
</template>

<script>
  export default {
    name: 'send_sms',
    data() {
      return {
        input: '',
        textarea: '',
        formInline: {
          remobile: '',
          sendmobile: '',
          region: ''
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
      z-index: 2;
     position:absolute;
    width: 920px;
  height:   200px;
    background: rgba(0, 0, 0, 0);
  top: 30%;
  left: 10%;
  border:none;
}
.input{
  z-index: 2;
  position:absolute;
  width: 920px;
  height:   100px;
  top: 60%;
}
.fd-help{
      z-index: 2;
     position:absolute;
     width: 150px;
  height:   50px;
    background: rgba(0, 0, 0, 0);
  top: 10%;
  left: 90%;
  border:none;
   font-size: large;
  font-weight:bold;
} 
.fd-query{
      z-index: 2;
     position:absolute;
     width: 150px;
  height:   50px;
    background: rgba(0, 0, 0, 0);
  top: 10%;
  left: 80%;
  border:none;
  font-size: large;
  font-weight:bold;
} 
</style>
