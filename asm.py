import re
import os.path
import sys

filename = "my_program.txt"
outfile = "a.txt"

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

with open(outfile,'w') as out:
    i = 1 # to keep track of current line being processed
    j = 1 # to keep track of current instr being processed
    for line in lines:
        line = line.rstrip().strip()
        if(len(line)!=0 and line[0] != '*'): # ignoring blank lines and comments
            asm_split = re.split('[\\s,]+',line.upper()) # making case insensitive
            opcode_s = opcode[asm_split[0]] #-----check for validity------#
            instr = opcode_s
            if(opcode_s == "0001" or opcode_s == "0010"): 
                # R-type Instruction
                RC = f'{int(asm_split[1][1:]):03b}' #-----Syntax Error and check for validity for regNum------#
                RA = f'{int(asm_split[2][1:]):03b}'
                RB = f'{int(asm_split[3][1:]):03b}'
                if asm_split[0] == "ADD" and asm_split[0] == "NDU" : CZ = "00"
                if asm_split[0] == "ADC" and asm_split[0] == "NDC" : CZ = "10"
                if asm_split[0] == "ADZ" and asm_split[0] == "NDZ" : CZ = "01"
                if asm_split[0] == "ADL" : CZ = "11"
                instr+=RA+RB+RC+'0'+CZ

            elif opcode_s == "0000" or opcode_s == "0111" or opcode_s == "0101" or opcode_s == "1000" or opcode_s == "1010" :
                # I-type Instruction
                RA   = f'{int(asm_split[1][1:]):03b}'#-----Syntax Error and check for validity for regNum------#
                RB   = f'{int(asm_split[2][1:]):03b}'

                if opcode_s == "0000": RA,RB = RB,RA
                if opcode_s != "1010":
                    IMM6 = f'{int(asm_split[3][1:]):06b}'#-----Value Error and formatting error----
                else : IMM6 = f'{0:06b}'
                instr+=RA+RB+IMM6

            else:
                # J-type Instruction
                RA   = f'{int(asm_split[1][1:]):03b}'#-----Syntax Error and check for validity for regNum------#
                IMM9 = f'{int(asm_split[2][1:]):09b}'#-----Value Error and formatting error----
                instr+=RA+IMM9

            out.write(instr+'\n')
            j+=1
    
        i+=1