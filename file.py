# Define a dictionary to store the file structure
file_structure = {
    'root': {
        'type': 'directory',
        'content': {}
    }
}

# Define the current working directory
current_directory = file_structure['root']

# Define a function to list the contents of the current directory
def list_directory():
    print('Contents of', current_directory['type'], ':')
    for item in current_directory['content']:
        print(item)

# Define a function to change the current directory
def change_directory(directory):
    global current_directory
    if directory in current_directory['content']:
        current_directory = current_directory['content'][directory]
    else:
        print('Directory not found')

# Define a function to create a new directory
def make_directory(directory):
    if directory not in current_directory['content']:
        current_directory['content'][directory] = {
            'type': 'directory',
            'content': {}
        }
    else:
        print('Directory already exists')

# Define a function to delete a directory or file
def delete(item):
    if item in current_directory['content']:
        del current_directory['content'][item]
    else:
        print('Item not found')

# Define a function to move a directory or file
def move(item, destination_directory):
    if item in current_directory['content']:
        if destination_directory in current_directory['content']:
            destination = current_directory['content'][destination_directory]
            if 'type' in destination and destination['type'] == 'directory':
                destination['content'][item] = current_directory['content'][item]
                del current_directory['content'][item]
            else:
                print('Destination is not a directory')
        else:
            print('Destination directory not found')
    else:
        print('Item not found')

# Define a function to print the current working directory
def present_working_directory():
    print('Current directory:', current_directory)

# Main loop to handle user input
while True:
    user_input = input('Enter a command: ')
    commands = user_input.split()
    if len(commands) == 0:
        continue
    if commands[0] == 'ls':
        list_directory()
    elif commands[0] == 'cd':
        if len(commands) == 1:
            change_directory('root')
        else:
            change_directory(commands[1])
    elif commands[0] == 'mkdir':
        if len(commands) == 1:
            print('Please specify a directory name')
        else:
            make_directory(commands[1])
    elif commands[0] == 'delete':
        if len(commands) == 1:
            print('Please specify an item to delete')
        else:
            delete(commands[1])
