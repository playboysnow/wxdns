<template>   
  <div class="hello" >

    <div class="label_send">
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
</div>

<div class="input">送信内容（表达歉意、告白、祝福等，推荐与对方面对面进行；若联系不上“比如被拉黑”，可采用此方式。切不可频繁发送打扰对方的生活）
   
  <el-input label="内容" type="textarea" :rows="8" id="area" maxlength="1340" v-model="textarea" placeholder="请输入内容，不允许特殊字符，不超过1340个字"  clearable></el-input>
  <p><span id="text-count">字数限制</span>1340个</p>

  </div>
</div>

</template>

<script>
/*
todo:
1、手机号格式校验
2、输入框剩余字数统计、特殊字符校验
3、数据封装、传后端接口
4、选择说吧时，弹出提示框，功能开发中
5、查询按钮放置、帮助页面
6、说吧页面显示，弹框提示
 */
  export default {
    
    name: 'send_sms',
    data() {
      var validatePhone = (rule, value, callback) => {
      if (/^1[34578]{1}\d{9}$/.test(value) == false) {
        callback(new Error("请输入正确的手机号"));
      } else {
        callback();
      }
    };
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
.al{
      z-index: 2;
     position:absolute;
    background: rgba(0, 0, 0, 0);
  top: 10%;
  border:none;  
}
.al_button{
      z-index: 2;
     position:absolute;
    background: rgba(0, 0, 0, 0);
  top: 10%;
  left:90%;
  border:none;  
}

.hello{
      z-index: 2;
     position:absolute;
    width: 920px;
  height:   200px;
    background: rgba(0, 0, 0, 0);
  top: 30%;
  left: 15%;
  border:none;
  
}
.label_send{
      z-index: 2;
     position:absolute;
    width: 920px;
  height:   100px;
    background: rgba(0, 0, 0, 0);

  border:none;
}
.input{
  z-index: 2;
  position:absolute;
  width: 920px;
  height:   100px;
  top: 40%;
  font-size: large;
  font-weight:bold;
  background: rgba(0, 0, 0, 0);
  border:none;

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
