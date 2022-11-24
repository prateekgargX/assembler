import re
import os.path
import sys

filename = "my_program.txt"

opcode = {
"ADD" : "0001","ADC" : "0001",
"ADZ" : "0001","ADL" : "0001",
"ADI" : "0000","NDU" : "0010",
"NDC" : "0010","NDZ" : "0010",
"LHI" : "0011",
"LW"  : "0111","SW"  : "0101",
"LM"  : "1100","SM"  : "1101",
"BEQ" : "1000","JAL" : "1001",
"JLR" : "1010","JRI" : "1011"
}

NumReg = 8
logNumReg = 3

with open(filename) as file: lines = file.readlines()

i = 1 # to keep track of current line being processed  
for line in lines:
    line = line.rstrip().strip()
    if(len(line)!=0 and line[0] != '*'): # ignoring blank lines and comments
        asm_split = re.split('[\\s,]+',line.upper()) # making case insensitive
        print(i,":")
        opcode_s = opcode[asm_split[0]] #-----check for validity------#
        if(opcode_s == "0001" or opcode_s == "0010"): 
            # R-type Instruction
            RC = f'{int(asm_split[1][1:]):03b}' #-----Syntax Error and check for validity for regNum------#
            RA = f'{int(asm_split[2][1:]):03b}'
            RB = f'{int(asm_split[3][1:]):03b}'
            print(opcode_s,RC,RA,RB)

        elif opcode_s == "0000" or opcode_s == "0111" or opcode_s == "0101" or opcode_s == "1000" or opcode_s == "1010" :
            # I-type Instruction
            RA   = f'{int(asm_split[1][1:]):03b}'#-----Syntax Error and check for validity for regNum------#
            RB   = f'{int(asm_split[2][1:]):03b}'

            if opcode_s == "0000": RA,RB = RB,RA
            if opcode_s != "1010":
                IMM6 = f'{int(asm_split[3][1:]):06b}'#-----Value Error and formatting error----
            else : IMM6 = f'{0:06b}'
            print(opcode_s,RA,RB,IMM6)

        else:
            # J-type Instruction
            RA   = f'{int(asm_split[1][1:]):03b}'#-----Syntax Error and check for validity for regNum------#
            IMM9 = f'{int(asm_split[2][1:]):09b}'#-----Value Error and formatting error----
            print(opcode_s,RA,IMM9)

        print(asm_split)

    i+=1