<template>
<div class="modal-cover">
	<div class="modal-wrapper">
		<div id="changePassword">
			<div class="modal-content">
			<div class="close-button-wrap">
			<button  @click="$emit('close')">✕</button>
			</div>
            
				<table class="input-authInfo-table">
					<tr class="accountInfoLine">
						<th>
							<label>{{ $t('USERID' )}}</label>
						</th>
						<td>
							<input name="emailAddress" type="text" class="loginID" disabled="disabled"
                                v-model="this.userId"/>
						</td>
                    </tr>
					<tr class="accountInfoLine">
						<th>
							<label>{{ $t('CURRENT.PASSWORD' )}}</label>
						</th>
						<td>
							<input name="password" type="password" class="loginPW" placeholder="PASSWORD"
								v-model="this.passwordInfo.oldPassword" />
							<br>
							<div class="validation-error" v-text="passwordValidErrorMessage.oldPassword"></div>
						</td>
					</tr>
					<tr class="accountInfoLine">
						<th>
							<label>{{ $t('NEW.PASSWORD' )}}</label>
						</th>
						<td>
							<input name="password" type="password" class="loginPW" placeholder="PASSWORD"
								v-model="this.passwordInfo.password" />
							<br>
							<div class="validation-error" v-text="passwordValidErrorMessage.password"></div>
						</td>
					</tr>
					<tr class="accountInfoLine">
						<th>
							<label>{{ $t('NEW.PASSWORD.CONFIRM' )}}</label>
						</th>
						<td>
							<input name="passwordConfirm" type="password" class="loginPW" placeholder="PASSWORD"
								v-model="passwordInfo.passwordConfirm" />
							<br>
							<div class="validation-error" v-text="passwordValidErrorMessage.passwordConfirm"></div>
						</td>
					</tr>
				</table>
                
                <button class="account-button-large" @click="changePassword()">{{ $t('CHANGE.PASSWORD' )}}</button>
                <button class="account-button-large-cancel" @click="$emit('close')">{{ $t('CANCEL' )}}</button>
			</div>
		</div>
	</div>
</div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
    mixins: [accountCommon],
    name: 'ChangePasswordModal',
    props: ['val'],
    data () {
        return {
            userId: this.val
        }
    },
    methods:  {
                
        changePassword: function() {
            let passwordValidInfo = {
                oldPassword: this.passwordInfo.oldPassword,
                password: this.passwordInfo.password,
                passwordConfirm: this.passwordInfo.passwordConfirm
            };

            if (!this.passwordValidCheck(passwordValidInfo)) {
                return false;
            }
            let jsonRequest = {
                oldPassword: this.passwordInfo.oldPassword,
                newPassword: this.passwordInfo.password
            };

            let url = this.apiServerURLCommon + "changepasswordproc";
            let completeUpdPwdMsg = this.$t("COMPLETE.UPDATE.PASSWORD");

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
                    if (jsonData.resultCd == "0") {
                        alert(completeUpdPwdMsg);

                    } else {
                        alert(jsonData.errorMsg);
                        return false;
                    }

                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
                    return false;
                });
        }
    }
}
</script>
<style>
.modal-open {
    display: inline-block;
    background-color: #666;
    color: red;
    margin: 10px;
}

.modal-open a {
    display: inline-block;
    padding: 5px;
    text-decoration: none;
    color: #fff;
}

.close-button-wrap {
    text-align: right;
}

.close-modal-link {
    color: gray;
    text-align: right;
    text-decoration: none;
}

.modal-cover {
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #22222B;
    opacity: 0.9;
    visibility: visible;
    /* transition: opacity 0.5s, visibility 0.5s; */
    z-index: 1;
}

.modal-wrapper {
    width: 100%;
    margin: 20;
    padding: 0;
    max-width: 600px;
    min-width: 300px;
    height: 100%;
    max-height: 300px;
    background-color: #fff;
    display: block;
    position: relative;
    opacity: 1;
    top: 25%;
    left: 20%;
    right: 20%;
    border: solid 1.5px #4169e1;
    z-index: 2;
}

.modal-content {
    margin: 25px;
    opacity: 1;
}

[v-cloak] {
    display: none;
}
</style>
