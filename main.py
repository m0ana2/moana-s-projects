import csv
import numpy as np

lst1 = []
lst2 = []
with open("a csv file.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        lst1.append(row["row_one"])
        lst2.append(row["row_two"])

def name_match():
    points = 0
    lst_range_num = [i for i in range(len(lst1))]
    random_num = np.random.choice(lst_range_num)
    print(lst1[random_num])
    my_answer = input("type the-//what ever u want to cross from the other list://")
    while my_answer == lst2[random_num]:
        points += 1
        lst1.pop(random_num)
        lst2.pop(random_num)
        lst_range_num.pop()
        if len(lst_range_num) != 0:
          random_num = np.random.choice(lst_range_num)
          print(lst1[random_num])
          my_answer = input("type the iata code of the country:")
        else:
            break

    print("you got: " + str(points) + " points with: " + str(len(lst1)) + " list 1 header.")
    if len(lst_range_num) != 0:
      print("currect answer is: " + lst2[random_num])
    else :
        print("you got everything right!")


name_match()