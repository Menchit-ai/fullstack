<template>
    <form>
        <div class="field">
            <input v-model="form.email" class="input" type="email" placeholder="email">
            <p/>
            <input v-model="form.password" class="input" type="password" placeholder="pwd">
            <p/>
            <button class="button is-primary" v-on:click="submit">Submit</button>
        </div>
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
        axios.post("users/",this.form)
      } catch (error) {
        console.log(error);
      }
    }
  },
};
</script>