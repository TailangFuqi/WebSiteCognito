from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def signup(request):

    resultCd = '0'
    errorMsg = ""
    access_token = ""

    try:
        jsonReq = json.loads(request.body)
        userId = jsonReq["userId"]
        emailAddress = jsonReq["emailAddress"]
        mobilePhoneNo = jsonReq["mobilePhoneNo"]
        given_name = jsonReq["given_name"]
        family_name = jsonReq["family_name"]
        gender = jsonReq["gender"]
        password = jsonReq["password"]
        zipcode = jsonReq["zipcode"]
        pref = jsonReq["pref"]
        city = jsonReq["city"]
        address = jsonReq["address"]

        mobilePhoneNo = mobilePhoneNo.lstrip("0")
        mobilePhoneNo = "+81" + mobilePhoneNo

        cognito = cognitoConf.getCognitoConf()

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_secret_access_key,
                                  aws_secret_access_key=cognito.aws_secret_access_key,
                                  )

        aws_result = aws_client.sign_up(
            ClientId=cognito.ClientId,
            Username=userId,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': emailAddress
                },
                {
                    'Name': 'phone_number',
                    'Value': mobilePhoneNo
                },

                {
                    'Name': 'family_name',
                    'Value': family_name
                },
                {
                    'Name': 'given_name',
                    'Value': given_name
                },
                {
                    'Name': 'gender',
                    'Value': gender
                },
                {
                    'Name': 'custom:zipcode',
                    'Value': zipcode
                },
                {
                    'Name': 'custom:pref',
                    'Value': pref
                },
                {
                    'Name': 'custom:city',
                    'Value': city
                },
                {
                    'Name': 'address',
                    'Value': address
                }
            ]
        )

        print(aws_result)

    except Exception as e:
        print(e)

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
