from faker import Faker
fake = Faker()
student_data = []
for i in range(10):
    temp_list = []
    temp_list.append(fake.name())
    temp_list.append(fake.random_int(18, 33))
    temp_list.append(fake.email())
    student_data.append(temp_list) 

print(student_data)
