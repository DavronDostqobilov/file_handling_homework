def main(data):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1=[]
    for i in range(len(data)):
        if not data[i].isdigit():
            list1.append(data[i])
    return list1
f=open('txt_file/data04.txt')
a=f.read()
print(main(a))    
# Read data from file