def main(data):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1=[]
    n=0
    m=0
    for i in range(len(data)):
        if data[i].isdigit():
            m+=1
        else:
            n+=1
    list1.append(m)
    list1.append(n)
    return list1
f=open('txt_file/data05.txt')
a=f.read()
print(main(a)) 
# Read data from file