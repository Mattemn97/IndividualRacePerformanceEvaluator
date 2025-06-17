import pandas as pd

def compute_driver_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola metriche base per ciascun pilota sulla base dei dati dei giri.
    
    :param df: DataFrame contenente i dati dei giri.
    :return: DataFrame con metriche aggregate per pilota.
    """
    metrics = []
    drivers = df['Driver'].unique()

    for driver in drivers:
        driver_data = df[df['Driver'] == driver]
        
        pp = driver_data.iloc[0]['Position']  # posizione partenza (primo giro registrato)
        pa = driver_data.iloc[-1]['Position']  # posizione arrivo (ultimo giro registrato)
        pg = pp - pa
        
        gc = driver_data['LapNumber'].nunique()
        
        # Sorpassi e altri dati non sono direttamente ricavabili dal dataset base
        # Placeholder a 0, andranno integrati con analisi avanzate o altre fonti
        se = 0
        ss = 0
        uc = 0
        cc = 0
        cs = 0
        rc = 0
        rs = 0
        gg = 0  # giri in testa (da calcolare se disponibile colonna leader)
        
        metrics.append({
            'Driver': driver,
            'PP': pp,
            'PA': pa,
            'PG': pg,
            'SE': se,
            'SS': ss,
            'UC': uc,
            'CC': cc,
            'CS': cs,
            'RC': rc,
            'RS': rs,
            'GG': gg,
            'GC': gc
        })
    
    return pd.DataFrame(metrics)

def save_driver_metrics(df: pd.DataFrame, output_path: str):
    """
    Salva le metriche dei piloti in un file CSV.
    
    :param df: DataFrame delle metriche
    :param output_path: Percorso del file CSV di output
    """
    df.to_csv(output_path, index=False, sep=';')

if __name__ == "__main__":
    input_file = "data/raw_race_data.csv"
    output_file = "data/driver_metrics.csv"
    
    data = pd.read_csv(input_file, sep=';')
    metrics = compute_driver_metrics(data)
    save_driver_metrics(metrics, output_file)
    print(f"Metriche salvate in {output_file}")
