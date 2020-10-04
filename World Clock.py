# This is a world clock that shows the time in countries that have a place
# in bricks.

import datetime
import pytz

# This is the part that includes turkey's timezone.
def dt_time_turkey():
    return datetime.datetime.now(tz=pytz.timezone("Turkey"))

# This is the part that included canada's timezones.

dt_time_cad_atlantic = datetime.datetime.now(tz=pytz.timezone("Canada/Atlantic"))

dt_time_cad_central = datetime.datetime.now(tz=pytz.timezone("Canada/Central"))

dt_time_cad_eastern = datetime.datetime.now(tz=pytz.timezone("Canada/Eastern"))

dt_time_cad_mountain = datetime.datetime.now(tz=pytz.timezone("Canada/Mountain"))

dt_time_cad_newfoundland = datetime.datetime.now(tz=pytz.timezone("Canada/Newfoundland"))

dt_time_cad_pacific = datetime.datetime.now(tz=pytz.timezone("Canada/Pacific"))

dt_time_cad_saskatchewan = datetime.datetime.now(tz=pytz.timezone("Canada/Saskatchewan"))

dt_time_cad_yukon = datetime.datetime.now(tz=pytz.timezone("Canada/Yukon"))

# This is the part that includes brazil's timezones

dt_time_braz_acre = datetime.datetime.now(tz=pytz.timezone("Brazil/Acre"))

dt_time_braz_denoronha = datetime.datetime.now(tz=pytz.timezone("Brazil/DeNoronha"))

dt_time_braz_east = datetime.datetime.now(tz=pytz.timezone("Brazil/East"))

dt_time_braz_west = datetime.datetime.now(tz=pytz.timezone("Brazil/West"))

# This is the part that includes rusia's timezones.

dt_time_rsy_krai = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+12"))

dt_time_rsy_magadan = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+11"))

dt_time_rsy_sakhalin = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+11"))

dt_time_rsy_vladivostok = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+10"))

dt_time_rsy_yakutsk = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+9"))

dt_time_rsy_irkutsk = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+8"))

dt_time_rsy_novosibirsk = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+7"))

dt_time_rsy_samara = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+4"))

dt_time_rsy_kaliningrad = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+12"))

# This is the part that includes India's timezone

dt_time_indi_antananarivo = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_chagos = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_christmas = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_cocos = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_comoro = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_kerguelen = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_mahe = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_maldives = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_mauritius = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_mayotte = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

dt_time_indi_reunion = datetime.datetime.now(tz=pytz.timezone("Indian/Antananarivo"))

# This part includes china's timezones

dt_time_chi_gmt8 = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+8"))


# This part includes south africa's timezones.

dt_time_sa_gmt2 = datetime.datetime.now(tz=pytz.timezone("Etc/GMT+2"))

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
    userselection = str(input("Enter your selection of option here: "))
    caseinsensetiveselection = userselection.lower()

    if caseinsensetiveselection == "exit":
        break

    elif caseinsensetiveselection == "tr":
        print("TURKEY TIMEZONE")
        print("Turkey: ", dt_time_turkey())
        print()


    elif caseinsensetiveselection == "ca":
        print("CANADA TIMEZONES")
        print("Atlantic: ",dt_time_cad_atlantic)
        print("Central: ",dt_time_cad_central)
        print("Eastern: ",dt_time_cad_eastern)
        print("Mountain: ",dt_time_cad_mountain)
        print("New Foundland: ",dt_time_cad_newfoundland)
        print("Pacific: ",dt_time_cad_pacific)
        print("Saskatchewan: ",dt_time_cad_saskatchewan)
        print("Yukon: ",dt_time_cad_yukon)
        print()



    elif caseinsensetiveselection == "bra":
        print("BRAZIL'S TIMEZONES")
        print("Acre: ", dt_time_braz_acre)
        print("Denoronha: ", dt_time_braz_denoronha)
        print("East: ", dt_time_braz_east)
        print("West: ", dt_time_braz_west)
        print()


    elif caseinsensetiveselection == "rus":
        print("RUSSIA'S TIMEZONES")
        print("Kamchatka Krai, Russia: ", dt_time_rsy_krai)
        print("Magadan: ", dt_time_rsy_magadan)
        print("Sakhalin: ", dt_time_rsy_sakhalin)
        print("Vladivostok: ", dt_time_rsy_vladivostok)
        print("Yakutsk: ", dt_time_rsy_yakutsk)
        print("Irkutsk: ", dt_time_rsy_irkutsk)
        print("Novosibirsk: ", dt_time_rsy_novosibirsk)
        print("Samara: ", dt_time_rsy_samara)
        print("Kaliningrad: ", dt_time_rsy_kaliningrad)
        print()


    elif caseinsensetiveselection == "ind":
        print("INDIA'S TIMEZONES")
        print("Antananarivo: ",dt_time_indi_antananarivo)
        print("Chagos: ", dt_time_indi_chagos)
        print("Christmas: ", dt_time_indi_christmas)
        print("Cocos: ", dt_time_indi_cocos)
        print("Comoro: ", dt_time_indi_comoro)
        print("Kerguelen: ", dt_time_indi_kerguelen)
        print("Mahe: ", dt_time_indi_mahe)
        print("Maldives: ", dt_time_indi_maldives)
        print("Mauritius: ", dt_time_indi_mauritius)
        print("Mayotte: ", dt_time_indi_mayotte)
        print("Reunion: ", dt_time_indi_reunion)
        print()

    elif caseinsensetiveselection == "chi":
        print("CHINA'S TIMEZONE")
        print("China: ",dt_time_chi_gmt8)
        print()

    elif caseinsensetiveselection == "sa":
        print("SOUTH AFRICA TIMEZONE")
        print("South Africa: ", dt_time_sa_gmt2)
        print()

    else:
        print("Sorry I couldn't understand your selection will you try again.")
