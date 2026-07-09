import requests
import json

TARGET_API_URL = "https://onebridge.breezy.hr/"


application_data = {
    "email": "ayushdipdl@gmail.com",
    "firstName": "Ayushdip",
    "lastName": "Deka",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

print(f"Sending application to {TARGET_API_URL}...")

try:
    response = requests.post(
        TARGET_API_URL,
        json=application_data,
        headers=headers,
    )

    # Check if the portal accepted it
    if response.status_code in [200, 201]:
        print("Success! Application submitted.")
        try:
            print(response.json())
        except ValueError:
            print("Response is not valid JSON.")
    else:
        print(f"Failed. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")