import boto3

# Function to send message to random SNS topic
def send_sns_message ():
    sns = boto3.client('sns')
    sns.publish(
        TopicArn="<SNS-ARN-HERE>",    
        Message="<message>"
    )

def lambda_handler(event, context):
    send_sns_message()
    
