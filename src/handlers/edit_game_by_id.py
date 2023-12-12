import json
import os
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def editGameByIdHandler(event, context):
    # Check if the HTTP method is PUT
    if event["httpMethod"] != "PUT":
        raise Exception(f"editGameByIdHandler only accepts PUT method, you tried: {event.httpMethod}")

    # Parse the JSON data from the request body
    body = json.loads(event["body"])

    # Extract game details from the JSON data
    game_id = event['pathParameters']['id']
    game_title = body.get("title", "")
    game_description = body.get("description", "")
    time_limit = body.get("timeLimit", 0)  # Assuming timeLimit is an integer

    # Extract challenge data from the JSON data
    challenges = body.get("challenges", [])

    # Define the DynamoDB table name
    table_name = os.environ["GAMES_TABLE"]

    # Prepare the update expression and attribute values
    update_expression = "SET GameTitle = :title, GameDescription = :desc, TimeLimit = :limit"
    expression_attribute_values = {
        ':title': {'S': game_title},
        ':desc': {'S': game_description},
        ':limit': {'N': str(time_limit)}
    }

    # Handle challenges
    if challenges:
        update_expression += ", Challenges = :challenges"
        expression_attribute_values[':challenges'] = {
            "L": [{"M": {
                "Title": {"S": c.get("title", "")},
                "Description": {"S": c.get("description", "")},
                "Type": {"S": c.get("type", "")}
            }} for c in challenges]
        }

    try:
        # Update the game item in DynamoDB
        dynamodb.update_item(
            TableName=table_name,
            Key={'id': {'S': game_id}},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

        # Create a response
        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,PUT"
            },
            "body": json.dumps({"message": "Game updated successfully", "gameId": game_id})
        }
    except Exception as e:
        # Handle any errors and return an error response
        response = {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,PUT"
            },
            "body": json.dumps({"message": str(e)})
        }

    return response
