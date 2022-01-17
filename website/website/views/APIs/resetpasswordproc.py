from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
import boto3
from ..common import cognitoConf


def resetpassword(request):

    resultCd = '0'
    errorMsg = ""

    try:
        jsonReq = json.loads(request.body)
        userId = jsonReq["userId"]

        cognito = cognitoConf.getCognitoConf()

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_access_key_id,
                                  aws_secret_access_key=cognito.aws_secret_access_key,
                                  )

        aws_result = aws_client.forgot_password(
            ClientId=cognito.ClientId,
            Username=userId
        )

        print(aws_result)

    except Exception as e:

        resultCd = '1'
        if e.response["Error"]["Code"] == "UsernameExistsException":
            errorMsg = "User already exists"
        else:
            errorMsg = "ErrorOnServer"

    ret = {"resultCd": resultCd,
           "errorMsg": errorMsg
           }
    return JsonResponse(ret)
