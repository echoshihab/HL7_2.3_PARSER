
from seg_parsers import MSHparser, PIDparser, PV1parser, ORCparser, OBRparser, OBX1parser
from fpdf import FPDF

report = FPDF()
report.add_page()
report.set_font("Arial", size=8)


with open('HL7sample.txt', 'rt') as myfile:
    for line in myfile:
        if line.startswith('MSH'):
            MSHparser(line, report)
        if line.startswith('PID'):
            PIDparser(line, report)
        if line.startswith('PV1'):
            PV1parser(line, report)
        if line.startswith('ORC'):
            ORCparser(line, report)
        if line.startswith('OBR'):
            OBRparser(line, report)
        if line.startswith('OBX|1'):
            OBX1parser(line, report)
    report.output("report.pdf")

    # new_line = myline.replace("/", "").replace("*", "")
    # print(new_line, end="")
