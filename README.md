# assembler

a utility to create binary from asm.

- One instruction or label per line.
- Blank lines are ignored.
- Comments start with a "*" as the first character and all subsequent characters on the line are ignored.
- Spaces and  commas delimit instruction elements.
- All immediate values are to be specified using '#' character, optionally format can also be specified. Valid formats are binary(b), hex(h), decimal(d). By default decimal is assumed.
<!-- 
- A label ends with a colon and must be a single symbol on its own line.
- A label is immediately followed by a instruction 
- A label can be any single continuous sequence of printable characters; a colon or space terminates the symbol. -->

<!-- - Address of 1st line taken to be 0. --can improve ORG  -->
<!-- 
Features:
- ORG Directive
- Labels
   -->
```bash
    python3 asm.py -h       
```
gives:

```
usage: assembler [-h] [-o O] inputfile

create binary from asm

positional arguments:
  inputfile   input file path

optional arguments:
  -h, --help  show this help message and exit
  -o O        output file name,defaults to a.txt

primarily made to be used for vhdl projects
```
an example,

```
python3 asm.py sample.txt -o out.txt
```
creates out.txt in the same directory.

```bash

Language definition:

LOAD D A   - load from address A to destination D
LOADA D A  - load using the address register from address A + RE to destination D
STORE S A  - store value in S to address A
STOREA S A - store using the address register the value in S to address A + RE
BRA L      - branch to label A
BRAZ L     - branch to label A if the CR zero flag is set
BRAN L     - branch to label L if the CR negative flag is set
BRAO L     - branch to label L if the CR overflow flag is set
BRAC L     - branch to label L if the CR carry flag is set

ADD RC RA RB  - execute RC <= RA + RB
ADC RC RA RB  - execute RC <= RA + RB if carry
ADZ RC RA RB  - execute RC <= RA + RB if Zero
ADL RC RA RB  - execute RC <= RA + RB(shift left by 1) 

ADI RC RA I6  - execute RC <= RA + I6(sign extended)

NDU RC RA RB  - execute RC <= RA nand RB bitwise
NDC RC RA RB  - execute RC <= RA nand RB bitwise if carry
NDZ RC RA RB  - execute RC <= RA nand RB bitwise if Zero

LHI RA I9     - execute RA <= I9(shift left by 7)

LW  RA RB I6  - execute RA <= M[RB+I6]
SW  RA RB I6  - execute M[RB+I6] <= RA
LM  RA I9     - see below
SM  RA I9     - see below

BEQ RA RB I6  - branch to PC+I6 if RA == RB
JAL RA I9     - RA <= PC+1, branch to PC+I9
JLR RA RB     - RA <= PC+1,branch to addr in RB
JRI RA I9     - branch to RA+I6
```

```
LM/SM:
Load(Store) multiple registers whose address is given in the immediate field (one bit per register, R0 to R7) in order from right to left, i.e, registers from R0 to R7 if corresponding bit is set. Memory address is given in reg A. Registers are loaded from (are stored to) consecutiveaddresses.
```

> **Note** assember can detect many syntax errors but they aren't guaranteed to be exhaustive.

