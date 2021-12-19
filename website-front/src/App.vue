<template>

  <div id="nav">
    <Header/>
    <router-view/>
  </div>
   
  
</template>
<script>
  import Header from './components/Header.vue'
  export default {
  components: {
    Header
  }
}
</script>
<style>
@import "./style/pagestyle.css";
</style>
