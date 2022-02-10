# Lesson_8_task_2_Var_2_Nazarenko_Dmytro

from random import randrange 
list_1 = set([randrange(3, 100, 3) for _ in range (30)])
list_2 = set([randrange(5, 100, 5) for _ in range (20)])

print (list_1 & list_2)
