# Made-for-learning

Description of the Project

The project Made-for-learning was creating for the Data Stewardship course at Vienna University during the autumn term 2023 and the spring term 2024. It was used for getting a first experience with GitHub and it contains a solution for the Python assignment of this course.
The task of the Python assignment was writing a short program according to the waterfall model and to present a documentation that describes:
1.	the problem that this program is going to resolve, 
2.	the design of the code,
3.	the implementation of the program, and
4.	the verification of the program.
The document Assigment_2-7_ThK.pdf contains a description of parts 1, 2 and 4. The document Quality_of_my_day_v2.py contains the code for the implementation. It is the second version of this code. The first version of this code is not published.

Brief Description of the Problem

The program Quality of my Day is inspired by quality-of-life questions that are used in medical research projects. It invites a person to a brief dialogue about the quality of their day. Answering these questions gives this person an opportunity to reflect about their current level of happiness. 
The program does not calculate any result that is based on widely accepted scientific research nor does it provide support to persons who need help. However, it might make people aware of things and experiences that add to the quality of their day but that they did not pay attention to. 

Brief Description of the Design

As for programming the program collects data from a person through a question answer dialogue and it uses the answers to calculate of quality-of-day score that can have value in the range of 0 to 5. In the next step, the program asks the person who uses it set a score for their current level of felt happiness that can have a value between 1 and 5. A values of 5 indicates high happiness and a value of 1 low happiness. 

The program proceeds to calculate the sum of the quality-of-day score and the score for felt happiness. This sum can have a value between 1 and 10. The results for the quality-of-day score and the score for felt happiness are written to a text file and plotted in a bar diagram. 

Many people who answer the questions of this program will have a scores for their quality of day and for their felt happiness that together give a sum that is equal or greater than 5. For these people, program follows a linear path that includes collecting data, calculating scores, and writing them to a text file. In the final step the data of the text file a plotted in a diagram.

For some people, the sum of their quality-of-day score and the score of their felt happiness might be lower than 5. In this case, the program enters another path where the program tells those people that that it noted that they might not have a good day. The person who has a dialogue with the program gets then an opportunity to continue or to quit if they prefer to do that.  

The program is written in Python 3.12 using Visual Studio code 1.85.1. It includes an array, a function, and a loop. It also collects data though a dialogue with a person and it writes them to a text file. As a complement the program also plots the data in the text file in a diagram.

Verification and Issues

The program was tested by white box testing, and it works well when the person who uses it answers all questions correctly. It cannot cope with incorrect input, however. If someone answers a question in a way that is not defined in the code, the program will report an error because the variables concerned will not be defined.  For instance, if a person wants to answer a question with Yes, the correct answer is “yes”. If that person enters “Yes” instead of “yes”, the program will report an error.  

2024-01-03/Th. Theresa Kieselbach
