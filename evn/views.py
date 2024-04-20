import re
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import timedelta
import random
import pandas as pd
from datetime import datetime
from datetime import datetime
def index(request):
    return render(request, 'index.html')

def submit_selection(request):
    global selected_value
    if request.method == 'POST':
        selected_value = request.POST.get('selection')
        print(selected_value)
        return render(request, 'home.html')
    else:
        return render(request, 'index.html')


def members(request):
    return render(request, 'home.html')


def date_gen(num, start_date, end_date):
    ## Generationg the date of call records
    p = 0
    date_list = []
    start_date = datetime.strftime(datetime.strptime(start_date, "%Y-%m-%d"), "%d-%b-%y")
    end_date = datetime.strftime(datetime.strptime(end_date, "%Y-%m-%d"), "%d-%b-%y")

    start_date = datetime.strptime(start_date, "%d-%b-%y")
    end_date = datetime.strptime(end_date, "%d-%b-%y")

    delta = end_date - start_date

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        repeat = rm.choice([1, 2, 3], p=[0.7, 0.15, 0.15])
        for j in range(repeat):
            if (p >= num):
                return date_list
            # l = date.strftime('%d-%b-%y')
            l = date
            date_list.append(l)
            p += 1

    return [date_list]


def dob_gen(category, date):
    formatted_date = datetime.strptime(date, '%d-%b-%y')

    if category == 'individual':
        age = random.randrange(16, 27)
        dob = formatted_date - timedelta(days=age * 365)
        dob = dob - timedelta(days=random.randrange(20, 50))

    elif category == 'father':
        age = random.randrange(50, 55)
        dob = formatted_date - timedelta(days=age * 365)
        dob = dob - timedelta(days=random.randrange(20, 50))
    elif category == 'spouse':
        age = random.randrange(14, 23)
        dob = formatted_date - timedelta(days=age * 365)
        dob = dob - timedelta(days=random.randrange(20, 50))

    return [age, dob.strftime('%d-%b-%y')]


def report_date_gen(num, date_list):
    report_date_list = []
    for i in range(len(date_list)):
        add = random.choice([0, 1, 2, 3])
        dt = date_list[i] + timedelta(days=add)
        report_date_list.append(dt)
    return report_date_list


def event_description1(n):
    df = pd.read_csv('evn/templates/lat_long_details.csv')
    time = time_gen(n)
    date = dates_gen(n)
    names = name_gen(n + 3)
    name, father_name = names[0], names[1]
    loc = []
    lat = []
    long = []
    for i in location_gen(n):
        loc.append(df.details[i])
        lat.append(str(df.lat[i]) + 'N')
        long.append(str(df.lng[i]) + 'E')
    return [lat, long, loc, name, father_name, date, time]


def generate_reference_ids(n):
    reference_ids = []

    for _ in range(n):
        prefix = random.choice(["I", "U"])
        random_number = random.randint(1000000, 9999999)
        reference_id = f"{prefix}:{random_number}"
        reference_ids.append(reference_id)

    return reference_ids


