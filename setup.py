import os

file_name = "data.txt"
# Encrypt the user input
def encrypt_data(data):
    # Add your encryption logic here
    # Example:
    encoded_data = base64.b64encode(data.encode())
    return encoded_data.decode()
    pass

# Decrypt the data from the file
def decrypt_data(data):
    # Add your decryption logic here
    # Example:
    decoded_data = base64.b64decode(data.encode()).decode()
    return decoded_data
    pass

# Check if the file exists
if not os.path.exists(file_name):
    # Create the file if it does not exist
    #---------------------first time during the installation-------------------
    open(file_name, "w").close()

    while(True):
        try:
            # Get user input
            user_input = input("Enter Password : ")
            # Write the encrypted data to the file
            with open(file_name, "w") as file:
                print("passwor dis  L ",user_input)
                print("encrypted is : ",encrypt_data(user_input))
                file.write(encrypt_data(user_input))
            break
        except:
            # Handle any exceptions that occur
            print("An error occurred while trying to get user input.")

# Open the file for reading
with open(file_name, "r") as file:
    # Do something with the file
    print("file is : ", file)
    pass
