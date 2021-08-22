# Copyright © 2021 All rights reserved. Doga Ege Ozden
# This is a world clock that shows the time in countries that have a place
# in bricks.

import datetime
import pytz


print("WORLD CLOCK")
print()

print("Welcome to world clock here you can see what time is in countries included Brazil, Russia, India, China, South Africa, Turkey and Canada")
print()

print("""
OPTIONS
Turkey: Tr
Canada: Ca
Brazil: Bra
Russia: Rus
India: Ind
China: Chi
South Africa: Sa
""")


while True:
    userselection = str(input("Enter your selection here: "))
    caseinsensetiveselection = userselection.lower()
    print()

    if caseinsensetiveselection == "exit":
        break

    elif caseinsensetiveselection == "tr" or caseinsensetiveselection == "turkey":
                # This is the part that includes turkey's timezone.
                def dt_time_turkey():
                    return datetime.datetime.now(tz=pytz.timezone("Turkey"))

                stringTimeP1 = dt_time_turkey().strftime("%H %M")
                stringDate = dt_time_turkey().strftime("%b, %d %Y")
                print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
                print("Date: {}".format(stringDate))
                print()


    elif caseinsensetiveselection == "ca" or caseinsensetiveselection == "canada":
        print("CANADA TIMEZONES")
        print("Atlantic(A)")
        print("Central(C)")
        print("Eastern(E)")
        print("Mountain(M)")
        print("New Foundland(NF)")
        print("Pacific(P)")
        print("Saskatchewan(S)")
        print("Yukon(Y)")
        print()

        question1 = input("Enter your timezone here: ")
        answer1 = question1.lower()
        print()
        if answer1 == "atlantic" or answer1 == "a":
            dt_time_cad_atlantic = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))

            stringTimeP1 = dt_time_cad_atlantic.strftime("%H %M")
            stringDate = dt_time_cad_atlantic.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "central" or answer1 == "c":
            dt_time_cad_central = datetime.datetime.now(tz=pytz.timezone("Canada/Central"))

            stringTimeP1 = dt_time_cad_central.strftime("%H %M")
            stringDate = dt_time_cad_central.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "eastern" or answer1 == "e":
            dt_time_cad_eastern = datetime.datetime.now(tz=pytz.timezone("Canada/Eastern"))

            stringTimeP1 = dt_time_cad_eastern.strftime("%H %M")
            stringDate = dt_time_cad_eastern.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "mountain" or answer1 == "m":
            dt_time_cad_mountain = datetime.datetime.now(tz=pytz.timezone("Canada/Mountain"))

            stringTimeP1 = dt_time_cad_mountain.strftime("%H %M")
            stringDate = dt_time_cad_mountain.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "newfoundland" or answer1 == "nf" or answer1 == "new foundland" or answer1 =="nfl":
            dt_time_cad_newfoundland = datetime.datetime.now(tz=pytz.timezone("Canada/Newfoundland"))

            stringTimeP1 = dt_time_cad_newfoundland.strftime("%H %M")
            stringDate = dt_time_cad_newfoundland.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "pacific" or answer1 == "p":
            dt_time_cad_pacific = datetime.datetime.now(tz=pytz.timezone("Canada/Pacific"))

            stringTimeP1 = dt_time_cad_pacific.strftime("%H %M")
            stringDate = dt_time_cad_pacific.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "saskatchewan" or answer1 == "s":
            dt_time_cad_saskatchewan = datetime.datetime.now(tz=pytz.timezone("Canada/Saskatchewan"))

            stringTimeP1 = dt_time_cad_saskatchewan.strftime("%H %M")
            stringDate = dt_time_cad_saskatchewan.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "yukon" or answer1 == "y":
            dt_time_cad_yukon = datetime.datetime.now(tz=pytz.timezone("Canada/Yukon"))

            stringTimeP1 = dt_time_cad_yukon.strftime("%H %M")
            stringDate = dt_time_cad_yukon.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        else:
            print("You didn't enter valid choice.")
            print()


    elif caseinsensetiveselection == "bra" or caseinsensetiveselection == "brazil":
        print("BRAZIL'S TIMEZONES")
        print("Acre(A)")
        print("Denoronha(D)")
        print("East(E)")
        print("West(W)")
        print()

        question1 = input("Enter your timezone here: ")
        answer1 = question1.lower()
        print()
        if answer1 == "acre" or answer1 == "a":
            dt_time_braz_acre = datetime.datetime.now(tz=pytz.timezone("Brazil/Acre"))

            stringTimeP1 = dt_time_braz_acre.strftime("%H %M")
            stringDate = dt_time_braz_acre.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "denoronha" or answer1 == "d":
            dt_time_braz_denoronha = datetime.datetime.now(tz=pytz.timezone("Brazil/DeNoronha"))

            stringTimeP1 = dt_time_braz_denoronha.strftime("%H %M")
            stringDate = dt_time_braz_denoronha.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "east" or answer1 == "e":
            dt_time_braz_east = datetime.datetime.now(tz=pytz.timezone("Brazil/East"))

            stringTimeP1 = dt_time_braz_east.strftime("%H %M")
            stringDate = dt_time_braz_east.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "west" or answer1 == "w":
            dt_time_braz_west = datetime.datetime.now(tz=pytz.timezone("Brazil/West"))

            stringTimeP1 = dt_time_braz_west.strftime("%H %M")
            stringDate = dt_time_braz_west.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        else:
            print("You didn't entered valid choice.")
            print()


    elif caseinsensetiveselection == "rus" or caseinsensetiveselection == "russia":
        print("RUSSIA'S TIMEZONES")
        print("Kamchatka Krai, Russia(KK)")
        print("Magadan(M)")
        print("Sakhalin(S)")
        print("Vladivostok(V)")
        print("Yakutsk(Y)")
        print("Irkutsk(I)")
        print("Novosibirsk(N)")
        print("Samara(SAM)")
        print("Kaliningrad(K)")
        print()

        question1 = input("Enter your timezone here: ")
        answer1 = question1.lower()
        print()
        if answer1 == "kamchatka krai, russia" or answer1 == "kk" or answer1 == "kamchatka":
            dt_time_rsy_krai = datetime.datetime.now(tz=pytz.timezone("Asia/Kamchatka"))

            stringTimeP1 = dt_time_rsy_krai.strftime("%H %M")
            stringDate = dt_time_rsy_krai.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "magadan" or answer1 == "m":
            dt_time_rsy_magadan = datetime.datetime.now(tz=pytz.timezone("Asia/Magadan"))

            stringTimeP1 = dt_time_rsy_magadan.strftime("%H %M")
            stringDate = dt_time_rsy_magadan.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "sakhalin" or answer1 == "s":
            dt_time_rsy_sakhalin = datetime.datetime.now(tz=pytz.timezone("Asia/Sakhalin"))

            stringTimeP1 = dt_time_rsy_sakhalin.strftime("%H %M")
            stringDate = dt_time_rsy_sakhalin.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "vladivostok" or answer1 == "v":
            dt_time_rsy_vladivostok = datetime.datetime.now(tz=pytz.timezone("Asia/Vladivostok"))

            stringTimeP1 = dt_time_rsy_vladivostok.strftime("%H %M")
            stringDate = dt_time_rsy_vladivostok.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "yakutsk" or answer1 == "y":
            dt_time_rsy_yakutsk = datetime.datetime.now(tz=pytz.timezone("Asia/Yakutsk"))

            stringTimeP1 = dt_time_rsy_yakutsk.strftime("%H %M")
            stringDate = dt_time_rsy_yakutsk.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "irkutsk" or answer1 == "i":
            dt_time_rsy_irkutsk = datetime.datetime.now(tz=pytz.timezone("Asia/Irkutsk"))

            stringTimeP1 = dt_time_rsy_irkutsk.strftime("%H %M")
            stringDate = dt_time_rsy_irkutsk.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "novosibirsk" or answer1 == "n":
            dt_time_rsy_novosibirsk = datetime.datetime.now(tz=pytz.timezone("Asia/Novosibirsk"))

            stringTimeP1 = dt_time_rsy_novosibirsk.strftime("%H %M")
            stringDate = dt_time_rsy_novosibirsk.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "samara" or answer1 == "sam":
            dt_time_rsy_samara = datetime.datetime.now(tz=pytz.timezone("Europe/Samara"))

            stringTimeP1 = dt_time_rsy_samara.strftime("%H %M")
            stringDate = dt_time_rsy_samara.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        elif answer1 == "kaliningrad" or answer1 == "k":
            dt_time_rsy_kaliningrad = datetime.datetime.now(tz=pytz.timezone("Europe/Kaliningrad"))

            stringTimeP1 = dt_time_rsy_kaliningrad.strftime("%H %M")
            stringDate = dt_time_rsy_kaliningrad.strftime("%b, %d %Y")
            print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
            print("Date: {}".format(stringDate))
            print()

        else:
            print("You didn't entered valid choice.")
            print()



    elif caseinsensetiveselection == "ind" or caseinsensetiveselection == "india":
        dt_time_indi_antananarivo = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

        stringTimeP1 = dt_time_indi_antananarivo.strftime("%H %M")
        stringDate = dt_time_indi_antananarivo.strftime("%b, %d %Y")
        print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
        print("Date: {}".format(stringDate))
        print()

    elif caseinsensetiveselection == "chi" or caseinsensetiveselection == "china":
        dt_time_chi_gmt8 = datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai"))

        stringTimeP1 = dt_time_chi_gmt8.strftime("%H %M")
        stringDate = dt_time_chi_gmt8.strftime("%b, %d %Y")
        print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
        print("Date: {}".format(stringDate))
        print()

    elif caseinsensetiveselection == "sa" or caseinsensetiveselection == "south africa":
        dt_time_sa_gmt2 = datetime.datetime.now(tz=pytz.timezone("Africa/Johannesburg"))

        stringTimeP1 = dt_time_sa_gmt2.strftime("%H %M")
        stringDate = dt_time_sa_gmt2.strftime("%b, %d %Y")
        print("Time: ",stringTimeP1.split(" ")[0]+":"+stringTimeP1.split(" ")[1])
        print("Date: {}".format(stringDate))
        print()

    else:
        print("You didn't entered valid country code.")
        print()
