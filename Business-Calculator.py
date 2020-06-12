# Hello My name is Doga Ege Ozden.
# Sorry I couldn't calculate some of the topics.
# The reason why ptyhon cannot calculate negative ln(ex: math.log(-5))
# But I can always provide formula sheets for calculating all of these topics.
# My webpage is dogaegeozden.com
# My gmail is dogaegeozden@gmail.com
# PLEASE CHECK MY CALCULATIONS TWICE BEFORE STARTING USING THIS APP.
# I tried to do my best but I'm a human being.

# IMPORTANT
# I can't accept any responsibility for any wrong calculation happen
# because of this calculator. So PLEASE CHECK MY CALCULATIONS TWICE!!!
# And you use it and develop it however you like
# I hope you like my application.

print("BUSINESS CALCULATOR")
print()

print("""Welcome to business calculator here you can easliy calculate your
problems related to business mathematic and finance.""")
print()

print("""FEATURES""")
print("""
Simple Calculator: 1
Mathematics of Business & Finance Calculator: 2
Business Statistics Calculator: 3
""")
print()


import math

feature = int(input("Select a feature: "))
print()

# This is the part for feature 1.
if feature == 1:
    print("""ARITMETICAL OPERATORS""")
    print("""
    Addition: +
    Subtract: -
    Division: /
    Multiply: *
    Square: sqr
    """)
    print()

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
    Reduced Profit(using markdown): RP2
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
    Principal: Pir
    Future Value: FV
    Amount of Compound Interest: ACI
    Periodic Interest Rate: PIR
    Number of Compounding Periods: NCP
    Nominal Interest Rate: NIR
    Periodic interest rate using future value and present value: PIR2
    Equivalent Periodic Interest Rate: EPIR
    Equivalent Nominal Interest Rate: ENIR
    Number of Compounding Periods: NCP2
    Time Period in Years: TPY
    Effective Interest Rate: EIR
    Future Value of an Ordinary Simple Annuity: FVOSA
    Present Value of an Ordinary Simple Annuity: PVOSA
    Number of Compounding Periods per Payment Period: NCPPPP
    Equivalent Periodic Interest Rate per Payment Period: EPIRPP
    Future Value of a Simple Annuity Due: FVSAD
    Present Value of a Simple Annuity Due: PVSAD
    Number of Payments, Given 'FV': NPGFV
    Number of Payments, Given 'PV': NPGPV ** I couldn't calculate this one I'm sorry
    Time Period (in years): TPY2
    Number of Payments, Given 'FV­Due': NPGFVD
    Number of Payments, Given ‘PV­Due': NPGPVD ** I couldn't calcuate this one I'm sorry
    """)
    print()

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

    # This is the part that calculates geometric mean.
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
    elif topic == "RP2":
        op = float(input("Enter your operating profit here: "))
        mrkdown = float(input("Enter your markdown amount here: "))
        rp2 = op - mrkdown
        print("Result: ",rp2)

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

    # This is the part that calculates principal.
    elif topic == "Pir":
        s = float(input("Enter your maturity value here: "))
        r = float(input("""Enter your simple interest as decimal number.
