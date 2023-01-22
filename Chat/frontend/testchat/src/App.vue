
<template>
<div class="dada">
  <!-- Comment  <div>{{chatArr}}</div> -->
  <div class="vftest"  v-for="chat in chatArr" :key="chat">
  <div class="tmp">{{chat}}</div>
  </div>
  <!-- Comment
  <div class="mainErea">
    <oneLog uname="こころ" msg="おは"/>
  </div>
  -->
  <input  v-model="message" type="text" placeholder="cocoroに話しかけましょう">
  <button v-on::click="good2">送信</button><br>
  <div class="setumei">
  cocoroは言葉遣いが怖いです<br>
  ♡を付けて話すと優しくなります<br>
  </div>
  <!-- Comment
  <button v-on::click="good2">Send2</button>
  -->


</div>
</template>

<script>

//import oneLog from "./components/oneLog";
import axios from 'axios';


export default {
  name: 'App',
  data() {
    return { count: 4 ,
    chatArr:[],
    baseArr:[],
    message:'',
    }
  },
  components: {
    //oneLog,
  },
  methods: {
    increment() {
      // `this` はコンポーネントインスタンスを参照
      this.count++
    },
    good(){
      console.log('fss');
      this.chatArr.push(this.message);
      this.message='';
    },
    good2(){
      //document.body.appendChild(document.createElement("div"));
      this.chatArr.push('自分:'+this.message);
      
      axios
      /** 
          .get("http://127.0.0.1:5000/chat/api",{
            params: {
            // ここにクエリパラメータを指定する
            value:this.message
            }   
          })
          */
          .get("http://127.0.0.1:5000/chat/api",{
            params: {
            // ここにクエリパラメータを指定する
            value:this.message
            }
          })//end
          .then((res) => {
            console.log(res['data']);
            console.log('p');
            console.log(res['data']);
            //this.posts = res.data.posts;
            this.chatArr.push('cocoro:'+res['data']);
            this.message='';
          })
          .catch((err) => {
            console.log(err);
            console.log('q');
          });
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.vftest {
  margin-top: 2px;
  text-align: left;
  background-color: #8cf183;
}

.setumei {
  margin-top: 5px;
  text-align: center;
  background-color: #b9b8b8;
}
</style>
