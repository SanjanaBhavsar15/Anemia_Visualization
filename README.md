
# 🩸 Anemia Analysis Dashboard – NFHS India 🇮🇳

This interactive **Streamlit dashboard** visualizes anemia-related insights across Indian states based on NFHS data. Users can explore gender-specific anemia rates, severity levels, and state-wise comparisons through dynamic charts and graphs.

---

## 📂 Dataset

The app uses an Excel file `Anemia_India_Merged_Updated.xlsx` containing:
- Anemia prevalence among 👶 children, 👩 women, and 👨 men
- Severity distribution: **Mild**, **Moderate**, **Severe**
- Data for all Indian states and UTs (excluding India aggregate)

---

## 🚀 Features

| Visualization Type     | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 📊 **Bar Chart**        | State-wise comparison for any selected indicator                            |
| 🥧 **Pie Chart**        | Top 5 states based on selected indicator in a pie representation             |
| 🌡️ **Heatmap**          | Color-coded intensity map of anemia prevalence                              |
| 🧱 **Stacked Bar Chart**| Severity-wise breakdown of anemia in women (mild, moderate, severe)         |
| 📈 **Line Chart**       | Trend line of anemia prevalence across states                               |
| 📦 **Box Plot**         | Distribution and outlier detection for a selected indicator                  |
| 🧭 **Gender Comparison**| Grouped bar chart for child, women, and men anemia rates                     |

---

## 🛠️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/anemia-dashboard
cd anemia-dashboard
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit app
```bash
streamlit run app.py
```

### 4. Upload the Excel file
Upload `Anemia_India_Merged_Updated.xlsx` when prompted.

---

## 📁 File Structure

```
📦 anemia-dashboard
├── app.py                     # Streamlit app file
├── Anemia_India_Merged_Updated.xlsx  # Dataset (can be user-uploaded)
├── requirements.txt           # Python dependencies
└── README.md                  # You're here!
```

---

## 📌 Dependencies

- streamlit
- pandas
- matplotlib
- seaborn
- openpyxl

> Install using:  
```bash
pip install streamlit pandas matplotlib seaborn openpyxl
```

---

## 🧠 Insights Enabled

- Which states have the highest anemia prevalence in children?
- How do gender disparities look across states?
- What is the severity distribution among women?
- Are there states with extreme outliers?

---

## 📄 License

This project is open-source under the MIT License.
