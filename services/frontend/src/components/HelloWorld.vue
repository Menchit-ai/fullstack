<template>
  <div>
    <p> {{ message }} </p>
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
        this.message = response.data;
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