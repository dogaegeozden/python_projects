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
Arithmetic Average: AA
Weighted Average: WA
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
Amount Credited: AC
Selling Price: SP
Amount of Markup: M
Selling Price2(using overhead expenses and operating profit): SP2
Rate of Markup on Cost: RMC
Rate of Markup on Selling Price: RMSP
Break Even Price: BPRC
Reduced Selling Price: RSP
Amount of Markdown: AMD
Reduced Profit(using cost and overhead expenses): RP
Reduced Profit(using markdown): RP1
Net Amount of Markup: NAM
Net Rate of Markup Based on Total Cost: NRMBTC
Net Rate of Markup Based on Total Sales: NRMBTS
Total Variable Costs: TVC
Total Costs: TC
Total Revenue: TR
Net Income: NI
At the break even point: ABE
Contribution Margin per Unit: CMPU
Contribution Ratio: CR
Cost-Volume-Profit Analysis: CVPA
Number of Units(Produced and sold): NU
Number of Units at the Break-Even Point: NUBE
Contribution Margin Percent: CMP
Total Contribution Margin: TMC
Interest: I
Maturity Value: MV
principal: PIR
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
    if topic == "AA":
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
    elif topic == "WA":
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

        print(discsl1)

        # THIS CODE ISN'T GIVING RIGHT ASWER DON'T FORGET.

        for c in range(len(discsl1)):
            discsl1[c] = ( 1 - discsl1[c] )

        startpoint = 1

        def multiplier(startpoint, discsl1):

            for n in discsl1:
                startpoint *= float(n)

            return startpoint

        multiplier(startpoint, discsl1)

        sedrR = 1 - multiplier(startpoint,discsl1)

        print(sedrR)

    # This is the part that calculates Amount Credited
    elif topic == "AC":
        ap = float(input("Enter your ammound paid here: "))
        sd = float(input("""Enter your single discount rate as decimal number.
ex: 50% = 0.5
Enter your single discount rate here: """))
        Ac = ap / ( 1 - sd )
        print("Result: ",Ac)

    # This is the part that calculates Selling price.
    elif topic == "SP":
        cst = float(input("Enter your cost here: "))
        mrkup = float(input("Enter your markup here: "))
        sp = cst + mrkup
        print("Result: ",sp)

    # This is the part that calculates Amount of markup.
    elif topic == "M":
        ohe = float(input("Enter your overhead expenses here: "))
        op = float(input("Enter your operating profit here: "))
        mrkup = ohe + op
        print("Result: ",mrkup)

    # This is the part that calculates Selling price2 using
    elif topic == "SP2":
        cst = float(input("Enter your cost here: "))
        ohe = float(input("Enter your overhead expenses here: "))
        op = float(input("Enter your operating profit here: "))
        sp = cst + ohe + op
        print("Result: ", sp)

    # This is the part that calculates Rate of Markup on Cost
    elif topic == "RMC":
        mrkup = float(input("Enter your markup amount here: "))
        cst = float(input("Enter your cost here: "))
        rmc = ( mrkup / cst ) * 100
        print("Result: ", rmc,"%")

    # This is the part that calculates Rate of Markup on Selling Price
    elif topic == "RMSP":
        mrkup = float(input("Enter your markup amount here: "))
        sp = float(input("Enter your selling price here: "))
        rmsp = ( mrkup / sp ) * 100
        print("Result: ", rmsp,"%")

    # This is the part that calculates break even price
    elif topic == "BPRC":
        cst = float(input("Enter your cost here: "))
        ohe = float(input("Enter your overhead expenses: "))
        bprc = cst + ohe
        print("Result: ", bprc)

    # This is the part that calculates
    elif topic == "RSP":
        sp = float(input("Enter your selling price here: "))
        mrkdwn = float(input("Enter your markdown amount here: "))
        rsp = sp - mrkdwn
        print("Result: ",mrkdwn)

    # This is the part that calculates amount of markdown
    elif topic == "AMD":
        sp = float(input("Enter your selling price here: "))
        sred = float(input("Enter your redused selling price: "))
        amd = sp - sred
        print("Result: ",amd)

    # This is the part that calculates Rate of Markdown
    elif topic == "RMD":
        mrkdown = float(input("Enter your amount of markdown here: "))
        sp = float(input("Enter your amount of selling price here: "))
        rmd = ( mrkdown / sp ) * 100
        print("Result: ",rmd,"%")

    # This is the part that calculates Reduced profit
    elif topic == "RP":
        rsp = float(input("Enter your reduced selling price or selling price here: "))
        cst = float(input("Enter your cost here: "))
        ohe = float(input("Enter your overhead expenses here: "))
        rp = rsp - cst - ohe
        print("Result: ",rp)

    # THis is the part that calculates reduced profit using markdown
    elif topic == "RP1":
        op = float(input("Enter your operating profit here: "))
        mrkdown = float(input("Enter your markdown amount here: "))
        rp = op - mrkdown
        print("Result: ",rp)

    # This is the part that calculates
    elif topic == "NAM":
        ts = float(input("Enter your total sales here: "))
        tc = float(input("Enter your total costs here: "))
        nam = ts - tc
        print("Result: ", nam)

    # This is the part that calculates Net Rate of Markup Based on Total Cost
    elif topic == "NRMBTC":
        nam = float(input("Enter your net amount of markup here: "))
        tc = float(input("Enter your total cost here: "))
        nrmbtc = ( nam / tc ) * 100
        print("Result: ",nrmbtc,"%")

    # This is the part that calculates Net Rate of Markup Based on Total Sales
    elif topic == "NRMBTS":
        nam = float(input("Enter your net amount of markup here: "))
        ts = float(input("Enter your total sales here: "))
        nrmbts = ( nam / ts ) * 100
        print("Result: ",nrmbts,"%")

    # this is the part that calculates total variable cost.
    elif topic == "TVC":
        vc = float(input("Enter your variable cost per unit here: "))
        x = float(input("Enter your number of units produced and sold here: "))
        tvc = vc * x
        print("Result: ",tvc)

    # This is the part that calculates total costs
    elif topic == "TC":
        fc = float(input("Enter your Fixed cost for a specific period here: "))
        tvc = float(input("Enter your total variable cost here: "))
        tc = fc + tvc
        print("Result: ",tc)

    # This is the part that calculates total revenues.
    elif topic == "TR":
        s = float(input("Enter your selling price here: "))
        x = float(input("Enter your number of units produced and sold here: "))
        tr = s * x
        print("Result: ",tr)

    # This is the part that calculates Net income.
    elif topic == "NI":
        tr = float(input("Enter your total revenue here: "))
        tc = float(input("Enter your total costs here: "))
        ni = tr - tc
        print("Result: ",ni)

    # This is the part that show what is the meaning of at the break even point
    elif topic == "ABE":
        print("At the break even point total revenue is equal to total cost. TR = TC !")

    # This is the part that calculates contribution margin per unit.
    elif topic == "CMPU":
        s = float(input("Enter your selling price per unit here: "))
        vc = float(input("Enter your variable cost here: "))
        cmpu = s - vc
        pritn("Result: ",cmpu)

    # This is the part that calculates
    elif topic == "CR":
        cm = float(input("Enter your contiribution margin here: "))
        s = float(input("Enter your selling price here: "))
        cr = ( cm / s ) * 100
        print("Result: ",cr,"%")

    # This is the part show what is the meaning of cost volume profit analysis
    elif topic == "CVPA":
        answr = str(input("""
The formula for cost volume profit analysis: S * x  = FC + (VC + x) + NI
What it means that is Total revenue = Total cost + Net income
Do you know your Total cost and Net income? (y/n)
"""))

        if answr == 'y':
            tc = float(input("Enter your total cost here: "))
            ni = float(input("Enter your net income here: "))
            cvpa = tc + ni
            print("Result: ",cvpa)

        elif answr == 'n':
            fc = float(input("Enter your fixed costs here: "))
            vc = float(input("Enter your variable cost here: "))
            ni = float(input("Enter your net income here: "))
            x = float(input("Enter your number of units produced and sold: "))
            cvpa = fc + ( vc * x ) + ni
            print("Result: ",cvpa)

    # This is the part that calculates Number of Units produced and sold.
    elif topic == "NU":
        fc = float(input("Enter your fixed cost here: "))
        ni = float(input("Enter your net income here: "))
        s = float(input("Enter your selling price here: "))
        vc = float(input("Enter you variable cost here: "))
        nu = ( fc + ni ) / ( s - vc )
        print("Result: ",nu)

    # This is the part that calcuates Number of Units at the Break-Even Point:
    elif topic == "NUBE":
        fc = float(input("Enter your fixed costs here: "))
        cm = float(input("Enter your contribution margin per unit here: "))
        nube = fc / cm
        print("Result: ",nube)

    # This is the part that calculates contribution margin percentage.
    elif topic == "CMP":
        tr = float(input("Enter your total revenues here: "))
        tvc = float(input("Enter yor total variable cost here: "))
        cmp = ( ( tr - tvc ) / tr ) * 100
        print("Result: ",cmp,"%")

    # This is the part that calculates total contribution margin.
    elif topic == "TCM":
        ni = float(input("Enter your net income here: "))
        fc = float(input("Enter your fixed costs here: "))
        tmc = ni + fc
        print("Result: ",tmc)

    # This is the part that calculates interest
    elif topic == "I":
         p = float(input("Enter your principal here: "))
         r = float(input("""
Enter your simple interest as a decimal number
ex: 70% = 0.7
Enter your simple interest here: """))
         t = float(input("Enter your time period here: "))
         i = p * r * t
         print("Result: ",i)

    # This is the part that calculates maturity value.
    elif topic == "MV":
        answr = str(input("Do you know your interest? (y/n) "))
        if answr == 'y':
            p = float(input("Enter your principal here: "))
            i = float(input("Enter your interest here: "))
            mv = p + i
            print("Result: ",mv)

        elif answr == 'n':
            p = float(input("Enter your interest here: "))
            r = float(input("""Enter your simple interest as decimal number.
ex: 70% = 0.7
Enter your simple interest rate here: """))
            t = float(input("Enter your time period here: "))
            mv2 = p * ( 1 + r * t )
            print("Result: ",mv2)

    elif topic == "PIR":
        s = float(input("Enter your maturity value here: "))
        r = float(input("""Enter your simple interest as decimal number.
ex: 70% = 0.7
Enter your simple interest rate here: """))
        t = float(input("Enter your time period here: "))
        pir = s / ( 1 + r * t)
        print("Result: ",pir)

        # THIS IS WHERE YOU LEFT
