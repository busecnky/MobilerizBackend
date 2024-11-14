import requests


response = requests.post('http://127.0.0.1:8001/vendors_and_products', json={
    "vendor_name": "Vendor1",
    "base_url": "https://673113a17aaf2a9aff0fc6e2.mockapi.io/api/v1/vendor1"
})

if response.status_code == 200:
    print("Veriler başarıyla kaydedildi.")
else:
    print("Hata oluştu:", response.status_code, response.text)