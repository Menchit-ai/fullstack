<template>
  <div>
    <p> {{ current_text.body }} </p>
     <div class="btn-toolbar" style="margin:auto;display:block">
        <button class="btn btn-primary" v-on:click="isHuman">Is human</button>
        <button class="btn btn-primary" v-on:click="isAI" style="margin-left:10px">Is AI</button>
      </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      texts: [],
      current_text: {}
    };
  },
  
  methods: {
    async getData(){
      try {
        const response = await axios.get("/texts/")
        this.texts = response.data
        var randomText = this.texts[Math.floor(Math.random()*this.texts.length)]
        this.current_text = randomText
      } catch (error) {
        console.log(error);
      }
    },

    async isHuman(){
        try {
            const q = "texts/" + this.current_text.id + "/human_count"
            await axios.post(q)
            var randomText = this.texts[Math.floor(Math.random()*this.texts.length)]
            this.current_text = randomText
      } catch (error) {
        console.log(error);
      }
    },

    async isAI(){
        try {
            const q = "texts/" + this.current_text.id + "/ai_count"
            await axios.post(q)
            var randomText = this.texts[Math.floor(Math.random()*this.texts.length)]
            this.current_text = randomText
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    this.getData();
  },
};
</script>

<style lang="scss" scoped>
  @import "@/form.scss";
</style>