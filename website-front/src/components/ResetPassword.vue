<template>
<div class="main-wrap">
    <div id="InputAuthInfoArea">
        <div class="ResetPasswordArea">
            <h2>{{ $t('RESET.PASSWORD' )}}</h2>
            <div class="loginInput">
                <table class="input-authInfo-table">
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t('USERID' )}}</label>
                        </th>
                        <td>
                            <input name="emailAddress" type="text" class="loginID" placeholder="ID"
                                v-model="userId" />
                        </td>
                    </tr>
                </table>
                <p>
                    <button class="account-button-large" @click="resetPasswordSubmit()" >{{ $t('RESET.PASSWORD' )}}</button>
                </p>
            </div>
        </div>
    </div>
</div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
    mixins: [accountCommon],
    data() {
        return  {
            userId: ""
        }
    },
    methods: {
        resetPasswordSubmit() {
            let jsonRequest = {
                userId: this.userId
            };

            let url = this.apiServerURLCommon + "resetpasswordproc";
            
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
                        alert(this.errorOnServer);
                    } else {                     
                        alert(this.$t("RESET.PASSWORD.SMS.SENT"));
                        location.href = '/reregistpassword';
                    }
                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
                });
        }
    }
}
</script>
