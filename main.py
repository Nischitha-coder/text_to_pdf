import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    df = pd.read_csv(filepath)
    pdf.add_page()
    pdf.set_font(family="Times", size=20, style="b")
    filename = Path(filepath).stem
    pdf.cell(w=0, h=15, txt=filename.title(),ln=1)
    # pdf.set_font(family="Times", size=10)
    # pdf.multi_cell(w=0, h=5, txt=df.columns[0], border=1)

    with open(filepath, 'r') as file:
        content = file.read()
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=5, txt=content)


pdf.output("output.pdf")