import pandas as pd
import requests
from bs4 import BeautifulSoup 

# Generate an automation workflow for data collection from csv and website

def extract_from_website(url):
    # Function to extract data from html website
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find a table element
        table = soup.find('table')

        # If a table is found, extract the data
        if table:
            headers = [th.text for th in table.find('tr').find_all('th')]
            data = []
		  # The loop will find all tr tags (table rows)
            for row in table.find_all('tr')[1:]:
			# Within each table row, select all td (table data)
                row_data = [td.text for td in row.find_all('td')]
			# Appends the value from the td to the data array
                data.append(dict(zip(headers, row_data)))

            return pd.DataFrame(data)
        else:
            print("No table found on the page.")
            return None
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None
    
def gather_data_from_sources():
  data_from_csv = pd.read_csv('sales_data.csv')
  # Example: Fetching data from a website using requests & BeautifulSoup 
  web_data_url = 'https://example.com/marketing_data'
  data_from_website = extract_from_website(web_data_url)   
  return pd.concat([data_from_csv, data_from_website], axis=1) # Combine data

def process_and_format_data(data):
  # ... Process data to create Price Per Unit column.
  formatted_data = data[['Total Order Price', 'Number of Units']] 
  formatted_data['Price Per Unit'] = formatted_data['Total Order Price'] / formatted_data['Number of Units']
  return formatted_data

def generate_report(data):
  # Generate final report (could use pandas' to_excel, or libraries like ReportLab, matplotlib, etc).
  data.to_excel('marketing_report.xlsx')
  print("Report generated successfully!") 
    
# Main Automation Flow
raw_data = gather_data_from_sources()
processed_data = process_and_format_data(raw_data)
generate_report(processed_data)