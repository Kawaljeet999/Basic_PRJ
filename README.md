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

Here's a README file for your `Column_ADD.xlsx` script:

---

# Column_ADD.xlsx Script

This Python script creates an Excel file named `Column_ADD.xlsx` using the `openpyxl` library. The script performs the following tasks:

1. **Workbook and Sheet Creation**:
   - A new workbook is created, and the active sheet is selected.

2. **Assign Values to Column A**:
   - The value `12` is assigned to every cell in column A (from row 1 to row 10).

3. **Assign Values to Column B**:
   - The values from a predefined list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` are assigned to column B (from row 1 to row 10).

4. **Sum Values of Columns A and B**:
   - The script iterates through each row (1 to 10), retrieves the values from columns A and B, and calculates their sum.
   - The sum is then stored in column C for the corresponding row.

5. **Optional Alternative Method**:
   - A commented-out alternative method shows how to directly use Excel formulas to calculate the sum of columns A and B in column C.

6. **Save Workbook**:
   - The final workbook is saved with the filename `Column_ADD.xlsx`.

## Prerequisites

- Python 3.x
- `openpyxl` library installed (`pip install openpyxl`)

## How to Use

1. Ensure you have Python and the `openpyxl` library installed.
2. Copy the script to your preferred location.
3. Run the script using a Python interpreter.
4. The output file `Column_ADD.xlsx` will be created in the same directory as the script.

## Explanation

- **Column A**: Contains the value `12` for rows 1 to 10.
- **Column B**: Contains values `1` to `10` respectively for rows 1 to 10.
- **Column C**: Contains the sum of the corresponding values in columns A and B.

For example:
- Row 1: Column A (`12`) + Column B (`1`) = Column C (`13`)
- Row 2: Column A (`12`) + Column B (`2`) = Column C (`14`)
- ... and so on until Row 10.

## Additional Notes

- The commented-out section provides an alternative approach using Excel formulas directly in the cells.
- The script is flexible and can be modified to handle different ranges or calculations as needed.

## License

This script is open-source and can be used freely for educational or personal projects.

---

This README provides a clear overview of the script, its purpose, and how to use it, while staying within 500 words.
