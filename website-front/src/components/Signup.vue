<template>
<div class="main-wrap">
    <h2>{{ $t('SIGNUP' )}}</h2>
    <div class="loginInput">
        <table class="input-account-table">
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('EMAIL.ADDRESS' )}}</label>
                </th>
                <td>
                    <input name="emailAddress" type="text" class="account-text-input" placeholder="ID"
                                v-model="accountInfo.emailAddress" />
                    <div class="validation-error" v-text="ValidErrorMessage.emailAddress"></div>            
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('USERID' )}}</label>
                </th>
                <td>
                    <input name="USERIDFLAG" type="radio" class="validate[required]" value="0"
                                v-model="userIdYn"
                                v-on:change="switchUserIdYn" />{{ $t('MAILADDRESS.AS.USERID' )}}
                    <input name="USERIDFLAG" type="radio" class="validate[required]" value="1"
                                v-model="userIdYn" v-on:change="switchUserIdYn" />{{ $t('ORIGINALID.AS.USERID' )}}
                    <div class="set-userId"
                                v-bind:class="{showUserIDField: showUserIdLine.show, hideUserIDField: showUserIdLine.hide}">
                                <input name="userID" type="text" placeholder="ID" v-model="accountInfo.userId" />
                                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.userId"></div>
                            </div>
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('MOBILE.PHONE.NO' )}}</label>
                </th>
                <td>
                    <input name="mobilePhoneNo" type="text" class="account-text-input" placeholder="ID"
                                v-model="accountInfo.mobilePhoneNo" />
                                <br>
                    <div class="validation-error" v-text="ValidErrorMessage.mobilePhoneNo"></div>
                </td>
                </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('PASSWORD' )}}</label>
                </th>
                <td>
                    <input name="password" type="password" class="account-text-input" placeholder="PASSWORD"
                        v-model="passwordInfo.password" />
                    <br>
                    <div class="validation-error" v-text="passwordValidErrorMessage.password"></div>
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('PASSWORD.CONFIRM' )}}</label>
                </th>
                <td>
                    <input name="passwordConfirm" type="password" class="account-text-input"
                        placeholder="PASSWORD" v-model="passwordInfo.passwordConfirm" />
                    <br>
                    <div class="validation-error" v-text="passwordValidErrorMessage.passwordConfirm"></div>
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('LASTNAME.FIRSTNAME' )}}</label>
                </th>
                <td>
                    <input name="lastname" type="text" class="account-text-input" placeholder="LASTNAME"
                        v-model="accountInfo.family_name" />
                    <input name="firstname" type="text" class="account-text-input" placeholder="FIRSTNAME"
                        v-model="accountInfo.given_name" />
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.family_name"></div>
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.given_name"></div>
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('GENDER' )}}</label>
                </th>
                <td>
                    <input name="GENDER" type="radio" class="validate[required]" value="1"
                            v-model="accountInfo.gender" />{{ $t('MALE' )}}
                    <input name="GENDER" type="radio" class="validate[required]" value="2"
                            v-model="accountInfo.gender" />{{ $t('FEMALE' )}}
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.gender"></div>
                </td>
            </tr>
            <tr class="accountInfoLine">
                <th>
                    <label>{{ $t('ZIPCODE' )}}</label>
                </th>
                <td>
                    <input name="zipcode" type="text" class="account-text-input" placeholder="ZIPCODE"
                            v-model="accountInfo.zipcode" />
                    <button  class="btnLogin" @click="getAddressByZip()" >{{ $t('SEARCH.ADDRESS' )}}</button>
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.zipcode"></div>
                </td>
            </tr>
            <tr>
                <th>
                    <label>{{ $t('PREFECTURE' )}}</label>
                </th>
                <td>
                    <input name="pref" type="text" class="account-text-input" placeholder="PREF"
                            v-model="accountInfo.pref" />
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.pref"></div>
                </td>
            </tr>
            <tr>
                <th>
                    <label>{{ $t('CITY' )}}</label>
                </th>
                <td>
                    <input name="city" type="text" class="account-text-input" placeholder="CITY"
                            v-model="accountInfo.city" />
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.city"></div>
                </td>
            </tr>
            <tr>
                <th>
                    <label>{{ $t('ADDRESS' )}}</label>
                </th>
                <td>
                    <input name="address" type="text" class="account-text-input" placeholder="ADDRESS"
                        v-model="accountInfo.address" />
                    <br>
                    <div class="validation-error" v-text="ValidErrorMessage.address"></div>
                </td>
            </tr>
        </table>
        <p>
            <button class="account-button-large" @click="signupSubmit()">{{ $t('SIGNUP')}} </button>
            <button class="account-button-large-cancel" @click="backToLoginPage()">{{ $t('CANCEL')}}</button>
        </p>
    </div>
