def case_swap(str):
    new_case=[]
    for i in range(len(str)):
        if (str[i].isupper())==True:
            new_case.append(str[i].lower())
        elif (str[i].islower()==True):
            new_case.append(str[i].upper())
        else:
            new_case.append(str[i])    
        res_str=''
    return res_str.join(new_case)
  
str = input()
ans = case_swap(str)
print(ans)