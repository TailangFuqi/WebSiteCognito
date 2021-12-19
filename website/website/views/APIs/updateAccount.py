from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def updateAccount(request):

    resultCd = '0'

    try:
        access_token = request.COOKIES['accessToken']

        cognito = cognitoConf.getCognitoConf()

        jsonReq = json.loads(request.body)

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_access_key_id,
                                  aws_secret_access_key=cognito.aws_secret_access_key,
                                  )

        result = aws_client.update_user_attributes(
            AccessToken=access_token,
            UserAttributes=[
                {
                    'Name': 'family_name',
                    'Value': jsonReq["family_name"]
                },
                {
                    'Name': 'given_name',
                    'Value': jsonReq["given_name"]
                },
                {
                    'Name': 'gender',
                    'Value': jsonReq["gender"]
                },
                {
                    'Name': 'custom:zipcode',
                    'Value': jsonReq["zipcode"]
                },
                {
                    'Name': 'custom:pref',
                    'Value': jsonReq["pref"]
                },
                {
                    'Name': 'custom:city',
                    'Value': jsonReq["city"]
                },
                {
                    'Name': 'address',
                    'Value': jsonReq["address"]
                }
            ]
        )

    except Exception as e:
        resultCd = '1'

    ret = {"resultCd": resultCd}

    response = Response()
    response.data = ret

    if resultCd == '0':
        response.set_cookie('accessToken', access_token, max_age=1800)

    return response
