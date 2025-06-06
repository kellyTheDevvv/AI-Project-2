import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset with pandas and display the first 5 rows
df = pd.read_csv('COVID DATA.csv') 
print(df.head())
print(df.info())

# Drop irrelevant columns (make sure the column names are correct!)
df_clean = df.drop(columns=['Serial Number', 'Country']) 

# Remove commas and convert all columns to numeric
for col in df_clean.columns:
    df_clean[col] = df_clean[col].astype(str).str.replace(',', '', regex=False) 
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
df_clean.dropna(inplace=True)

# Define Features and Target Variables
x = df_clean.drop(columns=['Active Cases'])
y = df_clean['Active Cases']

# Check the shape of the data
print(f'x shape: {x.shape}')
print(f'y shape: {y.shape}')

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a Regression Model
model = LinearRegression()
# Fit the model to the training data
model.fit(x_train, y_train)

# Evaluate the Model's Performance
y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f'R² Score: {r2:.2f}')
print(f'Root Mean Squared Error: {rmse:.2f}')

# Make predictions using the model
sample_input = pd.DataFrame([{
    "Total Cases": 1000000,
    "Total Deaths": 25000,
    "Total Recovered": 950000,
    "Total Test": 10000000,
    "Population": 50000000
}])
predicted_active_cases = model.predict(sample_input)[0]

# Show result
print(f'Predicted Active Cases: {round(predicted_active_cases)}') 

# Visualization - Line chart: Actual vs Predicted Active Cases
# Reset indices to ensure alignment
y_test_sorted = y_test.reset_index(drop=True)
y_pred_sorted = pd.Series(y_pred).reset_index(drop=True)

plt.figure(figsize=(12, 6))
plt.plot(y_test_sorted, label="Actual Active Cases", marker='o')
plt.plot(y_pred_sorted, label="Predicted Active Cases", marker='x')
plt.title("Line Chart: Actual vs Predicted Active COVID-19 Cases")
plt.xlabel("Sample Index")
plt.ylabel("Active Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
