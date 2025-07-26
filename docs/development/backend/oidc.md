This backend-only implementation adds OpenID Connect (OIDC) login via Google, GitHub, and Microsoft using [Authlib](https://docs.authlib.org).

## Features
Role-based login with Google, GitHub, Microsoft
Backend-only logic (no frontend UI changes)
Session-based user info (not persisted in DB)

## Setup Instructions

1. Install dependencies

```bash
pip install Authlib python-dotenv
```

1. Copy and fill your .env file

```bash
cp .env.example .env
```
3. Update .env with your OIDC client IDs and secrets

4. Run the app

```bash
flask run
```
5. Login

Visit:
http://localhost:5000/auth/login/google


http://localhost:5000/auth/login/github


http://localhost:5000/auth/login/microsoft


## File Structure

.env.example
auth/
└── oidc.py          # OIDC logic
gramps_webapi/
└── app.py           # Registers blueprint and OAuth setup

## Test
After login, you’ll be redirected back and shown user info. Session storage is temporary and can be extended for persistence.