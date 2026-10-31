
import pandas as pd
import numpy as np


# ==================================================
# 1. PANDAS SERIES
# ==================================================

# Creating a Series from a dictionary
points = {"Elolo": 2, "Abednego": 3}

point_series = pd.Series(points)
print(point_series)
print()

# Accessing Series index and values
print(point_series.index)
print(point_series["Elolo"])
print()

# Generating a random integer between 0 and 9
random_series = pd.Series(np.random.choice(10, size=1))
print(random_series)
print()

# Generating a Series using range()
generate = pd.Series(range(12))
print(generate)
print()

# Creating a Series with custom indexes
generate = pd.Series(
    range(5),
    index=["a", "b", "c", "d", "e"]
)
print(generate)
print()


# ==================================================
# 2. PERFORMING OPERATIONS ON SERIES
# ==================================================

random_series_one = pd.Series(np.random.rand(10))
random_series_two = pd.Series(np.random.rand(10))

# Addition
result = random_series_one + random_series_two
print(result)
print()

# Multiplication
multi = random_series_one[1:] * random_series_two[:-1]
print(multi)
print()

# Note: Pandas aligns values using index labels.


# ==================================================
# 3. CREATING DATAFRAMES
# ==================================================

# Method 1: From a dictionary of lists

countries = ["Ghana", "UAE", "Canada", "Uganda", "Togo"]
median_age = [45, 34, 23, 56, 32]

dataframe = {
    "Countries": countries,
    "Median_age": median_age
}

dataframe_df = pd.DataFrame(dataframe)
print(dataframe_df)
print()


# Method 2: From a list of tuples

data = [
    ("Ghana", 23, 34, 45, 56),
    ("UAE", 23, 34, 4, 57)
]

tuple_df = pd.DataFrame(data)
print(tuple_df)
print()


# Method 3: From a list of dictionaries

data = [
    {
        "Country": "Ghana",
        "Capital": "Accra",
        "Density": 4,
        "GDP": 1
    },
    {
        "Country": "UAE",
        "Capital": "Abu Dhabi",
        "Density": 6
    }
]

data_df = pd.DataFrame(data)
print(data_df)
print()

# ==================================================
# 4. ACCESSING DATAFRAME ELEMENTS
# ==================================================

# Accessing the Country column
print(data_df["Country"])
print()

# Accessing UAE
print(data_df["Country"].iloc[1])
print()

# Accessing the last row
print(data_df.iloc[-1])
print()

# Changing DataFrame indexes
data_df.index = ["a", "b"]
print(data_df)
print()

# ==================================================
# 5. ADDING AND DELETING COLUMNS
# ==================================================

# Adding a new column
data_df["Language"] = ["Ewe", "Arabic"]
print(data_df)
print()

# Deleting a column using del
# del data_df["Language"]

# Deleting a column using pop()
# removed_column = data_df.pop("Language")
# print(removed_column)

# Inserting a column at a specific position
data_df.insert(
    1,
    "Position",
    ["Middle", "First"]
)

print(data_df)
print()


# ==================================================
# 6. FILTERING AND CALCULATIONS
# ==================================================

# Checking countries with density below 5
less = data_df["Density"] < 5
print(less)
print()

# Returning matching rows
filtered_df = data_df[data_df["Density"] < 5]
print(filtered_df)
print()

# Adding Boolean results as a new column
data_df.insert(4, "Less than 5", less)

# Calculating total density
total_density = data_df["Density"].sum()
print(total_density)
print()

# Calculating density proportion
data_df["Density proportion"] = (
    data_df["Density"] / total_density
)

print(data_df)
print()

# ==================================================
# 7. TRANSPOSING AND LOOPING THROUGH DATAFRAMES
# ==================================================

print("Original DataFrame:")
print(data_df)
print()

# Transposing rows and columns
transpose = data_df.T

print("\nTransposed DataFrame:")
print(transpose)
print()

# Looping through transposed columns
for label, values in transpose.items():
    print(label)
    print(values)
print()


# ==================================================
# 8. COMBINING DATAFRAMES
# ==================================================

# Creating additional country records
new_data = [
    {
        "Country": "Ethiopia",
        "Capital": "Addis Ababa",
        "Density": 9
    },
    {
        "Country": "Mali",
        "Density": 7
    }
]

new_data_df = pd.DataFrame(new_data)

# Combining DataFrames vertically
combined_df = pd.concat(
    [data_df, new_data_df],
    ignore_index=True
)

print(combined_df)
print()

# ==================================================
# 9. CONCATENATING MULTIPLE DATAFRAMES WITH KEYS
# ==================================================

df1 = pd.DataFrame({
    "Density": [12, 23, 45, 65],
    "Median age": [18, 34, 23, 56],
    "Population in Million": [123, 234, 345, 567],
    "Population change(%)": [0.12, 0.23, 0.34, 0.45],
    "Country name": ["Ghana", "Togo", "Benin", "Nigeria"]
})

df2 = pd.DataFrame({
    "Density": [45, 67, 89, 43],
    "Median age": [45, 65, 23, 12],
    "Population in Million": [567, 876, 437, 934],
    "Population change(%)": [0.56, 0.76, 0.857, 0.81],
    "Country name": ["UAE", "India", "America", "Canada"]
})

df3 = pd.DataFrame({
    "Density": [45, 67, 36, 26],
    "Median age": [45, 41, 52, 55],
    "Population in Million": [345, 523, 432, 511],
    "Population change(%)": [0.45, 0.34, 0.23, 0.45],
    "Country name": ["Australia", "Antarctica", "Congo", "Burkina Faso"]
})

# Creating a list containing all DataFrames
frames = [df1, df2, df3]

# Combining DataFrames with hierarchical indexes
result = pd.concat(
    frames,
    keys=["Region one", "Region two", "Region three"]
)

print(result)
print()

# Accessing Region Two only
print(result.loc["Region two"])
print()

# Accessing the second row by position
print(result.iloc[1])
print()