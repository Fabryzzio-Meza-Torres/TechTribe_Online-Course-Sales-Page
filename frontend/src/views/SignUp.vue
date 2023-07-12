<template>
  <div>
    <h1>Sign Up!</h1>
    <div v-if="!isUserSubmitted">
      <form @submit.prevent.stop="signUpEvent">
        <div class="form-group">
          <label>First Name:</label>
          <input type="text" v-model="user.firstname" />
        </div>
        <div class="form-group">
          <label>Last Name:</label>
          <input type="text" v-model="user.lastname" />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <input type="email" v-model="user.email" />
        </div>
        <div class="form-group">
          <label>Password:</label>
          <input type="password" v-model="user.contrasena" />
        </div>
        <button class="submit-button" type="submit">Submit</button>
      </form>

      <div class="user-message-errors" v-if="errorLists.length > 0">
        <ul>
          <li v-for="error in errorLists" :key="error">
            {{ error }}
          </li>
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
        contrasena: "",
      },
      errorLists: [],
      isUserSubmitted: false,
    };
  },
  methods: {
    async signUpEvent() {
      const { success, errors = [], token = null } = await signUp(this.user);
      if (success) {
        this.isUserSubmitted = true;
        localStorage.setItem("TOKEN", token);
        setTimeout(() => {
          this.$router.push({ name: "cursos" });
        }, 2000);
      } else {
        this.errorLists = errors;
      }
    },
  },
};
</script>
