from services import *


class Main:

    def __init__(self):
        self.propositions_list = self.get_propositions()
        votings = self.get_votings()
        scoreService = ScoreService(votings)
        score = scoreService.calculate()
        self.print_score(score)

    def get_votings(self):
        voting_list = VotingService(self.propositions_list)
        print("Buscando as votações das proposições ocorridas no período selecionado...")
        return voting_list.get_from_ws()

    @staticmethod
    def export_score(score):
        dialect = csv.excel_tab
        dialect.delimiter = ';'
        with open('result.csv', mode='w') as csv_file:
            field_names = ['nome deputado', 'partido', 'estado', 'qtd de votos', 'pontuação bruta', 'pontuação']
            writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect=dialect)
            writer.writeheader()
            for key in score:
                congressman = score[key]
                writer.writerow({
                    'nome deputado': congressman.name,
                    'partido': congressman.party,
                    'estado': congressman.state,
                    'qtd de votos': congressman.voting_times,
                    'pontuação bruta': congressman.party_score,
                    'pontuação': congressman.score_percent
                })
        print("Arquivo gerado!")

    @staticmethod
    def print_score(score):
        for key in score:
            congressman = score[key]
            print("{} \t {}%".format(congressman.name, congressman.score_percent))

    @staticmethod
    def get_propositions():
        proposition_list = []
        ano_inicial, ano_final = input('Selecione o ano inicial e o ano final para a seleção das requisições: ').split()
        intervalo = range(int(ano_inicial), int(ano_final) + 1, 1)

        print('Buscando proposições...')

        for ano in intervalo:
            service = PropositionService(int(ano))
            year_list = service.get_from_ws()
            print('Encontradas {} proposições votadas no ano de {}'.format(len(year_list), ano))
            proposition_list.append(year_list)

        return proposition_list


if __name__ == "__main__":
    Main()
