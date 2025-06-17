import pandas as pd

def analyze_pit_penalties(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola pit stop sopra la media e penalità per ciascun pilota.

    :param df: DataFrame con colonne: Driver, PitDuration (sec), PenaltySeconds
    :return: DataFrame aggregato per pilota
    """
    pit_data = df[df['PitDuration'].notnull()]
    penalty_data = df[df['PenaltySeconds'].notnull()]

    avg_pit = pit_data['PitDuration'].mean()

    results = []
    drivers = df['Driver'].unique()

    for driver in drivers:
        driver_pits = pit_data[pit_data['Driver'] == driver]
        driver_penalties = penalty_data[penalty_data['Driver'] == driver]
        
        pits_over_avg = (driver_pits['PitDuration'] > avg_pit).sum()
        penalties_count = driver_penalties.shape[0]
        penalties_sec = driver_penalties['PenaltySeconds'].sum()
        
        results.append({
            'Driver': driver,
            'PSE': pits_over_avg,
            'PO': penalties_count,
            'POS': penalties_sec
        })
    
    return pd.DataFrame(results)

def save_pit_penalties(df: pd.DataFrame, output_path: str):
    """
    Salva i dati di pit stop e penalità in un CSV.

    :param df: DataFrame
    :param output_path: Percorso file output
    """
    df.to_csv(output_path, index=False, sep=';')

if __name__ == "__main__":
    input_file = "data/raw_pit_penalty_data.csv"
    output_file = "data/pit_penalties.csv"
    
    data = pd.read_csv(input_file, sep=';')
    result = analyze_pit_penalties(data)
    save_pit_penalties(result, output_file)
    print(f"Dati pit stop e penalità salvati in {output_file}")
