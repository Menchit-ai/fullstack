<template>
  <form>
      <div class="form-group">
        <label for="inputName">Pseudonym</label>
        <input v-model="form.email" class="form-control" id="inputPseudo" placeholder="Enter pseudo">
      </div>
      <div class="form-group">
        <label for="InputPassword">Password</label>
        <input v-model="form.password" type="password" class="form-control" id="InputPassword" placeholder="Password">
      </div>
      <button type="button" class="btn btn-primary" v-on:click="submit">Submit</button>
    </form>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      disabled:false,
      form:{
          email:null,
          password:null
      }
    };
  },
  
  methods: {
    async submit(){
      try {
        await axios.post("users/",this.form)
        this.form.email = null
        this.form.password = null
      } catch (error) {
        console.log(error);
      }
    }
  },
};
</script>

<style lang="scss" scoped>
  @import "@/form.scss"; 
</style>