
# Write a program where you can write the grades of subjects. Then calculate the mean,median and standard
# deviation of all grades.

import numpy as np

grades= []

while True:

    user_input = input("Enter grades:")

    if user_input == "quit":
        if not grades:
            print("List of grades is empty")
            break
        else:
            arr = np.array([grades]).astype(np.float)
            mean = np.mean(arr)
            median = np.median(arr)
            std_dev = np.std(arr)

            print("Grades mean: %0.2f, grades median: %0.2f, grades standard deviation: %0.2f" % (mean, median, std_dev))
            break

    else:
        grades.append(user_input)



