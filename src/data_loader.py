import pandas as pd
from pathlib import Path
DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
def load_macro():
 df = pd.read_csv(DATA_DIR / 'vietnam_macro_2020_2025.csv')
 df = df.sort_values('year').reset_index(drop=True)
 return df
def load_sectors():
 return pd.read_csv(DATA_DIR / 'vietnam_sectors_2024.csv')
def load_regions():
 return pd.read_csv(DATA_DIR / 'vietnam_regions_2024.csv')
if __name__ == '__main__':
 macro = load_macro()
 sectors = load_sectors()
 regions = load_regions()
 print('Macro shape:', macro.shape)
 print('Sectors shape:', sectors.shape)
 print('Regions shape:', regions.shape)
 print(macro.head())
