<template>
    <form>
        <div class="field">
            <input v-model="user_id" class="input" type="number" placeholder="user's id">
            <p/>
            <input v-model="form.body" class="input" type="text" placeholder="body">
            <p/>
            <button class="button is-primary" type="button" v-on:click="submit">Submit</button>
        </div>
    </form>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      disabled:false,
      user_id:null,
      form:{body:null}
    };
  },
  
  methods: {
    async submit(){
      try {
        const q = "users/" + this.user_id + "/texts/"
        axios.post(q,this.form)
        this.form.body = null
        this.user_id = null
      } catch (error) {
        console.log(error);
      }
    }
  },
};
</script>