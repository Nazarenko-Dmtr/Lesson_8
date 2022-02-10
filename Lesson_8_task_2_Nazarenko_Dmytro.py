# Lesson_8_task_2_Nazarenko_Dmytro

list_1 = []
list_2 = []
for i in range (3, 100, 3):
    list_1.append(i)
for j in range (5, 100, 5):
    list_2.append(j)
print (set(list_1) & set(list_2))