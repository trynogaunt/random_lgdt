import random
member_list = []

def add_list_random(loop_number:int, p_member_list:list):
    for i in range(loop_number):
        member = input("Nom du participant: ")
        p_member_list.append(member)


member_list = []
list_lenght = input("Combien de participants ?")
add_list_random(int(list_lenght), member_list)

last_input = input("Appuyez sur entrée pour lancer le tirage")
print(f"Le gagnant est {random.choice(member_list)}")

