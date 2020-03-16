from services.proposition_service import PropositionService
from services.voting_service import VotingService


class Main:

    def __init__(self):
        self.propositions_list = self.get_propositions()
        votings_list = self.get_votings()

    def get_votings(self):
        voting_list = VotingService(self.propositions_list)
        print("Buscando as votações das proposições ocorridas no período selecionado...")
        return voting_list.get_from_ws()

    @staticmethod
    def get_propositions():
        proposition_list = []
        ano_inicial, ano_final = input('Selecione o ano inicial e o ano final para a seleção das requisições: ').split()
        intervalo = range(int(ano_inicial), int(ano_final)+1, 1)

        print('Buscando proposições...')

        for ano in intervalo:
            service = PropositionService(int(ano))
            year_list = service.get_from_ws()
            print('Encontradas {} proposições votadas no ano de {}'.format(len(year_list), ano))
            proposition_list.append(year_list)

        return proposition_list


if __name__ == "__main__":
    Main()
