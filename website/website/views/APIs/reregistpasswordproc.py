from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def reregistpassword(request):

    resultCd = '0'
    errorMsg = ""

    try:
        jsonReq = json.loads(request.body)
        userId = jsonReq["userId"]
        activationKey = jsonReq["activationKey"]
        password = jsonReq["password"]

        cognito = cognitoConf.getCognitoConf()

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_access_key_id,
                                  aws_secret_access_key=cognito.aws_secret_access_key,
                                  )

        aws_result = aws_client.confirm_forgot_password(
            ClientId=cognito.ClientId,
            Username=userId,
            Password=password,
            ConfirmationCode=activationKey
        )

        print(aws_result)

    except Exception as e:
        resultCd = '1'
        if e.response["Error"]["Code"] == "UsernameExistsException":
            errorMsg = "User already exists"
        else:
            errorMsg = "Error happened in server"

    ret = {"resultCd": resultCd,
           "errorMsg": errorMsg
           }
    response = Response()
    response.data = ret
    return response
