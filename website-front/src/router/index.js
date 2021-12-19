import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Header from "../components/Header.vue";
import Signup from "../components/Signup.vue";
import Activation from "../components/Activation.vue";
import Login from "../components/Login.vue";
import ResetPassword from "../components/ResetPassword.vue";
import ReRegistPassword from "../components/ReRegistPassword.vue";
import EditAccount from "../components/EditAccount.vue";
import ChangePasswordModal from "../components/ChangePasswordModal.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/header",
    name: "header",
    component: Header,
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
  },
  {
    path: "/activation",
    name: "activation",
    component: Activation,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/resetpassword",
    name: "resetpassword",
    component: ResetPassword,
  },
  {
    path: "/reregistpassword",
    name: "reregistpassword",
    component: ReRegistPassword,
  },
  {
    path: "/editaccount",
    name: "editaccount",
    component: EditAccount,
  },
  {
    path: "/changepasswordmodal",
    name: "changepasswordModal",
    component: ChangePasswordModal,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
