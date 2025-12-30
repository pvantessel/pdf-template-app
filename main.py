from fpdf import FPDF
import pandas as pd
from helpers import draw_lines

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Set header
    pdf.add_page()
    pdf.set_font(family="Helvetica", style="B", size=20)
    pdf.set_text_color(254,0,0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Draw lines
    draw_lines(pdf)

    # Set footer
    pdf.ln(265)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] -1 ):
        # Set header
        pdf.add_page()

        # Draw lines
        draw_lines(pdf)

        # Set footer
        pdf.ln(277) # 265 (break lines ln) + 12 (height cell header)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
