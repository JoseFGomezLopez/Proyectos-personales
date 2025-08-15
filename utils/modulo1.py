def addition (*args): 
    total = 0
    for value in args:
        if(type(value) == int):
         total += value   
    return total