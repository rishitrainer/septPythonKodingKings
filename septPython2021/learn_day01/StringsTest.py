message = "Hello World"
statement = "this is awesome statement"
long_sapce = "   Hello     "
age = "21"
print(message[0])
print(message[5])
print(message[0:5]) # start:end inclusive:exclusive
print(message[-5:])
print(message[2:])
print(message[:6])
# reverse a String in single statement
print(message.upper())
print(message.lower())
print(statement.capitalize())
print(statement.title())
print(message.isdigit())
print(age.isnumeric())
print(message.isalpha())
print(long_sapce)
print(long_sapce.strip())

print(statement.count("s"))
print(statement.find("s",0,len(statement)))
print(statement.index("s",0,len(statement)))

stat = "Good Job {} and {}"
print(stat.replace("Job", "Task"))
print(stat.format("JeeNA", "Sowmya"))