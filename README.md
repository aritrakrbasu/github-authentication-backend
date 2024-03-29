# GitHub Authentication Backend

## Introduction

This project is an API server based on FastAPI (python), designed to facilitate the exchange of GitHub code for an access token. It provides a straightforward means for integrating GitHub authentication into your Python applications, allowing users to securely authenticate via GitHub OAuth.

## Features

- **FastAPI Backend:** Utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.
- **Secure Token Exchange:** Exchange GitHub code for access tokens securely.
- **RESTful API:** Provides a clean and easy-to-use RESTful API for authentication purposes.

## How To use

```bash
GET /github/callback?ci=<client_id>&cs=<client_secret>&ruri=<redirect_uri>&code=<code>
```

### Params


| Key  | Description |
| ------------- | ------------- |
| cs  | client_secret  |
| ci  | client_id  |
| ruri  | redirect_uri  |
| code  | code  |

## Responses

All the types of response that you will get if you call the api

### Success

```bash
{
   "status": "200",
   "msg": "Success",
   "access_token": "token"
}
```

### Error

```bash
{
   "status": "400",
   "msg": "Missing code",
   "key_missing":"code"
}
```

## For Self Installation

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/aritrakrbasu/github-authentication-backend.git
   ```

2. Navigate into the project directory:

   ```bash
   cd github-authentication-backend
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Start your development server

1. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

2. Make requests to the API endpoints as needed.

## API Endpoints

#### `GET /github/callback?ci=<client_id>&cs=<client_secret>&ruri=<redirect_uri>&code=<code>`

Exchanges GitHub code for an access token.



Apologies for the oversight. Here's the corrected markdown file for the README:

markdown
Copy code
# GitHub Authentication Backend

## Introduction

This project is an API server based on FastAPI, designed to facilitate the exchange of GitHub code for an access token. It provides a straightforward means for integrating GitHub authentication into your Python applications, allowing users to securely authenticate via GitHub OAuth.

## Features

- **FastAPI Backend:** Utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.
- **OAuth Integration:** Seamlessly integrate GitHub authentication into your applications.
- **Secure Token Exchange:** Exchange GitHub code for access tokens securely.
- **RESTful API:** Provides a clean and easy-to-use RESTful API for authentication purposes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/github-authentication-backend.git
    ```

2. Navigate into the project directory:

    ```bash
    cd github-authentication-backend
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory and add the following:

    ```plaintext
    GITHUB_CLIENT_ID=your-github-client-id
    GITHUB_CLIENT_SECRET=your-github-client-secret
    ```

    Replace `your-github-client-id` and `your-github-client-secret` with your GitHub OAuth application's client ID and client secret respectively.

## Usage

1. Start the server:

    ```bash
    uvicorn main:app --reload
    ```

2. Make requests to the API endpoints as needed.

## API Endpoints

### `POST /auth/github/exchange`

Exchanges GitHub code for an access token.

### Contributing
Contributions are welcome! Feel free to open issues or pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
Thanks to GitHub for providing OAuth authentication services.
This project was inspired by the need for a simple and secure way to authenticate users via GitHub in various client side applications.
