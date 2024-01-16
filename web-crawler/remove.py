import json

# Read the JSON file
with open('links.json', 'r') as file:
    data = json.load(file)

# Remove duplicates
data = [dict(t) for t in {tuple(sorted(d.items())) for d in data}]


# Write the updated data back to the JSON file
with open("links-test.json", "w") as f:
    json.dump(data, f, indent=4)
