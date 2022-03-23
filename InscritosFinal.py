import cx_Oracle
import config

connection = None

try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)
    while True:
        action = int(
            input(
                'Que ação deseja realizar? selecionar[1], inserir[2], modificar[3] ou deletar[4]? [0] para encerrar: '))
        if action == 1:

            cursor = connection.cursor()
            select = 'SELECT * FROM INSCRITOSS'
            cursor.execute(select)
            todas = int(input('Deseja selecionar todas as linhas? 0 para sim e 1 para não: '))
            if todas == 0:
                linhas = cursor.fetchall()
                for lin in linhas:
                    connection.cursor()
                    print('_' * 30)
                    print('{} | {} | {} | {}'.format(lin[0], lin[1], lin[2], lin[3]))
                    print('_' * 30)
            else:
                connection.cursor()
                linha = int(input('Quantas linhas deseja selecionar?'))
                linhas = cursor.fetchmany(linha)
                for lin in linhas:
                    print('_' * 30)
                    print('{} | {} | {} | {}'.format(lin[0], lin[1], lin[2], lin[3]))
                    print('_' * 30)

        elif action == 2:

            cursor = connection.cursor()
            while True:
                stop = int(input('Digite [0] para parar e [1] para continuar: '))

                if stop == 1:
                    nome = input('Nome: ')
                    idade = int(input('Idade: '))
                    sexo = input('Sexo: ')
                    sql = ('INSERT INTO INSCRITOSS(NOME, IDADE, SEXO) '
                           ' VALUES (:nome, :idade, :sexo)')
                    cursor.execute(sql, (nome, idade, sexo))
                    connection.commit()

                elif stop == 0:
                    break
                else:
                    print('_' * 30)
                    print('Ação Inválida, verifique os números e tente novamente.')
                    print('_' * 30)

        elif action == 3:

            cursor = connection.cursor()
            print('Digite o nuemro solicitado para editar os dados, e [0] caso deseje encerrar. ')
            select = "SELECT * FROM INSCRITOSS"
            cursor.execute(select)
            linhas = cursor.fetchall()
            print("[ NUM_ESC | NOME | IDADE | SEXO ]\n")
            for linha in linhas:
                print('_' * 30)
                print('{} | {} | {} | {}'.format(linha[0], linha[1], linha[2], linha[3]))
                print('_' * 30)

            while True:
                update = int(input('Que dado deseja modificar? nome[1], idade[2], sexo[3], parar[0]: '))
                if update == 1:

                    numInscricao = int(input('Digite o número de inscrição da pessoa: '))
                    nomeAtual = input('Nome Atual: ')
                    novoNome = input('Novo nome: ')
                    sql = ('UPDATE INSCRITOSS '
                           ' SET NOME = :novoNome '
                           ' WHERE NOME = :nomeAtual and NUM_INSCRICAO = :numInscricao ')
                    cursor.execute(sql, (novoNome, nomeAtual, numInscricao))
                    connection.commit()
                    print('Atualização concluida!')
                elif update == 2:
                    for linha in linhas:
                        print("_" * 30)
                        print("{} | {} | {} | {}".format(linha[0], linha[1], linha[2], linha[3]))
                        print("_" * 30)
                        numInscricao = int(input('Digite o número de inscrição da pessoa: '))
                        idadeAtual = input('Idade Atual: ')
                        novaIdade = input('Nova Idade: ')
                        sql = ('UPDATE INSCRITOSS '
                               ' SET IDADE = :novaIdade '
                               ' WHERE IDADE = :idadeAtual and NUM_INSCRICAO = :numInscricao ')
                        cursor.execute(sql, (novaIdade, idadeAtual, numInscricao))
                        connection.commit()
                        print('Atualização concluida!')
                elif update == 3:
                    for linha in linhas:
                        print('_' * 30)
                        print('{} | {} | {} | {}'.format(linha[0], linha[1], linha[2], linha[3]))
                        print('_' * 30)
                        numInscricao = int(input('Digite o número de inscrição da pessoa: '))
                        sexoAtual = input('Sexo Atual: ')
                        novoSexo = input('Novo Sexo: ')
                        sql = ('UPDATE INSCRITOSS '
                               ' SET SEXO = :novoSexo '
                               ' WHERE SEXO = :sexoAtual and NUM_INSCRICAO = :numInscricao ')
                        cursor.execute(sql, (novoSexo, sexoAtual, numInscricao))
                        connection.commit()
                        print('Atualização concluida!')
                elif update == 0:
                    break
                else:
                    print('_' * 30)
                    print('Ação Inválida, verifique os números e tente novamente.')
                    print('_' * 30)

        elif action == 4:

            cursor = connection.cursor()
            select = "SELECT * FROM INSCRITOSS"
            cursor.execute(select)
            linhas = cursor.fetchall()
            for linha in linhas:
                print('_' * 30)
                print('{} | {} | {} | {}'.format(linha[0], linha[1], linha[2], linha[3]))
                print('_' * 30)

            while True:
                delete = int(input('Digite [1] para continuar deletando, parar[0]: '))
                if delete == 1:
                    numInscricao = int(input('Digite o número de inscrição para deletar a linha: '))
                    sql = ('DELETE INSCRITOSS '
                           ' WHERE NUM_INSCRICAO = :numInscricao ')
                    cursor.execute(sql, {'numInscricao': numInscricao})
                    connection.commit()
                    print('Atualização concluida!')
                elif delete == 0:
                    break
                else:
                    print('_' * 30)
                    print('Ação Inválida, verifique os números e tente novamente.')
                    print('_' * 30)


        elif action == 0:
            print('Atualizações Concluidas!')
            break

        else:
            print('ERROR! Verifique se colocou as informações corretas e tente novamente.')

except cx_Oracle.Error as error:
    print(error)
finally:
    if connection:
        connection.close()
