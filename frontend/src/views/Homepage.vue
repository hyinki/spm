<template>
  <!-- Staff Section -->
  <div v-if="isStaff">
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
              <a class="nav-link" href="/viewteamschedule">Team Schedule</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/viewownschedule">Own Schedule</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/applyforarrangement"
                >Apply For Arrangement</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/viewarrangement">View Arrangement</a>
            </li>
          </ul>
          <!-- Account Section -->
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
      <h1>Welcome to the HomePage (Staff)</h1>
    </div>

    <div>
      <router-link to="/viewteamschedule">
        <button type="button" class="btn btn-primary btn-lg m-5">
          View Team Schedule
        </button>
      </router-link>
    </div>

    <div>
      <router-link to="/viewownschedule">
        <button type="button" class="btn btn-primary btn-lg m-5">
          View Own Schedule
        </button>
      </router-link>
    </div>

    <div>
      <router-link to="/applyforarrangement">
        <button type="button" class="btn btn-primary btn-lg m-5">
          Apply For Arrangement
        </button>
      </router-link>
    </div>
  </div>

  <!-- Manager Section -->
  <div v-if="isManager">
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
              <a class="nav-link" href="/viewteamschedule"
                >View Team Schedule</a
              >
            </li>

            <li class="nav-item">
              <a class="nav-link" href="/arrangement"
                >Approve/RejectArrangement</a
              >
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
      <h1>Welcome to the HomePage (Manager)</h1>
    </div>

    <div>
      <router-link to="/viewteamschedule">
        <button type="button" class="btn btn-primary btn-lg m-5">
          View Team Schedule
        </button>
      </router-link>
    </div>

    <div>
      <router-link to="/arrangement">
        <button type="button" class="btn btn-primary btn-lg m-5">
          Approve/Reject Arrangement
        </button>
      </router-link>
    </div>
  </div>

  <!-- HR Section -->
  <div v-if="isHR">
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
                >View Overall Schedulet</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/viewteamschedule"
                >View Team Schedule</a
              >
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
      <h1>Welcome to the HomePage (HR)</h1>
    </div>

    <div>
      <router-link to="/viewteamschedule">
        <button type="button" class="btn btn-primary btn-lg m-5">
          View Team Schedule
        </button>
      </router-link>
    </div>

    <div>
      <router-link to="/viewoverallschedule">
        <button type="button" class="btn btn-primary btn-lg m-5">
          View Overall Schedule
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import accountIcon from "@/assets/account.png"; // Import the account icon
import Cookies from "js-cookie"; // Import js-cookie to manage cookies
import axios from "axios"; // Import axios for API requests

export default {
  name: "Homepage",
  data() {
    return {
      accountIcon: accountIcon, // Make the imported icon available to the template
    };
  },
  computed: {
    ...mapGetters(["userRole"]), // Access the user's role from Vuex
    isStaff() {
      return this.userRole === "Staff"; // Only true if the user's role is 'Staff'
    },
    isManager() {
      return this.userRole === "Manager"; // Only true if the user's role is 'Manager'
    },
    isHR() {
      return this.userRole === "HR"; // Only true if the user's role is 'HR'
    },
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

<style scoped>
.container {
  max-width: 400px;
  margin-top: 50px;
}
</style>
