class Library:
    def __init__(self, listOfBook):
        self.books=listOfBook
      
    def DisplayAvailableBooks(self):
        print("Books present in this library are: ")
        for books in self.books:
            print("* "+ books)

    def borrowBook(self, Bookname):    
        if Bookname in self.books:
            print(f"You have been issued {Bookname}. Please keep it safe and return it within 30 days:")
            self.books.remove(Bookname)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available:")  
            return False      

    def returnBook(self, Bookname):
        self.books.append(Bookname)
        print("Thanks for returning this book! Hope you enjoy reading it. Have a great day ahead!:")
 

class Student:
    def requestBook(self):
        self.books=input("Enter the name of the book you want to borrow: ")
        return self.books

    def returnBook(self):
        self.books=input("Enter the name of the book you want to return: ")
        return self.books
        
    

if __name__=="__main__":
    centralLibrary=Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student=Student()

    # centraLibrary.DisplayAvailableBooks()
    while(True):

        WelcomeMSG='''\n ******** Welcome to Central Library ********
        Please choice an option:
        1. List all the books :
        2. Request a books :
        3. Add/Return a books :
        4. Exit the library :
        '''

        print(WelcomeMSG)
        a=int(input("Enter a Choice :"))
        if a== 1:
            centralLibrary.DisplayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())    
        elif a==3:
            centralLibrary.returnBook(student.returnBook()) 
        elif a==4:
            print("Thanks for choosing Central library! Have a great day ahead ")  
            exit()
        else :
            print("Invaild Choice!")                
       
           
     