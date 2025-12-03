# Malli API

## Introduction
Malli is an e-commerce platform that provides users with a seamless shopping experience.

## Setup
1. Clone the repository: `git clone https://github.com/your-username/malli-api`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Create a database: `python -m app.database`
6. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints
### User Endpoints
* `POST /api/register`: Create a new user account
* `POST /api/login`: Login to an existing user account
* `GET /api/users`: Get a list of all users
* `GET /api/users/{id}`: Get a single user by ID

### Product Endpoints
* `GET /api/products`: Get a list of all products
* `GET /api/products/{id}`: Get a single product by ID

### Cart Endpoints
* `POST /api/cart`: Add a product to the user's cart
* `GET /api/cart`: Get the user's cart

### Order Endpoints
* `POST /api/checkout`: Checkout the user's cart
* `GET /api/orders`: Get the user's order history

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)