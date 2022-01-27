name = 'German'
age = 25
height = 183
job = 'engineer-programmer'
hobby = 'Fishing'
sport_activity = 'Swimming'

person = [name, age, height, job, hobby, sport_activity]

result = age + height
result = age ** height
result = age % height
result = age * height
result = age / height

new_person = person[1:4]

employee = name + ' ' + job
print(employee)

just_dict = {'name': name, "age": age}
just_dict['name'] = 'Denis'
age = just_dict['age']
