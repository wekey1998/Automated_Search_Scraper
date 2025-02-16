#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import time
import random

# Define input and output file paths
input_file = "your_input_file.xlsx"  # Replace with actual input file path
output_file = "your_output_file.xlsx"  # Replace with actual output file path
geckodriver_path = "path_to_geckodriver"  # Replace with actual GeckoDriver path

# Load the Excel file and read all columns
df = pd.read_excel(input_file, engine="openpyxl")

# List of base URLs to match
base_urls = [
    "touchupxs.com",
    "abc.com",
    "xyz.com",
    # Add more base URLs here
]

# List of keywords to exclude
exclude_domains_keywords = ["amazon", "ebay", "sears"]

# Initialize WebDriver for Firefox
service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service)

# Function to perform Google search and extract results
def get_google_results(query):
    driver.get(f"https://www.google.com/search?q={query}")
    time.sleep(random.uniform(5, 10))  # Delay between 5 to 10 seconds

    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf a')
    snippets = driver.find_elements(By.CSS_SELECTOR, 'div.IsZvec')
    results = []
    for i, result in enumerate(search_results[:15]):  # Limit to top 15 results
        link = result.get_attribute('href')
        title = result.text
        snippet = snippets[i].text if i < len(snippets) else ""
        results.append((title, link, snippet))
    return results

# Function to check if any base URL is in the extracted link
def match_base_url(extracted_url, base_urls):
    extracted_url_lower = extracted_url.lower()
    parsed_url = urlparse(extracted_url_lower)
    url_to_check = parsed_url.netloc + parsed_url.path
    
    for base_url in base_urls:
        if base_url.lower() in url_to_check:
            return "Match"
    
    for base_url in base_urls:
        if base_url.lower() in parsed_url.netloc:
            return "Match"

# Store final flattened results
flat_results = []
total_items = len(df)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    item_name = row.get('item_name.value', None)
    if pd.notna(item_name):
        print(f"Searching term {index + 1}/{total_items}: {item_name}")
        search_results = get_google_results(item_name)
        
        for title, link, snippet in search_results:
            if any(keyword in link for keyword in exclude_domains_keywords):
                continue
            
            flat_row = row.to_dict()
            flat_row['Google_Title'] = title
            flat_row['Google_Link'] = link
            flat_row['Snippet'] = snippet
            flat_row['Domain'] = urlparse(link).netloc
            flat_row['Match_Status'] = match_base_url(link, base_urls)
            flat_results.append(flat_row)
        
        delay = random.uniform(15, 30)
        print(f"Waiting for {delay:.2f} seconds before the next search...")
        time.sleep(delay)

# Convert the flattened results into a new DataFrame
output_df = pd.DataFrame(flat_results)
output_df.to_excel(output_file, index=False, engine="openpyxl")

driver.quit()
print(f"Results saved to {output_file}")

