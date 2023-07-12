<template>
  <div class="form_register">
    <h1>Sign Up!</h1>
    <div v-if="!isUserSubmitted">
      <form @submit.prevent.stop="signUpEvent">
        <div class="form-group">
          <label>First Name:</label>
          <input type="text" v-model="user.firstname" class="controls" />
        </div>
        <div class="form-group">
          <label>Last Name:</label>
          <input type="text" v-model="user.lastname" class="controls" />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <input type="email" v-model="user.email" class="controls" />
        </div>
        <div class="form-group">
          <label>Password:</label>
          <input type="password" v-model="user.password" class="controls" />
        </div>
        <button class="botons" type="submit">Submit</button>
      </form>

      <div class="user-message-errors" v-if="errorLists.length > 0">
        <ul>
          <li v-for="error in errorLists" :key="error">{{ error }}</li>
        </ul>
      </div>
    </div>
    <div v-else>
      <span class="user-message-success">User created successfully!</span>
    </div>
  </div>
</template>

<script>
import { signUp } from "@/services/users.api";
export default {
  name: "SignUp",
  data() {
    return {
      user: {
        firstname: "",
        lastname: "",
        email: "",
        password: "",
      },
      errorLists: [],
      isUserSubmitted: false,
    };
  },
  methods: {
    async signUpEvent() {
      const response = await signUp(this.user);

      if (response && response.success) {
        this.isUserSubmitted = true;
        localStorage.setItem("TOKEN", response.token);
        setTimeout(() => {
          this.$router.push({ name: "cursos" });
        }, 2000);
      } else if (response && response.error) {
        this.errorLists = response.error;
      } else {
        this.errorLists = ["Usuario Creado"];
        console.log("Invalid response:", response);
      }
    },
  },
};
</script>

<style scoped>
.form_register {
  width: 400px;
  background: #24303c;
  padding: 30px;
  padding-right: 54px;
  margin: auto;
  border-radius: 4px;
  font-family: "calibri";
  color: white;
  box-shadow: 7px 13px 37px #000;
}

.form_register h1 {
  font-size: 31px;
  display: flex;
  margin-bottom: 20px;
}

.controls {
  width: 100%;
  background: #24303c;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 16px;
  border: 1px solid #1f53c5;
  font-family: "calibri";
  font-size: 18px;
  color: white;
}

.user-message-errors {
  height: 40px;
  text-align: center;
  font-size: 18px;
  line-height: 40px;
}

.user-message-errors a {
  color: white;
  text-decoration: none;
}

.user-message-errors a:hover {
  color: white;
  text-decoration: underline;
}

.botons {
  width: 423px;
  background: #1f53c5;
  border: none;
  padding: 12px;
  color: white;
  margin: 16px 0;
  font-size: 16px;
}
</style>
