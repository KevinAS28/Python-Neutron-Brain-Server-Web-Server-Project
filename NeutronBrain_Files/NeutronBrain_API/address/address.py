import os

def splitdir(addr):
    real = addr
    result = []
    addr = os.path.split(addr)
    while (addr[1]!=""):
        result.append(addr[1])
        addr = os.path.split(addr[0])
    return result[::-1]

if __name__ == "__main__":
    print(splitdir("/media/root/windows10"))