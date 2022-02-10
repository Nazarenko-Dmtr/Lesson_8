# Lesson_8_task_1_Nazarenko_Dmytro

line_1 = input("Print 1st line: ")
line_2 = input("Print 2nd line: ")

line_1 = set("".join(line_1.split()))
line_2 = set("".join(line_2.split()))

print (line_1 & line_2)
