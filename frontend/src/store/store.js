import { createStore } from 'vuex';

export default createStore({
  state: {
    user: {
      role: null,         // Store user's role (e.g., 'HR', 'Manager', etc.)
      Staff_ID: null,
      supervisor: null  // Store the Staff_ID
    },
  },
  mutations: {
    setRole(state, role) {
      state.user.role = role;  // Update the user role in the state
    },
    setEmployeeId(state, Staff_ID) {
      state.user.Staff_ID = Staff_ID;  // Update the Staff_ID in the state
    },
    setSupervisor(state, supervisor) {
      state.user.supervisor = supervisor;  // Update the Staff_ID in the state
    }
  },
  actions: {
    login({ commit }, { role, Staff_ID, supervisor }) {
      // Store the role and Staff_ID retrieved from the backend upon login
      commit('setRole', role);
      commit('setEmployeeId', Staff_ID);
      commit('setSupervisor', supervisor);

    },
  },
  getters: {
    userRole: (state) => state.user.role,            // Access the current user role
    employeeId: (state) => state.user.Staff_ID,   // Access the current Staff_ID
    supervisor: (state) => state.user.supervisor,   // Access the current Staff_ID
  },
});
