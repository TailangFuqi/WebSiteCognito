import { createApp } from "vue";
import App from "./App.vue";
import i18n from "./i18n";
import router from "./router";
import VueCookies from "vue3-cookies";

createApp(App)
  .use(router)
  .use(i18n)
  .use(VueCookies, {
    expireTimes: "30d",
  })
  .mount("#app");
