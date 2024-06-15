<!-- To Bring back the link to top--> 
<a name="readme-top"></a>

# Housing Prediction Microservice

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Ruban2205/housing-prediction-microservice.svg?style=for-the-badge
[contributors-url]: https://github.com/Ruban2205/housing-prediction-microservice/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Ruban2205/housing-prediction-microservice.svg?style=for-the-badge
[forks-url]: https://github.com/Ruban2205/housing-prediction-microservice/network/members
[stars-shield]: https://img.shields.io/github/stars/Ruban2205/housing-prediction-microservice.svg?style=for-the-badge
[stars-url]: https://github.com/Ruban2205/housing-prediction-microservice/stargazers
[issues-shield]: https://img.shields.io/github/issues/Ruban2205/housing-prediction-microservice.svg?style=for-the-badge
[issues-url]: https://github.com/Ruban2205/housing-prediction-microservice/issues
[license-shield]: https://img.shields.io/github/license/Ruban2205/housing-prediction-microservice.svg?style=for-the-badge
[license-url]: https://github.com/Ruban2205/housing-prediction-microservice/blob/main/LICENSE

This repository contains a microservice for predicting housing prices based on machine learning models.

## Overview

This microservice provides a REST API endpoint to predict housing prices. It utilizes a machine learning model trained on historical housing data to make predictions.

## Installation 

1. To run this microservice locally, follow these steps: 

```bash
git clone https://github.com/Ruban2205/housing-prediction-microservice.git
cd housing-prediction-microservice
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Start the microservice

```
python app.py
```

The microservice will start running locally at `http://localhost:5000`

## API Usage

**Endpoint**

- POST `/predict`

**Request Body**

The `/predict` endpoint expects a JSON object with the following format: 

```json
{
  "area": 1500,
  "rooms": 3,
  "age": 15
}
```

- `area` (integer): The area of the house in square feet.
- `rooms` (integer): The number of rooms in the house.
- `age` (integer): The age of the house in years.

**Response**

The endpoint responds with a JSON object containing the predicted price: 

```json
{
  "predicted_price": 250000
}
```

## Contributing

Thank you for considering contributing to the Housing Prediction Microservice! Please follow these guidelines:

1. **Reporting Bugs**: Search existing issues before reporting bugs.
2. **Enhancements**: Suggest new features or improvements via GitHub issues.
3. **Code Contributions**: Fork the repo, create a branch, and submit a pull request.
4. **Pull Requests**: Ensure tests are added for new code. Get a sign-off before merging.

## Deployment

For deployment, ensure to set the necessary environment variables and configure the microservice to run in a production environment. This typically involves using a production-grade WSGI server like Gunicorn and setting up appropriate logging.

## License 

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

Star ⭐ this repository for Future use 😊
