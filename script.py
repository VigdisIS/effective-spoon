from meeting_agenda import create_meeting_agenda
from gmail import send_email


def getReferent():
    file = open("referenter.txt", "r")

    lines = file.readlines()
    referent = lines[0].strip("\n")
    print(referent)
    file.close()

    file_re = open("referenter.txt", "w")
    for line in lines:
        if line.strip("\n") != referent:
            file_re.write(line)
    file_re.close()
    return referent


referent = getReferent()

ref, motelenke, meeting_date = create_meeting_agenda(referent)

print(f"Referent: {ref} \nMøtelenke: {motelenke} \nMøtedato: {meeting_date}")

print("\n")

print("Sending email..")

print("\n")

send_email(ref, motelenke, meeting_date)
