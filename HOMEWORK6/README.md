![UI Dashboard](Screenshots/UI%20Dashboard.jpg)

# Crypto Pulse API

Crypto Pulse is a small Flask startup-style API that fetches live crypto prices, (parse the incoming JSON, extract at least 3 specific pieces of data, add some custom logic , like filtering or calculating something new), and return your own clean, customized JSON dictionary to the user from CoinGecko (Bitcoin, Ethereum, Litecoin), calculates simple metrics (average,
spread, top performer), and serves a lightweight dashboard UI.

## Features

- Health check endpoint for service monitoring
- Crypto pricing endpoint with calculated metrics
- Built-in browser dashboard at `/api/v1/data`
- Root redirect from `/` to `/api/v1/data`

## Local Setup (Windows PowerShell)

1. Create a virtual environment:

```powershell
python -m venv .venv
```

2. Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```run command
pip install -r requirements.txt
```

## Run The App Locally

```
python app.py
```
or

```
flask run
```

Server URL: `http://127.0.0.1:5000`  
Dashboard URL: `http://127.0.0.1:5000/api/v1/data`

## API Endpoints

- `GET /` -> redirects to `/api/v1/data`
- `GET /api/v1/health` -> returns service status and version
- `GET /api/v1/crypto` -> returns live prices and calculated metrics
- `GET /api/v1/data` -> returns dashboard HTML page
