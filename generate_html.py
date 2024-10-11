import os
import pandas as pd
import plotly.express as px
import plotly.io as pio
import argparse

def generate_html(csv_file, output_dir):
    
    df = pd.read_csv(csv_file)

    # Clean up the data (convert the month columns to numeric)
    df.iloc[:, 3:] = df.iloc[:, 3:].apply(pd.to_numeric, errors='coerce')

    # Aggregate data by province for the bar chart (sum cases by province)
    df_province = df.groupby('PROVINCE').sum().reset_index()

    # Create a bar chart for total cases per province
    bar_chart = px.bar(df_province, x='PROVINCE', y='TOTAL', title="Total Dengue Cases by Province")
    bar_chart_html = pio.to_html(bar_chart, full_html=False)

    # Transform the data for the line chart (months on the x-axis, cases on the y-axis, and provinces as lines)
    df_province_long = df_province.melt(id_vars=['PROVINCE'], value_vars=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
                                        var_name='Month', value_name='Cases')

    # Create a line chart showing monthly cases for each province
    time_chart_fixed = px.line(df_province_long, x='Month', y='Cases', color='PROVINCE',
                               title="Monthly Dengue Cases in Each Province (2024)")
    time_chart_fixed.update_layout(xaxis_title="Month", yaxis_title="Number of Cases")
    time_chart_fixed_html = pio.to_html(time_chart_fixed, full_html=False)

    html_content_with_loader = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SITUATION REPORT ON DENGUE IN NEPAL- 2024</title>
        
        <!-- Import Google Fonts -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        
        <!-- Favicon -->
    <link rel="icon" href="https://via.placeholder.com/32x32.png?text=Favicon" type="image/png">
    
        <!-- Social Media Preview -->
        <meta property="og:title" content="Dengue Situation in Nepal - 2024">
        <meta property="og:description" content="Stay updated with the latest information on the dengue situation in Nepal. Get details on affected districts, case numbers, and more.">
        <meta property="og:image" content="https://via.placeholder.com/1200x630.png?text=Dengue+Situation+in+Nepal">
        <meta property="og:url" content="https://example.com/dengue-situation-nepal-2024">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:title" content="Dengue Situation in Nepal - 2024">
        <meta name="twitter:description" content="Up-to-date details on dengue cases across Nepal in 2024.">
        <meta name="twitter:image" content="https://via.placeholder.com/1200x630.png?text=Dengue+Situation+in+Nepal">


        <style>
            body {{
                font-family: 'Inter', sans-serif;
                background-color: #f9f9f9;
                color: #333;
                line-height: 1.6;
                margin: 0;
                padding: 0;
            }}
            .container {{
                margin: 40px auto;
                max-width: 90%; 
                display: none; 
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 20px;
                font-weight: 600;
            }}
            p.note {{
                background-color: #f0f0f0;
                padding: 15px;
                border-left: 4px solid #007bff;
                margin-bottom: 10px;
            }}
            .sources {{
                font-size: 0.8rem;
                color: #555;
                margin-top: 20px;
            }}
            .chart-container {{
                margin-bottom: 30px;
            }}
            .btn-primary {{
                background-color: #007bff;
                border: none;
                padding: 10px 20px;
                font-size: 1rem;
                border-radius: 5px;
                font-weight: 600;
            }}
            .btn-primary:hover {{
                background-color: #0056b3;
            }}
            footer {{
                margin-top: 50px;
                text-align: center;
                color: #777;
                font-size: 0.9rem;
            }}

            /* Loader styles */
            .loader {{
                border: 16px solid #f3f3f3;
                border-radius: 50%;
                border-top: 16px solid #3498db;
                width: 120px;
                height: 120px;
                animation: spin 2s linear infinite;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }}

            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}

            /* Full page overlay */
            #loader-container {{
                position: fixed;
                width: 100%;
                height: 100%;
                background-color: rgba(255, 255, 255, 0.8);
                z-index: 9999;
            }}
        </style>
    </head>
    <body>
        <!-- Loader -->
        <div id="loader-container">
            <div class="loader"></div>
        </div>

        <div class="container">
    
            <div class="mt-5">
                <h2>SITUATION REPORT ON DENGUE IN NEPAL- 2024</h2>
                <p>This is a public portal for the project that extracts tabular data from a PDF file (containing dengue cases data) and saves it to an Excel file. The extracted data can then be used for further analysis or reporting.</p>
                <p>You can view the full code that loads the PDF and converts it into Excel in the <a href="https://github.com/konishon/data-dengue-situation-report-nepal-2024">GitHub repository</a>.</p>

            </div>
            
            <!-- Download Button Below the Info Bar -->
            <div class="text-left mb-4">
                <a href="67049d6319129-2_extracted_tables.csv" class="btn btn-primary" download>Download Excel</a>
            </div>

            <!-- Responsive row for charts -->
            <div class="row">
                <!-- Bar Chart -->
                <div class="col-md-6 chart-container">
                    {bar_chart_html}
                </div>

                <!-- Line Chart -->
                <div class="col-md-6 chart-container">
                    {time_chart_fixed_html}
                </div>
            </div>

            <!-- Sources -->
            <div class="sources">
                Sources: <a href="https://edcd.gov.np/news/15-fifteenth-bi-weekly-situation-updae-on-dengue-and-cholera" target="_blank">https://edcd.gov.np/news/15-fifteenth-bi-weekly-situation-updae-on-dengue-and-cholera</a>
            </div>


            <!-- Footer -->
            <footer>
                &copy; 2024 
            </footer>
        </div>

        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

        <!-- JavaScript to hide the loader and show content once loaded -->
        <script>
            window.addEventListener('load', function () {{
                // Hide loader
                document.getElementById('loader-container').style.display = 'none';

                // Show the content
                document.querySelector('.container').style.display = 'block';
            }});
        </script>
    </body>
    </html>
    """

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the HTML content to the output directory
    output_file = os.path.join(output_dir, 'index.html')
    with open(output_file, 'w') as file:
        file.write(html_content_with_loader)

    print(f"Static HTML file with loader has been generated and saved to: {output_file}")

# Set up argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate static HTML report from CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--output_dir", default="docs/", help="Relative directory to save the generated HTML file")
    args = parser.parse_args()

    # Generate the HTML with loader
    generate_html(args.csv_file, args.output_dir)
