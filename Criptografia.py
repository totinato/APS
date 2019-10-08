from cryptography.fernet import Fernet
import os
import sys
#1-Para o codigo funcionar ele precisa de uma chave entao primeiro rode o codigo gerador_de_key que esta na mesma pasta
#2-apos gerar uma chave utilize a mesma para encriptar um arquivo(o nome do arquivo deve conter a extenção dele por exemplo teste.txt)
#3-caso queira finalize o programa e tente gerar uma nova chave e tentar a descriptografia com ela
#4-o arquivo que sera encriptado e excluido, portanto nao exclua a key
if os.path.exists("key.key")==True:
    file = open("key.key", "rb")
    key = file.read()
    file.close()
else:
    print("Chave de segurança nao encontrada por favor rode o codigo gerador de key primeiro")
    sys.exit()

encrypted=""
a=0


def encriptarmsg(mensagem,key):
    encoded = mensagem.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    mensagem_ecriptada=encrypted.decode()
    print("sua mensagem encriptada é",mensagem_ecriptada)
    return encrypted





def desencriptarmsg(encrypted,key):
    f2=Fernet(key)
    decrypted=f2.decrypt(encrypted)
    mensagem_original=decrypted.decode()
    print("sua mensagem descriptada é", mensagem_original)



def encriptararq (key):
    nome_arq=input("digite o nome do arquivo a ser encriptado")
    if os.path.exists(nome_arq)==True:
        with open(nome_arq,"rb")as f:
            data=f.read()
        ferenet=Fernet(key)
        encrypted=ferenet.encrypt(data)
        with open('encriptado.txt.encrypted',"wb")as f:
           f.write(encrypted)
        os.remove(nome_arq)
    else:
        print("arquivo nao encontrado")


def descriptararq (key):
    with open('encriptado.txt.encrypted',"rb")as f:
        data=f.read()
    ferenet=Fernet(key)
    encrypted=ferenet.decrypt(data)
    with open('descriptado.txt',"wb")as f:
       f.write(encrypted)




while a!=5:
    a = int(input("digite 1 para encriptar uma mensagem 2 para descriptografar e 3 para encriptar um arquivo 4 para descriptar um arquivo e 5 para sair"))
    if a == 1:
        mensagem = input("digite sua mensagem a ser encriptada")
        encrypted = encriptarmsg(mensagem, key)

    elif a == 2:
        if encrypted=="":
            print("voce precisa de digitar uma mensagem a ser descriptografada primeiro")
        else:
            desencriptarmsg(encrypted, key)
    elif a==3:
        try:
            encriptararq(key)
        except:
            print("Chave invalida")
    elif a==4:
        if os.path.exists("encriptado.txt.encrypted")==True:
            try:
                descriptararq(key)
            except:
                print("chave invalida")
        else:
            print("nao ha arquivo a ser desencriptado")
    elif a==5:
        print("codigo sendo finalizado")
        break





