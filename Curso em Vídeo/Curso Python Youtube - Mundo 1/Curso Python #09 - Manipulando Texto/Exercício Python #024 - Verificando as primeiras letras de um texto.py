# https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=34
# 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Em que cidade você nasceu? ')).strip()
print('Santo' in cidade[:5].title())
