🤖 AI Data Quality Checker Agent

An AI-powered data quality checking application built with Python and Streamlit.

This project allows users to upload a CSV file and automatically check the dataset for common data quality issues such as missing values and duplicate records.

🚀 Features

- 📂 Upload CSV files
- 📊 Display uploaded data
- 🔍 Detect missing values
- 🔁 Detect duplicate rows
- 📈 Display number of rows and columns
- ⚠️ Show data quality warnings
- ✅ Provide a simple data quality report
- 🌐 Easy-to-use Streamlit interface

🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- GitHub

📁 Project Structure

ai-data-quality-checker-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
└── sample_data/
    └── sample.csv

⚙️ Installation

1. Clone the repository

git clone https://github.com/Meganathkm/ai-data-quality-checker-agent.git

2. Open the project folder

cd ai-data-quality-checker-agent

3. Install the required libraries

pip install -r requirements.txt

▶️ Run the Application

Run the following command:

streamlit run app.py

The application will open in your browser.

📊 How to Use

1. Open the application.
2. Click Browse files.
3. Upload a CSV file.
4. The application displays the uploaded data.
5. The application checks the dataset for missing values.
6. The application checks for duplicate rows.
7. A data quality report is displayed.

🧪 Sample Data

A sample CSV file is available in:

sample_data/sample.csv

The sample dataset contains intentional data-quality issues such as:

- Missing Age
- Missing Email
- Missing Salary
- Duplicate records

These issues are included to demonstrate how the data quality checker works.

📋 Sample Output

The application displays:

Rows: 6
Columns: 5
Duplicate Rows: 1

Missing Values:

Age       1
Email     1
Salary    1

The application also displays warnings when missing values or duplicate rows are detected.

🎯 Project Objective

The objective of this project is to provide a simple and user-friendly tool for identifying common data quality problems in CSV datasets.

It can help users quickly identify incomplete or duplicate data before using the dataset for further analysis.

👨‍💻 Author

Meganath KM

📌 Future Improvements

- Automatic data cleaning
- Invalid email detection
- Outlier detection
- Data type validation
- AI-based data quality suggestions
- Downloadable data quality reports
- Support for Excel files