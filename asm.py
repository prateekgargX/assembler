import re
import time
start_time = time.time()

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
            opcode_s = opcode.get(asm_split[0]) 

            if opcode_s == None : #-----check for validity------#
                print ("SyntaxError: ""line-"+str(i)+" \""+asm_split[0]+"\": Not a valid instruction")
                quit()

            instr = opcode_s
            
            if(opcode_s == "0001" or opcode_s == "0010"): 
                # R-type Instruction
                # print(asm_split[1][0],asm_split[2][0],asm_split[3][0])
                #-----Syntax Error and check for validity for regNum------#
                # if(asm_split[1][0] == "R" and asm_split[2][0] == "R" and asm_split[3][0] == "R") :  raise Exception(str(i)+" :A custom message as to why you raised this.")
                try:
                    C = int(asm_split[1][1:])
                    A = int(asm_split[2][1:])
                    B = int(asm_split[3][1:])
                    if not(C<NumReg and B<NumReg and A<NumReg) :raise ValueError
                    RC = f'{C:03b}' 
                    RA = f'{A:03b}'
                    RB = f'{B:03b}'
                except ValueError:
                    print("line-"+str(i)+" :0-7 are only valid registers")
                    quit()

                CZ = "00"
                if asm_split[0] == "ADD" or asm_split[0] == "NDU" : CZ = "00"
                if asm_split[0] == "ADC" or asm_split[0] == "NDC" : CZ = "10"
                if asm_split[0] == "ADZ" or asm_split[0] == "NDZ" : CZ = "01"
                if asm_split[0] == "ADL" : CZ = "11"
                instr+=RA+RB+RC+'0'+CZ

            elif opcode_s == "0000" or opcode_s == "0111" or opcode_s == "0101" or opcode_s == "1000" or opcode_s == "1010" :
                # I-type Instruction
                
                try: #-----Syntax Error and check for validity for regNum------#
                    A = int(asm_split[1][1:])
                    B = int(asm_split[2][1:])
                    if not(B<NumReg and A<NumReg) :raise ValueError
                    RA   = f'{A:03b}'
                    RB   = f'{B:03b}'
                except ValueError:
                    print("line-"+str(i)+" :0-7 are only valid registers")
                    quit()

                if opcode_s == "0000": RA,RB = RB,RA
                if opcode_s != "1010":
                    try: 
                        imm = int(asm_split[3][1:])
                        if not(imm<pow(2,6)) :raise ValueError
                        IMM6 = f'{imm:09b}'#-----Value Error and formatting error----
                    except ValueError:
                        print("line-"+str(i)+" :0-7 are only valid registers")
                        quit()

                    IMM6 = f'{imm:06b}'#-----Value Error and formatting error----
                else : IMM6 = f'{0:06b}'
                instr+=RA+RB+IMM6

            else:
                # J-type Instruction

                try: #-----Syntax Error --------
                    A = int(asm_split[1][1:])
                    if not(B<NumReg and A<NumReg) :raise ValueError
                    RA   = f'{A:03b}'
                except ValueError:
                    print("line-"+str(i)+" :0-7 are only valid registers")
                    quit()

                try: 
                    imm = int(asm_split[2][1:])
                    if not(imm<pow(2,9)) :raise ValueError
                    IMM9 = f'{imm:09b}'#-----Value Error and formatting error----
                except ValueError:
                    print("line-"+str(i)+" :0-7 are only valid registers")
                    quit()
                
                instr+=RA+IMM9

            out.write(instr+'\n')
            j+=1
    
        i+=1

print("Execution finished in {:.4f} seconds".format(time.time()-start_time))
print("Total instructions : {}".format(j-1))


# R match, # match
# argparse
# function to handle different types of stuff b,d,h