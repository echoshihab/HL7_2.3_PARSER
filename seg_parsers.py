
from datetime import datetime


def MSHparser(line, output):
    MSH = line.split('|')
    output.cell(30, 3.5, txt=f'HL7 Version: {MSH[-2]}', ln=1, align="L")


def PIDparser(line, output):
    PID = line.split('|')
    pt_name = PID[5].replace('^', ' ')
    pt_dob = datetime.strptime(PID[7], '%Y%m%d').strftime('%d %b %Y')
    pt_gender = PID[8]
    pt_address = PID[11].replace('^', ' ')
    output.cell(30, 3.5, txt=f'DOB: {pt_dob}', ln=1, align="L")
    output.cell(30, 3.5, txt=f'Patient Name: {pt_name}', ln=1, align="L")
    output.cell(30, 3.5, txt=f'Address: {pt_address}', ln=1, align="L")


def PV1parser(line, output):
    PV1 = line.split('|')
    location_list = PV1[3].split('^')
    physician_list = PV1[8].split('^')
    exam_location = location_list[3]
    ref_physician = physician_list[2] + ' ' + physician_list[1]
    output.cell(30, 3.5, txt=f'Exam Location: {exam_location}', ln=1, align="L")
    output.cell(30, 3.5, txt=f'Referring Physician: {ref_physician}', ln=1, align="L")


def ORCparser(line, output):
    ORC = line.split('|')
    exam_date = datetime.strptime(ORC[7][0:8], '%Y%m%d').strftime('%d %b %Y')
    output.cell(30, 3.5, txt=f'Exam Date: {exam_date}', ln=1, align="L")


def OBRparser(line, output):
    OBR = line.split('|')
    accession = OBR[2]
    procedure_info = OBR[4].split('^')
    procedure_code = procedure_info[0]
    procedure_desc = procedure_info[1]
    reading_rad = OBR[-6].split('^')
    output.cell(30, 3.5, txt=f'Reading Radiologist: {reading_rad[2]} {reading_rad[1]}', ln=1, align="L")
    output.cell(30, 3.5, txt=f'Procedure code: {procedure_code}  Procedure Description: {procedure_desc}', ln=1, align="L")
    output.ln(h='4')


def OBX1parser(line, output):
    OBX1 = line.split('|')
    report_body = OBX1[5].replace('\\.br\\', ' ')
    output.write(3.5, txt=f'Report: {report_body} ')
