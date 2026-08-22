from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap
import os

CV_TEXT = '''Itay Matya
Mechanical Engineering Student
Phone: +972503401023
Email: itaymatya@gmail.com
Address: Shabazi 12, Rosh Haayin
Linkedin Github My Website
CONTACT
PROFESSIONAL
EXPERIENCE
EDUCATION
CERTIFICATES
B.sc. Mechanical Engineer Student | 2024-2028
SolidWorks Associate (CSWA) – Dassault Systèmes
SUMMARY
Second-year Mechanical Engineering student at Tel Aviv University with strong skills in
SolidWorks, problem-solving, and analytical thinking. Quick learner and team player with
high work ethic and hands-on experience in mechanical systems, field operations, and
construction.
Tel Aviv University, expected graduation date october 2028.
GPA: 84
graphical engineering grade: 99 (CAD)
Begin High school graduate | 2017
Full Matriculation Certificate
5 units in Mathematics, English, Chemistry, Physics
LANGUAGES Hebrew – native tongue.
English – high level both verbally and in writing.
MILITARY
RECORD
IDF / INFANTRY | Mar 2018 - Nov 2020
Field engineering – sapper, honorable discharged
Served on the front lines as a combat sapper and modified tank operator
Operated high-caliber weapon systems and demolition tools
assigned several roles which included management of manpower and as squad leader
Participated in active combat during the October 7 reserve call-up
Belko LED | 2017
worked in a manufacturing line for aluminum light fixtures, work included aluminum processing,
soldering electronic parts and electronic controls.
Construction Assistant | Dec 2020 - May 2021
Built light construction projects including pergolas, wooden decks, and garden structures as part
of a government-supported reintegration program
Metro Motor | Oct 2021 - Mar 2022
Managed inventory of mechanical parts and automotive components using SAP Warehouse
Management System (WMS)
Processed and tracked orders, coordinated with vendors, and ensured timely shipment and
restocking
Control Room Operator | Feb 2023 - Mar 2024
Monitored and managed operations across multiple parking lots using centralized control systems
Coordinated with on-site staff to ensure smooth vehicle flow, safe, efficient space utilization
Maintained logs and incident reports to support operational analysis and improvements
TECHNICAL
SKILLS
SolidWorks, python(basic) , MS excel
'''

OUTPUT_PATH = os.path.join('assets', 'pdf')
OUTPUT_FILE = os.path.join(OUTPUT_PATH, 'Itay_Matya_CV.pdf')

def ensure_output_dir():
    os.makedirs(OUTPUT_PATH, exist_ok=True)

def create_pdf(text, out_path):
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    margin = 40
    max_width = width - 2 * margin
    font_name = 'Helvetica'
    font_size = 10
    leading = font_size * 1.2

    textobject = c.beginText()
    textobject.setTextOrigin(margin, height - margin)
    textobject.setFont(font_name, font_size)

    for paragraph in text.split('\n'):
        if paragraph.strip() == '':
            textobject.moveCursor(0, -leading)
            continue
        wrapped = textwrap.wrap(paragraph, width=95)
        for line in wrapped:
            if textobject.getY() < margin + leading:
                c.drawText(textobject)
                c.showPage()
                textobject = c.beginText()
                textobject.setTextOrigin(margin, height - margin)
                textobject.setFont(font_name, font_size)
            textobject.textLine(line)

    c.drawText(textobject)
    c.save()

if __name__ == '__main__':
    ensure_output_dir()
    create_pdf(CV_TEXT, OUTPUT_FILE)
    print(f'Wrote PDF to {OUTPUT_FILE}')
