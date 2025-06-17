import pandas as pd

def compute_league_rating(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola la Valutazione di Lega base per ogni pilota.

    :param df: DataFrame con tutte le variabili aggregate per pilota
    :return: DataFrame con Valutazione di Lega
    """
    df['ValutazioneLega'] = (
        df['SE'] - df['SS'] + df['UC']
        - df['CC'] + df['CS']
        - df['RC'] - df['RS']
        + df['GG'] + df['GC']
    )
    return df

def compute_weighted_rating(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola la Valutazione di Lega ponderata per ogni pilota.

    :param df: DataFrame con tutte le variabili aggregate per pilota
    :return: DataFrame con Valutazione di Lega ponderata
    """
    df['ValutazionePonderata'] = (
        (df['PP'] * 0.75 + df['PG'])
        + (df['SE'] - df['SS'] + df['UC'])
        - (df['CC'] * 1.25 - df['PP'] + df['RC'] + df['RS'])
    )
    return df

def save_evaluation(df: pd.DataFrame, output_path: str):
    """
    Salva le valutazioni in un file CSV.

    :param df: DataFrame con valutazioni
    :param output_path: Percorso file output
    """
    df.to_csv(output_path, index=False, sep=';')

if __name__ == "__main__":
    input_file = "data/merged_driver_data.csv"
    output_file = "data/evaluation.csv"

    data = pd.read_csv(input_file, sep=';')
    data = compute_league_rating(data)
    data = compute_weighted_rating(data)
    save_evaluation(data, output_file)

    print(f"Valutazioni salvate in {output_file}")
