my_list = [1, 2, 3, 4, 6]

def multiply_list_map(my_list=[], number=0):
    #new_list = my_list.copy()
    new_list = list(map(lambda x: x * number, my_list.copy()))
    print (new_list, my_list)
multiply_list_map(my_list, 3)