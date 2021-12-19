<template>
<div class="header-content">
    <div class="header-left">
    {{ $t('SITE.TITLE')}}
    </div>
    <div class="header-right">

        <div class="logout-button-area">
            <button id="logout" type="button" class="logout-button" v-bind:class="{hideLogoutButton:hideLogoutButtonYn}" @click="submitLogout">{{ $t('LOGOUT' )}}</button>
        </div>
        <div id="locale-changer" class="select-lang">
            <select v-model="currentLang" @change=changeLocale>
                <option v-for="(lang, i) in langs" :key="`Lang${i}`" :value="lang.id">{{ lang.name }}</option>
            </select>
        </div>	
    </div>
</div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
  name: 'locale-changer',
  mixins: [accountCommon],
  data () {
    return { langs: [
      {'id':'en', 'name': 'English'}, 
      {'id':'ja', 'name': '日本語'},
      {'id':'cn', 'name': '繁體中文'}],
      currentLang: "" }
  },
  created() {
        if(this.$cookies.get("locale")) {
            this.currentLang = this.$cookies.get("locale");
            this.$i18n.locale = this.currentLang;
        } else {
            this.currentLang = this.$i18n.locale;
        }
  },
  methods: {
      changeLocale: function() {
          this.$i18n.locale = this.currentLang;
          this.$cookies.set("locale", this.$i18n.locale);
      }
  }
}
</script>
