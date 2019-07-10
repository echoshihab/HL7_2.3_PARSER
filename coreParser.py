
from seg_parsers import MSHparser, PIDparser, PV1parser, ORCparser, OBRparser, OBX1parser

textFile = open("parsedFile.txt", "wt")

with open('lorem.txt', 'rt') as myfile:
    for line in myfile:
        if line.startswith('MSH'):
            MSHparser(line, textFile)
        if line.startswith('PID'):
            PIDparser(line, textFile)
        if line.startswith('PV1'):
            PV1parser(line, textFile)
        if line.startswith('ORC'):
            ORCparser(line, textFile)
        if line.startswith('OBR'):
            OBRparser(line, textFile)
        if line.startswith('OBX|1'):
            OBX1parser(line, textFile)

       # new_line = myline.replace("/", "").replace("*", "")
            # print(new_line, end="")
