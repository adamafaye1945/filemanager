import os


def allow_permission_for_file(directory_path):
    """This give permission to all our program to execute in
    all of our file"""
    # Get a list of all files in the directory
    file_list = os.listdir(directory_path)

    # Loop through the files and change their permissions
    for filename in file_list:
        filepath = os.path.join(directory_path, filename)
        os.chmod(filepath, 0o755)
        
        
def allow_permission_for_directory(directory_path):
    """This give permission to all our program to execute in
    all of our directory"""
    
    for root, dirs, files in os.walk(directory_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.chmod(dir_path, 0o755)