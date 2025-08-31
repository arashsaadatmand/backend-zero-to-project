import requests

base_url = "http://127.0.0.1:8000"

# 1. اضافه کردن مخاطب
res = requests.post(f"{base_url}/contacts", json={"name": "Arash", "phone": "0912000000"})
print("POST:", res.json())

# 2. گرفتن همه مخاطب‌ها
res = requests.get(f"{base_url}/contacts")
print("GET all:", res.json())

# 3. جستجوی یک مخاطب
res = requests.get(f"{base_url}/contacts/Arash")
print("GET one:", res.json())

# 4. حذف مخاطب
res = requests.delete(f"{base_url}/contacts/Arash")
print("DELETE:", res.json())
