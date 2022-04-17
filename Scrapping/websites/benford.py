import math

# benefords distrubution
# returns a hash map with the benford dustrubion
def benford_distrubtion():
    benford = {}
    for d in range(1,9):
        percent = math.log(((1+d)/d),10)
        # todo : if want printed in 2 decimal places :str. format() 
        benford.update({f"{d}":round(percent * 100,2)})
    return benford

if __name__ == "__main__":
    benfordList = benford_distrubtion()
    for digit in benfordList:
        print(benfordList[digit])
