# 🧠 Predicting to Save Lives: Supervised Learning for COVID-19 Case Forecasting

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Health AI](https://img.shields.io/badge/SDG-3%20Good%20Health%20and%20Well-being-brightgreen)

### 🌍 Overview

This project applies **supervised machine learning** (Linear Regression) to **predict active COVID-19 cases** based on pandemic indicators such as total cases, deaths, recoveries, tests, and population data.

Aligned with the **United Nations Sustainable Development Goal 3 (SDG 3)** — *Good Health and Well-being* — this solution highlights the critical role of **AI in healthcare**, especially in pandemic preparedness and response.

---

### 🎯 Goals

- Predict **Active COVID-19 Cases**
- Assist in **resource planning** and **early warning systems**
- Showcase **ethical use of AI** in healthcare decision support

---

### 🧠 Machine Learning Approach

We used **Linear Regression** from `scikit-learn` to estimate the number of active cases from key health metrics.

### 🔍 Features Used

- `Total Cases`  
- `Total Deaths`  
- `Total Recovered`  
- `Total Test`  
- `Population`

### 🎯 Target Variable

- `Active Cases`

---

### 📊 Model Performance

After training, the model outputs: 
- `R² Score: 0.97`
- `Root Mean Squared Error: 1853.41`
- `Predicted Active Cases: 25000`


A **line chart** is also generated showing actual vs. predicted active cases.

---

## 🛠️ How to Use

### 1. Clone the Repository

git bash
git clone https://github.com/yourusername/covid19-prediction.git
cd covid19-prediction

### 2. Install Dependencies
Install the required Python packages:

`bash`

`pip install -r requirements.txt`

### 3. Add Dataset
Ensure that your dataset is named:

`text`

`COVID DATA.csv`
It should include the following columns: Serial Number, Country, Total Cases, Total Deaths, Total Recovered, Total Test, Population, Active Cases

### 4. Run the Script
`bash`
`python covid_prediction.py`
You’ll see model metrics printed in the terminal and a graph displayed.

## 📦 Requirements
The following Python libraries are required to run the project:
`-pandas`
`-numpy`
`-matplotlib`
`-scikit-learn`

## 📈 Sample Visualization
A graph is plotted comparing actual and predicted values of active cases using matplotlib:

Blue: Actual Active Cases

Orange: Predicted Active Cases

## 🛡️ Ethical Considerations
✅ Data Privacy: Dataset is anonymized and does not contain personal identifiers.

✅ Ethical AI Use: AI serves as a decision-support tool, not a replacement for medical professionals.

✅ Responsible Development: Model use is transparent, and limitations are acknowledged.

## 📄 License
This project is open-source and available under the MIT License.
You are free to use, distribute, and modify the code with proper credit.


## 🙌 Acknowledgments
Special thanks to healthcare professionals, data scientists, and open-data providers who made this kind of research possible. Together, we can build tools that contribute to global well-being and a smarter future in healthcare

## 👥 Contributors
This project was collaboratively developed as part of a health-focused AI research initiative:

Mary Njengah – marynjengah2011@gmail.com

Annie Kiruja – rodahannie65@gmail.com

Sparrow Manoti – nyamoitasparrow@gmail.com

Eric Kinyanjui – ericmbugua825@gmail.com

George Kelly – kellyochieng249@gmail.com
