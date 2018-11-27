<template>   
  <div class="hello" >

    <div class="label_send">
    <el-form :inline="true" :model="formInline" class="demo-form-inline" >
    <el-form-item label="类型">
    <el-select id="func" v-model="formInline.region" placeholder="选择类型" @change="change">
      <el-option label="短信" value="短信"></el-option>
      <el-option label="说吧" value="说吧"></el-option>
    </el-select>
    
    </el-form-item>
    <el-form-item label="手机号" required  prop="remobile" :rules="[
    {required:ture, message:'必须为11位可用手机号',trigger:'blur'}
    
    ]">
    <el-input v-model="formInline.remobile" id="remob"  placeholder="收件人手机号" disable="isable" @keyup.native="checknum" clearable></el-input>
  </el-form-item>
   <el-form-item label="手机号"  prop="sendmobile"  :rules="[
    {required:ture, message:'必须为11位可用手机号',trigger:'blur'}
    
    ]">
    <el-input v-model="formInline.sendmobile"   placeholder="本人手机号，用于接收回复" disable="isable" @keyup.native="checknum" clearable></el-input>
  </el-form-item>
    <el-form-item>
    <el-button type="primary" @click="onSubmit()">送信</el-button>
    </el-form-item>
    
</el-form>
</div>

<div class="input">送信内容（表达歉意、告白、祝福等，推荐与对方面对面进行；若联系不上“比如被拉黑”，可采用此方式。切不可频繁发送打扰对方的生活）
   
  <el-input label="内容" type="textarea" :rows="8" id="area" maxlength="1340" @input="word" v-model="textarea" placeholder="请输入内容，不允许特殊字符，不超过1340个字 
禁止发送股票、移民、面试招聘、彩票、返利、贷款、催款、投资理财、赌博、中奖、一元夺宝、一元秒杀、A货、医疗、整形、美容、会所、酒吧、足浴、暴力、恐吓、色情、皮草、助考，商标注册、加群、加QQ或者加微信、贩卖个人信息、宣传短信通道、游戏推广、会展推广、网站推广、优惠券类推广、卡类推广、保险推广、酒类、用户拉新、用户召回，另外金融、房地产、教育这几类
问题交流反馈加QQ群：482818592" 
   clearable></el-input>
  <p><span id="text-count">字数限制</span>{{word_num}}/1340个</p>

  </div>
</div>

</template>

<script>
/*
todo:
1、手机号格式校验
2、输入框剩余字数统计(done)、特殊字符校验、内容加缓存
3、数据封装、传后端接口    done
4、选择说吧时，弹出提示框，功能开发中 done
5、查询按钮放置、帮助页面  
6、说吧页面显示，弹框提示  done
7、兼容safri
 */
  export default {
    
    name: 'send_sms',
    data() {

      return {
        word_num: 1340,
        textarea: '',
        isable:'false',
        formInline: {
          remobile: '',
          sendmobile: '',
          region: ''
        },
   
      }
    },
    methods: {
      /*字数统计 */
       word: function(){
         var txt=this.textarea.length;
         this.word_num=1340-txt;
       },
     /*手机号为数字 */
       checknum: function(callback){
        this.formInline.remobile=this.formInline.remobile.replace(/[^\.\d]/g,'');
        this.formInline.remobile=this.formInline.remobile.replace('.','');
        this.formInline.sendmobile=this.formInline.sendmobile.replace(/[^\.\d]/g,'');
        this.formInline.sendmobile=this.formInline.sendmobile.replace('.','');
         },
      /*下拉框监听 */
      change: function(callback) {
          if(this.formInline.region=="说吧"){
            
            this.$alert("说吧功能开发中", '提示', {
          confirmButtonText: '确定',
          callback: action => {
               this.formInline.region=="";
          },
          
        });
          
          }
      },
      onSubmit: function(callback) { 
        var isable=this.isable;
        var region=this.formInline.region;
        var remobile=this.formInline.remobile;
        var sendmobile=this.formInline.sendmobile;
        var textarea=this.textarea;
        /* 参数判断 */
         if(region=="说吧"){
            
            this.$alert("说吧功能开发中", '提示', {
          confirmButtonText: '确定',
          callback: action => {
               this.formInline.region=="";
          },
          
        });
          
          }
          else if (region=="") {
            this.$alert("类型不能为空", '提示', {
          confirmButtonText: '确定',        
        });
          }
          if (remobile=="") {
            this.$alert("收信人手机号不能为空", '提示', {
          confirmButtonText: '确定',        
        });
          }
          else if (remobile.length!=11){
            this.$alert("收信人手机号为11位数字", '提示', {
          confirmButtonText: '确定',        
        });
          }
        else if (sendmobile!=""&&sendmobile.length!=11){
            this.$alert("本人手机号为11位数字", '提示', {
          confirmButtonText: '确定',        
        });
          }
        var postdata = {
          "textarea":textarea,
          "remobile":remobile,
          "sendmobile":sendmobile,
          "region":region
        };
        /*调试参数
        this.$alert(postdata, '提示', {
          confirmButtonText: '确定',
          callback: action => {
           router.push({name: 'index'});
            
          },
          
        });*/
        this.$http.post('/api/send_sms',postdata).then(response => {
          response = response.body;
          //var data=response.data;
          //this.$alert(postdata)
          if (response.status==0){
            this.$alert("发送成功", '提示', {
          confirmButtonText: '确定',
          callback: action => {
           router.push({name: 'send_sms'});     
          },
          
        });
          }
          else {
             this.$alert("腾讯云服务已放弃（模板单一，涉及个人隐私），其他服务调研中", '提示', {
          confirmButtonText: '确定',
          /*
            this.$alert("发送失败", '提示', {
          confirmButtonText: '确定',
          callback: action => {
           router.push({name: 'send_sms'});     
          },
          */
        });
          }
        })
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
    width: 930px;
  height:   200px;
    background: rgba(0, 0, 0, 0);
  top: 30%;
  left: 15%;
  border:none;
  
}
.label_send{
      z-index: 2;
     position:absolute;
    width: 930px;
  height:   100px;
    background: rgba(0, 0, 0, 0);

  border:none;
}
.input{
  z-index: 2;
  position:absolute;
  width: 930px;
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
