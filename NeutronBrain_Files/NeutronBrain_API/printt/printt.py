Integrated_Function = []
def Add_Function(func):
 Integrated_Function.append(func)

def Warn(text="Something went wrong"):
    banner = "[-WARNING-]"
    text = "%s %s" %(banner, text)
    print(text)
    for i in Integrated_Function:
     i(text)
    return text
def Error(text="An error has been occurred."):
    banner = "[-ERROR-]"
    text = "%s %s" %(banner, text)
    print(text)
    
    for i in Integrated_Function:
     i(text)    
    return text
def Info(text):
    banner = "[-INFO-] "
    text = "%s %s" %(banner, text)
    print(text)
    for i in Integrated_Function:
     i(text)    
    return text
module_name = "printt"
