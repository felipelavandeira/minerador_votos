from services.proposition_service import PropositionService


def main():
    service = PropositionService(2019)
    proposition_list = service.get_from_ws()

    for item in proposition_list:
        print(type(item))

    print(len(proposition_list))


if __name__ == "__main__":
    main()
