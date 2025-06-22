
import sys

def initial_phonebook():
    rows, cols=int(input("please enter initial number of contacts:")),2



    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order {ONLY}"%(i+1))
        print("NOTE * indicates mandatory fields")
        print(".............................................................")
        temp=[]
        for j in range(cols):

            if j ==0:
                temp.append(str(input("enter name")))

            if j==1:
                temp.append(int(input("enter number")))
            
        phone_book.append(temp)
    print(phone_book)
    return phone_book
pb=initial_phonebook()

def add_contact(pb):
    #adding a contact is the easiest because all you need to do is
    #append another list of details into the already existing list
    dip=[]
    for i in range(len(pb[0])):
        if i==0:
            dip.append(str(input("enter name"))),2
        if i==1:
            dip.append(str(input("enter number")))
    pb.append(dip)
    return(pb)
pb=add_contact(pb)
print(pb)
    
  