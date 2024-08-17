import json

input_file = '/Users/homesachin/Downloads/Company.json'
output_file = '/Users/homesachin/Downloads/CompanyExtracted.json'

with open(input_file, 'r') as file:
    data = json.load(file)

# Extract company data
company_data = []
for item in data:
    if item.get('type') == 'table':
        company_data.extend(item.get('data', []))

# Save extracted data to a new file
with open(output_file, 'w') as file:
    json.dump(company_data, file, indent=4)
