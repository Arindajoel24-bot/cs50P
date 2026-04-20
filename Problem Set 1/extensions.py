file_name = input("File name: ")

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")