ex: 70% = 0.7
Enter your simple interest rate here: """))
        t = float(input("Enter your time period here: "))
        pir = s / ( 1 + r * t)
        print("Result: ",pir)

    # This is that part that calcuates future value
    elif topic == "FV":
        pv = float(input("Enter your present value here: "))
        i = float(input("""Enter your periodic rate of interest as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        n = float(input("Enter your number of compounding periods during the term here: "))
        fv = pv * ( 1 + i ) ** n
        print("Result: ",fv)

    # This is the part that calculates present value.
    elif topic == "PV":
        fv = float(input("Enter your future value here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        n = float(input("Enter your number of compounding periods during the term here: "))
        pv = fv / ( ( 1 + i ) ** n )
        print("Result: ",pv)

    # This is the part that calculates
    elif topic == "ACI":
        fv = float(input("Enter your future value here: "))
        pv = float(input("Enter your present value here: "))
        aci = fv - pv
        print("Result: ",aci)

    # This is the part that calculates
    elif topic == "PIR":
        j = float(input("Enter your nominal (stated or quoted) annual interest rate here: "))
        m = float(input("Enter your number of compounding periods per year (compounding frequency: )"))
        pir = j / m
        print("Result: ",pir)

    # This is the part that calculates number of compounding periods
    elif topic == "NCP":
        m = float(input("Enter your number of compounding periods per year (compounding frequency) here: "))
        t = float(input("Enter your Time period or term in years here: "))
        ncp = m * t
        print("Result: ",ncp)

    # This is the part that calculates nominal interest rate,
    elif topic == "NIR":
        m = float(input("Enter your Number of compounding periods per year (compounding frequency) m here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        j = m * i
        print("Result: ",j)

    # This is the part that calculates periodci interest rate using future value and present value.
    elif topic == "PIR2":
        fv = float(input("Enter your future value here: "))
        pv = float(input("Enter your present value here: "))
        n = float(input("Enter your number of compounding periods during the term n here: "))
        pir2 = ( ( fv / pv ) ** ( 1 / n ) - 1 )
        print("Result: ",pir2)

    # This is the part that calculates equivalent periodic interest rate.
    elif topic == "EPIR":
        i1 = float(input("""Enter your periodic rate of interest i1 as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        m1 = float(input("Enter your m1 Number of compounding periods per year (compounding frequency) here: "))
        m2 = float(input("Enter your m2 Number of compounding periods per year (compounding frequency) here: "))
        epir = ( ( 1 + i1 ) ** ( m1 / m2 ) ) - 1
        print("Result: ",epir)

    # This is the part that calculates Equivalent Nominal Interest Rate
    elif topic == "ENIR":
        m2 = float(input("Enter your Number of compounding periods per year (compounding frequency) m2 here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        enir = m2 * i
        print("Result: ",enir)

    # This is the part that calculates Number of compounding periods.
    elif topic == "NCP2":
        fv = float(input("Enter your future value FV here: "))
        pv = float(input("Enter your present value PV here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        ncp2 = math.log( fv / pv ) / math.log( 1 + i )
        print("Result: ",ncp2)

    # This is the part that calculates time period in years.
    elif topic == "TPY":
        n = float(input("Enter your number of compounding periods during the term n here: "))
        m = float(input("Enter your Number of compounding periods per year (compounding frequency) m here: "))
        tpy = n / m
        print("Result: ",tpy)

    # This is the part that calculates Effective Interest Rate
    elif topic == "EIR":
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        m = float(input("Enter your Number of compounding periods per year (compounding frequency) m here: "))
        eir = ( ( 1 + i ) ** m ) - 1
        print("Result: ",eir)

    # This is the part that calculates future values of an ordinary simple annity.
    elif topic == "FVOSA":
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        n = float(input("Enter your Total number of payments during the term of an annuity(n) here: "))
        fvosa = pmt * ( ( ( ( 1 + i ) ** n ) - 1 ) / i )
        print("Result: ",fvosa)

    # This is the part that calculates Present value of an ordinary simple annuity.
    elif topic == "PVOSA":
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        n = float(input("Enter your Total number of payments during the term of an annuity(n) here: "))
        pvosa = pmt * ( ( 1 - ( ( 1 + i ) ** ( 1 / n ) ) ) / i )
        print("Result: ",pvosa)

    # This is the part that calculates Number of Compounding Periods per Payment Period
    elif topic == "NCPPPP":
        ncppy = float(input("Enter your number of compounding periods per year here: "))
        npp = float(input("Enter your number of payments per year here: "))
        ncpppp = ncppy / npp
        print("Result: ",ncpppp)

    # This is the part that calculates equivalent periodic interest rate per paymet period.
    elif topic == "EPIRPP":
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        c = float(input("Enter your number of compounding period per payment period (c) here: "))
        epirpp = ( ( 1 + i ) ** c ) - 1
        print("Result: ",epirpp)

    # This is the part that calcuates future value of a simple annuity due.
    elif topic == "FVSAD":
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        n = float(input("Enter your Total number of payments during the term of an annuity(n) here: "))
        fvsad = pmt * ( ( ( (1 + i ) ** n ) - 1 ) / i ) * ( 1 + i )
        print("Result: ",fvsad)

    # This is the part that calculates present value of a simple annuity due.
    elif topic == "PVSAD":
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        n = float(input("Enter your Total number of payments during the term of an annuity(n) here: "))
        pvsad = pmt * ( ( 1 - ( (1 + i ) ** ( 1 / n ) ) ) / i ) * ( 1 + i )
        print("Result: ",pvsad)

    # This is the part that calcualates number of payments given future value.
    elif topic == "NPGFV":
        fv = float(input("Enter your given future value here: "))
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        npgfv = math.log( 1 + ( ( i * fv ) / pmt ) ) / math.log( 1 + i )
        print("Result: ",npgfv)

    # This is the part that calcuates number of periods Number of Payments, Given 'PV'. It's calculating 'n'.
    elif topic == "NPGPV":
        pv = float(input("Enter your given present value here: "))
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        npgpv =  -math.log( 1 - ( ( i * pv ) / pmt ) ) / math.log( 1 + i )
        print("Result: ",npgpv)

    # This is the part that calcaulates time period in years.
    elif topic == "TPY2":
        n = float(input("Enter your Total number of payments during the term of an annuity(n) here: "))
        nppy = float(input("Enter your number of payments per year here: "))
        tpy2 = n / nppy
        print("Result: ",tpy2)

    # This is the part that calculates number of payments given FV due.
    elif topic == 'NPGFVD':
        print("I'm couldn't calculate this one I'm sory python can't calculate negative ln. But I can always provide the formula for the people ask for.")
        fv = float(input("Enter your given future value here: "))
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        npgfvd = math.log( 1 + ( ( i * fv ) / ( pmt * ( 1 + i ) ) ) ) / math.log( 1 + i )
        print("Result: ",npgfvd)

    # This is the part that calculates Number of Payments, Given ‘PV­Due ' it's calculating 'n'.
    elif topic == "NPGPVD":
        pv = float(input("Enter your given present value here: "))
        pmt = float(input("Enter your Amount of periodic payment in an annuity(PMT) here: "))
        i = float(input("""Enter your periodic rate of interest i as decimal number.
ex: 30% = 0.3 or 35% = 0.35
Enter your periodic rate of interest here:
"""))
        npgpvd = -math.log( 1 - ( ( i * pv ) / ( pmt * ( 1 + i ) ) ) ) / math.log( 1 + i )
        print("Result: ", npgpvd)

# This is the part for feature 3.
elif feature == 3:
    print("I'm solving calculating Statistics using this app. This part is not for share.")
