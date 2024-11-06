# Macro Name Table (MNT)
MNT = {}

# Macro Definition Table (MDT)
MDT = []

# Intermediate Code
intermediate_code = []

def pass1(input_code):
    global MNT, MDT, intermediate_code
    in_macro = False
    macro_name = None
    mdt_index = 0

    for line in input_code:
        words = line.strip().split()
    
        if words[0] == 'MACRO':
            in_macro = True
            continue

        elif in_macro:
            # Process Macro Header
            macro_name = words[0]
            MNT[macro_name] = mdt_index
            MDT.append(line)
            mdt_index += 1
            in_macro = False

        elif words[0] in MNT:
            # Intermediate code for macro invocation
            intermediate_code.append(f'MACRO_CALL {words[0]}')

        elif macro_name:
            # Add the body of the macro to MDT
            MDT.append(line)
            mdt_index += 1

        elif words[0] == 'MEND':
            # End of macro
            MDT.append(line)
            macro_name = None

        else:
            # Add non-macro lines to intermediate code
            intermediate_code.append(line)

    print("\nMacro Name Table (MNT):")
    print_table(["Macro Name", "MDT Index"], [[name, idx] for name, idx in MNT.items()])

    print("\nMacro Definition Table (MDT):")
    print_table(["MDT Index", "Instruction"], [[i, MDT[i]] for i in range(len(MDT))])

    print("\nIntermediate Code:")
    print_table(["Line Number", "Code"], [[i, intermediate_code[i]] for i in range(len(intermediate_code))])

    return MNT, MDT, intermediate_code


def pass2(MNT, MDT, intermediate_code):
    output_code = []

    for line in intermediate_code:
        words = line.strip().split()

        if words[0] == 'MACRO_CALL' and words[1] in MNT:
            macro_name = words[1]
            mdt_index = MNT[macro_name]

            # Expand macro from MDT
            while MDT[mdt_index] != 'MEND':
                output_code.append(MDT[mdt_index])
                mdt_index += 1

        else:
            # Directly add intermediate code lines
            output_code.append(line)

    print("\nExpanded Code:")
    print_table(["Line Number", "Code"], [[i, output_code[i]] for i in range(len(output_code))])

    return output_code


def print_table(headers, rows):
    print(" | ".join(f"{header:<15}" for header in headers))
    print("-" * (len(headers) * 17))  # Divider

    # Print each row with spacing
    for row in rows:
        print(" | ".join(f"{str(item):<15}" for item in row))

# Macro Input
input_code = [
    "MACRO",
    "INCR &ARG1, &ARG2",
    "ADD &ARG1",
    "ADD &ARG2",
    "MEND",
    "START",
    "INCR A, B",
    "INCR C, D",
    "END"
]

# Pass 1
MNT, MDT, intermediate_code = pass1(input_code)

# Pass 2
expanded_code = pass2(MNT, MDT, intermediate_code)
