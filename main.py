from bs4 import BeautifulSoup

data = {}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z']

course_list = {
    "15250": "Mathematics Extension 1",
    "15220": "Legal Studies",
    "15350": "Society and Culture",
    "15380": "Studies of Religion II",
    "15370": "Studies of Religion I",
    "15290": "Music 1",
    "15236": "Mathematics Standard 2",
    "15030": "Biology",
    "15255": "Mathematics Advanced",
    "15140": "English Advanced",
    "15050": "Chemistry",
    "15330": "Physics",
    "15270": "Modern History",
    "15320": "Personal Development, Health and Physical Education",
    "15260": "Mathematics Extension 2",
    "15255": "Mathematics Advanced",
    "15400": "Visual Arts",
    "15040": "Business Studies",
    "15210": "Information Processes and Technology",
    "15080": "Design and Technology",
    "15190": "Geography",
    "15090": "Drama",
    "15360": "Software Design and Development",
    "15160": "English Extension 1",
    "15110": "Economics",
    "15200": "Industrial Technology",
    "15800": "Italian Continuers",
    "15810": "Italian Extension",
    "26299": "Construction Examination",
    "15120": "Engineering Studies",
    "15790": "Italian Beginners",
    "27379": "Information and Digital Technology Examination",
}

def iter(suffix):
    
    global data

    with open(f"./nesa-band6/{suffix}.html", encoding="utf8", errors='ignore') as f:
        soup = BeautifulSoup(f, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        # {school: {course: [people]}}
        name, school, course = cols
        
        # Split course into list here
        # courses = ["XXXX", "XXXX"]
        temp = course.split(" ")
        courses = []
        for ele in temp:
            try:
                int(ele)
                if len(ele) == 5:
                    courses.append(ele)
            except (TypeError, ValueError) as e:
                continue

        if school not in data:
            data[school] = {}
        for course in courses:
                if course not in data[school]:
                    data[school][course] = [name]
                else:
                    data[school][course].append(name)

for i in alphabet:
    iter(i)

f = open('out.txt', 'w')
for school in data:
    f.write(f"{school}\n")
    for course in data[school]:
        if course in course_list:
            f.write(f"\t {course_list[course]}\n")
        else:
            f.write(f"\t {course}\n")
        for student in data[school][course]:
            f.write(f"\t\t {student}\n")
f.close()