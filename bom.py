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

def spread_fill_placeholders(ws, values):
    """Replaces {project}, {designer}... with the values entered"""
    for row in ws.iter_rows(min_row=1, max_row=FIRST_DATA_ROW - 1):
        for cell in row:
            if not isinstance(cell.value, str):
                continue

            for name, value in values.items():
                placeholder = "{" + name + "}"
                cell.value = cell.value.replace(placeholder, value)

def spread_copy_row_style(ws, row):
    """Stores the style of each cell in a template row"""
    styles = []

    for col in range(1, LAST_COL + 1):
        cell = ws.cell(row=row, column=col)
        styles.append(copy.copy(cell._style))

    height = ws.row_dimensions[row].height
    return styles, height

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

    print("Header fields (Enter keeps the value in brackets):")
    values = {
        "project"   : terminal_ask("Project", csv_path.stem),
        "designer"  : terminal_ask("Designed by"),
        "revision"  : terminal_ask("Revision"),
        "date"      : terminal_ask("Report date", date.today().strftime("%d-%b-%Y").upper()),
        "total"     : str(total_parts)
    }

    wb = load_workbook(TEMPLATE)
    ws = wb.active

    spread_fill_placeholders(ws, values)

    # Stores the styles of the template rows before deleting them
    odd_style = spread_copy_row_style(ws, FIRST_DATA_ROW)
    even_style = spread_copy_row_style(ws, EVEN_MODEL_ROW)
    total_style = spread_copy_row_style(ws, TOTAL_MODEL_ROW)

    footer = ws.cell(row=FOOTER_ROW, column=1)
    footer_text = footer.value
    footer_style = copy.copy(footer._style)

    ws.delete_rows(FIRST_DATA_ROW, ws.max_row)

    # One line for component


    wb.save(xlsx_path)
    print("BOM saved to", xlsx_path)


if __name__ == "__main__":
    main()