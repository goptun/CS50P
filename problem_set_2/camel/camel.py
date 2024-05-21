camel_case_variable = input("camelCase: ")

snake_case_variable = ""

for c in camel_case_variable:
    if c.isupper():
        snake_case_variable += "_" + c.lower()
    else:
        snake_case_variable += c

print("snake_case:", snake_case_variable)
