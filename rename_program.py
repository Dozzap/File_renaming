#import library
import os

#NOTE: THIS PROGRAM ONLY WORKS IF YOU WANT TO CHANGE FILES THAT IS UNDER THE SAME NAME

#Define rename function
def rename_files(directory, newName):

    #for each file in the given directory
    for filename in os.listdir(directory):

        #Give the name you want it to match
        #NOTE: use the most common reoccuring name
        if filename.startswith("Dana_Card"):

            #Get the length of the word you want to change
            id_start_index = len("Dana_Card") 
            
            #This will get the next characters after the word you want to change
            #NOTE: This will be the ID of the file
            #NOTE: This will also take care of cases in which the id is "Summary" or "124_F"
            id = filename[id_start_index:]

            #This gets the newName and the id and join them together
            new_filename = newName + id

            #This grabs the directory of the current file to be changed
            #NOTE: This is just a string that addresses the current file you are working on
            #example: "C:/Users/student3/Desktop/Complete typed cards/Dana_Card_X"
            old_path = os.path.join(directory, filename)


            #This provides the same function as the code line above, but for the new name
            new_path = os.path.join(directory, new_filename)

            #This is the rename function call from os library that swaps the name from old to new by changing the directory name of it
            os.rename(old_path, new_path)

            #This will verify what your file is renamed to
            print(f"File changed from {filename} to {new_filename}")
    
    #This will verify that the process is complete
    print("File change complate")



# NOTE: THIS IS WHERE YOU CUZTOMIZE WHAT YOU WANT TO CHANGE

# Specify the directory where the files are located
directory_path = "C:/Users/student3/Desktop/Complete typed cards"

# NOTE: THIS IS WHAT YOUR FILE NAME YOU WANT TO CHANGE TO
newName = "Polished_Card"

# Call the function to rename the files
rename_files(directory_path,newName)
