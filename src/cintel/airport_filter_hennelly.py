from pathlib import Path

import pandas as pd

files = list(Path("data").glob("ign_*_ontime.csv"))
df = pd.concat([pd.read_csv(f) for f in files])

stl = df[(df['DEST'] == 'STL')]
stl.to_csv("data/stl_2025_ontime.csv", index=False)
