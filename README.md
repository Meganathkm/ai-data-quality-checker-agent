🤖 AI Data Quality Checker

A simple and user-friendly AI-powered Data Quality Checker built with Python and Streamlit. This application helps users quickly identify common data quality issues in CSV files, such as missing values and duplicate records.

---

🚀 Features

- 📂 Upload CSV files
- 🧪 Use sample CSV data
- 📊 Preview uploaded data
- 🔍 Detect missing values
- ♻️ Detect duplicate rows
- 📈 Display total rows and columns
- ⚠️ Generate data quality warnings
- ✅ Easy-to-use Streamlit interface
- 📋 Provides a quick summary of dataset quality

---

🧠 How It Works

The application follows a simple data-quality checking workflow:

          CSV File
              │
              ▼
      ┌─────────────────┐
      │ Upload / Sample │
      │      Data       │
      └────────┬────────┘
               │
               ▼
      ┌─────────────────┐
      │ Data Preview    │
      └────────┬────────┘
               │
               ▼
      ┌─────────────────────────┐
      │ Data Quality Analysis   │
      │                         │
      │ • Missing Values        │
      │ • Duplicate Rows        │
      │ • Rows & Columns        │
      └──────────┬──────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Quality Report  │
        │ & Warnings      │
        └─────────────────┘

---

🔍 Data Quality Checks

1. Missing Values

The application checks every column for missing or empty values.

Example:

Name     Age     City
John     22      Coimbatore
Priya            Chennai
Arun     24      Coimbatore

The application identifies that the "Age" column contains a missing value.

---

2. Duplicate Rows

The application detects completely duplicated records in the dataset.

Example:

Name    Age    City
John    22     Coimbatore
Priya   23     Chennai
John    22     Coimbatore

The third row is identified as a duplicate.

---

3. Dataset Statistics

The application displays basic information such as:

- Total number of rows
- Total number of columns
- Column names
- Missing-value counts
- Duplicate-row count

---

🛠️ Technologies Used

Technology| Purpose
Python| Application development
Pandas| Data processing and analysis
Streamlit| Web application interface
CSV| Dataset input format

---

📁 Project Structure

AI-Data-Quality-Checker/
│
├── app.py
├── requirements.txt
├── README.md
│
└── sample_data/
    └── sample.csv

---

⚙️ Installation

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Run the application

streamlit run app.py

The application will open in your browser.

---

📊 Sample Dataset

The project includes a sample CSV file for testing.

Example:

Name,Age,City,Salary
Arun,24,Coimbatore,25000
Priya,,Chennai,28000
Kumar,26,Coimbatore,30000
Arun,24,Coimbatore,25000

This sample contains:

- A missing value
- A duplicate row
- Multiple columns
- Different data types

---

💻 Usage

1. Open the Streamlit application.
2. Upload a ".csv" file.
3. View the uploaded dataset.
4. Check the number of rows and columns.
5. Review missing-value information.
6. Check duplicate records.
7. Read the generated data-quality warnings.
8. Use the results to clean the dataset.

---

🌐 Streamlit Deployment

This application can be deployed using Streamlit Community Cloud.

Basic deployment steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Select the GitHub repository.
4. Select "app.py" as the main file.
5. Deploy the application.

---

🎯 Project Objective

The main objective of this project is to provide a simple automated solution for identifying common data-quality problems before using a dataset for further analysis.

It can be useful for:

- Data analysts
- Students
- Beginners learning data quality
- CSV data validation
- Basic data-cleaning workflows

---

🔮 Future Enhancements

Possible future improvements include:

- 🤖 AI-generated data quality recommendations
- 📊 Interactive data-quality dashboard
- 📈 Data-quality score
- 🧹 Automatic data cleaning
- 📥 Download cleaned CSV files
- 🔎 More validation rules
- 📑 Generate data-quality reports
- 🛡️ Detect incorrect data types and invalid values

---

👨‍💻 Author

Meganath KM

---

⭐ Project Highlights

This project demonstrates practical knowledge of:

- Python
- Pandas
- CSV data handling
- Data quality checking
- Streamlit
- GitHub
- Basic data analysis
- Web application deployment

---

📌 Conclusion

The AI Data Quality Checker provides a simple way to inspect CSV datasets and identify common quality issues such as missing values and duplicate records.

It is designed as a beginner-friendly project while providing a foundation for building more advanced AI-powered data-quality solutions.