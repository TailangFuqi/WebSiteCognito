from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def logout(request):
    resultCd = '0'
    errorMsg = ""
    access_token = ""

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

        aws_result = aws_client.global_sign_out(
            AccessToken=access_token
        )

        print(aws_result)

    except Exception as e:
        resultCd = '1'
        errorMsg = "Error happened in server"

    ret = {"resultCd": resultCd,
           "errorMsg": errorMsg}

    response = Response()
    response.data = ret
    response.delete_cookie('accessToken')

    return response
