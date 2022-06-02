import random

order_roll = int(input("How many orders?: "))

sucNum = 0
failNum = 0
failTaste = 0
failLook = 0
failSpill = 0
failTemp = 0

while order_roll > 0:
    order = 0
    failTest = 0
    fail = []
    if order == 0:
        while failTest < 4:
            if random.randint(0, 60) == 60:
                fail.append(failTest)
                if failTest == 0:
                    failTaste = failTaste + 1
                if failTest == 1:
                    failSpill = failSpill + 1
                if failTest == 2:
                    failLook = failLook + 1
                if failTest == 3:
                    failTemp = failTemp + 1


            failTest = failTest + 1

    if len(fail) > 0:
        failNum = failNum + 1
        print("fail", fail)

    else:
        sucNum = sucNum + 1
        order_roll = order_roll - 1

    fail.clear()

# TEST CODE (to be deleted in final version)

#print()
#print("attempts = ", (sucNum + failNum))
#print("fails = ", failNum)
#print("successes = ", sucNum)
#print("fail rate = ", float(int(float(failNum / (sucNum + failNum)) * 100000) / 1000), "%")

#print("\nfails:")
#if failNum > 0:
#    print("taste: ", float(int(float((failTaste / failNum) * 100000)) / 1000), "%")
#    print("look: ", float(int(float((failLook / failNum) * 100000)) / 1000), "%")
#    print("spill: ", float(int(float((failSpill / failNum) * 100000)) / 1000), "%")
#    print("temp.", float(int(float((failTemp / failNum) * 100000)) / 1000), "%")

#else:
#    print("NO FAILS!")

