from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view()
def getUserInfo(request):

    resultCd = '0'
    errorMsg = ""
    access_token = ""
    UserKeyArray = {"userId", "email", "gender", "given_name", "family_name", "phone_number",
                    "custom:zipcode", "custom:pref", "custom:city", "address"}
    resoonseArray = {}

    try:
        access_token = request.COOKIES['accessToken']

        cognito = cognitoConf.getCognitoConf()

        if access_token == '':
            resultCd = '1'
            errorMsg = "Can't get login session"

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_access_key_id,
                                  aws_secret_access_key=cognito.aws_secret_access_key,
                                  )

        aws_result = aws_client.get_user(
            AccessToken=access_token
        )

        userId = aws_result["Username"]

        jsonUserInfo = aws_result["UserAttributes"]

        resoonseArray["userId"] = userId

        for userAttribute in jsonUserInfo:
            if userAttribute["Name"] in UserKeyArray:
                key = userAttribute["Name"]
                value = userAttribute["Value"]

                if key.startswith("custom:"):
                    key = key.replace("custom:", "")

                if key == "phone_number":
                    value = "0" + value.lstrip("+81")

                resoonseArray[key] = value

    except Exception as e:

        resultCd = '1'
        errorMsg = "ErrorOnServer"

    ret = {
        'resultCd': resultCd,
        'errorMsg': errorMsg,
        'result': {}
    }
    ret["result"] = resoonseArray

    response = Response()
    response.data = ret

    if resultCd == '0':
        response.set_cookie('accessToken', access_token, max_age=1800)

    return response
