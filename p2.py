
#slicing method

# str="college"
# reversed = str[::-1]

# print(reversed)


alphabat="Data Science Data Science"
char_to_check="a"
lines= alphabat.splitlines()
line_count=0

for line in lines:
    if char_to_check in line:
        line_count +=1
        print(f"the char '{char_to_check}' appears in {line_count} line(s).")