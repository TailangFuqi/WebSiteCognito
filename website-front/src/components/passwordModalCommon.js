import accountCommon from "./accountCommon";
export default {
  mixins: [accountCommon],
  data: {
    showPasswordModal: false,
  },
  methods: {
    openPasswordModal: function () {
      this.showPasswordModal = true;
    },
    closePasswordModal: function () {
      this.showPasswordModal = false;
      this.passwordInfo.oldPassword = "";
      this.passwordInfo.password = "";
      this.passwordInfo.passwordConfirm = "";
      this.passwordValidErrorMessage.oldPassword = "";
      this.passwordValidErrorMessage.password = "";
      this.passwordValidErrorMessage.passwordConfirm = "";
    },
  },
};
