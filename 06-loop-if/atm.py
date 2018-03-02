money = 500
request = 277

if request <= money:
        if request <= 0:
            print "you can't request 0 or negative numbers"

        else:
            while request > 0:
                if request >= 100:
                    print "give 100"
                    request -= 100

                elif request >= 50:
                    print "give 50"
                    request -= 50

                elif request >= 10:
                    print "give 10"
                    request -= 10

                elif request >= 5:
                    print "give 5"
                    request -= 5

                else:
                    print "give " + str(request)
                    request -= 0

    else:
        print "Dude, you don't have this amount of money!!!"

