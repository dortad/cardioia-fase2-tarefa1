from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "frases_risco.csv"


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    X = df["frase"].astype(str)
    y = df["situacao"].astype(str)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.35,
        random_state=42,
        stratify=y,
    )

    vetorizador = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
    X_train_vec = vetorizador.fit_transform(X_train)
    X_test_vec = vetorizador.transform(X_test)

    modelo = LogisticRegression(max_iter=1000, random_state=42)
    modelo.fit(X_train_vec, y_train)

    previsoes = modelo.predict(X_test_vec)
    acuracia = accuracy_score(y_test, previsoes)

    print("=== Avaliação do classificador de risco ===")
    print(f"Acurácia: {acuracia:.2f}")
    print("\nRelatório de classificação:")
    print(classification_report(y_test, previsoes, zero_division=0))

    frases_novas = [
        "dor no peito e falta de ar",
        "cansaço leve sem desconforto",
        "sudorese fria e pressão no tórax",
    ]

    novas_entradas = vetorizador.transform(frases_novas)
    print("\nExemplos de classificação:")
    for frase, pred in zip(frases_novas, modelo.predict(novas_entradas)):
        print(f"- '{frase}' -> {pred}")


if __name__ == "__main__":
    main()
