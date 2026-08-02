import pandas as pd
import seaborn as sns
penguins = sns.load_dataset("penguins")

# Inspect Data
# 1. Show first 5 rows.
# 2. Print shape and dtypes.
# 3. Show count of missing values by column.

print(penguins.head())
print("-" * 100)
print(penguins.shape)
print("-" * 100)
print(penguins.dtypes)
print("-" * 100)
print(penguins.isna().sum())

# Task 2: Selection and Filtering
# 1. Select rows where `species == "Adelie"`.
# 2. Select columns `species`, `island`, `body_mass_g`.
# 3. Filter rows where `body_mass_g > 4500`.

adelie = penguins.loc[penguins["species"] == "Adelie"]
subset_cols = penguins[["species", "island", "body_mass_g"]]
heavy_penguins = penguins.loc[penguins["body_mass_g"] > 4500]
print(adelie)
print("-" * 100)
print(subset_cols)
print("-" * 100)
print(heavy_penguins)

# Task 3: Missing Data
# 1. Create `penguins_clean` by dropping rows with missing `sex`.
# 2. Fill missing `bill_length_mm` with median.
penguins_clean = penguins.dropna(subset=["sex"]).copy()
median_bill = penguins_clean["bill_length_mm"].median()
penguins_clean["bill_length_mm"] = penguins_clean["bill_length_mm"].fillna(median_bill)

# Task 4: GroupBy
# 1. Average `body_mass_g` by `species`.
# 2. Average `flipper_length_mm` by `species` and `sex`.
avg_mass_by_species = penguins_clean.groupby("species", as_index=False)["body_mass_g"].mean()
avg_flipper_species_sex = (
    penguins_clean.groupby(["species", "sex"], as_index=False)["flipper_length_mm"].mean()
)
print(avg_mass_by_species)
print("*" * 100)
print(avg_flipper_species_sex)

# Task 5: Merge and Reshape
# 1. Create a small lookup DataFrame mapping species to a short code.
# 2. Merge it with `penguins_clean`.
# 3. Create a pivot table of average `body_mass_g` by `species` and `sex`.
species_lookup = pd.DataFrame(
    {
        "species": ["Adelie", "Chinstrap", "Gentoo"],
        "species_code": ["ADL", "CHS", "GNT"],
    }
)
merged = penguins_clean.merge(species_lookup, on="species", how="left")

pivot = merged.pivot_table(
    values="body_mass_g",
    index="species",
    columns="sex",
    aggfunc="mean",
)

print(merged.head())
print('+' * 100)
print(pivot) 