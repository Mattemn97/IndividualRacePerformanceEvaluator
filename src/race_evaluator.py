import pandas as pd


def compute_league_rating(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola la valutazione di lega per ciascun pilota.

    :param df: DataFrame con i dati della gara
    :return: DataFrame con il pilota e la sua valutazione
    """
    # In questo esempio minimale ci basiamo su colonne generiche,
    # dovranno essere sostituite o integrate quando i dati veri saranno disponibili.
    result = (
        df.groupby("Driver")
        .agg({
            "Position": "min",  # Esempio: posizione migliore come surrogato
            "LapTime": "count"   # Numero di giri completati
        })
        .reset_index()
    )

    result["LeagueRating"] = (
        (result["LapTime"])  # GG + GC semplificato: giri completati
        - (result["Position"])  # penalizzazione posizione peggiore
    )
    return result


def save_rating(df: pd.DataFrame, output_path: str) -> None:
    """
    Salva la valutazione in un file CSV.

    :param df: DataFrame con la valutazione
    :param output_path: Percorso file CSV di output
    """
    df.to_csv(output_path, index=False, sep=';')


if __name__ == "__main__":
    INPUT_FILE = "data/2024_monza_race_data.csv"
    OUTPUT_FILE = "data/2024_monza_league_rating.csv"

    race_data = pd.read_csv(INPUT_FILE, sep=';')
    rating = compute_league_rating(race_data)
    save_rating(rating, OUTPUT_FILE)
    print(f"Valutazione salvata in {OUTPUT_FILE}")
