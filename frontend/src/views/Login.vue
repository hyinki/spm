<template>
  <div class="container">
    <h1 class="text-center mt-5">Login</h1>
    <form @submit.prevent="submitForm" class="mt-3">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <label for="username" class="form-label">Username</label>
        <input
          type="text"
          id="username"
          v-model="username"
          id="username"
          v-model="username"
          class="form-control"
          placeholder="Enter your username"
          placeholder="Enter your username"
          required
        />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <label for="password" class="form-label">Password</label>
        <input
          type="password"
          id="password"
          v-model="password"
          type="password"
          id="password"
          v-model="password"
          class="form-control"
          placeholder="Enter your password"
          placeholder="Enter your password"
          required
        />
        <a href="#" @click.prevent="forgotPassword">Forgot Password?</a>
        <a href="#" @click.prevent="forgotPassword">Forgot Password?</a>
      </div>

      <!-- Display error message -->
      <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'; // Import axios for HTTP requests
import Cookies from "js-cookie"; // Import js-cookie to manage cookies
import { mapActions } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "", // To store error messages from the backend
    };
  },
  methods: {
    ...mapActions(["login"]),
    async submitForm() {
      try {
        // Send login request to the backend
        const response = await axios.post("/api/login", {
          username: this.username,
          password: this.password,
        });

        // On success, store role and redirect
        const fetchedRole = response.data.role;
        this.login({ role: fetchedRole });
        Cookies.set("userRole", fetchedRole, { expires: 7 });

        this.$router.push("/homepage"); // Redirect to homepage

      } catch (error) {
        // Set the error message based on backend response
        if (error.response && error.response.status === 404) {
          this.errorMessage = "User not found";
        } else if (error.response && error.response.status === 401) {
          this.errorMessage = "Incorrect password";
        } else {
          this.errorMessage = "An unexpected error occurred. Please try again.";
        }
      }
    },
    forgotPassword() {
      if (this.username) {
        alert(`Password reset link has been sent to ${this.username}`);
      } else {
        alert("Please enter your username to reset your password.");
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 400px;
  margin-top: 50px;
}
</style>
