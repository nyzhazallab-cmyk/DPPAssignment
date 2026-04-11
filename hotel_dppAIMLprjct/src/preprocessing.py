from sklearn.model_selection import train_test_split
from src.config import TARGET, TEST_SIZE

def split_data(df):
    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    return train_test_split(X, y, test_size=TEST_SIZE, random_state=42)