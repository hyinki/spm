<template>
  <!-- Navbar -->
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
            <a class="nav-link" href="/viewteamschedule">View Team Schedule</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/arrangement">Approve/Reject Arrangement</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Title -->
  <div>
    <h1>Pending Work Arrangements</h1>
  </div>

  <!-- Table of Pending Requests -->
  <div class="container mt-4">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Select</th>
          <th>Name</th>
          <th>Date of Arrangement</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="request in pendingRequests" :key="request.id">
          <td>
            <input type="checkbox" v-model="selectedRequests" :value="request.id" />
          </td>
          <td>{{ request.name }}</td>
          <td>{{ formatDate(request.date) }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Approve and Reject Buttons for Selected Requests -->
  <div class="mt-3">
    <button class="btn btn-success" @click="approveSelected">Approve Selected</button>
    <button class="btn btn-danger" @click="rejectSelected">Reject Selected</button>
  </div>
</template>

<script>
export default {
  name: "Arrangement",
  data() {
    return {
      // Static pending requests data for now
      pendingRequests: [
        { id: 1, name: 'James Teo', date: '2024-03-02' },
        { id: 2, name: 'Mary Tan', date: '2024-04-05' },
        { id: 3, name: 'Sean Goh', date: '2024-11-15' }
      ],
      selectedRequests: []  // Store selected requests for approval/rejection
    };
  },
  methods: {
    // Approve selected requests
    approveSelected() {
      console.log(`Approved selected requests: ${this.selectedRequests}`);
    },
    // Reject selected requests
    rejectSelected() {
      console.log(`Rejected selected requests: ${this.selectedRequests}`);
    },
    // Format date to a readable format
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
    }
  }
};
</script>

<style scoped>
.table {
  margin-top: 20px;
}
.btn-success {
  margin-right: 10px;
}
</style>
