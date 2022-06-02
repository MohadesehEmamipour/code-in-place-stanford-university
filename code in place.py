import csv 

from participant import Participant
from section import Section

SECTION_DATA = "sections.csv"
STUDENT_DATA = "students.csv"

def create_sections():
    section_data = {} # keys are section numbers, values are corresponding sections

    with open(SECTION_DATA) as f:
        reader = csv.DictReader(f)

        for line in reader:
            section_number = int(line['section_number'])
            sl_name = line['sl_name']
            sl_email = line['sl_email']
            ohyay_link = line['ohyay_link']

            section_leader = Participant(sl_name, sl_email, "section leader")
            section = Section(section_number, section_leader, ohyay_link)

            section_data[section_number] = section

    return section_data
            
def assign_students(section_data):
    with open(STUDENT_DATA) as f:
        reader = csv.DictReader(f)

        for line in reader:
            student_name = line['name']
            student_email = line['email']
            section_number = int(line['section_number'])

            new_student = Participant(student_name, student_email, "student")

            section_for_student = section_data[section_number]
            section_for_student.add_student(new_student)

def main():
    section_data = create_sections()
    assign_students(section_data)

    for section_number in section_data:
        section = section_data[section_number]
        print("Section number: " + str(section.section_number))
        print("Section leader: " + section.section_leader.name)
        print("Section link: " + section.ohyay_link)
        print("Students: " + str(section.get_student_names()))

if __name__ == "__main__":
    main()
