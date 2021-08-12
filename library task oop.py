# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 02:48:00 2021

@author: anna gerd
"""

class libraryDepartment:
    
    def __init__(self):
        self.storage = []
        print(self)
        
    def addLibrary(self):
        lib = library(len(self.storage))
        self.storage.append(lib)
        return lib
        
    def __str__(self):
        return str(self.storage)
        

class book:
    
    def __init__(self, author, name):
        self.author = author
        self.name = name
        print(self)
    
    def __str__(self):
        return 'Book is added: ' + self.author + ', ' + self.name

class user:
    
    def __init__(self, passport, library):
        self.passport = passport
        self.givenBook = {}
        self.library = library
    
    def takeBook(self, name):
        book = self.library.giveBook(name)
        self.givenBook[name] = book
        print(name, book.author)
    
    def returnBook(self, name):
        bookUser = self.givenBook[name]
        self.givenBook.pop(name)
        self.library.addBook(bookUser.author, bookUser.name)
        
    def __str__(self): 
        return str(self.givenBook)

            
class library: 
    
    def __init__(self, number):
        self.bookStorage = {}
        self.userStorage = []
        self.number = number
        print(self)
        
    def addBook(self, author, name):
        bookOfLibrary = book(name,author)
        self.bookStorage[bookOfLibrary.name] = bookOfLibrary
        return bookOfLibrary

    def addListOfBooks(self, bookDict): 
        for i in bookDict.keys(): 
            self.addBook(i, bookDict[i])
    
    def addUser(self, passport):
        passportUser = user(passport, self)
        self.userStorage.append(passportUser)
        return passportUser
    
    def giveBook(self, name):
        bookUser = self.bookStorage[name]
        self.bookStorage.pop(name)
        return bookUser
    
    def getBookStorage(self):
        n = ""
        for i in self.bookStorage:
            n = n + str(i + " " + self.bookStorage[i].author + "\n")
        return n

    def __str__(self):
        return (str('Библиотека №' + str(self.number)) + ' \n' + self.getBookStorage())

class Interface:
    
    def __init__(self):
        self.GU = libraryDepartment()
        self.lib1 = self.GU.addLibrary()
        self.lib2 = self.GU.addLibrary()
        self.lib3 = self.GU.addLibrary()
        passport = input("Enter your passport: ")
        lib = input("Enter a number of library: ")
        if lib == str(self.lib1.number):
            self.us = self.lib1.addUser(passport)
            self.lib1.addListOfBooks({'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', })
            print(self.lib1)
        if lib == str(self.lib2.number):
            self.us = self.lib2.addUser(passport)
            self.lib2.addListOfBooks({'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', })
            print(self.lib2)
        if lib == str(self.lib3.number):
            self.us = self.lib3.addUser(passport)
            self.lib3.addListOfBooks({'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', })
            print(self.lib3)
    
    def takeBookInterface(self):
        name = input("Enter a name of the book: ")
        self.us.takeBook(name)
        print(self.us)
        
    
        
int1 = Interface()
int1.takeBookInterface()