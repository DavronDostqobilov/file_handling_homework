def main(data):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1=data.split()
    k=len(list1[0])
    for i in list1:
        if k<len(i):
            k=len(i)
    return k
f=open('txt_file/data06.txt')
a=f.read()
print(main(a))

