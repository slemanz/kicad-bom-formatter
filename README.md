# Kicad BOM Formatter

Turns the BOM exported by KiCad (.csv) into a formatted spreadsheet (.xlsx)
based on template.xlsx, with columns for unit price and total cost.

## Requirements

Python 3 and openpyxl:

```
pip install openpyxl
```

## Usage

```
python bom.py pcb_generic.csv
```

The script asks for the header fields in the terminal and saves
generated/pcb_generic_BOM.xlsx.