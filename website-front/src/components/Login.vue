<template>
<div class="main-wrap">
    <div id="loginForm">
            <h2>{{ $t('LOGIN')}}</h2>
                <table class="input-authInfo-table">
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t('USERID')}}</label>
                        </th>
                        <td>
                            <input name="userId" type="text" v-model="userId" placeholder="ID" />
                        </td>
                    </tr>
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t('PASSWORD')}}</label>
                        </th>
                        <td>
                            <input name="password" type="password" v-model="password" placeholder="PASSWORD" />
                        </td>
                    </tr>
                </table>
                <div class="account-error">
                    <p v-text="loginError"></p>
                </div>
                <p>
                    <button class="account-button-large" v-on:click="submitLogin()">{{ $t('LOGIN')}}</button> 
                </p>
            <table class="foot-button-table">                      
            <tr>
                <td>
                    <a href="/signup">{{ $t('SIGNUP' )}}</a>
                </td>
                <td>
                    <a href="/resetpassword">{{ $t('FORGOT.PASSWORD.LINK')}}</a>
                </td>
            </tr>
            </table>
        </div>
    </div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
mixins: [accountCommon],
data() {
    return {
        userId: "",
        password: "",
        loginError: "",
        token: ""
        }
    },
    methods: {
        submitLogin: function() {
           let jsonRequest = {
                userId: this.userId,
                password: this.password
            };

            let url = this.apiServerURLCommon + "loginproc";
            
            fetch(url, {
                    method: "POST",
                    credentials: 'include',
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": this.$cookies.get('csrftoken')
                    },
                    body: JSON.stringify(jsonRequest), 
                }).then((response) => {
                    return response.json();
                }).then((jsonData) =>  {
                    if (jsonData.resultCd == '1') {
                        if(jsonData.errorMsg == "NotAuthorizedException") {
                            this.loginError = this.$t("ACCOUNT.OR.PASSWORD.NOT.CORRECT");
                        } else {
                            this.loginError = this.errorOnServer;
                        }
                        
                    } else {
                        location.href = '/editaccount';
                    }
                
                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
            });
        }
    }
}
</script>
