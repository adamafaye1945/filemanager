import pathlib


class My_file_manager:
    def __init__(self, path_to_directory) -> None:
        # we will have pathlib go to our directory
        # put folder and files in a list
        
        
        self.path = path_to_directory
        
        # get to the directory 
        self.directory = pathlib.Path(self.path)
        
        # list of path
        file_list = list(self.directory.iterdir())
        
        
        file_folder_unsorted = [element for element in file_list]
        self.file_and_folder_name = sorted(file_folder_unsorted)
        self.file_zip = [element for element in file_list if element.suffix == '.zip']

        
    def show_list_of_all_file(self):
        """print list of file and folder name"""
        for i in range(len(self.file_and_folder_name)):
            print(self.file_and_folder_name[i])  
            
              
    def show_list_of_zip_file(self):
        """print list of downloaded zip file"""
        for i in range(len(self.file_zip)):
            print(self.file_zip[i])
        
    def find_duplicated_file_and_delete(self):
        """Function that delete all the duplicated file the duplicated file of a file
        """
        # duplicated file contains a duplication number in a parenthesis at the end
        # example 'essay (1).pdf' is a duplicate of 'essay.pdf'
        # we need to find the same file with the number in between parenthesis (duplicate)
        # and we delete it
        
         
        j = 0
        while j < len(self.file_and_folder_name):
            dup_counter = 1
            while f"({dup_counter})" in self.file_and_folder_name[j].name:
                if self.file_and_folder_name[j].is_file:
                    self.file_and_folder_name[j].unlink(missing_ok=True)
                else:
                    self.file_and_folder_name[j].rmdir()
                dup_counter+=1
                j+=1
            j+=1
        
    def delete_particular_zip(self, file_name):
        for path in self.file_zip:
            if path.name == file_name:
                print(path)            
        
manager = My_file_manager(path_to_directory='/Users/adama/Downloads/')
manager.find_duplicated_file_and_delete()