
from datetime import datetime


def MSHparser(line, output):
    MSH = line.split('|')
    output.write(f'HL7 Version: {MSH[-2]} \r\n')


def PIDparser(line, output):
    PID = line.split('|')
    pt_name = PID[5].replace('^', ' ')
    pt_dob = datetime.strptime(PID[7], '%Y%m%d').strftime('%d %b %Y')
    pt_gender = PID[8]
    pt_address = PID[11].replace('^', ' ')
    output.write(f'Patient Name: {pt_name} \r\n')
    output.write(f'DOB: {pt_dob} \r\n')
    output.write(f'Address: {pt_address} \r\n')


def PV1parser(line, output):
    PV1 = line.split('|')
    location_list = PV1[3].split('^')
    physician_list = PV1[8].split('^')
    exam_location = location_list[3]
    ref_physician = physician_list[2] + ' ' + physician_list[1]
    output.write(f'Exam Location: {exam_location} \r\n')
    output.write(f'Referring Physician: {ref_physician} \r\n')


def ORCparser(line, output):
    ORC = line.split('|')
    exam_date = datetime.strptime(ORC[7][0:8], '%Y%m%d').strftime('%d %b %Y')
    output.write(f'Exam Date: {exam_date} \r\n')


def OBRparser(line, output):
    OBR = line.split('|')
    accession = OBR[2]
    procedure_info = OBR[4].split('^')
    procedure_code = procedure_info[0]
    procedure_desc = procedure_info[1]
    reading_rad = OBR[-6].split('^')
    output.write(f'Reading Radiologist: {reading_rad[2]} {reading_rad[1]} \r\n')
    output.write(f'Procedure code: {procedure_code}  Procedure Description: {procedure_desc} \r\n')


def OBX1parser(line, output):
    OBX1 = line.split('|')
    report_body = OBX1[5].replace('\\.br\\', ' ')
    output.write(f'Report: {report_body}')
