import { createRouter, createWebHistory } from 'vue-router';
import store from '../store/store';// Import your Vuex store
import Home from '../views/Home.vue';  // Import from views
import Login from '../views/Login.vue';
import Homepage from '../views/Homepage.vue';
import ViewTeamSchedule from '../views/ViewTeamSchedule.vue';
import ViewOwnSchedule from '../views/ViewOwnSchedule.vue';
import ApplyForArrangement from '../views/ApplyForArrangement.vue';
import Arrangement from '../views/Arrangement.vue';
import ViewOverallSchedule from '../views/ViewOverallSchedule.vue';
import ViewArrangement from '../views/ViewArrangement.vue';



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/homepage',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/viewteamschedule',
    name: 'ViewTeamSchedule',
    component: ViewTeamSchedule
  },
  {
    path: '/viewownschedule',
    name: 'ViewOwnSchedule',
    component: ViewOwnSchedule,
    meta: { role: 'Staff' } 
  },
  {
    path: '/applyforarrangement',
    name: 'ApplyForArrangement',
    component: ApplyForArrangement,
    meta: { role: 'Staff' } 
  },
  {
    path: '/arrangement',
    name: 'Arrangement',
    component: Arrangement,
    meta: { role: 'Manager' } 
  },
  {
    path: '/viewoverallschedule',
    name: 'ViewOverallSchedule',
    component: ViewOverallSchedule,
    meta: { role: 'HR' } 
  },
  {
    path: '/viewarrangement',
    name: 'ViewArrangement',
    component: ViewArrangement,
    meta: { role: 'Staff' } 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard
router.beforeEach((to, from, next) => {
  const userRole = store.getters.userRole; // Get the user role from Vuex

  // Check if the route requires a specific role
  if (to.meta.role && to.meta.role !== userRole) {
    alert('Access Denied: You do not have permission to access this page.');
    next({ path: '/login' }); // Redirect to home page or another route
  } else {
    next(); // Allow access
  }
});


export default router;
