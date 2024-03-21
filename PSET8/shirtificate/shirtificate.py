from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica" , "B", 50)
        self._pdf.cell(0,60, 'CS50 shirtificate' , new_x = "LMARGIN" , new_y = "NEXT" , align = 'c' )
        self._pdf.image("shirtificate.png" , w = self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x = 42 , y = 140, txt="%s took CS50"%name)

    def save(self, name):
        self._pdf.output(name)


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()