from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def changepassword(request):

    resultCd = '0'
    errorMsg = ""
    access_token = ""

    try:
        jsonReq = json.loads(request.body)
        oldPassword = jsonReq["oldPassword"]
        newPassword = jsonReq["newPassword"]

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

        aws_result = aws_client.change_password(
            PreviousPassword=oldPassword,
            ProposedPassword=newPassword,
            AccessToken=access_token
        )

    except Exception as e:

        resultCd = '1'

        if e.response["Error"]["Code"] == "NotAuthorizedException":
            errorMsg = "NotAuthorizedException"
        else:
            errorMsg = "ErrorOnServer"

    ret = {
        'resultCd': resultCd,
        'errorMsg': errorMsg
    }

    response = Response()
    response.data = ret

    if resultCd == '0':
        response.set_cookie('accessToken', access_token, max_age=1800)

    return response
