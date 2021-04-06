# Chip8-Disassembler-in-Python

## Description
Little Disassembler for Chip 8 Roms,written in Python.
Creates Chip8-Sourcecode of .ch8 files(Hex or Pseudo-Assembly).If you want to learn more about Chip8 click [here](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM).


## How-To:
This program was designed to run in a terminal.
 ```python 
 python chdis.py <YOUR-FILE> <MODE>
 ```
 ## Modes:
 + -hex  {Creates a Hex-Dump)
 + -asm  {Creates Pseudo-Assembly)

## Note:
+ Make sure your ROM is in the same direction as "chdis.py".
+ Your "source code" will be in a .txt file named as "output-**"YOUR-FILE"**.txt",and will be located in the same directory as "chdis.py".
+ An unknown opcode will be indicated with:  ERROR: "opcode" in your output-file


