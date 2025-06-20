def coder(listname, varname, count, subpoint=None):
    import pyperclip
    outFile = ""

    if subpoint == None:
        for curInd in range(0, count):
            outstr = listname + "[" + str(curInd) + "] := " + varname + str(curInd + 1) + ";\r"
            outFile = outFile + outstr

    else:
        for curInd in range(0, count):
            outstr = listname + "[" + str(curInd) + "] := " + varname + str(curInd + 1) + "." + subpoint + ";\r"
            outFile = outFile + outstr


    pyperclip.copy(outFile)
    print("Complete")

if __name__ == "__main__":
    print("ListName[0] := VariableName.Element")
    print("Enter List Name")
    listname = input(">>")
    print("Enter Variable Name")
    varname = input(">>")
    print("Enter Count")
    count = int(input(">>"))
    print("Would you like to use a structed point element? [y/n]")
    if input(">>") in ["y", "Y"]:
        print("Enter the element name")
        subpoint = input(">>")
    else:
        subpoint = None

    coder(listname, varname, count, subpoint)
