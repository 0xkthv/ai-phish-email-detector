import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/emails.csv")
OUT_PATH = Path("data/processed/emails_clean.csv")

def main():
    df = pd.read_csv(RAW_PATH)
    df = df.dropna(subset=["email_text", "label"])
    df.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
