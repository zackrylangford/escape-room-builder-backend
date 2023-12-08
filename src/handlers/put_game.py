import json
import os
import boto3
import uuid  # Import the uuid library

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def putGameHandler(event, context):
    # Check if the HTTP method is POST
    if event["httpMethod"] != "POST":
        raise Exception(f"putGameHandler only accepts POST method, you tried: {event.httpMethod}")

    # Parse the JSON data from the request body
    body = json.loads(event["body"])

    # Extract game details from the JSON data
    game_title = body.get("title", "")
    game_description = body.get("description", "")
    time_limit = body.get("timeLimit", 0)  # Assuming timeLimit is an integer

    # Extract challenge data from the JSON data
    challenges = body.get("challenges", [])

    # Generate a UUID as the game ID
    game_id = str(uuid.uuid4())

    # Define the DynamoDB table name (you can replace this with your table name)
    table_name = os.environ["GAMES_TABLE"]

    # Create a DynamoDB item for the game
    game_item = {
        "id": {"S": game_id},  # Use the generated UUID as the ID
        "GameTitle": {"S": game_title},
        "GameDescription": {"S": game_description},
        "TimeLimit": {"N": str(time_limit)}
        # Add more attributes as needed
    }

    if challenges:
        game_item["Challenges"] = {"L": [
            {
                "M": {
                    "Title": {"S": c.get("title", "")},
                    "Description": {"S": c.get("description", "")},
                    "Type": {"S": c.get("type", "")}  # Include challenge type here
                }
            } for c in challenges]}

    try:
        # Put the game item into DynamoDB
        dynamodb.put_item(TableName=table_name, Item=game_item)

        # Create a response
        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"message": "Game added successfully", "gameId": game_id})
        }
    except Exception as e:
        # Handle any errors and return an error response
        response = {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"message": str(e)})
        }

    return response
