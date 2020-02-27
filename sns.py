import boto3

# Function to send message to random SNS topic
def send_sns_message ():
    sns = boto3.client('sns')
    sns.publish(
        TopicArn="arn:aws:sns:us-west-1:361310239170:hello-there",    
        Message="hello"
    )

def lambda_handler(event, context):
    send_sns_message()
    
