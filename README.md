# malli

..

## Tech Stack

- **Frontend**: React + Vite
- **Backend**: FastAPI + SQLAlchemy (Python)
- **Design**: Figma ([View Design](https://www.figma.com/design/cImhUChwG917zWUxE6kpDH/Flexible-Form-Template--Community-?node-id=1-187&t=sSJfLS9kZvttvbXR-0))

## Project Structure

```
malli/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and login
- Product browsing and searching
- Shopping cart management
- Checkout and payment processing
- Order history and tracking
- Product management for administrators
- Order management for administrators

## API Endpoints

- `POST /api/register` - Create a new user account
- `POST /api/login` - Login to an existing user account
- `GET /api/products` - Get a list of all products
- `GET /api/products/{id}` - Get a single product by ID
- `POST /api/cart` - Add a product to the user's cart
- `GET /api/cart` - Get the user's cart
- `POST /api/checkout` - Checkout the user's cart
- `GET /api/orders` - Get the user's order history

## License

MIT
