# akash-api-demo

Demo using Akash API

## Environment Variables

### 1. Backend

Create a `.env` file in the `backend` directory with the API key from https://chatapi.akash.network/

```dotenv
OPENAI_API_KEY=your_api_key_here
```

Build backend:
```bash
cd backend
docker build -t backend .
```

Run backend:
```bash
docker run -d -p 5001:5001 --name backend backend
```

### 2. Frontend

Build frontend:
```bash
cd frontend
docker build -t frontend .
```

Run frontend:
```bash
docker run -d -p 3000:3000 --name frontend frontend
```

### 3. Running Both

Create a `docker-compose.yml` file in your root directory:

```yaml
version: '3'
services:
  backend:
    build:
      context: ./backend
    ports:
      - "5001:5001"
    env_file:
      - ./backend/.env
  frontend:
    build:
      context: ./frontend
    ports:
      - "3000:3000"
```

Build and run both services:
```bash
docker-compose up --build
```

## Accessing the Application

- Frontend: Open http://localhost:3000 in your web browser.
- Backend: The backend API will be accessible at http://localhost:5001.
