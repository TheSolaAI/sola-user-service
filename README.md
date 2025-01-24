# Sola User Service

## Overview

Sola User Service is a Django DRF-based microservice for user authentication and management, designed for the SolaAI application. This service handles user registration, login, and profile management.

## Features

- User registration
- User login
- Token-based authentication
- User profile management
- Password reset

## Installation

### Prerequisites

- Python 3.13
- Django 5.2
- Django REST Framework

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/TheSolaAI/sola-user-service.git
    cd sola-user-service
    ```

2. Install `pipenv` if you haven't already:

    ```sh
    pip install pipenv
    ```

3. Install the dependencies and create a virtual environment:

    ```sh
    pipenv install --dev
    ```

4. Activate the virtual environment:

    ```sh
    pipenv shell
    ```

5. Apply migrations:

    ```sh
    python manage.py migrate
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

For detailed API documentation, please visit the Swagger docs available at the home page of the development server.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [support@solaai.xyz](mailto:support@solaai.xyz).
