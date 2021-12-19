<template>
<div class="main-wrap">
    <h2>{{ $t('REREGIST.PASSWORD' )}}</h2>			
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
		<tr class="accountInfoLine">
			<th>
				<label>{{ $t('ACTIVATIONKEY' )}}</label>
			</th>
			<td>
				<input name="activationKey" type="text" class="activationKey"
					placeholder="ACTIVATIONKEY" v-model="activationKey" />
			</td>
		</tr>
		<tr class="accountInfoLine">
			<th>
				<label>{{ $t('PASSWORD' )}}</label>
			</th>
			<td>
				<input name="password" type="password" class="loginPW" placeholder="PASSWORD"
					v-model="password" />
                <div class="validation-error" v-text="passwordValidErrorMessage.password"></div>
			</td>
		</tr>
		<tr class="accountInfoLine">
			<th>
				<label>{{ $t('PASSWORD.CONFIRM' )}}</label>
			</th>
			<td>
				<input name="passwordConfirm" type="password" class="loginPW" placeholder="PASSWORD"
					v-model="passwordConfirm" />
                <div class="validation-error" v-text="passwordValidErrorMessage.passwordConfirm"></div>
			</td>
		</tr>
	</table>
	<button  class="account-button-large" @click="reregistPasswordsubmit()">{{ $t('REREGIST.PASSWORD' )}}</button>
</div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
    mixins: [accountCommon],
    data () {
        return {
            userId: "",
            activationKey: "",
            password: "",
            passwordConfirm: "",
            loginErrorMessage: ""
        }
    },
    methods: {
        reregistPasswordsubmit() {
            let passwordValidInfo = {
                password: this.password,
                passwordConfirm: this.passwordConfirm
            };

            if (!this.passwordValidCheck(passwordValidInfo)) {
                this.clearPasswordInput();
                return false;
            }

            let jsonRequest = {
                userId: this.userId,
                activationKey: this.activationKey,
                password: this.password
            };

            let url = this.apiServerURLCommon + "reregistpasswordproc";
            let completeResetMsg = this.$t("COMPLETE.RESET.PASSWORD");

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
                .then(function(jsonData) {
                    if (jsonData.resultCd == '1') {
                        alert(jsonData.errorMsg);
                    } else {
                        alert(completeResetMsg);
                        location.href = '/login'
                    }
                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
                });
        }
    }
}
</script>
