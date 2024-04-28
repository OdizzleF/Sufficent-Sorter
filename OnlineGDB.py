#The purpose of this code: For a company to be able to input lists of inventory
#and to be easily able to view, sort, add, and remove from inventory.

#Imported random just for IDs which'll use random number generation.
import random

#User will open or make a new project
Projects=["Holderplace","Placeholder",'t']

#All prompts will be answered with buttons in VS-Code
#Exception will be anything that needs to be named

#A while loop that'll break as soon as user chooses a file to open.
while True:
    #prompt
    choice=input(" 'Open' or 'Add' project? ")
    #checks spelling
    if choice.lower() == 'open':
        print(Projects)
        choiceP=input('Which project? ')
        if choiceP in Projects:
            print ("You've chosen project",choiceP)
            break
        else:
            print("Cannot find project", choiceP)
        #The input above will open said project.
        continue
        #If there are no projects, will tell user no projects, click here to make one.
    
        #Will have to make a folder for files, kinda like how notepad does
        
    #if user adds, check spelling first.    
    elif choice.lower() == 'add':
        ProjectName=input("What would you like your project to be named?")
        #checks for an actual name
        if ProjectName == '':
            print("Can't leave space blank.")
        elif ProjectName in Projects:
            print("Project already exists")
        else:
            Projects.append(ProjectName)
            continue
    #later point may allow description for file
        
#Add buttons that offer to add:ItemList
#(ItemList as in "Shirts" and Columns for "Size, Color, For whom")


#lines 48 through 55 are set up outside the loop to avoid any issues inside it.
ListOfItemList=[]
DictOfItemList={}
ItemListIncrement=1
ListOfColumns=[]
#made a function outside a loop so it can be called as needed
#AddingList functions accepts a name, checks if that name is already taken
#If the name is already taken, it adds a (1),(2), et cetera for whichever iteration it is.
def AddingList():
    Namebase=1
    ItemList=(input("Name of your list: "))
    while True:
        if ItemList in ListOfItemList:
            ItemList=ItemList+"("+str(Namebase)+")"
            Namebase=Namebase+1
            if ItemList in ListOfItemList:
                continue
            else:
                ListOfItemList.append(ItemList)
                Namebase=1
                print(ItemList)
                break
            
        else:
            ListOfItemList.append(ItemList)
            Namebase=1
            print(ItemList)
            break
        
#Prompt now shows Add another list, or Edit one of the lists
while True:
    #User input
    choice1=input("'AddList', 'EditList','ViewList','Close'")
    if choice1.lower() == 'addlist':
        #This calls the function made beforehand.
        AddingList()
        
    elif choice1.lower() == 'editlist':
        print(ListOfItemList)
        #allows user to choose between multiple lists in a project and edit them.
        choice2=input('Which list?')
        if choice2 in ListOfItemList:
            while True:
                #Gives user choice of what they need to do to said list.
                choice3=input("'Name','Column','Delete', 'Back' ")
                if choice3.lower()=='name':
                    choiceN=input('What would you like to change the name too? (N to cancel)')
                    #N will be a button in VS-Code, its purpose is just to cancel
                    #If the list tries to get changed to an already existing list, it prevents it.
                    #If not canceled, nor already existing, user input (choiceN) is the new name of the list
                    if choiceN.lower() == 'n':
                        continue
                    elif choiceN.lower() in ListOfItemList:
                        print("List already exists.")
                    else:
                        #The code below finds the index of the list being renamed, gives it a variable
                        #Then the variable gets changed to the name submitted.
                        xN=ListOfItemList.index(choice2)
                        ListOfItemList[xN]=choiceN
                        print("Name changed successfully to",choiceN)
                elif choice3.lower()=='column':
                    #Put variables, lists, dictionary outside loop.
                    #These will be used to save the information about the product for inventory
                    xN=choice2+'_'+'attributes'
                    if xN in DictOfItemList:
                        True
                    else:
                        Quantity=0
                        IDs=[]
                        Sizes=[]
                        #The dictionary below saves a variable and 2 lists, to the key xQ
                        #xQ being (name of the list being edited)_attributes
                        DictOfItemList[xN]=(Quantity,IDs,Sizes)
                        
    
                    
                    while True:
                                
                        request = input("Would you like to Add or Remove from list (N to cancel): ")
                        
                        if request.lower()=='n':
                            break
                        
                        elif request.lower()=="add":
                            amount=int(input("How many?: "))
                            
                            for x in range(0,amount):
                                Letter=random.randint(1,3)
                                if Letter==1:
                                    Letter="A"
                                elif Letter==2:
                                    Letter="B"
                                elif Letter==3:
                                    Letter="C"
                                
                                Quantity = Quantity + 1 
                                SizeL=str(input("Length?: ")+"L")
                                SizeW=str(input("Width?: " )+"W")
                                Sized=(SizeL+"&"+SizeW)
                                print(Sized)
                                Sizes.append(Sized)
                            
                                ID=choice2+str(Quantity)+Letter+str(random.randint(1,10000))
                                print("The ID for the",choice2," is",ID)
                                IDs.append(ID)
                                
                                
                            continue1=input("Would you like add more? Y or N: ")
                            if continue1.lower() == "y":
                                continue
                            elif continue1.lower() == "n":
                                xTest=xN.keys()
                                print(xTest)
                                break
                            
                        elif request.lower()=="remove":
                            while True:
                            #This is simplified, I would like to add a checkmark while viewing the list.
                            #ALl checked will be removed.
                                resR = "\n".join("{} {}".format(x, y) for x, y in zip(IDs, Sizes))
                                print(resR)
                                choiceR=input("Which item # would you like to remove?(N to Cancel)")
                                if choiceR.lower()=='n':
                                    break
                                else:
                                    SpecR=int(choiceR)
                                    print(IDs[SpecR-1],Sizes[SpecR-1])
                                    choiceRC=input("Confirm removal? Y/N")
                                    if choiceRC.lower()=='y':
                                        DictOfItemList[xN][0]=Quantity-1
                                        DictOfItemList[xN][IDs.remove(choiceR)]
                                        DictOfItemList[xN][Sizes.remove(choiceR)]
                            
                        else:
                            print("And invalid input was made.")
                            
                    while True:
                        followup=input("Would you like to go 'Back' or 'View': ")
                        if followup.lower()=='back':
                            break
                        elif followup.lower()=='view':
                            Viewer=input("Would you like to 'View' all "+choice2+", or a 'Specific' (If specific, type # it's in")
                            if Viewer.lower()=='view':
                                res = "\n".join("{} {}".format(x, y) for x, y in zip(IDs, Sizes))
                                print(res)
                            elif Viewer.lower()=='specific':
                                Spec=int(input("Which"+choice2+"? "))
                                print(IDs[Spec-1],Sizes[Spec-1])
                elif choice3.lower()=='delete':
                    #These lines of code just check if you actually want to delete the list
                    #.remove is used to get rid of the list
                    choiceD=input('Are you sure? Y/N')
                    if choiceD.lower() == 'y':
                        ListOfItemList.remove(choice2)
                        break
                    else:
                        continue
                elif choice3.lower()=='back':
                    #this is here to take the user back to add,edit,view lists, or close program
                    break
                else:
                    #incase user doesn't put any of the 4 options
                    print("Invalid choice.")
    
    elif choice1.lower() == 'viewlist':
        continue
    elif choice1.lower() == 'close':
        #ends program
        break
        
    else:
        #if user submits an incorrect input
        print("An invalid input was made.")