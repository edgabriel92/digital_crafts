totalAmount = float(raw_input("Enter the total amount: "))
good_per = 20
fair_per = 15
bad_per = 10
service = raw_input("Was the service good, fair, or bad? ")
numOfPeople = float(raw_input("How many people do you want to split the bill with? "))

if service == "bad":
    service = bad_per
    tip = totalAmount / 100 * service
    print "The service was bad and deserves a %s percent tip" % bad_per
    print "Your tip should be %s" % tip 
    print float((totalAmount + tip) / numOfPeople)
elif service == "fair":
    service = fair_per
    tip = totalAmount / 100 * service
    print "The service was fair and deserves a %s percent tip" % fair_per
    print "Your tip should be %s"  % tip
    print float((totalAmount + tip) / numOfPeople)
elif service == "good":
    service = good_per
    tip = totalAmount / 100 * service
    print "The service was good and deserves a %s percent tip" % good_per
    print "Your tip should be %s" % tip
    print float((totalAmount + tip) / numOfPeople)
else:
    service = raw_input("Was the service good, fair, or bad? ")

