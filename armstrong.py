"""
What is Armstrong Number?
It is a number which is equal to the sum of cube of its digits.
For eg: 153, 370 etc.
Lets see it practically by calculating it,

Suppose I am taking 153 for an example

First calculate the cube of its each digits

  1^3 = (1*1*1) = 1

  5^3 = (5*5*5) = 125

  3^3= (3*3*3) = 27
"""


def get_armstrong_numbers(num_till=400):
    """

    Parameters
    ----------
    num_till

    Returns
    -------

    """
    arm_strong_number=[]
    for num in range(num_till):
        #    if num == sum([int(a)**3 for a in str(num)]):
        if num == sum([pow(int(a),3) for a in str(num)]):
            print(f"{num} is a armstrong number")
            arm_strong_number.append(num)
        else:
            print(f"{num} is not a armstrong number")

    print(f"armstrong numbers ={arm_strong_number}")

if __name__ == "__main__":
    get_armstrong_numbers(18000)
    print(__doc__)

