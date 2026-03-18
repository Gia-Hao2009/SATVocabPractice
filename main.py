import os
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#1. kết nối ggsheet (chain reaction)
scope= ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds= ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope) #key
client = gspread.authorize(creds)
sheet= client.open("SAT_Vocab-Hao").sheet1


#2.fetch data
all_data = sheet.get_all_records()
data_limit = all_data[:800]


#3.random
random_vocab_list = random.sample(data_limit,5)
def clear():
    os.system('cls')

#4. main
while True: #big loop
    while True:
    # -- first layer
        #def info
        for i, definition in enumerate(random_vocab_list, 1):
            words = definition.get('Words', '-bug-')
            ipa = definition.get('IPA', '-bug-')
            type = definition.get('Type', '-bug-')
            vie = definition.get('Vie-meaning', '-bug-')
            synonym =  definition.get('Synonym', '-bug-')
            def1 = definition.get('Definition 1', '-bug-')
            def2 = definition.get('Definition 2', '-----')

            #print
            print(f"Từ {i}. {words}:")
            print(f"IPA: {ipa} ")
            print(f"Type: {type} ")
            print(f"Vie-meaning: {vie} ")
            print(f"Synonym: {synonym} ")
            print(f"Definition 1: {def1} ")
            print(f"Definition 2(if): {def2} \n")
    # -- second layer
        a = input("Bạn có muốn đi tiếp không Y/N: ")
        if a.upper() == "Y":
            for i, definition in enumerate(random_vocab_list, 1):
                words = definition.get('Words', '-bug-')
                print(f"{i}. {words}\n\n")
        
        b = input("Quay lại: (B or esc): ")
        if b.upper() == "B":
            break
        elif b.upper() == "ESC":
            exit()
        else:
            continue

