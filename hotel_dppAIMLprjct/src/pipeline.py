from .data_loader import load_data
from .preprocessing import split_data
from .feature_engineering import add_features
from .models.logistic import build_model
from .evaluation import evaluate

def run_pipeline():

    df = load_data()

    df = add_features(df)

    X_train, X_test, y_train, y_test = split_data(df)

    num_cols = X_train.select_dtypes(include='number').columns
    cat_cols = X_train.select_dtypes(exclude='number').columns

    model = build_model(num_cols, cat_cols)

    model.fit(X_train, y_train)

    score = evaluate(model, X_test, y_test)

    print("F1 Score:", score)