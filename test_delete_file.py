from functions.delete_file import delete_file

# create dummy file
with open("calculator/test_delete.txt", "w") as f:
    f.write("This is a test file for deletion.")
print("Dummy file created: calculator/test_delete.txt")
# test delete_file function
result = delete_file("./calculator", "test_delete.txt")
print(result)