def description(num):
    path = 'evn/templates/output (1).csv'
    count = 0
    data = pd.read_csv(path)
    description = []
    catogorie = []
    sub_catogorie = []
    event_name = []
    area = []
    source_agency = []
    associated_org = []
    Action_Taken = []
    Grading = []
    country = []
    Location = []
    l = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', 'Actual',
         'other']
    datav = event_description1(num)
    # print('datav', datav, flush= True)
    lat = datav[0]
    long = datav[1]
    loc = datav[2]
    Address = []
    District = []
    state = []
    Events = [
        'CEASEFIRE VIOLA110N 1B', 'CEASEFIRE VIOlATION LC', 'CYBER ATTACK', 'CYBER ATTACK/CRIME', 'CYBER CRIME/ ATTACK',
        'CYBER CRIME/ ATTACK', 'Planning to Attack Kuki', 'BANDH/SHUTDOWN/STRIKE/BLOCKADE', 'CIVIL UNREST J K', 'CLASH',
        'HATE SPEECH', 'LYNCHING', 'Planning to Attack Kuki', 'PROTEST', 'STONE PELTING DURING PROTEST', 'AIR STRIKES',
        'APPREHENSION TRT/ INSUR/CADRES', 'APPREHENSION TRT/INSUR/CADRES', 'EXCHANGE OF FIRE BETN SF AND TRTS/ INSUR',
        'EXCHANGE OF FIRE BETN SF AND TRTS/INSUR', 'FIRING INCIDENT/ENCOUNTER', 'REC OF ARMS/AMN/EXPLOSIVES/IED',
        'SEARCH OP/CASO', 'SF OPS', 'SURRENDER', 'APPREHENSION LEADERS', 'APPREHENSION TRT/INSUR/CADRES',
        'APPREHENSION WEAPONS', 'ARREST', 'COMN WITH SF', 'COMN WITH SF', 'COUNTER INT OPS', 'COUNTER INT OPS',
        'DETENTION',
        'DETENTION', 'FIRING INCIDENT/ENCOUNTER', 'REC OF ARMS/ AMN/EXPLOSIVES/IED', 'MORTAL/ARTY ATTACK',
        'ATTACK ON CHURCH',
        'ATTACK ON CHRISTIANS', 'ATTACK ON GURUDWARA', 'ATTACK ON HINDUS', 'ATTACK ON MOSQUE', 'ATTACK ON SHIAS',
        'ATTACK ON SIKHS', 'ATTACK ON TEMPLES', 'ATTACKS ON RELIGIOUS LEADERS', 'ATTACKS ON SUNNIS',
        'ATTACKS ON HOUSES',
        'IED ATTACK', 'INCIDENT RELATED TO TRT ORG', 'INTER FACTIONAL CLASH', 'MOV OF CADRES',
        'ATTACK ON CISF PERS/INFRA',
        'ATTACK ON SF', 'Intelligence Dispute Between Two Villages', 'ACTIVITIES OF CADRES', 'Ambush',
        'APHC Protest Programme Intelligence', 'Appointment Intelligence', 'Apprehension/Information Intelligence',
        'ATTACK ON CIVILIANS', 'ATTACK UNSUCCESSFUL', 'Attempt to Release Arrested Cadre', 'BASIC MILITARY TRG',
        'BOMB BLAST',
        'BOMB BLAST Intelligence', 'Cross Border Activities', 'DEFECTION LIKELY', 'DIRECTIVE',
        'DISPOSAL OF MEMORY CARD',
        'DISPOSAL OF MONEY', 'EST OF NEW TRT GP', 'EST OF NEW TRT GP Intelligence', 'EXTORTION CONFIRMED',
        'Formation of LIMGUARD',
        'Formation of New Camp', 'HARASSMENT', 'IFC', 'INCIDENT RELATED TO TRT ORG', 'Infilt', 'JOINING OF NEW CADRES',
        'Khalistani Propognda Intelligence', 'KIDNAPPING', 'LOC OF OGW', 'LOC OF TRTs', 'MEETINGS',
        'Meitei Wearing Army Uniform to Attack Kukis', 'Mov of Trts', 'OTHER TRT RELATED ACTIVITIES',
        'Pak Frequency Tracking Vehicle', 'Passing Out Parade Intelligence', 'Planning to Attack',
        'Planning to Attack Meties',
        'Planning to Kill', 'Planning to Target', 'Plastic Explosives', 'PROCUREMENT', 'PROCUREMENT OF ARMS AMN LIKELY',
        'PROCUREMENT OF SIM', 'Proliferation of looted Arms', 'Providing Logistic Support', 'Provision of Ammunition',
        'REC OF ARMS/AMN/EXPLOSIVES', 'RECRUITMENT PLANNING', 'RELEASED', 'REQMT OF CADRES', 'REQMT OF FUNDS',
        'REQMT OF LOGISTICS', 'RESTRUCTURE OF TRT ORG', 'RETALIATION', 'Shortage of Arms/Ammunitions',
        'Smuggling of Firearms/Explosives', 'SMUGGLING OF ILIICIT WEAPONS', 'Social Media Post Intelligence',
        'SURRENDER LIKELY', 'Terror Activity', 'TERROR STRIKES', 'Threat Advisory', 'TRF OF CADRES',
        'TRF OF CADRES LIKELY',
        'TRF OF EQPT', 'TRF OF FUNDS', 'TRF OF OGW', 'Attack', 'ATTACK ON CIVILIANS', 'BLAST', 'CAMPING OF CADRES',
        'CHARGE OF HIGHER COMD', 'DEFECTION', 'DESERTION', 'DiSPOSAL OF EQPT', 'DISSENT', 'ESCAPE', 'EXFILT',
        'EXTORTION',
        'INNOVATION TACTICS', 'JOINT ACTION', 'KILLING', 'LIKELY ATTACK', 'Likely BAT Attack/ Infiltration',
        'Likely to Attack',
        'LOC CAMP OFFICE HIDEOUT CACHE', 'LOC OF CADRES', 'LOC OF LDRS', 'LOC OF SUSPECT', 'LOGISTICS',
        'MORALE OF CADRES',
        'NEXUS', 'Planning to Attack', 'Planning to Attack/Rally', 'PROCUREMENT OF EQPT', 'RECRUITMENT', 'TRG',
        'Likely BAT Attack/ Infiltration', '44th Republic Day Celebration', 'ABDUCTION', 'ACTIVITIES',
        'Arrest Of PLA Cadre',
        'BLOCKADE/COUNTER BLOCKADE', 'BUDGET SESSION', 'Checking Aadhaar Cards', 'Consignment of Arms/Arnn and Hand',
        'Construction of New Camp', 'DEMAND FOR SEPARATE STATE', 'DEMAND OF ARMS/AMN',
        'Directed Non-Manipuris to Vacate the places',
        'Disrupt the visit of PM India', 'Est of New Camp', 'Exchange of Currency', 'G-20 Summit', 'Grenade',
        'Gun fight between NSCN/IM and ZUF', 'Internal Dispute', 'INTERNAL ISSUES', 'Likely lnfift',
        'Likely Target Meitei Villages',
        'LOC OF KNA AND JAFHS CADRES', 'MOBILIZ PUBLIC SUPPORT', 'MOV OF OGWs', 'MOVEMENT',
        'Movement of Suspected Persons',
        'Penalty Imposed', 'Plan to oppose the visit of Sh Rahul Gandhi', 'PLANNING TO AMBUSH',
        'Planning to Disrupt PMs Visit to USA',
        'PRESENCE OF CADRES', 'PRESS RELEASE', 'PROMOTIONS', 'RAISING DAY', 'SUSPICIOUS ACTIVITES', 'Threatening',
        'Torching/ Burning of Houses', 'TRANSPORTATION OFARMS/AMN', 'Youth Willing to Join', 'ATTACKS ON EDUCATIONAL']

    Township = []
    action = ['Armed Assault', 'Bombing/Explosion', 'Assassination', 'Hostage Taking (Kidnapping)', 'Hijacking']
    for j in range(0, num):
        splited = loc[j].split(',')
        # print('splitted', splited, flush=True)
        District.append((splited[-4])[1:].strip("'"))
        state.append((splited[-3])[1:].strip("'"))
        Township.append((splited[0])[2:].strip("'"))
    # print(state)
    EVENT_DESCRIPTION = event_description(num)
    for i in range(num):
        description.append(random.choice(EVENT_DESCRIPTION))
        catogorie.append(random.choice(['Intelligence','Threat','Thuraya Activites']))
        sub_catogorie.append(random.choice(data.SubCategory))
        event_name.append(random.choice(Events))
        area.append(random.choice(['ROI', 'Nort East']))
        source_agency.append(random.choice(data.SourceAgency))
        associated_org.append(random.choice(data.AssociatedOrg))
        Grading.append(random.choice(l))
        country.append('India')
        Location.append(random.choice(['Address', 'Incident Site', 'Area of Operation']))
        Address.append(random.choice(['Bulding 21', '56/c', '65A/c/1']))
        Action_Taken.append(random.choice(action))

    reference = generate_reference_ids(num)

    return [description, catogorie, sub_catogorie, event_name, area, source_agency, associated_org, Action_Taken,
            Grading, lat, long, country, Location, state, District, Township, Address, reference]


