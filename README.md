# Automated_Search_Scraper
This Python script automates Google searches for a list of items stored in an Excel file. It extracts the top 15 search results, including titles, links, and snippets, and saves them to an output Excel file. The script also checks if the retrieved links match specified base URLs and excludes results containing unwanted keywords.
# Automated Google Search Scraper Using Selenium and Pandas

## Description
This Python script automates Google searches for a list of items stored in an Excel file. It extracts the top 15 search results, including titles, links, and snippets, and saves them to an output Excel file. The script also checks if the retrieved links match specified base URLs and excludes results containing unwanted keywords. It introduces randomized delays to mimic human behavior and avoid detection.

## Features
- Reads search queries from an Excel file.
- Scrapes the top 15 Google search results.
- Extracts titles, URLs, and snippets.
- Matches retrieved links with predefined base URLs.
- Excludes results containing specific keywords.
- Introduces random delays to avoid detection.
- Saves results to an output Excel file.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.7)
- Google Chrome or Mozilla Firefox
- GeckoDriver (for Firefox) or ChromeDriver (for Chrome)

### Required Python Libraries
Install dependencies using pip:
```sh
pip install pandas selenium openpyxl
```

## Usage
1. Replace `your_input_file.xlsx`, `your_output_file.xlsx`, and `path_to_geckodriver` in the script with actual paths.
2. Update the `base_urls` and `exclude_domains_keywords` lists as needed.
3. Run the script:
```sh
python search_scraper.py
```

## Configuration
- **Input File:** Contains the search terms.
- **Output File:** Stores extracted search results.
- **Web Driver Path:** Ensure GeckoDriver or ChromeDriver is correctly installed and referenced in the script.

## Best Practices for Open Source
- **Respect Google’s Terms of Service:** Scraping public data may have restrictions. Check Google’s [robots.txt](https://www.google.com/robots.txt) and [Terms of Service](https://policies.google.com/terms).
- **Implement Rate Limits:** Avoid sending excessive requests to prevent getting blocked. Consider adding delays between requests.
- **Use a User-Agent Header:** Customize request headers to mimic human behavior.
- **Consider Alternative APIs:** Google provides a [Shopping API](https://developers.google.com/shopping-content) for retrieving shopping data.
- **Include a Disclaimer:** State that this project is for educational purposes only and should not be misused.
- **Add a License:** Use an open-source license (e.g., MIT) to clarify permissions.

## License
This project is licensed under the MIT License

## Author
Vigneshwaran


