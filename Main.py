import ConnectionOracle
from InterfataGrafica import GUI


def main():
    gui = GUI("Gestiunea unui spital judetean")
    gui.EditareFereastra()

    ConnectionOracle.CloseConnection()


if __name__ == '__main__':
    main()
