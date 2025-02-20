import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<21} {'Speed':<9} {'MTU':<10}")
print("-" * 50, "-" * 20, "-" * 10, "-" * 10)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    print(f"{attributes['dn']:<50} {attributes['descr']:<21} {attributes['speed']:<9} {attributes['mtu']:<10}")
