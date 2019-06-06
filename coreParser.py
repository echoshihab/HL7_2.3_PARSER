
from datetime import datetime

with open('lorem.txt', 'rt') as myfile:
    for line in myfile:
        if line.startswith('MSH'):
            MSH = line.split('|')
            print(f'HL7 Version: {MSH[-2]}')
        if line.startswith('PID'):
            PID = line.split('|')
            pt_name = PID[5].replace('^', ' ')
            pt_dob = datetime.strptime(PID[7], '%Y%m%d').strftime('%d %b %Y')
            pt_gender = PID[8]
            pt_address = PID[11].replace('^', ' ')
            print(f'Patient Name: {pt_name}')
            print(f'DOB: {pt_dob}')
            print(f'Address: {pt_address}')
        if line.startswith('PV1'):
            PV1 = line.split('|')
            location_list = PV1[3].split('^')
            physician_list = PV1[8].split('^')
            exam_location = location_list[3]
            ref_physician = physician_list[2] + ' ' + physician_list[1]
            print(f'Exam Location: {exam_location}')
            print(f'Referring Physician: {ref_physician}')
        if line.startswith('ORC'):
            ORC = line.split('|')
            exam_date = datetime.strptime(
                ORC[7][0:8], '%Y%m%d').strftime('%d %b %Y')
            print(f'Exam Date: {exam_date}')
        if line.startswith('OBR'):
            OBR = line.split('|')
            accession = OBR[2]
            procedure_info = OBR[4].split('^')
            procedure_code = procedure_info[0]
            procedure_desc = procedure_info[1]
            reading_rad = OBR[-6].split('^')
            print(f'Reading Radiologist: {reading_rad[2]} {reading_rad[1]}')
            print(f'Procedure code: {procedure_code}  Procedure Description: {procedure_desc}')
        if line.startswith('OBX|1'):
            OBX1 = line.split('|')
            report_body = OBX1[5].replace('\\.br\\', ' ')
            print(f'Report: {report_body}')

   # new_line = myline.replace("/", "").replace("*", "")
        #print(new_line, end="")
