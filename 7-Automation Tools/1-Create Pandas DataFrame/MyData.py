#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ============================================================
# PYTHON DATA ANALYSIS SCRIPT
# Generated from Excel Export
# File: MyData.py
# Data Source: MyData.xlsx
# ============================================================

# SECTION 1: IMPORT LIBRARIES
# These libraries are needed for data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SECTION 2: LOAD EXCEL DATA
# Read the Excel file created by the export
df = pd.read_excel('MyData.xlsx')
print('Data loaded successfully!')
print(f'Shape: {df.shape}')  # (rows, columns)
print(f'Columns: {list(df.columns)}')

# SECTION 3: DATA EXPLORATION
# Basic data inspection
print('\\n=== DATA PREVIEW ===')
print(df.head())  # First 5 rows

print('\\n=== DATA INFORMATION ===')
print(df.info())  # Data types and non-null counts

print('\\n=== BASIC STATISTICS ===')
print(df.describe())  # Statistical summary

# SECTION 4: CHECK FOR MISSING VALUES
missing_values = df.isnull().sum()
print('\\n=== MISSING VALUES ===')
print(missing_values[missing_values > 0])

# SECTION 5: SAVE AS CSV (OPTIONAL)
# Uncomment below to save as CSV
# df.to_csv('MyData.csv', index=False)
# print('Data saved as CSV')

# SECTION 6: NEXT STEPS
# Add your own analysis code below:
# 
# 1. Data cleaning
#    df_clean = df.dropna()  # Remove missing values
# 
# 2. Filtering data
#    filtered = df[df['column_name'] > 100]
# 
# 3. Grouping and aggregation
#    grouped = df.groupby('category_column').mean()
# 
# 4. Visualization
df['numeric_column'].hist()
plt.show()

