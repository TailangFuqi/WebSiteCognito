from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import boto3
from ..common import cognitoConf


@api_view(['POST'])
def login(request):

    resultCd = '0'
    errorMsg = ""
    access_token = ""

    try:
        jsonReq = json.loads(request.body)
        loginUserId = jsonReq["userId"]
        loginPassword = jsonReq["password"]

        cognito = cognitoConf.getCognitoConf()

        aws_client = boto3.client('cognito-idp',
                                  region_name=cognito.region_name,
                                  aws_access_key_id=cognito.aws_access_key_id,
                                  aws_secret_access_key=cognito.aws_secret_access_key,
                                  )

        aws_result = aws_client.initiate_auth(
            ClientId=cognito.ClientId,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": loginUserId,
                "PASSWORD": loginPassword,
            }
        )

        access_token = aws_result["AuthenticationResult"]["AccessToken"]

    except Exception as e:

        resultCd = '1'

        if e.response["Error"]["Code"] == "NotAuthorizedException":
            errorMsg = "Incorrect user name or password"
        else:
            errorMsg = "Error happened in server"

    ret = {"resultCd": resultCd,
           "errorMsg": errorMsg,
           "accessToken": access_token}
    response = Response()
    response.data = ret

    if resultCd == '0':
        response.set_cookie('accessToken', access_token, max_age=1800)

    return response