import random


def generate_description(n):
    colors = ["Black", "Blue", "Green", "Red", "Yellow"]
    clothing = ["T-shirt and Jeans", "Gray Suit", "Traditional Sari", "Casual Shorts and T-shirt",
                "Formal Business Attire"]
    headwear = ["Baseball Cap", "Fedora Hat", "Sun Hat", "Headscarf", "Cowboy Hat"]
    descriptions = []
    l = [1, 2, 3, 4, 5, 6, 10, 17, 16, 15]
    for _ in range(n):
        p = random.choice(l)
        if p % 2 == 0:  # Randomly decide whether to start with "He"
            description = (
                f"He was carrying a {random.choice(colors)} colored Shoulder Bag and wearing a "
                f"{random.choice(colors)} coloured {random.choice(clothing)} and a {random.choice(headwear)}."
            )
        elif p % 3 == 0:
            description = (
                f"A {random.choice(colors)} colored Backpack and was dressed in a "
                f"{random.choice(colors)} {random.choice(clothing)} with a {random.choice(headwear)}."
            )
        else:
            description = (
                f"{random.choice(colors)} {random.choice(clothing)} with a {random.choice(headwear)}."
            )
        descriptions.append(description)

    return descriptions


from numpy import random as rm


def individual(num):
    Type = []
    salutation = []
    religion = []
    first = []
    last = []
    dob = []
    Age = []
    cast = []
    description = []
    nationality = []
    orgname = []
    associationdate = []
    address = []
    country = []
    lat = []
    long = []
    District = []
    state = []
    Township = []
    Note = []
    datav = event_description1(num)
    # lat = datav[0]
    # long = datav[1]
    loc = datav[2]
    muslim_first_names = [
    "Mohammed", "Ali", "Omar", "Ahmed", "Youssef", "Abdullah", "Ibrahim", "Adam", "Mustafa", "Yasin",
    "Hassan", "Hussein", "Khalid", "Yousef", "Anas", "Amir", "Bilal", "Tariq", "Jamil", "Karim",
    "Zaid", "Musa", "Omar", "Zakariya", "Sami", "Fahad", "Rashid", "Hadi", "Taha", "Rayan",
    "Nasir", "Ismail", "Hamza", "Saeed", "Imran", "Rami", "Majid", "Ziyad", "Rahim", "Ridwan",
    "Zain", "Faris", "Riyad", "Nabil", "Yahya", "Idris", "Amin", "Rafiq", "Salman", "Ayaan",
    "Talha", "Faisal", "Hadi", "Samir", "Nizar", "Zohaib", "Mujahid", "Ilyas", "Asad", "Naeem",
    "Jafar", "Arif", "Najib", "Wasim", "Usman", "Aziz", "Waleed", "Jawad", "Saif", "Usama",
    "Aariz", "Fawaz", "Yaseen", "Sulaiman", "Aasim", "Ayman", "Hassan", "Bashir", "Qasim", "Nadeem",
    "Yunus", "Arman", "Aayan", "Taimur", "Tahir", "Wahid", "Azhar", "Arafat", "Raheem", "Arman",
    "Imad", "Haroon", "Shakir", "Jamal", "Subhan", "Hanan", "Luqman", "Razi", "Shayan", "Waqas",
    "Arham", "Subhan", "Sufyan", "Tabish", "Talib", "Shoaib", "Tanveer", "Zakir", "Adil", "Wajid",
    "Yusuf", "Zayan", "Zeeshan", "Ayaan", "Jibran", "Laith", "Rayyan", "Subhan", "Zubair", "Adnan",
    "Aqeel", "Arslan", "Azaan", "Burhan", "Danish", "Fahim", "Farhan", "Hakim", "Kareem", "Khizar",
    "Mujtaba", "Noman", "Qaiser", "Rameez", "Raqib", "Sabir", "Sahil", "Saqlain", "Sikandar", "Umar",
    "Wasiq", "Yaqub", "Zahid", "Zakaria", "Zia", "Zohaib", "Aamir", "Abdul", "Ahmad", "Ahsan",
    "Akram", "Amjad", "Anwar", "Asim", "Atif", "Azam", "Azim", "Babar", "Fazal", "Ghulam",
    "Haris", "Hassan", "Inayat", "Irshad", "Ismat", "Javed", "Junaid", "Kamran", "Khaldun", "Khalil",
    "Khurram", "Majid", "Moin", "Mudassir", "Mujahid", "Mukhtar", "Nadir", "Naeem", "Najib", "Nasir",
    "Qadir", "Rafiq", "Raheel", "Rashad", "Rashid", "Rehan", "Riaz", "Sajid", "Salah", "Sami",
    "Saqib", "Sarwar", "Shakir", "Taher", "Talib", "Talha", "Tariq", "Usman", "Wahid", "Wasim",
    "Yasin", "Zaheer", "Zakir", "Zaman", "Zia", "Zubair"
    ]
    muslim_last_names = [
    "Ali", "Khan", "Hussain", "Ahmed", "Mohammad", "Abdullah", "Ibrahim", "Hassan", "Hussein", "Malik",
    "Saleh", "Farooq", "Rahman", "Karim", "Siddiqui", "Raza", "Qureshi", "Amin", "Mansoor", "Saeed",
    "Shah", "Noor", "Zaman", "Yusuf", "Baig", "Chaudhry", "Haque", "Abbasi", "Sultan", "Akhtar",
    "Mahmood", "Arif", "Rashid", "Aziz", "Rehman", "Aslam", "Ashraf", "Awan", "Afzal", "Bukhari",
    "Nawaz", "Durrani", "Asif", "Khattak", "Haider", "Iqbal", "Jan", "Malik", "Nasir", "Rehman",
    "Riaz", "Sabir", "Tariq", "Warsi", "Zaidi", "Zia", "Zulfiqar", "Kazmi", "Shahid", "Asghar",
    "Bhatti", "Khan", "Rana", "Chowdhury", "Ghani", "Hamid", "Shafi", "Arshad", "Khalid", "Imran",
    "Sharif", "Afridi", "Butt", "Zafar", "Qadir", "Aslam", "Sher", "Rauf", "Memon", "Babar",
    "Nadeem", "Haque", "Khawaja", "Sheikh", "Tanveer", "Javed", "Shahzad", "Ashraf", "Mughal", "Bajwa",
    "Kareem", "Khokhar", "Qadri", "Qazi", "Zubair", "Lone", "Latif", "Sadiq", "Waseem", "Hayat",
    "Nisar", "Bashir", "Arshad", "Mustafa", "Bilal", "Nazir", "Masood", "Parvez", "Noman", "Hameed",
    "Babar", "Awan", "Shahbaz", "Akram", "Amin", "Ashraf", "Aslam", "Bilal", "Farid", "Gulzar", "Hameed",
    "Hanif", "Haque", "Haq", "Hussain", "Iqbal", "Israr", "Jamil", "Khalid", "Khan", "Mahmood",
    "Mehmood", "Mirza", "Mujahid", "Munir", "Nawaz", "Rafique", "Rashid", "Rehman", "Sadiq", "Sajid",
    "Saleem", "Sultan", "Tariq", "Zafar", "Zaidi", "Zaman", "Zia", "Zulfiqar", "Abbas", "Afridi",
    "Ahmed", "Ali", "Anwar", "Arshad", "Asif", "Babar", "Bashir", "Bhatti", "Butt", "Chaudhry",
    "Farooq", "Gul", "Hameed", "Hussain", "Iqbal", "Islam", "Javed", "Khan", "Malik", "Masood",
    "Mir", "Nawaz", "Rahman", "Rashid", "Rehman", "Saeed", "Sarwar", "Shah", "Shahid", "Sheikh",
    "Siddique", "Tariq", "Warsi", "Yaqoob", "Zaman", "Zia", "Zubair"
    ]
    l = ['21', '23', '25', '19', '20']
    c = ['Hindu', 'Muslim']
    org = ['Al-Qaeda', 'Islamic State (ISIS/ISIL)', 'Taliban', 'Boko Haram', 'Hezbollah']
    apper = generate_description(10)
    for i in range(num):
        splited = loc[i].split(',')
        if i % 5 == 0:
            Type.extend(['Individual', 'Father'])
            description.append(random.choice(apper))
            Note.append(random.choice(apper))
            Note.append(random.choice(apper))
            description.append(None)
            l = datav[0][i]
            lat.extend([l, l])
            lo = datav[0][i]
            long.extend([lo, lo])
            p = (splited[-4])[1:].strip("'")
            District.extend([p, p])
            t = (splited[-3])[1:].strip("'")
            state.extend([t, t])
            f = (splited[0])[2:].strip("'")
            Township.extend([f, f])
            country.extend(['India', 'India'])
            first.extend([random.choice(muslim_first_names), random.choice(muslim_first_names)])
            last.extend([random.choice(muslim_last_names), random.choice(muslim_last_names)])
            address.extend(
                [random.choice(['Building 21', '56/c', '65A/c/1']), random.choice(['Building 21', '56/c', '65A/c/1'])])

            ca = random.choice(c)
            cast.extend([ca, ca])
            present_date = datetime.now()
            formatted_date = present_date.strftime('%d-%b-%y')
            d = dob_gen('individual', formatted_date)
            dob.append(d[1])
            Age.append(d[0])
            d = dob_gen('father', formatted_date)
            dob.append(d[1])
            if (i % 2 == 0):
                orgname.extend([None, None])
            else:
                orgname.extend([random.choice(org), random.choice(org)])
            Age.append(d[0])
            m = rm.choice(['Hindu', 'muslim', 'skihs'], p=[0.05, 0.8, 0.15])
            n = random.choice(['Indian', 'Pakistan'])
            religion.extend([m, m])
            nationality.extend([n, n])
            i += 1
        else:
            if (Type[i - 1] == 'Individual' and i % 3 == 0):
                Type.append('Spouse')
                present_date = datetime.now()
                formatted_date = present_date.strftime('%d-%b-%y')
                d = dob_gen('spouse', formatted_date)
                dob.append(d[1])
                Age.append(d[0])

            elif (Type[i - 1] == 'Father' and i % 6 == 0):
                Type.append('Spouse')
                present_date = datetime.now()
                formatted_date = present_date.strftime('%d-%b-%y')
                d = dob_gen('spouse', formatted_date)
                dob.append(d[1])
                Age.append(d[0])

            else:
                Type.append('Individual')
                present_date = datetime.now()
                formatted_date = present_date.strftime('%d-%b-%y')
                d = dob_gen('individual', formatted_date)  # Use 'individual' instead of 'Individual'
                dob.append(d[1])
                Age.append(d[0])
            Note.append(random.choice(apper))
            description.append(random.choice(apper))
            first.append(random.choice(muslim_first_names))
            last.append(random.choice(muslim_last_names))
            District.append((splited[-4])[1:].strip("'"))
            state.append((splited[-3])[1:].strip("'"))
            Township.append((splited[0])[2:].strip("'"))
            country.append('India')
            cast.append(random.choice(c))
            address.append(random.choice(['Building 21', '56/c', '65A/c/1']))
            nationality.append(random.choice(['India', 'Pakistan']))
            orgname.append(random.choice(org))
            religion.append(rm.choice(['Hindu', 'muslim', 'skihs'], p=[0.05, 0.8, 0.15]))
            lat.append(datav[0][i])
            long.append(datav[1][i])

    l = name_gen(num)
    Alis = l[0]
    salutation = [None] * num
    associationdate = date_gen(num, startDate, EndDate)

    return [Type[:num], salutation[:num], first[:num], last[:num], dob[:num], Age[:num], cast[:num], Alis[:num],
            description[:num],
            nationality[:num], address[:num], country[:num], state[:num], District[:num], Township[:num], lat[:num],
            long[:num],
            orgname[:num], associationdate[:num], Note[:num], religion[:num]]


