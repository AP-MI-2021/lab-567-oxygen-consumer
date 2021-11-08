from Tests.run_all_tests import run_all_tests
from UI.console import run_menu
from UI.cli import run_cli


def main():
    run_all_tests()

    lista = []
    while True:
        ui = input("Introduceti cli pt cli (incomplet) sau ui pt ui: ")
        if ui == "ui":
            run_menu(lista)
            break
        elif ui == "cli":
            run_cli(lista)
            break
        else:
            print("Optiune inexistenta")


if __name__ == "__main__":
    main()
