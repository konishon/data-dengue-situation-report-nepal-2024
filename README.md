# Dengue Cases Nepal 2024 Data Extraction

This project is a Python script that extracts tabular data from a PDF file (containing dengue cases data) and saves it to an Excel file. The extracted data can then be used for further analysis or reporting.


## Features

- Extract tables from a PDF document using `pdfplumber`.
- Convert the extracted tables into a `pandas` DataFrame.
- Save the DataFrame to an Excel file with a name derived from the original PDF file.
- Command-line interface for easy use.

## Requirements

To run this script, you need to have Python installed along with the following Python libraries:

- `pdfplumber`
- `pandas`
- `openpyxl`

### Installation

To install the required packages, follow these steps:

1. Clone the repository or download the script files.
2. Install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Usage 
python dengue_cases_nepal_data_extraction.py path/to/your/pdf_file.pdf

This will generate an Excel file named dengue_cases_nepal_extracted_tables.xlsx in the same directory as your PDF file.


### Error Handling

- If the PDF file doesn't exist, the script will raise a FileNotFoundError.
- If no tables are found in the PDF, the script will raise a ValueError.

### License 
This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

