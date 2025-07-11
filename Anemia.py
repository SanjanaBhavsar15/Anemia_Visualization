import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="📊 Anemia Analysis Dashboard", layout="wide")
st.title("🩸 NFHS Anemia Analysis Across India")

# File uploader
uploaded_file = st.file_uploader("📂 Upload Anemia Excel File", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace("\n", " ").str.replace("’", "'")

    # Remove 'India' aggregate row
    df = df[df["State/UT"] != "India"].copy()

    # Convert data columns to numeric
    numeric_cols = df.columns[3:]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Select indicator and chart type
    col_to_plot = st.selectbox("📌 Select Indicator to Visualize", options=numeric_cols)
    chart_type = st.radio("📊 Choose Chart Type", ["Bar Chart", "Pie Chart", "Heatmap", "Stacked Bar Chart", "Line Chart","Box Plot"])

    st.subheader("📈 Visualization")

    if chart_type == "Bar Chart":
        sorted_df = df.sort_values(by=col_to_plot, ascending=False)
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=sorted_df, x="State/UT", y=col_to_plot, ax=ax)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots()
        top_states = df.nlargest(5, col_to_plot)
        ax.pie(top_states[col_to_plot], labels=top_states["State/UT"], autopct='%1.1f%%')
        ax.set_title(f"Top 5 States by {col_to_plot}")
        st.pyplot(fig)

    elif chart_type == "Heatmap":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df[numeric_cols].transpose(), cmap="YlGnBu", annot=False)
        ax.set_yticklabels(numeric_cols, rotation=0)
        st.pyplot(fig)

   
    elif chart_type == "Stacked Bar Chart":
        st.warning("Stacked Bar works best for multiple grouped columns (e.g., Women Mild/Moderate/Severe)")
        if {"Women_Mild (11.0–11.9)", "Women_Moderate (8.0–10.9)", "Women_Severe (<8.0)"}.issubset(df.columns):
            fig, ax = plt.subplots(figsize=(14, 6))
            stacked_data = df.set_index("State/UT")[[
                "Women_Mild (11.0–11.9)",
                "Women_Moderate (8.0–10.9)",
                "Women_Severe (<8.0)"
            ]]
            stacked_data.plot(kind="bar", stacked=True, colormap="Pastel1", ax=ax)
            plt.xticks(rotation=90)
            plt.title("Women Anemia Severity by State")
            st.pyplot(fig)
        else:
            st.error("Required columns for stacked bar chart not found in data.")

    elif chart_type == "Line Chart":
        fig, ax = plt.subplots(figsize=(14, 6))
        line_df = df.sort_values(by=col_to_plot)
        sns.lineplot(data=line_df, x="State/UT", y=col_to_plot, marker="o", ax=ax)
        plt.xticks(rotation=90)
        plt.title(f"Line Chart of {col_to_plot}")
        st.pyplot(fig)

    elif chart_type == "Box Plot":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(y=df[col_to_plot], ax=ax)
        plt.title(f"Box Plot of {col_to_plot}")
        st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>Made with ❤ by <b>Sanjana Bhavsar</b> | AI/ML Engineer</p>",
    unsafe_allow_html=True
) 

