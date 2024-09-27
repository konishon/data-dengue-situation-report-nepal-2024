import camelot
import pandas as pd
import os
import argparse
from tqdm import tqdm
from openpyxl import load_workbook

OUTPUT_DIR = './data/CSVs/'

def extract_tables_with_camelot(pdf_path):
    """Extracts tables from a PDF using camelot and returns them as a list of DataFrames."""
    tables = camelot.read_pdf(
        pdf_path, 
        pages="all", 
        flavor="stream",  
        split_text=True,  
    )

    if not tables:
        raise ValueError("No tables found in the PDF")

    combined_tables = pd.concat([table.df for table in tqdm(tables, desc="Processing tables")])

    correct_headers = [
        'SN', 'PROVINCE', 'DISTRICT', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'TOTAL'
    ]
    
    # Replace the headers of the DataFrame
    combined_tables.columns = correct_headers

    return combined_tables

def filter_valid_provinces(df):
    """Keeps only rows that contain valid province names."""
    valid_provinces = [
        "KOSHI PROVINCE", "MADHESH PROVINCE", "BAGMATI PROVINCE", 
        "GANDAKI PROVINCE", "LUMBINI PROVINCE", "KARNALI PROVINCE", 
        "SUDUR PASHCHIM PROVINCE"
    ]
    
    df_filtered = df[df['PROVINCE'].isin(valid_provinces)]

    return df_filtered

def save_to_csv(df, output_path):
    """Saves the DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Data successfully extracted and saved to {output_path}.")

def show_csv_content(df):
    """Shows a preview of the first few rows of the CSV file."""
    print("\nPreview of the CSV content:")
    print(df.head()) 

def main():
    parser = argparse.ArgumentParser(description="Extract tables from a PDF and save them to an Excel file.")
    parser.add_argument("pdf_path", help="Path to the input PDF file")
    parser.add_argument("--auto-clean", action="store_true", help="Automatically clean rows without valid province values. It tries to remove rows that do not contain province names like 'KOSHI PROVINCE', 'MADHESH PROVINCE', etc. However, be aware that this operation might fail for non-standard table structures or misaligned data.")
    
    args = parser.parse_args()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    base_name = os.path.splitext(os.path.basename(args.pdf_path))[0]
    output_csv_path = os.path.join(OUTPUT_DIR, f"{base_name}_extracted_tables.csv")

    if not os.path.exists(args.pdf_path):
        raise FileNotFoundError(f"File not found: {args.pdf_path}")
    
    try:
        print(f"Extracting tables from {args.pdf_path}...")
        df = extract_tables_with_camelot(args.pdf_path)

        # Auto-clean rows without valid province values if the flag is set
        if args.auto_clean:
            print("Auto-clean enabled: Attempting to remove rows without valid province names...")
            print("This may fail if the table structure is non-standard or if there are misaligned data points.")
            df = filter_valid_provinces(df)

        save_to_csv(df, output_csv_path)
        
        show_csv_content(df)
        
        print(f"\nYou can access the file here: {output_csv_path}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
