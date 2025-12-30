def draw_lines(pdf, start_y=20, end_y=290, step=10):
    for y in range(start_y, end_y, step):
        pdf.line(10, y, 200, y)