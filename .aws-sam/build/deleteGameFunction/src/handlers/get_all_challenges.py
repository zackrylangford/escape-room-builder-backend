import json
import os
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def getAllChallengesHandler(event, context):
    try:
        # Get the DynamoDB table name from environment variables
        table_name = os.environ['CHALLENGES_TABLE']

        # Query the DynamoDB table to get all challenges
        response = dynamodb.scan(TableName=table_name)

        # Extract the items (challenges) from the response
        challenges = response.get('Items', [])

        # Transform DynamoDB items to a list of dictionaries
        challenge_list = []
        for challenge in challenges:
            challenge_dict = {
                'id': challenge['id']['S'],  # Assuming 'id' is the challenge name
                'Description': challenge['Description']['S']
            }
            challenge_list.append(challenge_dict)

        # Return the list of challenges as JSON
        return {
            'statusCode': 200,
            'body': json.dumps(challenge_list)
        }
    except ClientError as e:
        # Handle any errors and return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
