import requests


url = "http://127.0.0.1:8000/vendors/fetch"  # FastAPI sunucunuzun çalıştığı URL


vendor_data = {
    "vendor_name": "Vendor1",
    "base_url": "https://673113a17aaf2a9aff0fc6e2.mockapi.io/api/v1/:vendor1"
}


response = requests.post(url, json=vendor_data)


if response.status_code == 200:
    print("Vendor başarıyla eklendi!")
    print(response.json())
else:
    print("Vendor eklenirken hata oluştu:", response.status_code)
    print(response.text)
