import boto3

def lambda_handler(event, context):
  sendEmail()

def sendEmail():
  ses = boto3.client('ses',region_name="us-west-2")
  response = ses.send_email(
            Source=os.environ['SES_SRC'],
            Destination={
                'ToAddresses': [
                    'boyu.wang@sony.com',
                ],
            },
            Message={
                'Subject': {
                    'Data': 'test 1207-1255',
                },
                'Body':{
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': "nothing"
                    }
                }
            }
    )
if __name__ == "__main__":
  sendEmail()
