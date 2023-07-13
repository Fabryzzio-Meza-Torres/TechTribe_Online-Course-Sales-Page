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
    path: "/sign-in",
    name: "signIn",
    component: () =>
      import(/* webpackChunkName: "singIn" */ "../views/SignIn.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "signUp" */ "../views/SignUp.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
