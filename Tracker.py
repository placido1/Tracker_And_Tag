import pandas as pd


with open('testeTag.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

dados_com_classes_e_nomes = []

classes_validas = ["Xbow", "Frost", "Fire", "Raiz", "Caça-Espiritos", "Offtank", "Elevado","Silence", "Main Healer", "Bruxo", "Quebra Reinos", "Oculto", "Main Tank"]

def obter_classe_numerada(nome):
    while True:
        print(f"Escolha a classe correspondente para {nome}:")
        for i, classe in enumerate(classes_validas, start=1):
            print(f"{i}. {classe}")
        
        
        
        
        escolha = input("Digite o número da classe: ")
        
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(classes_validas):
                return classes_validas[escolha - 1]
        
        print("Opção inválida. Por favor, escolha uma opção válida.")

for linha in linhas:
    partes = linha.strip().split(':')
    if len(partes) > 1:
        nome = partes[0].strip()
        dano = float(partes[1].split('(')[0].replace(',', '').strip())  # Converter para int
        complemento = (linha.split('|')[1].replace(',', '.').strip())  # Converter para float usando ponto decimal
        
        
        
        
        
        verifica_print = input(nome+" tem print: ")
        if verifica_print == 's':
            
            classe = obter_classe_numerada(nome)    
            durabilidade = None
            while durabilidade is None:
                try:
                    durabilidade = int(input(f"Digite a durabilidade (0 a 100) para {nome}: "))
                    if 0 <= durabilidade <= 100:
                        break
                    else:
                        print("Valor fora do intervalo permitido (0 a 100).")
                except ValueError:
                    print("Digite um valor numérico válido.")

            dados_com_classes_e_nomes.append((nome, dano, classe, durabilidade))
        


df = pd.DataFrame(dados_com_classes_e_nomes, columns=['Nome', 'Dano', 'Classe', 'Durabilidade'])

df_teste = df

body = df_teste.values.tolist()


imprimir_tracker = []
classe_referencia = []
maior_dano = 0
fire_damage = []
caça_damage = []
xbow_damage = []
frost_damage = []
raiz_damage = []
bruxo_durabilidade = []
elevado_durabilidade = []
mainhealer_durabilidade = []
silence_durabilidade = []
offtank_durabilidade = []
maintank_durabilidade = []
quebraReinos_durabilidade = []
oculto_durabilidade = []
suporte_durabilidade = []
Scout_adicionado = []

if 'Raiz' in body[0]:
    classe_referencia = body[0]
    maior_dano = float(classe_referencia[1])
   
    for fire in body:
        if "Fire" in fire:
            
            if fire[1] >= 0.75 * maior_dano:
                if fire[3] >= 90:
                    fire_damage = [fire[0], fire[2], '+1']
                    imprimir_tracker.append(fire_damage)
                    print(fire_damage)
                elif fire[3] < 80:
                    fire_damage = [fire[0], fire[2], '-1']
                    imprimir_tracker.append(fire_damage)
                    print(fire_damage)
            elif fire[1] < 0.45* maior_dano:
                fire_damage = [fire[0], fire[2], '-1']
                imprimir_tracker.append(fire_damage)    
                print(fire_damage)
            elif fire[3] < 80:
                fire_damage = [fire[0], fire[2], '-1']
                imprimir_tracker.append(fire_damage)   
                print(fire_damage)  
    for frost in body:
        if "Frost" in frost:
            
            if frost[1] >= 0.75 * maior_dano:
                if frost[3] >= 90:
                    frost_damage = [frost[0], frost[2], '+1']
                    imprimir_tracker.append(frost_damage)
                    print(frost_damage)
                elif frost[3] < 80:
                    frost_damage = [frost[0], frost[2], '-1']
                    imprimir_tracker.append(frost_damage)
                    print(frost_damage)
            elif frost[1] < 0.45* maior_dano:
                    frost_damage = [frost[0], frost[2], '-1'] 
                    imprimir_tracker.append(frost_damage)   
                    print(frost_damage)
            elif frost[3] < 80:
                    frost_damage = [frost[0], frost[2], '-1'] 
                    imprimir_tracker.append(frost_damage)  
                    print(frost_damage)
    for xbow in body:
        if "Xbow" in xbow:
            
            if xbow[1] >= 0.80 * maior_dano:
                if xbow[3] >= 90:
                    xbow_damage = [xbow[0], xbow[2], '+1']
                    imprimir_tracker.append(xbow_damage)
                    print(xbow_damage)
                elif xbow[3] < 80:
                    xbow_damage = [xbow[0], xbow[2], '-1']
                    imprimir_tracker.append(xbow_damage)
                    print(xbow_damage)
            elif xbow[1] < 0.55* maior_dano:
                xbow_damage = [xbow[0], xbow[2], '-1'] 
                imprimir_tracker.append(xbow_damage)   
                print(xbow_damage)
            elif xbow[3] < 80:
                xbow_damage = [xbow[0], xbow[2], '-1'] 
                imprimir_tracker.append(xbow_damage)  
                print(xbow_damage)
    for raiz in body:
        if "Raiz" in raiz:
            
            if raiz[1] >= 0.80 * maior_dano:
                if raiz[3] >= 90:
                    raiz_damage = [raiz[0], raiz[2], '+1']
                    imprimir_tracker.append(raiz_damage)
                    print(raiz_damage)
                elif raiz[3] < 80:
                    raiz_damage = [raiz[0], raiz[2], '-1']
                    imprimir_tracker.append(raiz_damage)
                    print(raiz_damage)
            elif raiz[1] < 0.55* maior_dano:
                raiz_damage = [raiz[0], raiz[2], '-1']
                imprimir_tracker.append(raiz_damage)    
                print(raiz_damage)
            elif raiz[3] < 80:
                raiz_damage = [raiz[0], raiz[2], '-1']
                imprimir_tracker.append(raiz_damage)   
                print(raiz_damage)
    for caça in body:
        if "Caça-Espiritos" in caça:
            
            if caça[1] >= 0.45 * maior_dano:
                if caça[3] >= 90:
                    caça_damage = [caça[0], caça[2], '+1']
                    imprimir_tracker.append(caça_damage)
                    print(caça_damage)
                elif caça[3] < 80:
                    caça_damage = [caça[0], caça[2], '-1']
                    imprimir_tracker.append(caça_damage)
                    print(caça_damage)
            elif caça[1] < 0.30* maior_dano:
                caça_damage = [caça[0], caça[2], '-1']
                imprimir_tracker.append(caça_damage)    
                print(caça_damage)
            elif caça[3] < 80:
                caça_damage = [caça[0], caça[2], '-1']
                imprimir_tracker.append(caça_damage)   
                print(caça_damage)
else:
    
    classe_referencia = body[0]
    maior_dano = float(classe_referencia[1])
   
    for fire in body:
        if "Fire" in fire:
            
            if fire[1] >= 0.80 * maior_dano:
                if fire[3] >= 90:
                    fire_damage = [fire[0], fire[2], '+1']
                    imprimir_tracker.append(fire_damage)
                    print(fire_damage)
                elif fire[3] < 80:
                    fire_damage = [fire[0], fire[2], '-1']
                    imprimir_tracker.append(fire_damage)
                    print(fire_damage)
            elif fire[1] < 0.50* maior_dano:
                fire_damage = [fire[0], fire[2], '-1']
                imprimir_tracker.append(fire_damage)   
                print(fire_damage)
            elif fire[3] < 80:
                fire_damage = [fire[0], fire[2], '-1']
                imprimir_tracker.append(fire_damage)  
                print(fire_damage)  
    for frost in body:
        if "Frost" in frost:
            
            if frost[1] >= 0.80 * maior_dano:
                if frost[3] >= 90:
                    frost_damage = [frost[0], frost[2], '+1']
                    imprimir_tracker.append(frost_damage)
                    print(frost_damage)
                elif frost[3] < 80:
                    frost_damage = [frost[0], frost[2], '-1']
                    imprimir_tracker.append(frost_damage)
                    print(frost_damage)
            elif frost[1] < 0.50* maior_dano:
                    frost_damage = [frost[0], frost[2], '-1']
                    imprimir_tracker.append(frost_damage)    
                    print(frost_damage)
            elif frost[3] < 80:
                    frost_damage = [frost[0], frost[2], '-1']
                    imprimir_tracker.append(frost_damage)   
                    print(frost_damage)
    for xbow in body:
        if "Xbow" in xbow:
            
            if xbow[1] >= 0.85 * maior_dano:
                if xbow[3] >= 90:
                    xbow_damage = [xbow[0], xbow[2], '+1']
                    imprimir_tracker.append(xbow_damage)
                    print(xbow_damage)
                elif xbow[3] < 80:
                    xbow_damage = [xbow[0], xbow[2], '-1']
                    imprimir_tracker.append(xbow_damage)
                    print(xbow_damage)
            elif xbow[1] < 0.60* maior_dano:
                xbow_damage = [xbow[0], xbow[2], '-1']
                imprimir_tracker.append(xbow_damage) 
                print(xbow_damage)
            elif xbow[3] < 80:
                xbow_damage = [xbow[0], xbow[2], '-1']
                imprimir_tracker.append(xbow_damage)   
                print(xbow_damage)
    for raiz in body:
        if "Raiz" in raiz:
            
            if raiz[1] >= 0.85 * maior_dano:
                if raiz[3] >= 90:
                    raiz_damage = [raiz[0], raiz[2], '+1']
                    imprimir_tracker.append(raiz_damage)
                    print(raiz_damage)
                elif raiz[3] < 80:
                    raiz_damage = [raiz[0], raiz[2], '-1']
                    imprimir_tracker.append(raiz_damage)
                    print(raiz_damage)
            elif raiz[1] < 0.60* maior_dano:
                raiz_damage = [raiz[0], raiz[2], '-1']
                imprimir_tracker.append(raiz_damage)   
                print(raiz_damage)
            elif raiz[3] < 80:
                raiz_damage = [raiz[0], raiz[2], '-1']
                imprimir_tracker.append(raiz_damage)   
                print(raiz_damage)
    for caça in body:
        if "Caça-Espiritos" in caça:
            
            if caça[1] >= 0.50 * maior_dano:
                if caça[3] >= 90:
                    caça_damage = [caça[0], caça[2], '+1']
                    imprimir_tracker.append(caça_damage)
                    print(caça_damage)
                elif caça[3] < 80:
                    caça_damage = [caça[0], caça[2], '-1']
                    imprimir_tracker.append(caça_damage) 
                    print(caça_damage)
            elif caça[1] < 0.35* maior_dano:
                caça_damage = [caça[0], caça[2], '-1']
                imprimir_tracker.append(caça_damage)     
                print(caça_damage)
            elif caça[3] < 80:
                caça_damage = [caça[0], caça[2], '-1']
                imprimir_tracker.append(caça_damage)    
                print(caça_damage)

for suporte in body:
    if 'Offtank' in suporte:
        if suporte[3] >= 90:
            offtank_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(offtank_durabilidade)
            print(offtank_durabilidade)
        elif suporte[3] < 80:
            offtank_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(offtank_durabilidade)
            print(offtank_durabilidade)
for suporte in body:
    if 'Elevado' in suporte:
        if suporte[3] >= 90:
            elevado_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(elevado_durabilidade)
            print(elevado_durabilidade)
        elif suporte[3] < 80:
            elevado_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(elevado_durabilidade)
            print(elevado_durabilidade)
for suporte in body:
    if 'Silence' in suporte:
        if suporte[3] >= 90:
            silence_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(silence_durabilidade)
            print(silence_durabilidade)
        elif suporte[3] < 80:
            silence_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(silence_durabilidade)
            print(silence_durabilidade)
for suporte in body:
    if 'Main Healer' in suporte:
        if suporte[3] >= 90:
            mainhealer_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(mainhealer_durabilidade)
            print(mainhealer_durabilidade)
        elif suporte[3] < 80:
            mainhealer_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(mainhealer_durabilidade)
            print(mainhealer_durabilidade)
for suporte in body:
    if 'Bruxo' in suporte:
        if suporte[3] >= 90:
            bruxo_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(bruxo_durabilidade)
            print(bruxo_durabilidade)
        elif suporte[3] < 80:
            bruxo_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(bruxo_durabilidade)
            print(bruxo_durabilidade)   
for suporte in body:
    if 'Quebra Reinos' in suporte:
        if suporte[3] >= 90:
            quebraReinos_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(quebraReinos_durabilidade)
            print(quebraReinos_durabilidade)
        elif suporte[3] < 80:
            quebraReinos_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(quebraReinos_durabilidade)
            print(quebraReinos_durabilidade)
for suporte in body:
    if 'Oculto' in suporte:
        if suporte[3] >= 90:
            oculto_durabilidade = [suporte[0], suporte[2], '+1']
            imprimir_tracker.append(oculto_durabilidade)
            print(oculto_durabilidade)
        elif suporte[3] < 80:
            oculto_durabilidade = [suporte[0], suporte[2], '-1']
            imprimir_tracker.append(oculto_durabilidade)
            print(oculto_durabilidade)

Scout = input(str('Deseja adicionar o Scout? Se sim precione "s"'))

if "s" in Scout:
    nome_scout = input(str('Digite o nome: '))
    ponto_scout = input(str('Digite +1 ou -1: '))
       
    Scout_adicionado = [nome_scout,'Scout', ponto_scout]
    imprimir_tracker.append(Scout_adicionado) 
    print(Scout_adicionado)



with open('saida.txt', 'w') as arquivo:
    
        
    for tratamento_final in imprimir_tracker:
        arquivo.write(f'{tratamento_final[0]} {tratamento_final[1]} {tratamento_final[2]} \n ' )
        