import numpy as np
from django.http import HttpResponse
import csv
import datetime
from datetime import timedelta
from datetime import datetime, timedelta
import random
import pandas as pd


def time_gen(num):
    time = datetime.now()
    i = 0
    time_li = []
    while i < num:
        i += 1
        time_change = timedelta(minutes=random.randint(50, 400))
        time += time_change
        time_li.append(time.strftime("%H:%M:%S"))

    return time_li


def dates_gen(num):
    ## Generationg the date of call records
    p = 0
    date_list = []
    start_date = datetime.strptime('25-Jan-19', '%d-%b-%y')
    end_date = datetime.strptime('8-May-65', '%d-%b-%y')
    delta = end_date - start_date

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        repeat = random.randint(5, 8)
        for j in range(repeat):
            if (p >= num):
                return date_list
            l = date.strftime('%d-%b-%y')
            date_list.append(l)
            p += 1

    return [date_list]


def name_gen(n):
    name = []
    father_names = []
    first_names = [
    "Mohammed", "Ali", "Omar", "Ahmed", "Youssef", "Abdullah", "Ibrahim", "Adam", "Mustafa", "Yasin",
    "Hassan", "Hussein", "Khalid", "Yousef", "Anas", "Amir", "Bilal", "Tariq", "Jamil", "Karim",
    "Zaid", "Musa", "Omar", "Zakariya", "Sami", "Fahad", "Rashid", "Hadi", "Taha", "Rayan",
    "Nasir", "Ismail", "Hamza", "Saeed", "Imran", "Rami", "Majid", "Ziyad", "Rahim", "Ridwan",
    "Zain", "Faris", "Riyad", "Nabil", "Yahya", "Idris", "Amin", "Rafiq", "Salman", "Ayaan",
    "Talha", "Faisal", "Hadi", "Samir", "Nizar", "Zohaib", "Mujahid", "Ilyas", "Asad", "Naeem",
    "Jafar", "Arif", "Najib", "Wasim", "Usman", "Aziz", "Waleed", "Jawad", "Saif", "Usama",
    "Aariz", "Fawaz", "Yaseen", "Sulaiman", "Aasim", "Ayman", "Hassan", "Bashir", "Qasim", "Nadeem",
    "Yunus", "Arman", "Aayan", "Taimur", "Tahir", "Wahid", "Azhar", "Arafat", "Raheem", "Arman",
    "Imad", "Haroon", "Shakir", "Jamal", "Subhan", "Hanan", "Luqman", "Razi", "Shayan", "Waqas",
    "Arham", "Subhan", "Sufyan", "Tabish", "Talib", "Shoaib", "Tanveer", "Zakir", "Adil", "Wajid",
    "Yusuf", "Zayan", "Zeeshan", "Ayaan", "Jibran", "Laith", "Rayyan", "Subhan", "Zubair", "Adnan",
    "Aqeel", "Arslan", "Azaan", "Burhan", "Danish", "Fahim", "Farhan", "Hakim", "Kareem", "Khizar",
    "Mujtaba", "Noman", "Qaiser", "Rameez", "Raqib", "Sabir", "Sahil", "Saqlain", "Sikandar", "Umar",
    "Wasiq", "Yaqub", "Zahid", "Zakaria", "Zia", "Zohaib", "Aamir", "Abdul", "Ahmad", "Ahsan",
    "Akram", "Amjad", "Anwar", "Asim", "Atif", "Azam", "Azim", "Babar", "Fazal", "Ghulam",
    "Haris", "Hassan", "Inayat", "Irshad", "Ismat", "Javed", "Junaid", "Kamran", "Khaldun", "Khalil",
    "Khurram", "Majid", "Moin", "Mudassir", "Mujahid", "Mukhtar", "Nadir", "Naeem", "Najib", "Nasir",
    "Qadir", "Rafiq", "Raheel", "Rashad", "Rashid", "Rehan", "Riaz", "Sajid", "Salah", "Sami",
    "Saqib", "Sarwar", "Shakir", "Taher", "Talib", "Talha", "Tariq", "Usman", "Wahid", "Wasim",
    "Yasin", "Zaheer", "Zakir", "Zaman", "Zia", "Zubair"
    ]
    last_names = [
    "Ali", "Khan", "Hussain", "Ahmed", "Mohammad", "Abdullah", "Ibrahim", "Hassan", "Hussein", "Malik",
    "Saleh", "Farooq", "Rahman", "Karim", "Siddiqui", "Raza", "Qureshi", "Amin", "Mansoor", "Saeed",
    "Shah", "Noor", "Zaman", "Yusuf", "Baig", "Chaudhry", "Haque", "Abbasi", "Sultan", "Akhtar",
    "Mahmood", "Arif", "Rashid", "Aziz", "Rehman", "Aslam", "Ashraf", "Awan", "Afzal", "Bukhari",
    "Nawaz", "Durrani", "Asif", "Khattak", "Haider", "Iqbal", "Jan", "Malik", "Nasir", "Rehman",
    "Riaz", "Sabir", "Tariq", "Warsi", "Zaidi", "Zia", "Zulfiqar", "Kazmi", "Shahid", "Asghar",
    "Bhatti", "Khan", "Rana", "Chowdhury", "Ghani", "Hamid", "Shafi", "Arshad", "Khalid", "Imran",
    "Sharif", "Afridi", "Butt", "Zafar", "Qadir", "Aslam", "Sher", "Rauf", "Memon", "Babar",
    "Nadeem", "Haque", "Khawaja", "Sheikh", "Tanveer", "Javed", "Shahzad", "Ashraf", "Mughal", "Bajwa",
    "Kareem", "Khokhar", "Qadri", "Qazi", "Zubair", "Lone", "Latif", "Sadiq", "Waseem", "Hayat",
    "Nisar", "Bashir", "Arshad", "Mustafa", "Bilal", "Nazir", "Masood", "Parvez", "Noman", "Hameed",
    "Babar", "Awan", "Shahbaz", "Akram", "Amin", "Ashraf", "Aslam", "Bilal", "Farid", "Gulzar", "Hameed",
    "Hanif", "Haque", "Haq", "Hussain", "Iqbal", "Israr", "Jamil", "Khalid", "Khan", "Mahmood",
    "Mehmood", "Mirza", "Mujahid", "Munir", "Nawaz", "Rafique", "Rashid", "Rehman", "Sadiq", "Sajid",
    "Saleem", "Sultan", "Tariq", "Zafar", "Zaidi", "Zaman", "Zia", "Zulfiqar", "Abbas", "Afridi",
    "Ahmed", "Ali", "Anwar", "Arshad", "Asif", "Babar", "Bashir", "Bhatti", "Butt", "Chaudhry",
    "Farooq", "Gul", "Hameed", "Hussain", "Iqbal", "Islam", "Javed", "Khan", "Malik", "Masood",
    "Mir", "Nawaz", "Rahman", "Rashid", "Rehman", "Saeed", "Sarwar", "Shah", "Shahid", "Sheikh",
    "Siddique", "Tariq", "Warsi", "Yaqoob", "Zaman", "Zia", "Zubair"
    ]
    for i in range(n):
        last_name=random.choice(last_names)
        name.append(random.choice(first_names)+" "+last_name)
        father_name = random.choice(first_names)
        while (name[-1] == father_name):
            father_name = random.choice(first_names)
        father_names.append(father_name+' '+last_name)
    return [name, father_names]


