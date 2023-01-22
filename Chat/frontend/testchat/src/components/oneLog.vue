<template>
    <div class="hole">
    <div class="uname">あ{{uname}}</div>
    <div class="umessage">{{msg}}</div>
    </div>
</template>
  
  <script>
  export default {
    
    name: 'oneLog',
    props: {
      uname: String,
      msg: String,
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  