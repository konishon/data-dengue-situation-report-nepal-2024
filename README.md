# Dengue Cases Nepal 2024 Data Extraction 

This project is a Python script that extracts tabular data from a PDF file of **Epidemiology and Disease Control Division Department of Health Services, Ministry of Health & Population** (containing dengue cases data) and saves it to an Excel file. The extracted data can then be used for further analysis or reporting.

> ℹ️ Visit the public data download platform to view dengue situation reports for Nepal 2024 on [https://konishon.github.io/data-dengue-situation-report-nepal-2024/](https://konishon.github.io/data-dengue-situation-report-nepal-2024/)


## Features

- Extract tables from a PDF document using `pdfplumber`.
- Convert the extracted tables into a `pandas` DataFrame.
- Save the DataFrame to an Excel file with a name derived from the original PDF file.


### Installation

To install the required packages, follow these steps:

1. Clone the repository or download the script files.
2. Install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Usage 
#### Generating CSVs from PDFs
```bash
python generate_html.py data/CSVs/66f3af5ec20b2-2_extracted_tables.csv
```
![image](https://github.com/user-attachments/assets/59c1c126-326b-4fbd-94c3-5034bc369977)

This will generate an CSV file named dengue_cases_nepal_extracted_tables.CSV

#### Generatic Static Public Data Download Page
```bash
python generate_html.py data/CSVs/66f3af5ec20b2-2_extracted_tables.csv
```
![image](https://github.com/user-attachments/assets/eeb553d2-34f8-4b8f-a789-2dd04ae9065f)


This will generate the public data download page avalaible at [https://konishon.github.io/data-dengue-situation-report-nepal-2024/](https://konishon.github.io/data-dengue-situation-report-nepal-2024/)

### Error Handling

- If the PDF file doesn't exist, the script will raise a FileNotFoundError.
- If no tables are found in the PDF, the script will raise a ValueError.

### License 
This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

