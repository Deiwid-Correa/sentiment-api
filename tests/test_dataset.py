import pandas as pd

DATASET_PATH = "sentiment_dataset.csv"

def test_dataset_structure():
    df = pd.read_csv(DATASET_PATH)
    assert list(df.columns) == ["texto", "sentimiento"]

def test_dataset_not_empty():
    df = pd.read_csv(DATASET_PATH)
    assert len(df) > 0

def test_dataset_no_nulls():
    df = pd.read_csv(DATASET_PATH)
    assert df.isnull().sum().sum() == 0

def test_dataset_no_duplicates():
    df = pd.read_csv(DATASET_PATH)
    assert df.duplicated().sum() == 0

def test_sentiment_labels_valid():
    df = pd.read_csv(DATASET_PATH)
    valid_labels = {"positivo", "neutro", "negativo"}
    assert set(df["sentimiento"].unique()).issubset(valid_labels)
