
import httpx
import asyncio

async def register_and_login():
    base_url = "http://localhost:8000/api/v1"
    
    # 1. Register a new user
    signup_url = f"{base_url}/auth/signup"
    user_data = {
        "email": "superuser@example.com",
        "password": "strong_password" 
    }
    print(f"Registering user: {user_data['email']}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(signup_url, json=user_data)
            response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx) 
            print("User registered successfully:", response.json())
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 400 and "Email already registered" in e.response.text:
            print(f"User {user_data['email']} already registered. Proceeding to login.")
        else:
            print(f"Failed to register user: {e.response.status_code} - {e.response.text}")
            return
    except httpx.RequestError as e:
        print(f"An error occurred while registering user: {e}")
        return

    # 2. Log in to get a token
    login_url = f"{base_url}/auth/login"
    login_data = {
        "username": user_data["email"],
        "password": user_data["password"]
    }
    print(f"Logging in user: {user_data['email']}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(login_url, data=login_data)
            response.raise_for_status()
            token_response = response.json()
            print("Login successful. Access Token:", token_response["access_token"])
            # Now you have the access token, you can set it as an environment variable
            # For demonstration, we'll just print it.
            return token_response["access_token"]
    except httpx.HTTPStatusError as e:
        print(f"Failed to login: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        print(f"An error occurred while logging in: {e}")
    return None

if __name__ == "__main__":
    access_token = asyncio.run(register_and_login())
    if access_token:
        print(f"\n--- Use this token as AUTH_TOKEN: {access_token} ---")
    else:
        print("\n--- Failed to obtain access token ---")
