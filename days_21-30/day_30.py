# # day 30

# try:
#     file = open("a_file.txt")
#     a_dict = {"name": "Christian"}
#     print(a_dict["name"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("stuff")
# except KeyError as error_msg:
#     print(f"{error_msg} is not valid key")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height should be under 3 meters")


bmi = weight / height ** 2
