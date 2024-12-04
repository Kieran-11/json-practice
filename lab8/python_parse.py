import json

# Read the JSON file
input_file = 'data/schacon.repos.json'
output_file = 'chacon.csv'

# Load data from JSON
with open(input_file, 'r') as file:
    repositories = json.load(file)

# Open the output CSV file in write mode
with open(output_file, 'w') as csv_file:
    # Write the header
    csv_file.write("name,html_url,updated_at,visibility\n")
    
    # Process the first 5 repositories
    for repo in repositories[:5]:
        # Extract required fields
        name = repo.get('name', '')
        html_url = repo.get('html_url', '')
        updated_at = repo.get('updated_at', '')
        visibility = repo.get('visibility', '')

        # Assemble the line and write to the CSV
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)

print(f"CSV file '{output_file}' created with the first 5 repositories.")
