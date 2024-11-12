import re

def instruction_to_hex(instruction):
    part = instruction.split()
    
    op1_int = int(part[1])
    op1_bin = bin(op1_int)[2:]
    p_op1_bin = op1_bin.zfill(14)

    op2_int = int(part[2])
    op2_bin = bin(op2_int)[2:]
    p_op2_bin = op2_bin.zfill(14)

    wordlen = len(part[0])
    last = part[0][wordlen-1]

    retHex = ""

    if(last == "i"):
        newWord = part[0][:-1]
        if(newWord == "ADD"): retHex = "0001"
        elif (newWord == "NAND"): retHex = "0011"
        elif (newWord == "SRL"): retHex = "0101"
        elif (newWord == "LT"): retHex = "0111"
        elif (newWord == "CP"): retHex = "1001"
        elif (newWord == "CPI"): retHex = "1011"
        elif (newWord == "BZJ"): retHex = "1101"
        elif (newWord == "MUL"): retHex = "1111"
            
    else:
        if(part[0] == "ADD"): retHex = "0000"
        elif (part[0] == "NAND"): retHex = "0010"
        elif (part[0] == "SRL"): retHex = "0100"
        elif (part[0] == "LT"): retHex = "0110"
        elif (part[0] == "CP"): retHex = "1000"
        elif (part[0] == "CPI"): retHex = "1010"
        elif (part[0] == "BZJ"): retHex = "1100"
        elif (part[0] == "MUL"): retHex = "1110"

    retHex += p_op1_bin + p_op2_bin

 
    d_retHex = int(retHex, 2)
    h_retHex = hex(d_retHex).upper()[2:]
    str_retHex = str(h_retHex)
    pstr_retHex = str_retHex.zfill(8)

    return pstr_retHex


def hex_to_instruction(hex_string):
    integer_value = int(hex_string, 16)
    binary_length = len(hex_string)*4
    binary_string = bin(integer_value)[2:]
    p_binary_string = binary_string.zfill(binary_length)
    opcode = int(p_binary_string[:3], 2)
    imm = p_binary_string[3]
    rsA = int(p_binary_string[4:18], 2)
    rsB = int(p_binary_string[18:], 2)
    inst_text = ""
    if(opcode == 0): inst_text = "ADD"
    elif (opcode == 1): inst_text = "NAND"
    elif (opcode == 2): inst_text = "SRL"
    elif (opcode == 3): inst_text = "LT"
    elif (opcode == 4): inst_text = "CP"
    elif (opcode == 5): inst_text = "CPI"
    elif (opcode == 6): inst_text = "BZJ"
    elif (opcode == 7): inst_text = "MUL"

    if imm == "1": inst_text += "i " 
    else: inst_text += " "

    inst_text += str(rsA)+" "+str(rsB)
    
    return inst_text


def instruction_list_to_memory():
    memoryLocCounter = 0
    with open("memory.txt", "r") as file:
        prevLocMode = 0
        prevLoc = 0
        spaced = False
        for line in file:
            memoryLoc = 0

            if(len(line) <= 1):
                continue

            if(line[0].isdigit()):
                if(prevLocMode != 0):
                    if(spaced == False):
                        spaced = True
                        print("")
                    prevLocMode = 0
                memoryLoc = line.split(":", 1)[0].strip()
                if ((abs(int(memoryLoc) - prevLoc) > 1) and (spaced == False)):
                    print("")
                instruction = line.split(" ", 1)[1] if " " in line else line.strip()
                if(instruction[-1] == "\n"):
                    instruction = instruction[:-1]
                spaced = False
            elif(line[0] != ""):
                if(prevLocMode != 1):
                    if(spaced == False):
                        spaced = True
                        print("")
                    
                    prevLocMode = 1
                instruction = line[:-1]
                memoryLoc = memoryLocCounter
                if ((abs(int(memoryLoc) - prevLoc) > 1) and (spaced == False)):
                    print("")
                spaced = False
                memoryLocCounter += 1
            prevLoc = int(memoryLoc)
            hexInstr = instruction_to_hex(instruction)
            memoryFormat = "mem["+str(memoryLoc)+"] = 32'h"+hexInstr+";"
            print(memoryFormat)

def memory_to_instruction_list():
    memoryLoc = 0
    prevLoc = 0
    with open("memory.txt", "r") as file:
        for line in file:
            if(line[0] != "m" or 'h' not in line):
                continue

            processed_line = line.split('h', 1)[1] if 'h' in line else line.strip()
            processed_line = processed_line[:-2]

            match = re.search(r'\[(\d+)\]', line)
            
            if match:
                if (int(memoryLoc) > 0):
                    memoryLoc = match.group(1)
                    if (abs(int(memoryLoc) - prevLoc) > 1):
                        print("")
                else:
                    memoryLoc = match.group(1)
            else:
                continue

            print(memoryLoc, end=": ")
            finalInst = hex_to_instruction(processed_line)
            print(finalInst)
            prevLoc = int(memoryLoc)

def main():
    print("")
    while(1):
        print("(1) Hex to instruction")
        print("(2) Instruction to hex")
        print("(3) Instruction list to memory format")
        print("(4) Memory format to instruction list")
        print("(x) Exit")
        mod = input("Select mode: ")
        if(mod == "1"):
            print("")
            while(1):
                hex = input("Enter hex: ")
                if(hex == "x"):
                    print("")
                    break
                instr = hex_to_instruction(hex)
                print(instr)
                print("")

        elif(mod == "2"):
            print("")
            while(1):
                instr = input("Enter instruction: ")
                if(instr == "x"):
                    print("")
                    break
                hex = instruction_to_hex(instr)
                print(hex)
                print("")
        elif(mod == "3"):
            instruction_list_to_memory()
            print("")
        elif(mod=="4"):
            print("")
            memory_to_instruction_list()
            print("")
        else:
            exit()



if __name__ == '__main__':
    main()
