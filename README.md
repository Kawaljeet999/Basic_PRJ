# Basic_PRJ

Here's a README file for your project:

---

# Bedsheet Size Data Extraction

This project demonstrates how to extract data from a web page, specifically a bedsheet size chart, and export it to an Excel file using Python. The project utilizes the `requests`, `BeautifulSoup`, and `pandas` libraries.

## Project Overview

The goal of this project is to automate the process of fetching bedsheet size data from a website and organizing it into a structured format that can be easily analyzed or used for further processing. The data is extracted from a table on the webpage and is then exported to an Excel file.

## Prerequisites

To run this project, you'll need to have Python installed on your system along with the following libraries:

- `requests`: To make HTTP requests and fetch the HTML content from the web page.
- `BeautifulSoup4`: To parse the HTML content and extract the required data.
- `pandas`: To organize the extracted data into a DataFrame and export it to an Excel file.

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Project Workflow

1. **Fetch HTML Content**: The script starts by sending an HTTP GET request to the specified URL to fetch the HTML content of the web page.

2. **Parse HTML with BeautifulSoup**: The fetched HTML content is then parsed using BeautifulSoup to create a parse tree, allowing for easy extraction of specific elements.

3. **Extract Data**: The script locates the table containing the bedsheet size data and extracts all rows (`<tr>` tags) from the table. Each row is further broken down into individual cells (`<td>` tags), and the text content is extracted and cleaned.

4. **Organize Data**: The extracted data is organized into a list of lists, which is then converted into a pandas DataFrame. The DataFrame is structured with columns corresponding to the type of bedsheet and its respective dimensions.

5. **Export to Excel**: Finally, the DataFrame is exported to an Excel file named `Sheet.xlsx`. The index is not included in the Excel file for a cleaner output.

## Running the Script

Simply run the Python script in your preferred environment:

```bash
python script.py
```

After execution, the bedsheet size data will be saved in an Excel file named `Sheet.xlsx` in the same directory as the script.

## Note

Ensure that the URL in the script points to the correct webpage containing the bedsheet size chart. The structure of the table on the webpage should match the script’s parsing logic.

## License

This project is open-source and available under the MIT License.

---

This README provides a concise overview of your project and instructions on how to use it.
