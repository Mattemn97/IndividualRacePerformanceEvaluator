import pandas as pd


def generate_weekly_report(evaluation_df: pd.DataFrame, output_path: str):
    """
    Genera un report settimanale semplice in formato CSV con le valutazioni medie per pilota.

    :param evaluation_df: DataFrame con colonne Driver, ValutazioneLega, ValutazionePonderata
    :param output_path: Percorso file CSV di output
    """
    report = evaluation_df.groupby('Driver').agg({
        'ValutazioneLega': 'mean',
        'ValutazionePonderata': 'mean'
    }).reset_index()

    report.to_csv(output_path, index=False, sep=';')


if __name__ == '__main__':
    input_file = 'data/evaluation.csv'
    output_file = 'reports/weekly_report.csv'

    df = pd.read_csv(input_file, sep=';')
    generate_weekly_report(df, output_file)

    print(f'Report settimanale salvato in {output_file}')
