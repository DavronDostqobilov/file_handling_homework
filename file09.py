def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    mx=9
    for i in range(len(data)):
        if data[i].isdigit():
            if mx>=int(data[i]):
                mx=int(data[i])
    return mx
f=open('txt_file/data09.txt')
a=f.read()
print(main(a))
# Read data from file