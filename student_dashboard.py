students=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10']
Marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]
def display_dash_board(students, Marks):
    #unequal length inputs that way we used zip() iterator that aggregates elements from each of the iterables.
    dictionary = dict(zip(students,Marks))

    print('a : Top 5 rank students are,in the descending order of marks ')
    top_5_students = sorted(dictionary.items(), key=lambda item: item[1],reverse=True)[:5]
    for key, value in top_5_students:
          print("%s: %s" % (key, value))
    
    print('b : least 5 rank student are, in the increasing order of marks')
    
    least_5_students = sorted(dictionary.items(), key=lambda item: item[1])[:5]
    for key, value in least_5_students:
          print("%s: %s" % (key, value))
    
    print('c : Who got marks between >25th percentile <75th percentile, in the increasing order of marks.')
    students_within_25_and_75 = sorted(dictionary.items(), key=lambda item: item[1])
    for key, value in students_within_25_and_75:
        
          if 25 < value < 75:
            print("%s: %s" % (key, value))

display_dash_board(students, Marks)
