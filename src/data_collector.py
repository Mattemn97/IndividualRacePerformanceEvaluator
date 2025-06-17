import fastf1
import fastf1.api
import pandas as pd
from pathlib import Path


def fetch_race_data(year: int, gp: str) -> pd.DataFrame:
    """
    Recupera i dati telemetrici di un gran premio specifico.

    :param year: L'anno del campionato
    :param gp: Nome del gran premio (esempio: 'Monza')
    :return: DataFrame con i dati del gran premio
    """
    session = fastf1.get_session(year, gp, 'R')
    session.load()

    laps = session.laps
    
    # Selezioniamo solo le colonne utili
    columns = [
        'Driver', 'Position', 'LapTime', 'PitOutTime', 'PitInTime', 'IsAccurate'
    ]
    df = laps[columns].copy()
    return df


def save_race_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    Salva i dati raccolti in un file CSV.

    :param df: DataFrame con i dati da salvare
    :param output_path: Percorso di destinazione del file CSV
    """
    df.to_csv(output_path, index=False, sep=';')


if __name__ == "__main__":
    # Esempio di utilizzo
    YEAR = 2024
    GP_NAME = "Monza"
    OUTPUT_FILE = Path("data/2024_monza_race_data.csv")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = fetch_race_data(YEAR, GP_NAME)
    save_race_data(data, OUTPUT_FILE)
    print(f"Dati salvati in {OUTPUT_FILE}")
