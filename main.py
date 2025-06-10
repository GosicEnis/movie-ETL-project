import pandas as pd


# === EXTRACT ===
def extract_movie_data(file_name):
    return pd.read_csv(file_name)

# === TRANSFORM ===


# Pretvaranje kolona u numericke vrednosti
def convert_columns_to_numeric(data):
    data["budget"] = pd.to_numeric(data["budget"], errors="coerce")
    data["box_office"] = pd.to_numeric(data["box_office"], errors="coerce")
    return data.dropna(subset=["budget", "box_office"])


# Filtriranje po drzavi
def filter_by_country(data, country):
    return data[data["country"] == country].copy()


# Dodavanje nove kolone 'balance'
def calculate_balance(data):
    data["balance"] = data["box_office"] - data["budget"]
    return data


# Uklanjanje nepotrebnih kolona
def remove_unnecessary_columns(data):
    return data.drop(["language", "country", "duration", "budget", "box_office"], axis=1)


# Sortiranje po bilansu
def sort_by_balance(data):
    return data.sort_values(by="balance", ascending=False)


# Uzimanje top 10 filmova
def get_top_10(data):
    return data.head(10)

# === LOAD ===


# Upis u Excel fajl
def load_to_excel(data, output_file):
    data.to_excel(output_file, index=False)


# === KOMPLETAN ETL ZA JEDNU DRZAVU ===
def etl_for_country(data, country_name, output_file):
    df = (data.pipe(filter_by_country, country_name)
              .pipe(calculate_balance)
              .pipe(sort_by_balance)
              .pipe(get_top_10)
              .pipe(remove_unnecessary_columns))
    load_to_excel(df, output_file)


# === MAIN ===

def main():
    file_name = "movies.csv"
    data = extract_movie_data(file_name)
    data = convert_columns_to_numeric(data)

    countries = {
        "USA": "top_10_usa.xlsx",
        "Russia": "top_10_russia.xlsx",
        "UK": "top_10_uk.xlsx",
        "South Korea": "top_10_south_korea.xlsx"
    }

    for country, output_file in countries.items():
        etl_for_country(data, country, output_file)

    print("ETL process completed. Files were successfully created.")


if __name__ == "__main__":
    main()