</div>
</template>
<script>
import accountCommon from "./accountCommon";
export default {
    mixins: [accountCommon],
    data() {
        return {
            userIdYn: false,
            showUserIdLine: {
                show: false,
                hide: true
            },
            updatePasswordYn: false
        }
    },
    methods: {
        switchUserIdYn() {
            if (this.userIdYn == "1") {
                this.showUserIdLine.show = true;
                this.showUserIdLine.hide = false;
            } else {
                this.showUserIdLine.show = false;
                this.showUserIdLine.hide = true;
            }
        },
        signupSubmit() {
            "use strict";
            if (this.userIdYn == '0') {
                this.accountInfo.userId = this.accountInfo.emailAddress;
            }

            var accountValidInfo = [];

            accountValidInfo.push({
                key: 'emailAddress',
                value: this.accountInfo.emailAddress
            });
            accountValidInfo.push({
                key: 'userId',
                value: this.accountInfo.userId
            });
            accountValidInfo.push({
                key: 'mobilePhoneNo',
                value: this.accountInfo.mobilePhoneNo
            });
            accountValidInfo.push({
                key: 'gender',
                value: this.accountInfo.gender
            });
            accountValidInfo.push({
                key: 'given_name',
                value: this.accountInfo.given_name
            });
            accountValidInfo.push({
                key: 'family_name',
                value: this.accountInfo.family_name
            });
            accountValidInfo.push({
                key: 'zipcode',
                value: this.accountInfo.zipcode
            });
            accountValidInfo.push({
                key: 'pref',
                value: this.accountInfo.pref
            });
            accountValidInfo.push({
                key: 'city',
                value: this.accountInfo.city
            });
            accountValidInfo.push({
                key: 'address',
                value: this.accountInfo.address
            });

            if (!this.accountValidationCheck(accountValidInfo)) {
                this.clearPasswordInput();
                return false;
            }

            let passwordValidInfo = {
                password: this.passwordInfo.password,
                passwordConfirm: this.passwordInfo.passwordConfirm
            };

            if (!this.passwordValidCheck(passwordValidInfo)) {
                this.clearPasswordInput();
                return false;
            }

            let jsonRequest = {
                emailAddress: this.accountInfo.emailAddress,
                userId: this.accountInfo.userId,
                mobilePhoneNo: this.accountInfo.mobilePhoneNo,
                password: this.passwordInfo.password,
                gender: this.accountInfo.gender,
                given_name: this.accountInfo.given_name,
                family_name: this.accountInfo.family_name,
                zipcode: this.accountInfo.zipcode,
                pref: this.accountInfo.pref,
                city: this.accountInfo.city,
                address: this.accountInfo.address
            }

            let url = this.apiServerURLCommon + "signupproc";

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
                        if(jsonData.errorMsg == "UsernameExistsException") {
                            alert(this.$t("ERROR.ACCOUNT.EXISTS"));    
                        } else {
                            alert(this.errorOnServer);
                        }
                        return false;
                    } else {
                        alert(this.$t("ACTIVATE.SMS.SENT"));
                        location.href = '/activation'
                    }
                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
                });
        },
        backToLoginPage() {
            location.href = '/login';
        }
    }
}
</script>
