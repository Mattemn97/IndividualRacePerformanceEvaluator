import fastf1
import pandas as pd

def collect_race_data(year: int, grand_prix: str, session_type: str = 'R') -> pd.DataFrame:
    """
    Scarica i dati della gara tramite FastF1 e restituisce un DataFrame con le informazioni principali.
    
    :param year: Anno del gran premio
    :param grand_prix: Nome del gran premio (es. 'Monza')
    :param session_type: Tipo di sessione (default 'R' per Race)
    :return: DataFrame con i dati dei giri
    """
    session = fastf1.get_session(year, grand_prix, session_type)
    session.load()
    laps = session.laps
    
    if laps.empty:
        raise ValueError("Nessun dato trovato per la gara specificata.")
    
    # Seleziona alcune colonne base
    df = laps[['Driver', 'LapNumber', 'Position', 'PitInTime', 'PitOutTime', 'Time', 'LapTime']].copy()
    
    return df

def save_race_data(df: pd.DataFrame, output_path: str):
    """
    Salva il DataFrame in un file CSV.
    
    :param df: DataFrame da salvare
    :param output_path: Percorso del file CSV di output
    """
    df.to_csv(output_path, index=False, sep=';')

if __name__ == "__main__":
    # Esempio di utilizzo
    year = 2024
    grand_prix = "Monza"
    output_file = "data/raw_race_data.csv"
    
    data = collect_race_data(year, grand_prix)
    save_race_data(data, output_file)
    print(f"Dati salvati in {output_file}")
