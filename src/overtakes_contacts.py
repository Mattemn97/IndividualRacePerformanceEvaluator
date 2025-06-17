import pandas as pd

def detect_overtakes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analizza i dati giro per giro per stimare i sorpassi effettuati e subiti da ciascun pilota.

    :param df: DataFrame dei dati gara ordinato per LapNumber e Position
    :return: DataFrame con sorpassi effettuati e subiti per pilota
    """
    overtakes_data = []
    drivers = df['Driver'].unique()
    
    # Inizializza dizionario per conteggi
    counts = {driver: {'SE': 0, 'SS': 0} for driver in drivers}
    
    # Ordina per giro e posizione
    df_sorted = df.sort_values(by=['LapNumber', 'Position'])
    
    for lap in df_sorted['LapNumber'].unique():
        lap_data = df_sorted[df_sorted['LapNumber'] == lap]
        prev_lap_data = df_sorted[df_sorted['LapNumber'] == (lap - 1)]
        
        if prev_lap_data.empty:
            continue
        
        for driver in drivers:
            curr_pos = lap_data[lap_data['Driver'] == driver]['Position']
            prev_pos = prev_lap_data[prev_lap_data['Driver'] == driver]['Position']
            
            if curr_pos.empty or prev_pos.empty:
                continue

            curr_pos = curr_pos.iloc[0]
            prev_pos = prev_pos.iloc[0]

            if curr_pos < prev_pos:
                counts[driver]['SE'] += 1
            elif curr_pos > prev_pos:
                counts[driver]['SS'] += 1

    for driver in drivers:
        overtakes_data.append({
            'Driver': driver,
            'SE': counts[driver]['SE'],
            'SS': counts[driver]['SS'],
            'UC': 0,  # da calcolare con dati pit stop avanzati
            'CC': 0,  # da calcolare con dati contatti
            'CS': 0   # da calcolare con dati contatti
        })

    return pd.DataFrame(overtakes_data)

def save_overtakes_contacts(df: pd.DataFrame, output_path: str):
    """
    Salva i dati di sorpassi e contatti in un CSV.
    
    :param df: DataFrame
    :param output_path: Percorso file output
    """
    df.to_csv(output_path, index=False, sep=';')

if __name__ == "__main__":
    input_file = "data/raw_race_data.csv"
    output_file = "data/overtakes_contacts.csv"
    
    data = pd.read_csv(input_file, sep=';')
    result = detect_overtakes(data)
    save_overtakes_contacts(result, output_file)
    print(f"Dati sorpassi e contatti salvati in {output_file}")
