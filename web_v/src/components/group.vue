<template>
  <div class="group">
  <section>
    <mu-appbar title="说吧">
      <mu-flat-button label="写说说" icon="border_color" slot="right">
      </mu-flat-button>
    </mu-appbar>
    <mu-row>
      <mu-col width="20" tablet="20" desktop="20">
        &nbsp;
      </mu-col>
      <mu-col width="20" tablet="65" desktop="60">
        <mu-card>
          <mu-card-header title="snow" subTitle="大声地说出来">
            <mu-avatar slot="avatar">
            </mu-avatar>
          </mu-card-header>
          <mu-card-media title="关于说吧">
           
          </mu-card-media>
          <mu-card-title title="说吧" />
          <mu-card-text>
            交流论坛
          </mu-card-text>
        </mu-card>
      </mu-col>
      <mu-col width="20" tablet="20" desktop="20">
        &nbsp;
      </mu-col>
    </mu-row>
  </section>
  </div>
</template>



<style>
   .group{
      z-index: 2;
     position:absolute;
    width: 920px;
  height:   200px;
    background: rgba(0, 0, 0, 0);
  top: 10%;
  left: 10%;
} 
</style>

<script>
  export default {
    name: 'group',
    data() {
     
      return {
        
      }
    }
  };
</script>