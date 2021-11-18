<template>
  <form>
      <div class="form-group">
        <label for="inputEmail">Email address</label>
        <input v-model="form.email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input v-model="form.password" type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
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
        await axios.post("users/",this.form).catch(error => {console.log(error)})
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
  @import "@/form.scss"; //Here i add extra "./"(current directory)
</style>