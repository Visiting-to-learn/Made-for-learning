print("\n""Hello and welcome!""\n""\n""This program gives you an opportunity to reflect about your current level of happiness.""\n""It uses an interactive function that calculates the sum of your quality-of-day score and of your felt level of happiness.""\n""It is made for giving you some time to reflect about your day.""\n""Please note that this program does not calculate a result that is based on widely accepted scientifc research.""\n") #Start of the program and welcome text.
answer0=input("Do you want to proceed? (yes/no): ") #The program asks, if the person who uses it would like to continue or to quit.
if answer0=="yes":
    pass
else:
    print("\n""Thank you for coming by! Have a good day!""\n")
    quit()
print("\n""Please answer the following questions to calculate your quality-of-day score.""\n")
answer1=input("Did you sleep well during the night? (yes/no): ") #Here starts a series of 5 interactive questions that make decisions about some quality-of-day parameters. The answer is either yes and it will set a score of 1, or it is no and it will set a score of 0. Any answer that is different from yes will set a score of 0. 
if answer1=="yes":
    sleep=1
if answer1=="no":
    sleep=0
answer2=input("Did you have a good breakfast, a good lunch, or a good dinner? (yes/no): ")
if answer2=="yes":
    meal=1
if answer2=="no":
    meal=0
answer3=input("Do you feel safe? (yes/no): ")
if answer3=="yes":
    safety=1
if answer3=="no":
    safety=0
answer4=input("Did you to talk to someone nice today? (yes/no): ")
if answer4=="yes":
    social=1
if answer4=="no":
    social=0
answer5=input("Did you enjoy your day so far? (yes/no): ")
if answer5=="yes":
    nice_day=1
if answer5=="no":
    nice_day=0
import numpy as np #The variables of the quality-of-day questions are stored in an array that calaculates their sum. To be able to use the array, the program must import the library numpy.
array1=np.array([sleep, meal, safety, social, nice_day])
for number in [array1]:
    print("\n""Thank you for your answers! The scores that you entered are:",number,)
quality=np.sum(array1)
print("Your quality-of-day score for today is the sum of the scores that you entered, and it has the value",quality,"out of a range of 0 to 5.""\n") #The calculation of the quality-of-dat score is complete and the program shows the result.
answer6=input("Are you happy today? Please set a score between 1 and 5 for the level of your felt happiness.""\n""A score of 5 means that you are very happy and a score of 1 means that you are very unhappy. (1/2/3/4/5): ") #The program asks the person who uses it to make a decision about their happiness and to enter a value between 1 and 5 for the level of their felt happiness right now.
if answer6=="1": 
    felt_happiness=1
if answer6=="2":
    felt_happiness=2
if answer6=="3":
    felt_happiness=3
if answer6=="4":
    felt_happiness=4
if answer6=="5":
    felt_happiness=5 
def function(quality): #This function calculates the sum of the variables quality and felt_happiness. As it does not perform any advanced mathematical calculation the import of the library math is not necessary.
    return(quality+felt_happiness)
if (function(quality))>=5: #The function (happiness(quality)) makes a decision about how to proceed in this program. The following if-statements open for a further dialogue, but they do not add new features to the program.
    pass
else:
    answer7=input("\n""It seems that you do not have a good day today. Do you have somone who you can can talk to about it? (yes/no): ")
    if answer7=="yes":
        print("\n""That is excellent!")
        answer8=input("\n""Would you like to proceed? (yes/no): ")
        if answer8=="yes":
            pass
        if answer8=="no":
            print("\n""Take care! Thank you for coming by!""\n")
            quit()
    if answer7=="no":
        print("\n""I am sorry to hear that.")
        answer9=input("\n""Would you like to proceed anyway? (yes/no): ")
        if answer9=="yes":
            pass
        if answer9=="no":
            print("\n""Take care! Thank you for coming by!""\n")
            quit()
print("\n""The sum of your scores for the quality of your day and for your felt happiness is",(function(quality)),"out of a range of 1 to 10.""\n""\n""Your results are saved to the file my_data_doc.txt in your default user folder.""\n""Please view the bar diagram for a graphical visualization.""\n""The parameter max_possible_score visualizes the highest possible value for the quality-of-day-score and for the level of felt happiness.""\n""\n""The diagram is saved as a png-image file with the name Figure_1 in your default user folder.""\n""\n""Thank you for using this program!""\n""To end this program, please close the diagram.""\n")
max_possible_score=5 #This variable is not used in any calculation. It is included to display the highest possible score value in the diagram and it has no other purpose.
file=open("my_data_doc.txt", "w") #The program writes the variables "quality", "felt_happiness" and "max_possible_score" as strings to the comma-separated text file my_data_doc.text that has a header row. It is important that all calaculations are finished when the variables are written as strings to a text file.
quality=repr(quality)
felt_happiness=repr(felt_happiness)
max_possible_score=repr(max_possible_score)
file.write("variable_name"",""variable_value""\n""quality"","+quality+"\n""felt_happiness"","+felt_happiness+"\n""max_possible_score"","+max_possible_score+"\n") #File saved in your default user folder.
file.close() #The program closes the text file my_data_doc.txt
from datetime import datetime #The program imports datetime.
now=datetime.now() #The variable "now" contains the current date and time. It is used to include the current date in the diagram.
import matplotlib.pyplot as plt #The program imports the library matplotlib.pyplot. It then opens and reads the text file my_data_doc.txt and plots the variables in this file in a bar diagram.
names=[] 
scores=[] 
f=open("my_data_doc.txt","r") 
f.readline()
for row in f: 
    row=row.split(",") 
    names.append(row[0]) 
    scores.append(int(row[1]))
plt.ylim(0,6)
plt.bar(names, scores, color="c", width=0.3, label=now) 
plt.xlabel("Quality of Life Parameters", fontsize=12) 
plt.ylabel("Scores [Arbitrary Units]", fontsize=12) 
plt.title("My Quality of Day and Felt Happiness", fontsize=20) 
plt.legend()
plt.savefig("Figure_1.png") #The program saves a file with the diagram in the default user folder.
plt.show() #The program shows the diagram. This is the last step of the program.
#This code was written by Th. Theresa Kieselbach at Umeå University Library, Sweden using Python 3.12 and Visual Studio Code 1.85.1. It has a GNU General Public License. The file with the code has the name Quality_of_my_day_v2.py. It contains version 2.0 of this code.