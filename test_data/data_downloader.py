import requests
import pandas as pd

# URL of the Excel file
url = "https://federaciondecafeteros.org/app/uploads/2024/04/Exportaciones.xlsx"

# Download the file
try:
    response = requests.get(url)
    response.raise_for_status()
except Exception as e:
    print(f"Error fetching the data: {e}")

# Save the file locally
with open("test_data/Exportaciones.xlsx", "wb") as f:
    f.write(response.content)
print("File downloaded successfully :)")

