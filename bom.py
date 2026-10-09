import copy
import csv
import sys
from datetime import date
from pathlib import Path

from openpyxl import load_workbook

TEMPLATE = Path(__file__).parent / "template.xlsx"
GENERATED = Path(__file__).parent / "generated"

# Template rows
FIRST_DATA_ROW = 8   # linha modelo ímpar (fundo branco)
EVEN_MODEL_ROW = 9   # linha modelo par (fundo azul claro)
TOTAL_MODEL_ROW = 10 # linha de TOTAL
FOOTER_ROW = 12      # nota sobre DNP

# Template columns
COL_NUMBER = 1
COL_REFERENCE = 2
COL_QTY = 3
COL_DESCRIPTION = 4
COL_MPN = 5
COL_LCSC = 6
COL_PACKAGE = 7
COL_UNIT_PRICE = 8
COL_TOTAL = 9
LAST_COL = 9

# Others
REFERENCE_CHARS_PER_LINE = 19
DESCRIPTION_CHARS_PER_LINE = 60
EXTRA_LINE_HEIGHT = 14
DNP_COLOR = "FFC00000"

def csv_kicad_read(csv_path):
    """Reads the KiCad CSV and returns only the components that go into the BOM"""
    parts = []

    with open(csv_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Exclude from BOM"] != "":
                continue
            parts.append(row)

    return parts

def terminal_ask(terminal_question, default=""):
    """Prompts for input in the terminal. If the answer is empty, uses the default"""
    if default != "":
        terminal_question = terminal_question + " [" + default + "]"

    terminal_answer = input(terminal_question + ": ").strip()

    if terminal_answer == "":
        return default
    return terminal_answer

def main():
    if len(sys.argv) != 2:
        print("Usage: python bom.py path/to/project.csv")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    xlsx_path = GENERATED / (csv_path.stem + "_BOM.xlsx")

    parts = csv_kicad_read(csv_path)

    total_parts = 0
    for part in parts:
        total_parts = total_parts + int(part["Qty"])

    print(total_parts)


if __name__ == "__main__":
    main()