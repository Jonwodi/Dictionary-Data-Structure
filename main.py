# Dict items are key value pairs enclosed in curly brackets
# Dict is ordered as of python 3.7
# Dict is mutable
# Dict keys are unique, cannot have duplicates
# Elements can be of different data types


'''
Dict Attributes
'''
# print(dir(dict))
# print(help(dict.pop))


'''
Creating Python Dictionary
'''
# dict = {}
# dict = {"Name": "Jordan", "Age": 23}
# dict["Age"] = 24
# dict = dict([("MJ", 23), ("Kobe", 24)])
# print(dict)
# print(type(dict))


'''
Access Dictionary Values
'''

# dict = {"Name": "Jordan", "Age": 23}
# print(dict["Name"])
# print(dict.get("Age"))
# print(dict.keys())
# print(dict.values())

# dict = [{"Name": "Jordan", "Age": 23},{"Name": "Steph", "Age": 30}]
# print(type(dict))
# print(dict)
# print(dict[0])
# print(dict[1])
# print(dict[1]["Name"])

# for n in range(len(dict)):
#   print(dict[n]["Name"])
# for n in range(len(dict)):
#   print(dict[n]["Age"])



'''
Changing Dictionary elements
'''

# dict = {"Name": "Jordan", "Age": 23}
# dict["Name"] = "Jay"
# dict["Age"] = 24
# print(type(dict))
# print(dict)
# print(id(dict))

# ==========================================

# dict = {"Name": "Jordan", "Age": 23}
# dict.update({"Name": "Steph", "Age": 30})
# dict["Age"] = 24
# print(type(dict))
# print(dict)
# print(id(dict))

# ==========================================

# dict = {"Name": "Jordan", "Age": 23}
# dict.setdefault("Name","Steph")
# dict.setdefault("Language","Python")
# dict["Age"] = 24
# print(type(dict))
# print(dict)
# print(id(dict))



'''
Remove Element From Dictionary
'''

# dict = {"Name": "Jordan", "Age": 23}
# dict.pop("Name")
# print(type(dict))
# print(dict)
# print(id(dict))

# =====================================

# dict = {"Name": "Jordan", "Age": 23}
# dict.popitem()
# print(type(dict))
# print(dict)
# print(id(dict))

# ==========================================

# dict = {"Name": "Jordan", "Age": 23}
# dict.clear()
# print(type(dict))
# print(dict)
# print(id(dict))

# =============================================

# dict = {"Name": "Jordan", "Age": 23}
# del dict
# print(type(dict))
# print(dict)
# print(id(dict))

'''
Dictionary Membership Test
'''
# dict = {"Name": "Jordan", "Age": 23}
# print("Name" in dict)
# print("Name" not in dict)
# print("Names" in dict)



