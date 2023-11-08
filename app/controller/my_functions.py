



def formatar(valor):
    hora = valor
    valor = hora.strftime('%H:%M:%S.%f')[:-4]
    return valor