import requests

def get_example():
    response = requests.get("https://google.com")
    print(f"상태코드: {response.status_code}")
    print(response.text)

if __name__ == "__main__":
    get_example()