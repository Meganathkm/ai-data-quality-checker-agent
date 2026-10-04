import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Data Quality Checker",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Quality Checker")
st.write("Check your CSV data for common quality issues.")

option = st.radio(
    "Choose an option:",
    ["🧪 Use Sample Data", "📂 Upload CSV"]
)

if option == "🧪 Use Sample Data":

    data = {
        "Name": [
            "Meganath",
            "Mounika",
            "Arun",
            "Priya",
            "Karthik",
            "Meganath"
        ],
        "Age": [
            22,
            21,
            None,
            24,
            23,
            22
        ],
        "Email": [
            "meganath@gmail.com",
            "mounika@gmail.com",
            "arun@gmail.com",
            None,
            "karthik@gmail.com",
            "meganath@gmail.com"
        ],
        "Salary": [
            25000,
            28000,
            30000,
            27000,
            None,
            25000
        ],
        "Department": [
            "IT",
            "HR",
            "Finance",
            "IT",
            "HR",
            "IT"
        ]
    }

    df = pd.DataFrame(data)

    st.success("✅ Sample data loaded successfully!")

else:

    uploaded_file = st.file_uploader(
        "Upload your CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        st.info("Please upload a CSV file.")
        st.stop()


st.subheader("📊 Data Preview")
st.dataframe(df)

st.subheader("🔍 Data Quality Report")

missing_values = df.isnull().sum()
duplicate_rows = df.duplicated().sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Duplicate Rows", duplicate_rows)

st.write("### Missing Values")

missing_table = pd.DataFrame({
    "Column": missing_values.index,
    "Missing Values": missing_values.values
})

st.dataframe(missing_table)

if duplicate_rows > 0:
    st.warning(
        f"⚠️ Found {duplicate_rows} duplicate row(s)."
    )
else:
    st.success("✅ No duplicate rows found.")

if missing_values.sum() > 0:
    st.warning(
        "⚠️ Missing values were found in the dataset."
    )
else:
    st.success("✅ No missing values found.")

st.success("✅ Data quality check completed!")
    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Duplicate Rows", duplicate_rows)

    st.write("### Missing Values")

    missing_table = pd.DataFrame({
        "Column": missing_values.index,
        "Missing Values": missing_values.values
    })

    st.dataframe(missing_table)

    if duplicate_rows > 0:
        st.warning(f"⚠️ Found {duplicate_rows} duplicate row(s).")
    else:
        st.success("✅ No duplicate rows found.")

    if missing_values.sum() > 0:
        st.warning("⚠️ Missing values were found in the dataset.")
    else:
        st.success("✅ No missing values found.")

    st.success("✅ Data quality check completed!")