"""just practicing doc string"""
def test():
    """output hello to console"""
    print("hello")

def average(a_num:int, b_num:int,c_num:int)->float:
    """This function return average of three numbers
       :param: a is the first number
       :param: b is the second number       
       :param: c is the third number
       :return: a float which indicates avg of given three numbers 
    """
    return(a_num+b_num+c_num)/3

a:int=2
print(a)
