def Get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * Get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result=Get_multiplied_digits(40203)
print(result)