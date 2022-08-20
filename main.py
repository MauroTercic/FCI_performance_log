from bbva_fci import FCI
from datetime import date
import pandas as pd

pd.options.mode.chained_assignment = None # getting rid of a warning message
#  lines
l1 = "¿Qué queres hacer?\n"
l2 = "Tipea 1 para agregar nuevo balance\n"
l3 = "Tipea 2 para ver todo\n"
l4 = "Tipea 3 para ver el balance actual\n"
l5 = "Tipea 4 para ver el gráfico de rendimientos\n"
l6 = "Tipea 'exit' para salir\n"
l7 = "-----Escribi aca:"
l8 = "*Ingresa el nuevo balance sin ´,´:"


#  running code

if __name__ == "__main__":

    while True:
        inp = input(f"---------------------------------\n*{l1}*{l2}*{l3}*{l4}*{l5}*{l6}{l7}")
        if str(inp) == "exit":
            break

        elif int(inp) == 1:
            try:
                inp2 = input(f"---------------------------------\n{l8}")
                obj = FCI(float(inp2), date.today())  # create the object and convert to date
                obj.add()
                print(f"{inp2} agregado.")
                FCI.calculate_changes()
            except:
                print("Input invalido")

        elif int(inp) == 2:
            FCI.show_all()

        elif int(inp) == 3:
            print("Balance actual:")
            FCI.show_current_balance()

        elif int(inp) == 4:
            FCI.show_graph()

        else:
            print("Input inválido")
