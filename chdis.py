import sys
import os


def decoder(num):
    second_digits = num[2] + num[3]

    """
    This dictionary includes codes that are always the same
    """
    const_codes = {
        "0000": "NOP",
        "ffff": "NOP",
        "00e0": "CLS",
        "00ee": "RET",
        "00fb": "SCRIGHT",
        "00fc": "SCLEFT",
        "00fd": "EXIT",
        "00fe": "LOW",
        "00ff": "HIGH"

    }

    if num in const_codes:
        return const_codes[num]

    elif num[0] == "0" and num not in const_codes:
        return f"SYS {num[1]}{second_digits}"

    elif num[0] == "1":
        return f"JMP {num[1]}{second_digits}"

    elif num[0] == "2":
        return f"CALL {num[1]}{second_digits}"

    elif num[0] == "3":
        return f"SE V{num[1]},{second_digits}"

    elif num[0] == "4":
        return f"SNE V{num[1]},{second_digits}"

    elif num[0] == "5":
        return f"SE V{num[1]},V{num[2]}"

    elif num[0] == "6":
        return f"LD V{num[1]},{second_digits}"

    elif num[0] == "7":
        return f"ADD V{num[1]},{second_digits}"

    elif num[0] == "8":
        if num[3] == "0":
            return f"LD V{num[1]},V{num[2]}"
        elif num[3] == "1":
            return f"OR V{num[1]},V{num[2]}"
        elif num[3] == "2":
            return f"AND V{num[1]},V{num[2]}"
        elif num[3] == "3":
            return f"XOR V{num[1]},V{num[2]}"
        elif num[3] == "4":
            return f"ADD V{num[1]},V{num[2]}"
        elif num[3] == "5":
            return f"SUB V{num[1]},V{num[2]}"
        elif num[3] == "6":
            return f"SHR V{num[1]}[,V{num[2]}]"
        elif num[3] == "7":
            return f"SUBN V{num[1]},V{num[2]}"
        elif num[3] == "e":
            return f"SHL V{num[1]}[,V{num[2]}]"

    elif num[0] == "9":
        return f"SNE V{num[1]},V{num[2]}"

    elif num[0] == "a":
        return f"LD I,{num[1]}{second_digits}"

    elif num[0] == "b":
        return f"JMP V0,{num[1]}{second_digits}"

    elif num[0] == "c":
        return f"RND V{num[1]},{second_digits}"

    elif num[0] == "d":
        if num[3] == "0":
            return f"DRW V{num[1]},V{num[2]},0"
        else:
            return f"DRW V{num[1]},V{num[2]},{num[3]}"

    elif num[0] == "e":
        if second_digits == "9e":
            return f"SKP V{num[1]}"
        elif second_digits == "a1":
            return f"SKNP V{num[1]}"

    elif num[0] == "f":
        if second_digits == "07":
            return f"LD V{num[1]},DT"
        elif second_digits == "0a":
            return f"LD V{num[1]},K"
        elif second_digits == "15":
            return f"LD DT,V{num[1]}"
        elif second_digits == "18":
            return f"LD ST,V{num[1]}"
        elif second_digits == "1e":
            return f"ADD I,V{num[1]}"
        elif second_digits == "29":
            return f"LD F,V{num[1]}"
        elif second_digits == "30":
            return f"LD HF,V{num[1]}"
        elif second_digits == "33":
            return f"LD B,V{num[1]}"
        elif second_digits == "55":
            return f"LD [I],V{num[1]}"
        elif second_digits == "65":
            return f"LD V{num[1]},[I]"
        elif second_digits == "75":
            return f"LD R,V{num[1]}"
        elif second_digits == "85":
            return f"LD V{num[1]},R"

    else:
        return f"ERROR: {num}"


class dissassembler:

    def __init__(self, filename, mode):
        if os.path.isfile(f"{filename}"):
            self.filename = filename
        else:
            print(f"Cant find File: {filename}")
            exit()

        modes = ["-hex", "-asm"]

        if mode in modes:
            self.mode = mode
        else:
            print(f"Invalid Argument: {mode}")
            exit()

    """
    Reads 2 Bytes from the File(A Chip 8 Instruction is 2 Bytes long)
    """

    def reader(self):
        with open(self.filename, "rb") as file:
            while True:

                char = file.read(2)
                if char:
                    yield char
                else:
                    file.close()
                    return

    """
    This function writes whatever the decoder-function returns into a .txt-file
    """

    def writer(self):

        code = self.reader()
        file_content = open(self.filename, "rb").read()

        if os.path.isfile(f"output-{self.filename}.txt"):
            os.remove(f"output-{self.filename}.txt")

        # Creates a Hex-Dump of the Input-File
        if self.mode == "-hex":
            for i in range(0, len(file_content)):

                try:
                    code_ = next(code).hex()

                    output_file = open(f"output-{os.path.basename(self.filename)}.txt", "a")
                    if code_ is not None:
                        output_file.write(f"{code_}\n")
                    output_file.close()

                except Exception as error:
                    print(error)
                    break

        # Creates Pseudo-Assembly of the Input-File
        else:

            for i in range(0, len(file_content)):

                try:
                    code_ = next(code).hex()
                    final_code = decoder(code_)
                    output_file = open(f"output-{os.path.basename(self.filename)}.txt", "a")
                    if final_code is not None:
                        output_file.write(f"{final_code}\n")
                    output_file.close()

                except Exception as error:
                    print(error)
                    break


if len(sys.argv) == 3:
    new_dis = dissassembler(sys.argv[1], sys.argv[2])
    print("Running...")
    new_dis.writer()
    print("Done.")
else:
    print("Error: No Arguments are given!")
    exit()

