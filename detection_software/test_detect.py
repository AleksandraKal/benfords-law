from detect import detection_data
import pytest

# test the case when plugging in benford distrubution true
# input - 10000
def test_benford():
    test = []
    for i in range (1,302):
        test.append(1)
    for j in range(1,177):
        test.append(2)
    for k in range (1,126):
        test.append(3)
    for l in range (1,98):
        test.append(4)
    for m in range (1,80):
        test.append(5)
    for n in range(1, 68):
        test.append(6)
    for o in range(1, 59):
        test.append(7)
    for p in range(1, 52):
        test.append(8)
    for r in range(1, 47):
        test.append(9)

    assert len(test) == 1000
    assert detection_data(test) == True