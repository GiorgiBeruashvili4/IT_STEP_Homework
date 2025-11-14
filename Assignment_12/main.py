# საშინაო დავალება 12


# 1

# import os

# def create_json_file(path, file):       
#     file_path = None

#     if len(path.split('/')) == 2:            
#         file_path = f"{path}/{file}.json"       

#     os.makedirs(path, exist_ok=True)
  
#     try:
#         with open(file_path, mode='x', encoding='utf-8') as f:
#          ...
#     except FileExistsError:
#         print(f"File '{file_path}' already exists")
#     except (TypeError, UnboundLocalError):
#         print(f"Path must by two-level, for example: 'files/json'")
  
#     return file_path

# create_file("test","file_1")





# 2

# def read_json_file(path):
#     with open(path, mode='r', encoding='utf-8') as f:
#         return json.loads(f.read)
    
# print(read_file("test/file_1"))





# 3

# import json

# my_dict=[
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]

# def update_json_file(path, my_dict):
#     with open(path, mode='r', encoding='utf-8') as f:
#         data=json.loads(f.read())

#     for i in my_dict:
#         data.append(i)

#     with open(path, mode='w', encoding='utf-8') as f:
#         f.write(json.dumps(data, indent=2))

# update_file("test/file.json", my_dict)





# 4

# def update_json_file(path, new_data):
#     with open(path, mode='a', encoding='utf-8') as f:
#         return f.write(new_data)
    
# update_file("test/file_1", "new information")
