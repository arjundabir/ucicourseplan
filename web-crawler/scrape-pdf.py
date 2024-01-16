import requests
import pdfplumber
import json

# URL of the PDF file
pdf_url = "https://catalogue.uci.edu/undergraduatedegrees/undergraduatedegrees.pdf"

# Download the PDF
response = requests.get(pdf_url)
response.raise_for_status()  # Ensure the download was successful

# Save the PDF to a local file
with open("undergraduatedegrees.pdf", "wb") as f:
    f.write(response.content)

# Open the PDF with pdfplumber
with pdfplumber.open("undergraduatedegrees.pdf") as pdf:
    links = []
    for page in pdf.pages:
        # Extract links from each page
        page_links = page.hyperlinks
        links.extend(page_links)

# Create a JSON object
json_data = []
for link in links:
    json_data.append({"uri": link['uri']})

# Write the JSON object to a file
with open("links.json", "w") as f:
    json.dump(json_data, f, indent=4)
