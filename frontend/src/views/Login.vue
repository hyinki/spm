<template>
  <div class="container">
    <h1 class="text-center mt-5">Login</h1>
    <form @submit.prevent="submitForm" class="mt-3">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input
          type="text"
          id="username"
          v-model="username"
          class="form-control"
          placeholder="Enter your username"
          required
        />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input
          type="password"
          id="password"
          v-model="password"
          class="form-control"
          placeholder="Enter your password"
          required
        />
        <a href="#" @click.prevent="forgotPassword">Forgot Password?</a>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import Cookies from "js-cookie"; // Import js-cookie to manage cookies
import axios from 'axios';  // Import axios for API requests
import { mapActions } from "vuex";
import Toastify from 'toastify-js';  // Import Toastify for notifications
import "toastify-js/src/toastify.css";  // Import Toastify CSS

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["login"]),
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:5000/login', {
          user_ID: this.username,
          password: this.password
        });

        // Handle successful login
        if (response.data.status === "success") {
          console.log(response.data)
          const fetchedRole = response.data.role;
          const Staff_ID = response.data.staffId; 
          const supervisor = response.data.supervisor; 

          console.log(Staff_ID)

          // Store the role in Vuex state
          this.login({ role: fetchedRole });

          // Set a cookie for the role, which expires in 7 days
          Cookies.set("userRole", fetchedRole, { expires: 7 });
          Cookies.set("Staff_ID", Staff_ID, { expires: 7 }); 
          Cookies.set("supervisor", supervisor, { expires: 7 }); 


          // Display success toast
          Toastify({
            text: `Login successful for ${this.username}`,
            duration: 3000,  // Toast duration in milliseconds
            close: true,     // Show close button
            gravity: "top",  // Position of toast
            position: "center", // Center horizontally
            backgroundColor: "#4caf50",  // Green for success
          }).showToast();

          this.$router.push("/homepage"); // Redirect after login
        } else {
          // Display error toast
          Toastify({
            text: `Login failed: ${response.data.message}`,
            duration: 3000,
            close: true,
            gravity: "top",
            position: "center",
            backgroundColor: "#f44336",  // Red for failure
          }).showToast();
        }
      } catch (error) {
        // Display error toast for request failure
        Toastify({
          text: `An error occurred: wrong username or password.`,
          duration: 3000,
          close: true,
          gravity: "top",
          position: "center",
          backgroundColor: "#f44336",  // Red for failure
        }).showToast();
      }
    },
    forgotPassword() {
      if (this.username) {
        // Display info toast
        Toastify({
          text: `Password reset link has been sent to ${this.username}`,
          duration: 3000,
          close: true,
          gravity: "top",
          position: "center",
          backgroundColor: "#2196f3",  // Blue for info
        }).showToast();
      } else {
        // Display warning toast
        Toastify({
          text: "Please enter your username to reset your password.",
          duration: 3000,
          close: true,
          gravity: "top",
          position: "center",
          backgroundColor: "#ff9800",  // Orange for warning
        }).showToast();
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
