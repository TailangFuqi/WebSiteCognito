from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def activation(request):

    resultCd = '0'
    errorMsg = ""
    access_token = ""

    try:
        jsonReq = json.loads(request.body)
        userId = jsonReq["userId"]
        activationKey = jsonReq["activationKey"]

        cognito = cognitoConf.getCognitoConf()

        cognito.username = userId

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_access_key_id,
                                  aws_secret_access_key=cognito.aws_access_key_id,
                                  )

        aws_result = aws_client.confirm_sign_up(
            ClientId=cognito.ClientId,
            Username=userId,
            ConfirmationCode=activationKey,
        )

    except Exception as e:

        resultCd = '1'
        print(e)
        if e.response["Error"]["Code"] == "ExpiredCodeException":
            errorMsg = "UserId or activation key is not correct"
        elif e.response["Error"]["Code"] == "CodeMismatchException":
            errorMsg = "UserId or activation key is not correct"
        else:
            errorMsg = "Error happened in server"

    ret = {"resultCd": resultCd,
           "errorMsg": errorMsg
           }
    response = Response()
    response.data = ret
    return response
