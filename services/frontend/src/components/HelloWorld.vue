<template>
  <div>
    <p> {{ message }} </p>
    <p> Le but ici est de deviner si le texte proposé est écrit par un humain ou une intelligence artificielle. </p>
    <p> Les textes humains sont créés par les visiteurs du site, qui alimentent la base de données. Quant aux textes IA, ils sont générés régulièrement par l'IA de texte GPT2. </p>
    <p> Pour proposer un nouveau texte, il faut d'abord vous enregistrer. Cliquez sur "Register" pour créer un compte avec votre email. Ensuite, vous pourrez proposer vos textes avec 
    l'onglet "Write new text". </p>
    <p> Si vous voulez jouer au jeu, cliquez sur l'onglet "Quizz". Un trexte vous sera proposé, et il faudra deviner si il provient d'un cerveau humain ou robotique! </p>
    <p> Sachez que ceci a été écrit par un humain bien entendu, même si notre IA a le potentiel d'écrire ce texte. </p>
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
        const response = await axios.get("/");
        this.message = "Bienvenue sur notre site de quizz : IA ou humain ?";
        console.log(response)
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
  @import "@/form.scss"; //Here i add extra "./"(current directory)
</style>