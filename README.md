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

## KiCad CSV

Export the BOM from the schematic editor with **Tools > Generate Bill of
Materials** as CSV.
The column order does not matter, but the header names must be exactly:

| Column | Content |
| --- | --- |
| Reference | Designators, e.g. C1,C2 |
| Qty | Quantity |
| Description | Short description of the part |
| DNP | Any text marks the row as Do Not Populate (shown in red) |
| Exclude from BOM | Any text drops the row from the spreadsheet |
| MPN | Manufacturer part number |
| LCSC | LCSC part number |
| Package | Footprint / package |

Group the symbols **only by MPN** when exporting, so each row of the
spreadsheet is one unique part.
