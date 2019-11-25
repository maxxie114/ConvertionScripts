def search(num, lst, count = 0):
    if num == lst[int((len(lst)-1)/2)]:
        print("count: ", count)
        return True
    elif len(lst) == 1:
        print("count: ", count)
        return False
    elif num < lst[int((len(lst)-1)/2)]:
        return search(num, lst[0:int((len(lst)-1)/2)],count+1)
    else:
        return search(num, lst[int((len(lst)-1)/2)+1:len(lst)],count+1)

lst = [i for i in range(1000000)]
for i in range(15):
    a = input("number to search:")
    print(search(int(a),lst))
