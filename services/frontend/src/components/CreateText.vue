<template>
    <form>
        <div class="field">
            <input v-model="user_mail" class="input" placeholder="pseudonym">
            <input v-model="pwd" class="input" type="password" placeholder="password">
            <div class="form-group">
              <label for="exampleFormControlTextarea1">Example textarea</label>
              <textarea v-model="form.body" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            </div>
            <button class="button is-primary" type="button" v-on:click="submit">Submit</button>
        </div>
    </form>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      user_mail:null,
      pwd:null,
      form:{body:null}
    };
  },
  
  methods: {
    async submit(){
      try {
        const q = "users/" + this.user_mail + "/texts/"
        await axios.post(q,this.form)
        this.form.body = null
        this.user_mail = null
        this.pwd = null
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