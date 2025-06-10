# 📊 ETL Process on Movie Dataset

This project demonstrates a complete ETL (Extract, Transform, Load) process using Python and the pandas library, applied to a dataset of movies.

## 🧠 Project Description

The goal of this script is to extract, clean, transform, and export insights about movies based on their performance in different countries. The process involves:

- Reading movie data from a CSV file (`movies.csv`)
- Filtering movies by country (USA, Russia, UK, South Korea)
- Converting budget and box office columns to numeric values
- Calculating the balance (box office - budget)
- Sorting the movies by profitability
- Selecting the top 10 most profitable movies for each country
- Exporting the results into separate Excel files

## 🧩 Dataset Structure

The dataset (`movies.csv`) includes over 500 movie entries with the following columns:

- `title`
- `release_year`
- `genre`
- `director`
- `language`
- `country`
- `duration`
- `budget`
- `box_office`

## ⚙️ How It Works

### Extract

The data is loaded from `movies.csv`.

### Transform

- Non-numeric values in `budget` and `box_office` are cleaned.
- The dataset is filtered by specified countries.
- A new column `balance` is calculated.
- Unnecessary columns are removed.
- Data is sorted by balance.

### Load

The transformed top 10 movies per country are saved in Excel files:

- `top_10_usa.xlsx`
- `top_10_russia.xlsx`
- `top_10_uk.xlsx`
- `top_10_south_korea.xlsx`

## 🚀 How to Run

Make sure you have `pandas` and `openpyxl` installed (for Excel export):

```bash
pip install pandas openpyxl
```

Then simply run the script:

```bash
python main.py
```

## 📂 Output Files

After running the script, you will find four Excel files, each containing the top 10 movies with the highest profit in the specified countries.

## 📌 Author

**Enis Gosić**
