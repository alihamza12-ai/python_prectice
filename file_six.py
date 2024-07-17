from typing import Union
st_per : Union[int,float] =int(input("enter student percentage"))
grade = ""

if st_per >= 0 and st_per < 33:
     grade="c"
elif st_per >= 33 and st_per < 43:
     grade="B"
elif st_per >= 43 and st_per < 69:
     grade="B+"
elif st_per >= 69 and st_per < 80:
     grade="A+" 
elif st_per >= 80:
     grade="A+"
else:
    grade="fail"
print(f"Dear student your percentage is {st_per} and your grade is {grade}")