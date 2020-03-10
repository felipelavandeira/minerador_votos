from services.proposition_service import PropositionService


def main():

    proposition_list = []
    ano_inicial, ano_final = input('Selecione o ano inicial e o ano final para a seleção das requisições: ').split()
    intervalo = range(int(ano_inicial), int(ano_final), 1)

    print('Buscando proposições...')

    for ano in intervalo:
        service = PropositionService(int(ano))
        year_list = service.get_from_ws()
        print('Encontradas {} proposições votadas no ano de {}'.format(len(year_list), ano))
        proposition_list.append(year_list)


if __name__ == "__main__":
    main()
