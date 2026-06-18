import requests, json

resp = requests.get("https://api.github.com/zen")
data = {"quote": resp.text, "status": resp.status_code}
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
print("Saved:", data["quote"])