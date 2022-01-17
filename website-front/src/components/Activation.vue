<template>
<div class="main-wrap">
    <h2>{{ $t('ACTIVATION.TITLE' )}}</h2>
    <div class="loginInput">
        <table class="input-authInfo-table">
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('USERID' )}}</label>
                </th>
                <td>
                    <input name="emailAddress" type="text" class="loginID" placeholder="ID"
                        v-model="emailAddress" />
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('ACTIVATIONKEY' )}}</label>
                </th>
                <td>
                    <input name="activationKey" type="text" class="activationKey"
                        placeholder="ACTIVATIONKEY" v-model="activationKey" />
                </td>
            </tr>
        </table>
        <p>
            <button class="account-button-large" @click="activationSubmit" >{{ $t('SEND.ACTIVATIONKEY' )}}</button>
        </p>
    </div>
</div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
    mixins: [accountCommon],
    data() {
        return  {
            emailAddress: "",
            activationKey: "",
            loginErrorMessage: ""
        }
    },
    methods: {
        activationSubmit() {

            let jsonRequest = {
                userId: this.emailAddress,
                activationKey: this.activationKey
            };

            let url = this.apiServerURLCommon +  "activationproc";
            
            fetch(url, {
                    method: "POST",
                    credentials: 'include',
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": this.$cookies.get('csrftoken')
                    },
                    body: JSON.stringify(jsonRequest)
                })
                .then(response => {
                    return response.json();
                })
                .then(jsonData => {
                    if (jsonData.resultCd == '1') {
                        if(jsonData.errorMsg == "CodeMismatchException") {
                            alert(this.$t("ACTIVATIONKEY.NOT.CORRECT"));
                        } else if (jsonData.errorMsg == "ExpiredCodeException") {
                            alert(this.$t("ACTIVATIONKEY.EXPIRED"));
                        } else {
                            alert(this.errorOnServer);
                        }
                    } else {
                        alert(this.$t("COMPLETE.ACTIVATION"));
                        location.href = '/login';
                    }
                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
                });
        }
    }
}
</script>
