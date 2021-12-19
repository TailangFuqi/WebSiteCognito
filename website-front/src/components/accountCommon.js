export default {
  data: {
    apiServerURLCommon: "http://127.0.0.1:8000/",
    hideLogoutButtonYn: true,
    accountInfo: {
      emailAddress: "",
      userId: "",
      mobilePhoneNo: "",
      given_name: "",
      family_name: "",
      gender: "",
      zipcode: "",
      pref: "",
      city: "",
      address: "",
    },
    passwordInfo: {
      oldPassword: "",
      password: "",
      passwordConfirm: "",
    },

    ValidErrorMessage: {
      emailAddress: "",
      userId: "",
      given_name: "",
      mobilePhoneNo: "",
      family_name: "",
      gender: "",
      zipcode: "",
      pref: "",
      city: "",
      address: "",
    },
    passwordValidErrorMessage: {
      password: "",
      passwordConfirm: "",
    },
    unexpectedError: "",
  },
  created() {
    let url = this.apiServerURLCommon + "getcsrftoken";
    fetch(url, {
      method: "get",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
    }).catch((err) => {
      alert("Fail" + err);
    });
    this.unexpectedError = this.$t("UNEXPECTED.ERROR");
  },
  methods: {
    getAddressByZip: function() {
      var url = new URL("https://api.zipaddress.net/");
      var param = {
        zipcode: this.accountInfo.zipcode,
      };
      url.search = new URLSearchParams(param);

      fetch(url)
        .then((response) => {
          return response.json();
        })
        .then((jsonData) => {
          if (jsonData.code == "200") {
            this.accountInfo.pref = jsonData.data.pref;
            this.accountInfo.city = jsonData.data.city;
            this.accountInfo.address = jsonData.data.town;
          } else {
            alert("Error was returned");
          }
        })
        .catch((err) => {
          alert("Fail to call API" + err);
        });
    },
    accountValidationCheck: function(accountValidInfo) {
      this.ValidErrorMessage.emailAddress = "";
      this.ValidErrorMessage.userId = "";
      this.ValidErrorMessage.mobilePhoneNo = "";
      this.ValidErrorMessage.given_name = "";
      this.ValidErrorMessage.family_name = "";
      this.ValidErrorMessage.gender = "";
      this.ValidErrorMessage.zipcode = "";
      this.ValidErrorMessage.pref = "";
      this.ValidErrorMessage.city = "";
      this.ValidErrorMessage.address = "";

      let validCheck = [
        {
          key: "emailAddress",
          format: /^([a-zA-Z0-9])+([a-zA-Z0-9._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9._-]+)+$/,
          len: 100,
          mandatory: true,
          keyName: "EMAIL.ADDRESS",
        },
        {
          key: "userId",
          format: /[a-zA-Z0-9@_.-]*/,
          len: 100,
          mandatory: true,
          keyName: "USERID",
        },
        {
          key: "mobilePhoneNo",
          format: /^0[789]0[0-9]{8}$/,
          len: 11,
          mandatory: true,
          keyName: "MOBILE.PHONE.NO",
        },
        {
          key: "family_name",
          format: "",
          len: 256,
          mandatory: true,
          keyName: "LASTNAME",
        },
        {
          key: "given_name",
          format: "",
          len: 256,
          mandatory: true,
          keyName: "FIRSTNAME",
        },
        {
          key: "gender",
          format: "",
          len: 1,
          mandatory: true,
          keyName: "GENDER",
        },
        {
          key: "zipcode",
          format: "",
          len: 7,
          mandatory: true,
          keyName: "ZIPCODE",
        },
        {
          key: "pref",
          format: "",
          len: 7,
          mandatory: true,
          keyName: "PREFECTURE",
        },
        {
          key: "city",
          format: "",
          len: 256,
          mandatory: true,
          keyName: "CITY",
        },
        {
          key: "address",
          format: "",
          len: 256,
          mandatory: true,
          keyName: "ADDRESS",
        },
      ];

      let result = true;
      let i = 0;
      let j = 0;

      for (i = 0; i < validCheck.length; i++) {
        for (j = 0; j < accountValidInfo.length; j++) {
          if (accountValidInfo[j].key == validCheck[i].key) {
            if (validCheck[i].mandatory == true) {
              if (accountValidInfo[j].value == "") {
                this.ValidErrorMessage[accountValidInfo[j].key] = this.$t(
                  "VALIDERROR.NOTFILLED",
                  {
                    fieldName: this.$t(validCheck[i].keyName),
                  }
                );
                result = false;
                continue;
              }
            }
            if (validCheck[i].len < accountValidInfo[j].value.length) {
              this.ValidErrorMessage[accountValidInfo[j].key] = this.$t(
                "VALIDERROR.LENGTH",
                {
                  fieldName: this.$t(validCheck[i].keyName),
                  maxLength: validCheck[i].len,
                }
              );
            }
            if (validCheck[i].format != "") {
              if (!accountValidInfo[j].value.match(validCheck[i].format)) {
                this.ValidErrorMessage[accountValidInfo[j].key] = this.$t(
                  "VALIDERROR.FORMAT",
                  {
                    fieldName: this.$t(validCheck[i].keyName),
                  }
                );
                result = false;
              }
            }
          }
        }
      }

      return result;
    },
    passwordValidCheck: function(passwordInfo) {
      let result = true;
      this.passwordValidErrorMessage.oldPassword = "";
      this.passwordValidErrorMessage.password = "";
      this.passwordValidErrorMessage.oldPassword = "";

      if (this.updatePasswordYn) {
        if (passwordInfo.oldPassword == "") {
          this.passwordValidErrorMessage.oldPassword = this.$t(
            "VALIDERROR.NOTFILLED",
            {
              fieldName: this.$t("CURRENT.PASSWORD"),
            }
          );
          result = false;
        }
      }
      if (passwordInfo.password == "") {
        this.passwordValidErrorMessage.password = this.$t(
          "VALIDERROR.NOTFILLED",
          {
            fieldName: this.$t("PASSWORD"),
          }
        );
        result = false;
      }
      if (passwordInfo.passwordConfirm == "") {
        this.passwordValidErrorMessage.passwordConfirm = this.$t(
          "VALIDERROR.NOTFILLED",
          {
            fieldName: this.$t("PASSWORD.CONFIRM"),
          }
        );
        result = false;
      }

      if (result == false) {
        return result;
      }

      if (this.updatePasswordYn) {
        if (passwordInfo.oldPassword == passwordInfo.password) {
          alert(this.$t("UPDATE.PASSWORD.RULE"));
          result = false;
          this.passwordValidErrorMessage.password = this.$t(
            "UPDATE.PASSWORD.RULE"
          );
        }
      }

      if (
        !passwordInfo.password.match(
          /^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{8,100}/
        )
      ) {
        this.passwordValidErrorMessage.password = this.$t("VALIDERROR.FORMAT", {
          fieldName: this.$t("PASSWORD"),
        });
        result = false;
      }

      if (passwordInfo.password != passwordInfo.passwordConfirm) {
        this.passwordValidErrorMessage.passwordConfirm = this.$t(
          "PASSWORD.NOTEQUAL"
        );
        result = false;
      }

      return result;
    },
    clearPasswordInput: function() {
      this.passwordInfo.oldPassword = "";
      this.passwordInfo.password = "";
      this.passwordInfo.passwordConfirm = "";
    },
    submitLogout: function() {
      var url = this.apiServerURLCommon + "logoutproc";

      fetch(url, {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": this.$cookies.get("csrftoken"),
        },
      })
        .then(function() {
          location.href = "/login";
        })
        .catch((err) => {
          alert("Fail" + err);
          location.href = "/login";
        });
    },
  },
};
