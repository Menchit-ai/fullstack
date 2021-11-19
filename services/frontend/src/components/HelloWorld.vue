<template>
  <div>
    <p> {{ message }} </p>
    <p> The goal here is to guess if the proposed text is written by a human or an artificial intelligence. </p>
    <p> Human texts are created by visitors, which feed the database. As for AI texts, they are generated regularly by the GPT2 AI text. </p>
    <p> To propose a new text, you must first register. Click on "Register" to create an account with your email. Then, you can submit your texts with
    the "Write new text" tab. </p>
    <p> If you want to play the game, click on the "Quizz" tab. You will be proposed a text, and you will have to guess if it comes from a human or robotic brain! </p>
    <p> Know that this text was written by a human of course, even though our AI has the potential to write this. </p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      message: ""
    };
  },
  
  methods: {
    async getData(){
      try {
        const response = await axios.get("/")
        this.message = response.body;
      } catch (error) {
        console.log(error);
      }
    }
  },

  created() {
    this.getData();
  },
};
</script>

<style lang="scss" scoped>
  @import "@/form.scss"; 
</style>