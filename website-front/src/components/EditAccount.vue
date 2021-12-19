<template>
<div class="main-wrap">
        <div class="InputAuthInfoArea">
            <h2>{{ $t( 'EDIT.ACCOUNT.INFO')}}</h2>
                <table class="input-account-table">
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t( 'USERID')}}</label>
                        </th>
                        <td>
                            <input name="userId" id="USERID" type="text" class="account-text-input" disabled="disabled"
                                v-model="accountInfo.userId" />
                        </td>
                    </tr>
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t( 'EMAIL.ADDRESS')}}</label>
                        </th>
                        <td>
                            <input name="emailAddress" id="MAIL" type="account-text-input" class="account-text-input"
                                v-model="accountInfo.emailAddress" />
                            <br>
                            <div class="validation-error" v-text="ValidErrorMessage.emailAddress"></div>
                        </td>
                    </tr>
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t( 'MOBILE.PHONE.NO')}}</label>
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
                            <label>{{ $t( 'LASTNAME.FIRSTNAME')}}</label>
                        </th>
                        <td>
                            <input name="lastname" type="text" class="account-text-input" v-model="accountInfo.family_name" />
                            <input name="firstname" type="text" class="account-text-input" v-model="accountInfo.given_name" />
                            <br>
                            <!--
                            <div class="validation-error" v-text="ValidErrorMessage.family_name"><br></div>
                            <div class="validation-error" v-text="ValidErrorMessage.given_name"></div>
                            -->
                        </td>
                    </tr>
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t( 'GENDER')}}</label>
                        </th>
                        <td>
                            <input name="GENDER" type="radio" class="validate[required]" value="1"
                                v-model="accountInfo.gender" />{{ $t( 'MALE')}}
                            <input name="GENDER" type="radio" class="validate[required]" value="2"
                                    v-model="accountInfo.gender" />{{ $t( 'FEMALE')}}
                                <br>
                            <div class="validation-error" v-text="ValidErrorMessage.gender"></div>
                        </td>
                    </tr>
                    <tr class="accountInfoLine">
                        <th>
                            <label>{{ $t( 'ZIPCODE')}}</label>
                        </th>
                        <td>
                            <input name="zipcode" type="text" class="account-text-input" placeholder="ZIPCODE"
                                v-model="accountInfo.zipcode" />
                            <button type="button" class="btnLogin"
                                @click="getAddressByZip()">{{$t('SEARCH.ADDRESS')}}</button>
                            <br>
                            <div class="validation-error" v-text="ValidErrorMessage.zipcode"></div>
                        </td>
                    </tr>
                    <tr>
                        <th>
                            <label>{{ $t( 'PREFECTURE')}}</label>
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
                            <label>{{ $t( 'CITY')}}</label>
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
                            <label>{{ $t( 'ADDRESS')}}</label>
                        </th>
                        <td>
                            <input name="address" type="text" class="account-text-input" placeholder="ADDRESS"
                                v-model="accountInfo.address" />
                            <br>
                            <div class="validation-error" v-text="ValidErrorMessage.address"></div>
                        </td>
                    </tr>
                    <tr>
                        <th>
                            {{ $t( 'CHANGE.PASSWORD')}}
                        </th>
                         <td>
                            <button class="btnLogin"
                                @click="openPasswordModal">{{$t('CHANGE.PASSWORD')}}</button>
                        </td>
                    </tr>
                </table>
                <button  @click="submitUpdate" class="account-button-large">{{ $t( 'UPDATE')}}</button>
            </div>
        </div>
<ChangePasswordModal  :val="this.accountInfo.userId" v-show="showPasswordModal" @close="closePasswordModal"></ChangePasswordModal>
</template>
<script>
import accountCommon from "./accountCommon";
import ChangePasswordModal from "./ChangePasswordModal.vue";

export default  {
    mixins: [accountCommon],
    components: {
        ChangePasswordModal
    },
    data() {
        return {
            showPasswordModal:false,
            updatePasswordYn: true,
            count: 0,
        }
    },
    created () {
        let url = this.apiServerURLCommon + "getUserInfo";
        fetch(url, {
                method: "GET",
                credentials: 'include',
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": this.$cookies.get('csrftoken')
                    }
            })
            .then((response) => {
                return response.json();
            })
            .then((jsonData) => {
                // JSONデータを扱った処理など
                if (jsonData.resultCd == '0') {
                    this.accountInfo.userId = jsonData.result.userId;
                    this.accountInfo.emailAddress = jsonData.result.email;
                    this.accountInfo.mobilePhoneNo = jsonData.result.phone_number;
                    this.accountInfo.gender = jsonData.result.gender;
                    this.accountInfo.given_name = jsonData.result.given_name;
                    this.accountInfo.family_name = jsonData.result.family_name;
                    this.accountInfo.zipcode = jsonData.result.zipcode;
                    this.accountInfo.pref = jsonData.result.pref;
                    this.accountInfo.city = jsonData.result.city;
                    this.accountInfo.address = jsonData.result.address;

                    this.hideLogoutButtonYn = false;
                } else {
                    alert('Error was returned');
                    location.href = '/login';
                }
            }).catch(err => {
                console.log(err);
                alert(this.unexpectedError);
                location.href = '/login';
            });
        
    },
    methods: {
        submitUpdate: function() {
            alert("Update your account");

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
                return false;
            }

            var jsonRequest = {
                emailAddress: this.accountInfo.emailAddress,
                given_name: this.accountInfo.given_name,
                family_name: this.accountInfo.family_name,
                gender: this.accountInfo.gender,
                zipcode: this.accountInfo.zipcode,
                pref: this.accountInfo.pref,
                city: this.accountInfo.city,
                address: this.accountInfo.address
            };

            var url = this.apiServerURLCommon + "updateaccount";

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
                        alert('Succeed updating');
                    } else {
                        alert('Failed to update account info');
                    }
                }).catch(err => {
                    console.log(err);
                    alert(this.unexpectedError);
                });
        },
        openPasswordModal: function() {
            this.showPasswordModal = true;
            this.passwordValidErrorMessage.oldPassword = "";
            this.passwordValidErrorMessage.password = "";
            this.passwordValidErrorMessage.passwordConfirm = "";
        },
        closePasswordModal: function() {
            this.clearPasswordInput();
            this.showPasswordModal = false;
        }
    }
}

</script>

