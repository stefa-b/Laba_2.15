if __name__ == "__main__":
         # open the newfile.txt in read mode. causes error if no such file exists.
         fileptr = open("newfile.txt", "x")
         print(fileptr)
         if fileptr:
             print("File created successfully")
             # closes the opened file
             fileptr.close()