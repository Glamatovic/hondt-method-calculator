# D’Hondt Method Calculator

## Description
This Python software calculates elections’ seat allocation by using the ![D’hondt method of apportionment.](https://en.wikipedia.org/wiki/D%27Hondt_method)
With this software you will be able to:
- Simulate the allocation of seats through the D’Hondt Method
- Visualize the allocation seat-by-seat
- See the voting percentage for each running list
- Simulate a coalition scenario between the parties who won seats

## Requirements
This sofware runs on Python 3. It also requires the installation of the python prettytable module. 

## Usage
After with the installation of the prettytable module, all you'll need is to download the 'Hondt.py' file and start it with command 'python Hondt.py'.

### Start
Upon starting the program, you'll be asked to insert 3 values:
![img1](https://imgur.com/xU40lqS)
- The number of seats contested in this election (whose allocation will be solved)
- The number of lists/parties running in the election
- The percentage threshold (The percentage of votes below which a party is barred from winning seats)

If you've made any mistakes inserting this data, don't worry! You can edit them before the allocation

After inserting the initial values, you'll be asked to insert the name and vote tally for each list in the election, one list at a time.

![img2](https://imgur.com/iZ3KqqT)

At the end of inserting all of these values, you will be asked if you want to go to the editor to correct anything. You may respond with a Y if yes or an N if you want to skip the editing and go straight to calculations
![img3](https://imgur.com/6zGw5ox)

### Edition
If you go to the editor, you'll be able to change the info you've inserted previously.
- You may type the word ADD if you want to add another list to the election
- ... the word SEATS to change the amount of seats contested
- ... the word THRESHOLD to change the percentage threshold
- Or, if you want to change something about one of the lists you should type their index number, on the left side of the table
![img4](https://imgur.com/IIRrOS4)
- If you choose one of the lists, you may edit the name of the list, its vote tally, or remove it from the election. You'll just need to type the corresponding number.
Note: Only type the word or number corresponding to your choice, without quotes or spaces.

Once you've done all the editions you need, type STOP for the program to start allocating seats

### Seat Allocation
After the edition (or the data insertion if you decide to skip that part), the program will allocate the seats to the lists using D'Hondt method. The terminal will print the allocation seat-by-seat as it happens.
![img5](https://imgur.com/FG981LI)

Lastly a table with the final results
![img6](https://imgur.com/N43h6QD)

You'll be asked if you want to go to the coalition simulator, to simulate a coalition scenario with these election results.
### Coalition Simulator
The last part of the program execution is a coalition simulator. You'll see a table much like the ones we've seen already, only this time we just see the lists that won seats. 
![img7](https://imgur.com/1E12QU1)
The procedure is fairly simple, just type the index number (at the leftmost column) of the list to either add or remove it from the coaliton. If you were to make a coalition with A and B, for example, you'd type 0 first to add A to the coalition
![img8](https://imgur.com/j3s6QdY)
And then 1 to add B. This would be enough for a majority in this specific scenario.
![img9](https://imgur.com/SIgwMqY)
You can simulate as many scenarios as you'd like here. You can remove parties from the coalition by inputting their index number too. Once you're done experimenting, input STOP to conclude the software's execution.

## Roadmap
Some ideas I'm considering for the next iteration include an 'other lists' tab, to calculate the percentage accurately without adding all the lists concerned. Also including whatif scenarios, such as which lists would get the next seats, or how many votes would they need. Am also planning to use other apportionment methods such as Saint-Langué. Lastly also trying to make the software compatible with CSV data
