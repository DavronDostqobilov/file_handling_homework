def main(data):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    # Read data from file
    list1=[]
    x=data.split(',')
    for i in x:
        list1.append(int(i))
    return list1
f=open('txt_file/data01.txt')
a=f.read()
print(main(a))