def location_gen(num):
    df = pd.read_csv('evn/templates/lat_long_details.csv')
    loc = []
    for i in range(num):
        loc.append(random.randrange(0, len(df)))
    return loc


def gen_phone(num):
    numbers_list = []

    while len(numbers_list) < num:
        number = ''.join(random.choice('6789'))
        for i in range(0, 9):
            number = number + random.choice('1234567890')
        numbers_list.append(number)

    return numbers_list


def event_description(n):
    df = pd.read_csv('evn/templates/lat_long_details.csv')
    time = time_gen(n)
    date = dates_gen(n)
    names = name_gen(n + 3)
    name, father_name = names[0], names[1]
    loc = []
    lat = []
    long = []
    for i in location_gen(n):
        loc.append(df.details[i])
        lat.append(str(df.lat[i]) + 'N')
        long.append(str(df.lng[i]) + 'E')

    phone_no = gen_phone(n + 3)
    description = []
    for i in range(0, n):
        s = random.choice(['a', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'])
        splited = loc[i].split(',')
        if s == 'a':
            description.append(
                f"There have been recent instances wherein unidentified missed calls originating from +92 numbers (Pakistan Numbers) were received by {name[i]}. Anas personnel  regully briefed as well as sensitized not to entertain such calls. However, the details of one such call received from +92 number is as below .Time  Date Receiving Place  Mobile No. Unidentified No {time[i]} As on {date[i]} {splited[-4]} {splited[-3]} +91{phone_no[i]}  ,+92{phone_no[i + 1]}")
        elif s == 'a1':
            description.append(
                f'Today {date[i]} at {time[i]} one Muslim youth (27/28 yrs), sporting a black jacket, Height 5.6 approximately, appering to be of {loc[i]} origin by facial built and mannerisms was spotted roaming in a Muslim locality, namely {splited[0]}. He was carrying a Black colored Shoulder Bag and wearing a white coloured Pathani Suit (Muslim Kurta/Payjama) and a Skull cap. He was found talking on his mobile to some unknown person using a mix of English, Urdu, Kashmir, and Punjabi languages. He spoke in Urdu language but with a Punjabi tone and slang. During the conversation he was heard informing the other end that he would now discontinue talking on the Mobile number in use and would again talk to him in about 30 minutes but using a new Mobile number. The said unknown Muslim youth who seemed to be suspicious was noticed loitering and talking on mobile in the area for about half an hour in the said locality. When the local Muslims of the area noted him they grew suspicious and confronted him and asked him about his identity, reason for his presence in the area. He took a flimsy plea and swiftly escaped from the area. Though the residents of the area tried to locate him but could not trace.  This incident seems to be sensitive in the backdrop of the recent india News regarding movement of terrorist/suspected elements Unito India from across the border. (Grading: A)')
        elif s == 'a2':
            description.append(
                f'A Thuraya entity (IMEI No : {9843509}) was found active at {lat[i]} , {long[i]} about 85.8 Kms NE of {date[i]} {splited[-4]}, {splited[-3]} on {date[i]} at {time[i]} (Gps Age : NA) Entity contacted telephone number {phone_no[i]}')
        elif s == 'a3':
            description.append(
                f'Communication between suspect {name[i]} (UID {90398}) from {date[i]} {splited[0]} (MT {lat[i]}, {long[i]}) and unidentified suspect on {date[i]} revealed that two HM terrorists were arrested by SF at {date[i]} {splited[-4]} (MT {lat[i]}, {long[i]}) on {date[i]}. Further, they were probably working with slain terrorist {name[i]}, who was killed on {date[i]}.(Grading: C2)')
        elif s == 'a4':
            description.append(
                f'The following activity of Thuraya terminal was observed near India Border  Between {time[i]} {date[i]} & {time[i]} on {date[i]}, a Thuraya terminal ({lat[i]}, {long[i]}) in {loc[i]}, about 46 Kms SW of Ali Bag Port, Maharashtra Border')
        elif s == 'a5':
            description.append(
                f'An {name[i]} s/o {father_name[i]}, r/o {splited[0]}, PS {date[i]} {splited[-4]},  provides shelter to a group of 4 terrorists who are active in {date[i]} {splited[-4]} area.')
        elif s == 'a6':
            description.append(
                f'Communication between suspect {name[i]} (UID {90398}) from {splited[0]} (MT {lat[i]}, {long[i]}) and suspect {name[i + 1]} on {date[i]} revealed that 2 terrorists were present in the house of {name[i + 2]} , s/o {father_name[i]} in{splited[0]}, on {date[i]}.\r\n(Grading: C2)')

    return description


def replace_with_nan(df: pd.DataFrame):
    if df.shape[0] > 1:
        df.iloc[1:, :11] = np.nan
    return df


def main(request):
    global startDate,EndDate
    if request.method == "POST":
        num = int(request.POST.get('num'))
        startDate = request.POST.get('startDate')
        EndDate = request.POST.get('endDate')
        Location= request.POST.get('location')
        category= request.POST.get('category')
        if selected_value == "event":
            event_dates = date_gen(num, startDate, EndDate)
            report_dates = report_date_gen(num, event_dates)
            others = description(num)
            dic = {
                'EVENT Date': event_dates,
                'REPORT Date': report_dates,
                'Reference': others[17],
                'CATEGORY': others[1],
                'EVENT SUB CATEGORY': others[2],
                'EVENT NAME': others[3],
                'EVENT DESCRIPTION': others[0],
                'AREA': others[4],
                'SOURCE/AGENCY': others[5],
                # 'ASSOCIATE ORG': others[6],
                'Action Taken': others[7],
                'Grading': others[8],
                'Location_Type': others[12],
                'Address': others[16],
                'Country': others[11],
                'State': others[13],
                'District': others[14],
                'Township': others[15],
                'Lat': others[9],
                'Long': others[10]
            }
            df = pd.DataFrame(dic)
            df = df.sort_values(['EVENT Date', 'REPORT Date'], axis=0, ascending=True, ignore_index=True)
            df['EVENT Date'] = df['EVENT Date'].apply(lambda x: x.strftime('%d/%m/%Y'))
            df['REPORT Date'] = df['REPORT Date'].apply(lambda x: x.strftime('%d/%m/%Y'))
            df['District'] = df['District'].apply(lambda x: re.sub(' +', ' ', x.replace('District', '').strip()))
            df = df.groupby('EVENT Date').apply(replace_with_nan)
            if Location!='ALL':
                df = df[df['State'].str.contains(Location, case=False, na=False)]
            if  category !='ALL':
                df = df[df['CATEGORY'].str.contains(category, case=False, na=False)]

        else:
            others = individual(num)
            dic = {
                'Type': others[0],
                'Salutation': others[1],
                'First Name': others[2],
                'Last Name': others[3],
                'DOB': others[4],
                'AGE': others[5],
                'Cast': others[6],
                'Alias': others[7],
                'description': others[8],
                'nationality': others[9],
                'religion': others[20],
                'Address': others[10],
                'Country': others[11],
                'State': others[12],
                'District': others[13],
                'Township': others[14],
                'Lat': others[15],
                'Long': others[16],
                'Org Name/Alias': others[17],
                'Association Date': others[18],
                'Note': others[19]
            }

            df = pd.DataFrame(dic)
            df['District'] = df['District'].apply(lambda x: re.sub(' +', ' ', x.replace('District', '').strip()))
        csv = df.to_csv(index=False)

        # Prepare response for CSV download
        response = HttpResponse(csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=data.csv'

        return response
    else:
        # Handle other HTTP methods, e.g., 'GET'
        return HttpResponse("This view only supports POST requests.")