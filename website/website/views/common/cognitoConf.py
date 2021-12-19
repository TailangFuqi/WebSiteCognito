import os

class getCognitoConf():
    region_name = ''
    aws_access_key_id = ''
    aws_secret_access_key = ''
    ClientId = ''
    SecretHash = ''
        
    def __init__(self):
        self.region_name = os.environ['AWS_REGIONNAME']
        self.aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        self.aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        self.ClientId = os.environ['AWS_CLIENT_ID']
    
