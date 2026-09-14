from pathlib import Path
import csv
import re

BASE_DIR = Path(__file__).resolve().parent
TXT_PATH = BASE_DIR / "sintomas_pacientes.txt"
CSV_PATH = BASE_DIR / "mapa_sintomas_doencas.csv"


def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"[^a-zà-úç\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def carregar_mapa() -> list[tuple[str, str]]:
    mapeamento = []
    with CSV_PATH.open("r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            sint1 = (linha.get("Sintoma 1") or "").strip().lower()
            sint2 = (linha.get("Sintoma 2") or "").strip().lower()
            doenca = (linha.get("Doença Associada") or "").strip()
            if sint1 and doenca:
                mapeamento.append((sint1, doenca))
            if sint2 and doenca:
                mapeamento.append((sint2, doenca))
    return mapeamento


def sugerir_diagnostico(frase: str, mapeamento: list[tuple[str, str]]) -> str:
    frase_normalizada = normalizar(frase)
    diagnosticos = []

    for sintoma, doenca in mapeamento:
        if sintoma in frase_normalizada:
            diagnosticos.append(doenca)

    if not diagnosticos:
        return "Diagnóstico não identificado com base no mapa de sintomas."

    contagem = {}
    for item in diagnosticos:
        contagem[item] = contagem.get(item, 0) + 1

    return max(contagem, key=contagem.get)


def main() -> None:
    mapeamento = carregar_mapa()

    with TXT_PATH.open("r", encoding="utf-8") as arquivo:
        frases = [linha.strip() for linha in arquivo if linha.strip()]

    print("=== Diagnósticos sugeridos ===")
    for indice, frase in enumerate(frases, start=1):
        diagnostico = sugerir_diagnostico(frase, mapeamento)
        print(f"{indice}. {frase}\n   Diagnóstico sugerido: {diagnostico}\n")


if __name__ == "__main__":
    main()
