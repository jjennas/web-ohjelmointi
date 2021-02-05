import re, statistics
#function finds numbers in string
def finding_numbers(s):
    return re.findall(r"-?\d+",s)

answer = input("Give integers, can be separated by any character")
if not answer:
    print("Please input integers separated by any character")
else:
    numbers = finding_numbers(answer)
    # Tries to convert string of numbers into list of integers
    try:
        int_list = [int(i) for i in numbers]
        print(f"Sum is {sum(int_list)}, mean is {statistics.mean(int_list):.1f} and median is {statistics.median(int_list):.1f}")
    except ValueError:
        print("Error! No integers was given")


