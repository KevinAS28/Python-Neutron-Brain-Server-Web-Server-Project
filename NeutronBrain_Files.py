import os, imp
thefiles = "NeutronBrain_Files"
def Load_Module(module="", dari="NeutronBrain_API", asname=""):
        try:
            import_from = os.listdir (thefiles)
            the_module = os.path.join(thefiles, import_from[import_from.index(dari)], module)
            module = imp.load_source(module+".py", os.path.join(os.getcwd(), the_module, module+".py"))
            module.parent_dir = os.getcwd()
            module.NeutronBrain_Files = imp.load_source("NeutronBrain_Files.py", os.path.join(os.getcwd(), "NeutronBrain_Files.py"))
            return module                    
        except Exception as err:
            print("[-ERROR-] Cannot load", module, "\n", str(err))

def Get_Address_In_Other_Files(folder="", file=""):
        file = os.path.join(thefiles, "Other_Files", folder, file)
        if (os.access(file, os.R_OK)):
            return os.path.join(os.getcwd(), file)
        return False

def Module_Lister(folder=""):
            return os.listdir(os.path.join(os.getcwd(), thefiles, folder))

def Other_Files_Reader(file=""):
            addr = os.path.join(thefiles, "Other_Files", file)
            with open(addr, "rb") as baca:
                return baca.read()

def Other_Files_Lister(folder=""):
        addr = os.path.join(thefiles, "Other_Files", folder)
        result = os.listdir(addr)
        for i in range(len(result)):
            result[i] = os.path.join(thefiles, "Other_Files", folder, result[i])
