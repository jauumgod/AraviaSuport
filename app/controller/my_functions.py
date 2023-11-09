import random
import string



def formatar(valor):
    hora = valor
    valor = hora.strftime('%H:%M:%S.%f')[:-4]
    return valor





def gerar_token_aleatorio(tamanho=20):
    caracteres = string.ascii_letters + string.digits  + string.punctuation # Letras maiúsculas, minúsculas e dígitos
    token = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return token