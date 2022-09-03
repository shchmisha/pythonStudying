student_attendance = {"Bob": 95, "Rolf": 80, "Anne": 100}

# for student in student_attendance:
#     # a for loop on the dictionary returns the keys of the dictionary
#     print(f'{student}: {student_attendance[student]}')
#     # in order to get access to the values of the keys, get the value from the dict directly by accesing the value of the given key

# for student, attendance in student_attendance.items():
#     # a for loop on the dictionary returns the keys of the dictionary
#     print(f'{student}: {attendance}')

# attendance_values = student_attendance.values()
# for value in attendance_values:
#     print(value)

# if "Bob" in student_attendance:
#     print("bob is present")

friends = [
    {"name": "a", "age": 1},
    {"name": "b", "age": 2},
    {"name": "c", "age": 3}
]

for friend in friends:
    for key, value in friend.items():
        print(key, value)
    for i in friend:
        print(i)

    for value in friend.values():
        print(value)