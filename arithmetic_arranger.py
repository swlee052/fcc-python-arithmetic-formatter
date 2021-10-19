def arithmetic_arranger(problems, getAnswer = False):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  firLine = ""
  secLine = ""
  thirLine = ""
  fourLine = ""
  
  for p in problems:
    probSplit = p.split()
    numA = probSplit[0]
    op = probSplit[1]
    numB = probSplit[2]
    width = max(len(numA), len(numB)) + 2

    if not numA.isnumeric() or not numB.isnumeric():
      return "Error: Numbers must only contain digits."
    if op != "+" and op != "-":
      return "Error: Operator must be '+' or '-'."
    if len(numA) > 4 or len(numB) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    firLine += numA.rjust(width, " ") + " "*4
    secLine += op + " "*(width-1-len(numB)) + numB + " "*4
    thirLine += "-"*width + " "*4

    if getAnswer:
      if op == "+":
        fourLine += str(int(numA) + int(numB)).rjust(width, " ") + " "*4
        
      else:
        fourLine += str(int(numA) - int(numB)).rjust(width, " ") + " "*4

  arranged_problems = firLine.rstrip() + "\n" + secLine.rstrip() + "\n" + thirLine.rstrip()
  if getAnswer:
    arranged_problems += "\n" + fourLine.rstrip()
  return arranged_problems