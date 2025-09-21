string_1 = "Aello world addy Oother Aucker"

rf = [i for i in string_1.lower().split() if i[0] == 'a']

print(rf)