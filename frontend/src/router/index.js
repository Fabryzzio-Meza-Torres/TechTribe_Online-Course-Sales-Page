import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/cursos",
    name: "cursos",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "curso" */ "../views/VistaCursos.vue"),
  },
  {
    path: "/asesorias",
    name: "asesorias",
    component: () =>
      import(/* webpackChunkName: "asesoria" */ "../views/VistaAses.vue"),
  },
  {
    path: "/profesores",
    name: "profesores",
    component: () =>
      import(/* webpackChunkName: "profesores" */ "../views/VistaProfs.vue"),
  },
  {
    path: "/sign-up",
    name: "signUp",
    component: () =>
      import(/* webpackChunkName: "singUp" */ "../views/SignUp.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "singUp" */ "../views/FormRegis.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
