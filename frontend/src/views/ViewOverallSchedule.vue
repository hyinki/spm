<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="/homepage">PlanPro</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/homepage"
              >Home</a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/viewoverallschedule"
              >View Overall Schedule</a
            >
          </li>

          <li class="nav-item">
            <a class="nav-link" href="/viewteamschedule">View Team Schedule</a>
          </li>
        </ul>

        <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <span class="nav-link">
                <img
                  :src="accountIcon"
                  alt="Account"
                  style="width: 20px; margin-right: 5px"
                />
                Hello, {{ userRole }}
              </span>
            </li>
            <li class="nav-item">
              <button class="btn btn-primary" @click="logout">Logout</button>
            </li>
          </ul>
      </div>
    </div>
  </nav>
  <div>
    <h1>Welcome to the viewoverallschedule</h1>
  </div>
</template>


<script>
import { mapGetters } from "vuex";
import accountIcon from "@/assets/account.png"; // Import the account icon
import Cookies from "js-cookie"; // Import js-cookie to manage cookies
import axios from "axios"; // Import axios for API requests

export default {
  name: "viewoverallschedule",
  data() {
    return {
      accountIcon: accountIcon, // Make the imported icon available to the template
    };
  },
  computed: {
    ...mapGetters(["userRole"]), // Access the user's role from Vuex
    
  },
  methods: {
    async logout() {
      try {
        await axios.post(
          "http://localhost:5000/logout",
          {},
          { withCredentials: true }
        ); // Make POST request to logout
        Cookies.remove("Staff_ID");
        Cookies.remove("userRole");
        this.$router.push("/login"); // Redirect to the login page after logout
      } catch (error) {
        console.error("Logout failed:", error); // Handle any errors that occur during logout
      }
    },
  },
};
</script>
