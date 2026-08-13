import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'], 
        'Age': [25, 30, np.nan, 35], 
        'City': ['New York', np.nan, 'London', 'Paris']}
df = pd.DataFrame(data)

# 1. Identifying missing values
print("Missing value counts per column:\n", df.isnull().sum())

# 2. Removing missing values (dropna)
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing value:\n", df_dropped)

# 3. Imputing with mean (for numerical columns)
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with mean:\n", df_filled_mean)

# 3. Imputing with median (for numerical columns)
df_filled_median = df.fillna(df.median(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with median:\n", df_filled_median)

# 4. Handling outliers (demonstration with 'Age')
# Assuming we identify 40 as an outlier based on domain knowledge or visualization
df['Age_capped'] = df['Age'].clip(upper=40)  # Cap values at 40
print("\nDataFrame with 'Age' capped at 40:\n", df)

# 5. Data type conversion
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, handling errors
print("\nData types after conversion:\n", df.dtypes)

# 6. Exploratory Data Analysis
print("\nDescriptive statistics:\n", df.describe())

# Group by and aggregate
grouped_data = df.groupby('City')['Age'].mean()
print("\nAverage Age by City:\n", grouped_data)