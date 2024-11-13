(1) Hex to instruction
  Single convert from 32-bit hexadecimal number to VSCPU assembly code.
(2) Instruction to hex
  Single convert from VSCPU assembly code to 32-bit hexadecimal number.
(3) Instruction list to memory format
  Multiple conversion from VSCPU assembly code list to ready-to-paste memory format. Reads the assembly code from a text file named "memory.txt" in the same directory. Writes memory register array as "mem". (E.g -> mem[128] = 31'hD01B800D)
  If memory location is stated uses that memory locations. If there's no memory location it gives the locations on it's own, starting from 0.
(4) Memory format to instruction list
  Multiple conversion from memory format to VSCPU assembly code list. Each line should be in the form of "mem[{MEMORY_LOCATION}] = 32'h{HEX_NUMBER}". Reads the memory format from a text file named "memory.txt" in the same directory. Skips commented lines.
