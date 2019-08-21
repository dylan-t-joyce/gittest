def add_greetings(names):
  list_of_names = []
  for name in names:
    list_of_names.append("Hello, %s" % name)
  return list_of_names

print(add_greetings(["Owen", "Max", "Sophie"]))
    

#python test2.py