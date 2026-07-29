import requests

URL = "https://www.mvdis.gov.tw/m3-emv-trn/exm/locations"

response = requests.get(
    URL,
    timeout=30
)

print("狀態碼：", response.status_code)
print(response.text[:500])