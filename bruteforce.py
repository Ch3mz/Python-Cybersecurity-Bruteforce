'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
import zipfile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(file, password_file):
   # tacking line no. at which password is found
   id = 0
   with open (password_file, 'rb') as file: # opens file in binary mode
      #iteration on each line
      # split lines into words 
       for line in file:
           for word in line.split():
             #extraction with the current password
               try:
                   id += 1
                   file.extractall(password_file=word)
                   print("password found at line", id)
                   print("password is", word.decode())
                   return True
               except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                   continue
   return False
                

       

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
         password_file= 'rockyou.txt'

         #ZipFile object intialised 
         file = zipfile.ZipFile('enc.zip')
         #count of number of words present in the file
         cnt = len(list(open(password_file, "rb")))
         print("There are total", cnt, "number of passowrds to test")

         if attempt_extract(file, password_file) == False:
           print ("Password not found in this file")
if __name__ == "__main__":
    main()
