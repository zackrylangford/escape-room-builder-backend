# Escape Room Builder Backend

## Introduction
Welcome to the **Escape Room Builder Backend** repository! This project is an innovative web application that allows users to create, manage, and share custom escape room experiences. It's designed for escape room enthusiasts and creators who want to explore and craft unique and interactive puzzles and challenges.

## Project Status
**Note**: This project is currently in the development phase. The features described below are planned and not yet implemented.

## Features
- **Escape Room Creation**: Users can create personalized escape rooms, setting timers and adding various challenges.
- **Challenge Customization**: Offers a mix of pre-built and user-generated challenges. Users can add trivia, puzzles, and more, with a future feature to incorporate AI-generated trivia questions.
- **Real-Time Playthrough**: Users can play through their escape rooms with real-time tracking of progress and completion of challenges.
- **Social Sharing**: Escape rooms can be shared with friends or the community, featuring a competitive aspect with leaderboards and time tracking.

## Technical Overview
- **Backend**: Built with AWS services, including API Gateway, Cognito, DynamoDB, and Lambda functions utilizing SAM (Serverless Application Model).
- **Database**: DynamoDB - NoSQL database for storing escape room game definitions as well as challenge definitions created by game admins.
- **Authentication**: Cognito - User authentication and authorization.
- **API**: API Gateway - REST API for interacting with the backend.
- **Lambda Functions**: Lambda functions for interacting with the database and performing CRUD operations.
- **Hosting**: Hosted on AWS. 
- **Frontend Integration**: Connects with [Escape Room Builder Frontend](https://github.com/zackrylangford/escape-room-builder-frontend).

## Installation and Setup

### Prerequisites
- **AWS Account**: You'll need an AWS account to set up the backend. If you're not familiar with AWS, you can use our pre-built backend for pulling challenge information and pre-built escape room games that we have already built to help you. Please [contact us](mailto:zack@cloudzack.com) for API keys and integration instructions.
- **SAM CLI (Optional)**: You'll need to install the [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) to build and deploy the backend in your AWS account.
- **Python 3.9 or Later**: You'll need to install Python 3.9 or later to run your builds and test locally.

### Getting Started
1. **Clone the Repository**:
```
git clone https://github.com/zackrylangford/escape-room-builder-backend.git
```
2. **SAM Build and Deploy** (Optional): If you're using the SAM CLI, you can build and deploy the backend with the following commands:
```
sam build
```
```
sam deploy --guided
```

### Frontend Access and Understanding
- **Frontend Repository**: To understand how the frontend is structured, check out our [Escape Room Builder Frontend Repository](https://github.com/zackrylangford/escape-room-builder-frontend).


## Usage

### Current Functionality
As of now, the Escape Room Builder is in its early development stages. Here's what you can do:
- **Add Escape Rooms**: You can add new escape rooms defined by a JSON dictionary using the put_game.py function and retrieve those game definitions with the get_all_games.py dictionary. In the future, users will be able to create and manage their own escape rooms with actual gameplay.


### Backend Interaction and API Testing
- **Authenticated API Calls**: If you're interested in making authenticated calls to the API that we have set up for production, we can set you up with a Cognito user login and API Key. This will allow you to fully test and interact with our API. Please [contact us](mailto:zack@cloudzack.com) for more information.

### Future Developments
We're working on adding more features, including:
- **Creating and Managing Escape Rooms**: Users will be able to create custom escape rooms, set timers, and add challenges.
- **Challenge Customization**: Including both pre-built and user-generated challenges.
- **Real-Time Gameplay**: Play through escape rooms with real-time progress tracking.
- **Social Features**: Share escape rooms and compete on leaderboards.

Stay tuned for these exciting updates!

## Contributing
We warmly welcome contributions! If you're interested in contributing, please read our [Contributing Guidelines](CONTRIBUTING.md).

## Code of Conduct

Our project is committed to providing a welcoming and inclusive experience for everyone. We expect all participants to adhere to our [Contributor Code of Conduct](CODE_OF_CONDUCT.md).


## Support and Feedback
For support, questions, or feedback, please [open an issue](https://github.com/zackrylangford/escape-room-builder-backend/issues).

or email us at [zack@cloudzack.com](mailto:zack@cloudzack.com).

or find me on Threads (https://threads.net/@zackrydlangford)!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

We hope this project sparks your creativity and enthusiasm for interactive and collaborative gaming experiences!
