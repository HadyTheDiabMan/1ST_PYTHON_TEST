'''
Created on Feb 6, 2020

@author: hdiab22
'''


def main():
    
    gradebook = []
    student=-1 #keep track of index for grand list.(gradebook)
    response=input("Add Student (Y/N): ")
    while response=="Y":
        student+=1
        gradebook.append([]) # you now have a 2d list
        add_grade = input("Add grade Y/N ")
        while add_grade=="Y":
            grade=float(input("Enter grade: "))
            gradebook[student].append(grade) #This goes to first list(student) and appends grade
            add_grade=input('Add another grade Y or N?: ')
        response=input("Add another student Y/N: ")
        
        
    for student in gradebook:
        print(student)
    
if __name__ == "__main__":
    main()