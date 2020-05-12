# This is a business calculator that calculates business
# mathematic and finance problems its not done yet but you can get
# right answers till Single equivalent discount rate: SEDR
# topic.

print("BUSINESS CALCULATOR")
print()

print("""Welcome to business calculator here you can easliy calculate your
problems related to business mathematic and finance.""")
print()

print("""FEATURES""")
print("""
Simple Calculator: 1
Business Calculator: 2
""")
print()

print("""ARITMETICAL OPERATORS""")
print("""
Addition: +
Subtract: -
Division: /
Multiply: *
Square: sqr
""")
print()

print("TOPICS :")
print("""
Arithmetic Average: A
Weighted Average: W
Geometric Mean: G
Portion: P
Percentage Chanbge: PC
Pay for pay period: PP
Hourlly rate of pay: HRP
Property tax: PT
Property tax expressed as mill rate: PTM
Amount of trade discount: ATD
Net price: NP
Net price after a series of discounts: NPASD
Single equivalent discount rate: SEDR
""")
print()

feature = int(input("Select a feature: "))

# This is the part for feature 1.
if feature == 1:
    n1 = float(input("Enter your first number: "))
    while True:
        symbol = input("Enter your operator or the topic: ")
        n2 = float(input("Enter your number: "))
        if n2 == " ":
            break
        if symbol == "+":
            n1 += n2
            print("Result: ", n1)
        elif symbol == "*":
            n1 *= n2
            print("Result: ", n1)
        elif symbol == "-":
            n1 -= n2
            print(n1)
        elif symbol == "/":
            n1 /= n2
            print("Result: ", n1)
        elif symbol == "sqr":
            n1 *= n1
            print("Result:", n1)

# This is the part for feature 2.
elif feature == 2:
    topic = input("Enter your topic here: ")

    # This is the part that calculates aritetic average.
    if topic == "A":
        nums = input("""
Hint: Enter your numbers by putting ',' between them and no spacing.
Enter your numbers: """)
        numl = nums.split(",")
        def Adder(numl):
            startpoint = 0

            for n in numl:
                startpoint += float(n)

            return startpoint
        Adder(numl)

        Aresult = Adder(numl) / len(numl)
        print(Aresult)

    # This is the part that calculates weighted average.
    elif topic == "W":
        nums = input("""
Hint: Enter your numbers in right order by putting ',' between them and no spacing.
example: 1,2,3
Enter your numbers: """)
        wvals = input("""
Hint: Enter your weight values in right order by putting ',' between them and no spacing.
example: 1,2,3
Enter your weight values: """)
        numl = nums.split(",")
        wvall = wvals.split(",")
        numl1 = [ float(n) for n in numl ]
        wvall1 = [ float(wv) for wv in wvall ]

        for c in range(len(numl1)):
            numl1[c] = numl1[c] * wvall1[c] / sum(wvall1)
        numl1 = sum(numl1)

        print(numl1)

    elif topic == "G":
        nums = input("""
Hint: Enter the numbers that you want to calculate their geometric mean by putting ','
between them no spacing.
example: 1,2,3
Enter your numbers: """)
        numl = nums.split(',')
        numl1 = [ float(item) for item in numl ]

        def Multiplier(numl1):
            startpoint = 1

            for n in numl1:
                startpoint *= float(n)

            return startpoint
        Multiplier(numl1)

        Gresult = Multiplier(numl1) ** (1/len(numl1))

        print("Result: ", Gresult)

    # This is the part that calculates portion.
    elif topic == "P":
        base = float(input("Enter your base value here: "))
        rate = float(input("Enter your rate number here: "))
        portion = rate / base
        print("Result: ",portion)

    # This is the part that calculates percnetage change.
    elif topic == "PC":
        finval = float(input("Enter you final value here: "))
        initval = float(input("Enter you initial value here: "))
        percchange = (( finval - initval ) / initval ) * 100
        print("Result: ",percchange)

    # This is the part that calculates pay for pay period.
    elif topic == "PP":
        Annusall = float(input("Enter your annual salary here: "))
        Npp = float(input("Enter your number of pay periods per year: "))
        Ppp = Annusall / Npp
        print("Result: ",Ppp)

    # This is the part that calculates Hourly rate.
    elif topic == "HRP":
        wp = float(input("Enter your weekly pay here: "))
        numofworkhourperweek = float(input("Enter your number of work hours per week here: "))
        Hourlyrateofpay = wp / numofworkhourperweek
        print("Result: ", Hourlyrateofpay)

    # This is the part that calculates property tax.
    elif topic == "PT":
        avp = float(input("Enter your assessed value of property: "))
        tr = float(input("""
Hint: If your tax rate defined as percentage don't for get to enter as decimal number.
ex: 90% = 0.9
Enter your tax rate here: """))
        pt = avp * tr
        print("Result: ", pt)

    # This is the part that calculates property tax expressed as mill rate.
    elif topic == "PTM":
        avp = float(input("Enter your assessed value of property here: "))
        mr = float(input("Enter your mill rate here: "))
        ptm = ( avp / 1000 ) * mr
        print("Result: ",ptm)

    # This is the part that calculates amount of trade discount
    elif topic == "ATD":
        sdr = float(input("Enter your single discount rate here: "))
        lp = float(input("Enter your list price here: "))
        atd = sdr * lp
        print("Result: ",atd)

    # This is the part that calculates Net price.
    elif topic == "NP":
        lp = float(input("Enter your list price here: "))
        sdr = float(input("Enter your single discount rate here: "))
        np = lp * ( 1 - d )
        print("Result; ",np)

    #This is the part that calculates Net price after series of discounts.
    elif topic == "NPASD":
         lp = float(input("Enter your list price here: "))
         dsc = input("""
Hint: Enter your discounts here by putting ',' between each other if your
discounts are described as percentage don't forget to enter it as decimal number
ex: 60% = 0.6
Enter your discounts here: """)
         discl = dsc.split(',')
         discl1 = [ float(n) for n in discl ]

         for c in range(len(discl1)):
            discl1[c] = ( 1 - discl1[c] )

         def multiplier(discl1):
             startpoint = lp

             for n in discl1:
                 startpoint *=float(n)

             return startpoint

         multiplier(discl1)

         print(multiplier(discl1))

    # This ts the part that calculates single equivalent discount rate to a seres of dicounts.
    elif topic == "SEDR":
        discs = input("""
Hint: Enter your discounts here by putting ',' between each other if your
discounts are described as percentage don't forget to enter it as decimal number
ex: 60% = 0.6
Enter your discounts here: """)
        discsl = discs.split(',')
        discsl1 = [ float(n) for n in discsl ]

        # THIS CODE ISN'T GIVING RIGHT ASWER DON'T FORGET.

        # for c in range(len(discsl1)):
        #     discsl1[c] = ( 1 - discsl1[c] )
        #
        # startpoint = 1
        #
        # def multiplier(startpoint, discsl1):
        #
        #     for n in discsl1:
        #         startpoint *= float(n)
        #
        #     return startpoint
        #
        # multiplier(startpoint, discsl1)
        #
        # startpoint1 = float(startpoint)
        # print(startpoint1)
        #
        # def subtractor(startpoint1):
        #     endpoint = float(1 - startpoint)
        #
        #     return endpoint
        #
        # subtractor(startpoint1)
        #
        # print("Result: ",subtractor(startpoint))
