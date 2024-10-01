<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">PlanPro</a>
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
            <a class="nav-link active" aria-current="page" href="/homepage">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/viewteamschedule">Team Schedule</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/viewownschedule">Own Schedule</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/applyforarrangement">Apply For Arrangement</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/viewarrangement">ViewArrangement</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div>
    <h1>Apply for arrangement</h1>
  </div>

  <div class="container">
    <!-- Date Picker -->
    <div class="row mb-4">
      <div class="col">
        <label for="startDate">Start Date</label>
        <input type="date" id="startDate" v-model="startDate" class="form-control" />
      </div>
      <div class="col">
        <label for="endDate">End Date</label>
        <input type="date" id="endDate" v-model="endDate" class="form-control" />
      </div>
    </div>

    <!-- Requester Information -->
    <div class="row mb-4">
      <div class="col">
        <label for="requesterId">Requester ID:</label>
        <input type="text" id="requesterId" v-model="requesterId" class="form-control" />
      </div>
      <div class="col">
        <label for="requesterSupervisor">Requester Supervisor:</label>
        <input type="text" id="requesterSupervisor" v-model="requesterSupervisor" class="form-control" />
      </div>
    </div>

    <!-- Request Status -->
    <div class="row mb-4">
      <div class="col">
        <label for="requestStatus">Request Status:</label>
        <select id="requestStatus" v-model="requestStatus" class="form-select">
          <option value="Pending">Pending</option>
          <option value="Approved">Approved</option>
          <option value="Denied">Denied</option>
        </select>
      </div>
    </div>

    <!-- Weekly Schedule Dropdowns -->
    <div class="row mb-4" v-for="(day, index) in weekdays" :key="index">
      <div class="col">
        <label :for="day">{{ day }}:</label>
        <select :id="day" v-model="schedule[day]" class="form-select">
          <option value="NULL">NULL</option>
          <option value="AM">AM</option>
          <option value="PM">PM</option>
          <option value="Whole Day">Whole Day</option>
        </select>
      </div>
    </div>

    <!-- Submit Button -->
    <div class="row mb-4">
      <div class="col">
        <button class="btn btn-primary" @click="submitRequest">Submit Request</button>
      </div>
    </div>

    
  </div>
</template>

<script>
import axios from 'axios';  // Or use fetch API
import Cookies from "js-cookie";

export default {
  name: "ApplyForArrangement",
  data() {
    return {
      startDate: null,
      endDate: null,
      requesterId: Cookies.get("Staff_ID") || 'DEFAULT_VALUE',
      requesterSupervisor: Cookies.get("supervisor") || 'DEFAULT_VALUE',
      requestStatus: 'Pending',
      weekdays: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      schedule: {
        Monday: 'NULL',
        Tuesday: 'NULL',
        Wednesday: 'NULL',
        Thursday: 'NULL',
        Friday: 'NULL',
        Saturday: 'NULL',
        Sunday: 'NULL',
      },
      arrangements: [],
    };
  },
  methods: {
    // Method to submit the request
    async submitRequest() {
      try {
        const response = await axios.post('http://localhost:5000/submit_wfh_request', {
          start_date: this.startDate,
          end_date: this.endDate,
          monday: this.schedule.Monday,
          tuesday: this.schedule.Tuesday,
          wednesday: this.schedule.Wednesday,
          thursday: this.schedule.Thursday,
          friday: this.schedule.Friday,
          saturday: this.schedule.Saturday,
          sunday: this.schedule.Sunday,
          requester_id: this.requesterId,
          requester_supervisor: this.requesterSupervisor,
          request_status: this.requestStatus
        });

        if (response.data.status === "success") {
          alert("Request submitted successfully!");
          this.resetForm();
        } else {
          alert("Request submission failed.");
        }
      } catch (error) {
        console.error("There was an error submitting the request:", error);
        alert("Error submitting request.");
      }
    },

    // Reset the form
    resetForm() {
      this.startDate = null;
      this.endDate = null;
      this.schedule = {
        Monday: 'NULL',
        Tuesday: 'NULL',
        Wednesday: 'NULL',
        Thursday: 'NULL',
        Friday: 'NULL',
        Saturday: 'NULL',
        Sunday: 'NULL',
      };
      this.requesterId = '151543';
      this.requesterSupervisor = '151408';
      this.requestStatus = 'Pending';
    }
  },
};
</script>
