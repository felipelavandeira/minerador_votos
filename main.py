from services import *


class Main:

    def __init__(self):
        self.propositions_list, init_year, end_year = self.get_propositions()
        votings = self.get_votings(init_year, end_year)
        scoreService = ScoreService(votings)
        score = scoreService.calculate()
        self.export_score(score)

    def get_votings(self, init_year: int, end_year: int):
        voting_list = VotingService(self.propositions_list, init_year, end_year)
        print("Buscando as votações das proposições ocorridas no período selecionado...")
        return voting_list.get_from_ws()

    @staticmethod
    def export_score(score):
        dialect = csv.excel_tab
        dialect.delimiter = ';'
        with open('files/result.csv', mode='w') as csv_file:
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
        period_list = ['2011 2012', '2019 2020']
        print('Selecione uma entre as opções:\n1 - 1º Mandato Dilma(2011/2012)\n2 - 1º Mandato Bolsonaro(2019/2020)')
        index = input('Digite o número da opção desejada: ')
        init_year, end_year = period_list[int(index) - 1].split()
        intervalo = range(int(init_year), int(end_year) + 1, 1)

        print('Buscando proposições...')

        for ano in intervalo:
            service = PropositionService(int(ano))
            year_list = service.get_from_ws()
            print('Encontradas {} proposições votadas no ano de {}'.format(len(year_list), ano))
            proposition_list.append(year_list)

        return proposition_list, init_year, end_year


if __name__ == "__main__":
    Main()
