import sys
from prettytable import PrettyTable

print("D'Hondt Method Calculator")
Seatscontested=int(input("How many seats are contested in this election? "))
Listsrunning=int(input("How many lists are running in this election? "))
Threshold=float(input("What is the electoral threshold percentage? (answer 0 if there is none) %"))
Lists=[]
Voteswon=[]
Seatswon=[]
Quotients=[]
affirmative=["Y", "YES", "SIM", "S", "OUI", "O"]

while len(Lists) != Listsrunning:
    List=str(input("Name the #" + str(len(Lists)+1) + " list running: "))
    Votes=float(input("How many votes did " + List + " get? "))
    Lists.append(List)
    Voteswon.append(Votes)
    Quotients.append(Votes)
    Seatswon.append(0)

print("\nVOTING BREAKDOWN:")
i=0
Progress=None
EditGrid = PrettyTable()
EditGrid.add_column("Index Number", [num for num in range(0, len(Lists))])
EditGrid.add_column("List name", [List for List in Lists])
EditGrid.add_column("Votes", [int(Votes) for Votes in Voteswon])
print(EditGrid)
Progress=(input("Do you want to change any of the data you've entered before the seat allocation? (Y/N)"))
if Progress.upper() in affirmative:
    print("\nEDITOR:")
    edit=""
    while edit.upper != "STOP":
        EditGrid.clear()
        EditGrid.add_column("Index Number", [num for num in range(0, len(Lists))])
        EditGrid.add_column("List name", [List for List in Lists])
        EditGrid.add_column("Votes", [int(Votes) for Votes in Voteswon])
        print(EditGrid)
        edit=(input("\nIf you want to change the name or amount of votes of a specific list the index number (the leftmost number on the table) of the list whose data you want to change.\nIf you want to add another list to the election, type ADD.\nIf you want to change the number of seats in contention (Currently " + str(Seatscontested) + ") type SEATS.\nIf you want to change the threshold percentage, type THRESHOLD.\nIf you want no more changes, type STOP and the program will proceed with the seat allocation: "))
        if edit.upper()=="SEATS":
            Seatscontested=int(input("Type the new amount of seats contested: "))
        elif edit.upper()=="ADD":
            List=str(input("Name the #" + str(len(Lists)+1) + " list running: "))
            Votes=float(input("How many votes did " + List + " get? "))
            Lists.append(List)
            Voteswon.append(Votes)
            Quotients.append(Votes)
            Seatswon.append(0)
        elif edit.upper()=="STOP":
            break
        elif edit.upper()=="THRESHOLD":
            Threshold=float(input("What is the new electoral threshold percentage? (answer 0 if there is none) %"))
        else:
            try:
                edition=int(edit)
            except:
                continue
            if edition in range(0, len(Lists)):
                change=(input("\nIf you want to change the name of " + Lists[edition] + " you may type 1. If you want to change the amount of votes (currently " + str(Voteswon[edition]) + "), type 2. If you want to remove this candidacy, type 3. Type 4 to go back to the editor without changes."))
                Listchange=int(change)
                if Listchange==1:
                    Lists[edition]=(input("Type the new name of this list: "))
                if Listchange==2:
                    Voteswon[edition]=float(input("Type the new vote tally of this list: "))
                if Listchange==3:
                    Lists.pop(edition)
                    Voteswon.pop(edition)
                    Quotients.pop(edition)
                    Seatswon.pop(edition)
            else:
                continue

def percentage(Votes, total=sum(Voteswon)):
    return round((Votes/total)*100,2)

print("\nSEAT ALLOCATION:")
while Seatscontested != 0:
    ilook=0
    iresult=0
    while ilook != len(Quotients):
        if Quotients[ilook] == max(Quotients):
            iresult=ilook
        ilook+=1
    if percentage(Voteswon[iresult])<Threshold:
        Quotients[iresult]=0
    else:
        Seatswon[iresult]+=1
        Seatscontested-=1
        Quotients[iresult]=(Voteswon[iresult]/(Seatswon[iresult]+1))
        print (Lists[iresult] + " has won a seat, the candidacy has now " + str(Seatswon[iresult]) + " seats in total. " + str(Seatscontested) + " seats remain")

print("\nFINAL RESULTS:")


resultGrid = PrettyTable()
resultGrid.add_column("List Name", [list for list in Lists]),
resultGrid.add_column("Votes", [int(votes) for votes in Voteswon]),
resultGrid.add_column("%", [percentage(votes) for votes in Voteswon]),
resultGrid.add_column("Seats", [seats for seats in Seatswon])
print(resultGrid)

Majoritycutoff=int((sum(Seatswon)/2)+1)
def majoritystatus(seats):
    if seats >= Majoritycutoff:
        return "an absolute "
    else:
        return "a relative "


if Voteswon.count(max(Voteswon))!=1:
    print("More than one candidate is tied with the most votes.")
else:
    i=0
    for votes in Voteswon:
        if votes == max(Voteswon):
            print (Lists[i] + " has won the election. The candidacy has achieved " + majoritystatus(max(Seatswon)) + "majority.")
        i+=1
if majoritystatus(max(Seatswon))=="an absolute ":
    sim=str(input("With this seat composition there is no need for a coalition. Would you nonetheless like to open the Coalition Simulator? (Y/N)"))
else:
    sim=str(input("With this seat composition a coalition is necessary. Would you like to open the Coalition Simulator? (Y/N)"))
if sim.upper() not in affirmative:
    print("Program execution complete.")
    sys.exit()
print("\nCOALITION SIMULATOR:")
Coalparties=[]
Coalseats=0
Potparties=[]
Potseats=[]
Select=""

def CPremoval(index):
    global Coalparties 
    global Coalseats
    global Potparties
    global Potesats
    Coalparties.remove(Potparties[index])
    Coalseats-=Potseats[index]

def CPaddition(index):
    global Coalparties 
    global Coalseats
    global Potparties
    global Potesats
    Coalparties.append(Potparties[index])
    Coalseats+=Potseats[index]

CoalGrid = PrettyTable()

i=0
for Seats in Seatswon:
    if Seats != 0:
        Potseats.append(Seats)
        Potparties.append(Lists[i])
    i+=1

while Select.upper() != "STOP":
    CoalGrid.clear()
    CoalGrid.add_column("Index", [num for num in range(0, len(Potparties))]),
    CoalGrid.add_column("List Name", [list for list in Potparties]),
    CoalGrid.add_column("Seats won", [seats for seats in Potseats]),
    CoalGrid.add_column("In Coalition?", [list in Coalparties for list in Potparties])

    print(CoalGrid)
    if len(Coalparties)==0:
        print("Your coalition has no members selected yet.")
        print("You need " + str(Majoritycutoff) + " seats for a majority")
    else:
        print("The following members are in your coalition:" + str(Coalparties))
        print("Your current coalition has: " + str(Coalseats) + " seats. You need " + str(Majoritycutoff) + " for a majority")
        if Coalseats >= Majoritycutoff:
            print("YOUR COALITION HAS A MAJORITY!")
    Select=input("You may add/remove a member from your coalition by typing their index number (the leftmost number on the table). Alternatively, type STOP to end the execution:")
    if Select.upper() != "STOP":
        if Potparties[int(Select)] in Coalparties:
            CPremoval(int(Select))
        else:
            CPaddition(int(Select))

print("Program execution complete.")
