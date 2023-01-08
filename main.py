
def converter_bn_b10(bn, num):
    
    bn = int(bn) #convertendo o numero da base para o tipo inteiro
    num = str(num) #convertendo o numero para o tipo string
    #tratando numero com sinal
    sinal = ""
    if(num[0] == "-") | (num[0] == "+"): 
        sinal = num[0]
        num = num[1:]
        
    maior_sig = 0 #variavel para definir qual e o maior expoente para o fator de conversao
    if("." not in num): maior_sig = len(num.split(".")[0]) -1 #definindo o valor de maior_sig caso num seja inteiro
    else: 
        maior_sig = len(num.split(".")[0]) -1 #definindo o valor de maior_sig caso o numero nao seja inteiro
        num = num.replace(".", "") #removendo o ponto do numero
    t_num = len(num) #variavel que contem a quantidade de algarismos do numero
    cont = 0; #variavel para contar a posicao dos algarismos
    num_dec = 0.0; #variavel para armazenar o resultado da conversao
    
    #loop para converter para base 10
    while cont != t_num:
        #fator de conversao do algarismo, equivale uma unidade correspondente a posicao(casa) que o algarismo esta
        fator_conversao = float(bn ** (maior_sig - cont)) 
        algarismo = num[cont]; #armazenando um algarismo
        
        #verificando se o algarismo e um numero, se nao for converte a letra para o correspondente na base 10
        if not algarismo.isnumeric(): 
          if ord(algarismo) > 63: #Evitando caracteres invalidos
            algarismo = (ord(algarismo) - 55) 
          else: algarismo = -1
        algarismo = int(algarismo) #convertendo o algarismo para inteiro
        
        #verificando se ha algum erro por parte do usuario:
        if (algarismo < bn) & (algarismo >= 0): num_dec += algarismo * fator_conversao #se nao tiver, realiza a conversao para base 10 e soma na variavel de retorno
        else: return "Esse numero nao e de base " + str(bn) #se tiver, retorna uma mensagem de erro
        cont+=1
    if(num_dec == int(num_dec)): num_dec = int(num_dec) #removendo o ponto, caso a resposta seja inteira
    return(sinal+str(num_dec)) #retornando o resultado

def converter_b10_bn(bn, num):
    bn = int(bn)
   
    #tratando numero com sinal
    sinal = ""
    if(num[0] == "-") | (num[0] == "+"): 
        sinal = num[0]
        num = num[1:]
    if (not num.replace(".","").isnumeric()): return "Esse numero nao e de base 10" #verificando se ha algum erro por parte do usuario
    #dividindo o numero em parte inteira e nao inteira
    p_int = int(str(num).split(".")[0])
    p_nint =0;
    if("." in num): p_nint = float("0." + str(num).split(".")[1])  #contornando um erro caso o numero seja apenas inteiro
    
    #loop para converter a parte inteira para base bn
    dif = p_int #variavel que armazena o numero que sera usado no loop
    num_bn = "" #variavel que armazena o resultado
    while dif > 0: 
        div_int = dif // bn 
        resto_dInt = dif % bn
        
        #se o resto for maior que 9 converte esse numero para uma letra de valor correspondente na base bn
        if(resto_dInt > 9): resto_dInt = chr(55 + resto_dInt) 
        num_bn = str(resto_dInt) + num_bn #adiciona esse resto no inicio do resultado
        dif = div_int #redefine o numero usado no loop
    
    #loop para converter a parte nao inteira para base bn
    dif = p_nint
    cont = 0 
    num_bn += "." 
    #(bn ** cont) � o valor da casa atual da parte nao inteira em que uma unidade sera convertida
    #10**-10 e a tolerancia para conversao
    
    while dif * (bn ** cont) > 10**-10: #dessa forma a conversao trunca ao valor que a casa ira assumir for menor que tolerancia
        cont -= 1; num_add = 0
        
        #procedimento para obter o algarismo que sera adicionado a resposta
        multi = dif * bn
        num_add = int(multi) #parte inteira
        multi -= num_add #parte fracionaria
         
        if(num_add > 9): num_add = chr(55 + num_add) #se o num_add for maior que 9 converte esse numero para uma letra de valor correspondente na base bn
        num_bn+= str(num_add) #adiciona o algarismo ao final da resposta
        dif = multi #redefine o numero usado no loop
         
    if(num_bn[-1] == "."): num_bn = num_bn[:-1] #removendo o ponto, caso a resposta seja inteira
    return sinal + str(num_bn);

def troca_de_base(a,b,S):
    
    if(a != 10): num_dec = converter_bn_b10(a, S) #Se a base que o numero esta for diferente da base 10, converte o numero em S para base 10 e define num_dec com o retorno
    else: num_dec = S #se ele for igual so define num_dec para o numero em S
    
    if "Esse numero nao e de base" in num_dec: return num_dec #Checando erro
    
    if(int(b) == 10): return num_dec #se a base final for a base 10, retorna num_dec
    return converter_b10_bn(b, num_dec)#senao retorna a conversao do num_dec para a base b

