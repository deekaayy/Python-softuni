data_list = input()

special_elements = [",", ";", ":", ".", "!", "(", ")", "\"", "\'", "\\", "/", "[", "]", " "] #damn

for el in special_elements:
    data_list = data_list.replace(el,' ')
data_list=data_list.split()
lower_case = []
upper_case = []
mixed_case = []

for char in data_list:
    if char.islower():
        if char.isalpha():
            lower_case.append(char)
        else:
            mixed_case.append(char)
    elif char.isupper():
        if char.isalpha():
            upper_case.append(char)
        else:
            mixed_case.append(char)
    else:
        mixed_case.append(char)

print(f"Lower-case: {', '.join(lower_case)}")
print(f"Mixed-case: {', '.join(mixed_case)}")
print(f"Upper-case: {', '.join(upper_case)}")