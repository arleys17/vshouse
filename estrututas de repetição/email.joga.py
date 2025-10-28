#colocar email para verificar
def verificar_email(email):
    #vericar se o email esta correto
    if '@jogajuntoinstituto.org' in email:
        return True
    else :
        return False
    #solicar um email
email_usuario = input(' digite seu email:')
#vai fazer a verificação
if verificar_email(email_usuario):
    print('email verificado! bem vindo ao instuto joga junto')
else:
    print(' email invalido! use email do jogajuntoinstututo.org')