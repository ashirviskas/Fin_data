import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def input_attrs(initial_string):
    print(initial_string)
    rev = input("Revenues")
    cogs = input("Costs of goods")
    assets = input("Total assets")
    liab = input("Total liabilities")
    equity = input("Equity")
    net = input("Net income")
    return rev, cogs, assets, liab, equity, net


def delta_1_year(year_1, year_2):
    delta = (int(year_2.rev) - int(year_1.rev)) / int(year_1.rev) * 100
    return round(delta, 2)


while True:
    end = ""
    print(
        "Welcome to financial analysis. This project will help you to visualise financial data. You can choose to compare historical data over a number of accounting periods (horizontal analysis) or analyse single reporting period (vertical analysis)")
    select_menu = int(input("Please enter 1 (vertical analysis) or 2 (horizontal analysis)"))
    if select_menu in [1, 2]:
        if select_menu == 1:

            # Objective-oriented programming
            class Year:
                def __init__(self, rev, cogs, assets, liab, equity, net):
                    self.rev = rev
                    self.cogs = cogs
                    self.assets = assets
                    self.liab = liab
                    self.equity = equity
                    self.net = net


            # under development. Target: to identify delta between values and diferiancate color of text according to output
            # class Features:
            #      def Delta_1_year(self, delta):
            #          self.delta = (int(year2.rev) - int(year1.rev)) / int(year1.rev) * 100
            #          return round(self.delta, 2)
            #
            #      def Color_change(self):
            #          if self.delta < 0:
            #              Colo = 'r'
            #          elif self.delta > 0:
            #              Colo = 'g'

            while end not in ("Q", "q"):
                select_H_Main = int(input("Enter number of comparative periods\n 2 year\n 3 year\n 4 year: "))
                years = []
                for year_id in range(select_H_Main):
                    attrs = input_attrs('Enter ' + str(year_id) + ' period data: ')
                    year = Year(*attrs)
                    years.append(year)

                while end not in ("Q", "q"):
                    print(
                        "please select\n 1 - revenues\n 2 - cogs\n 3 - assets\n 4 - liabilities\n 5 - equity\n 6 - net income")
                    select_H_2 = int(input("Please enter selection"))
                    if select_H_2 == 1:



                        plt.style.use("bmh")  # revenue
                        x_axis = np.arange(1, 3)
                        labels = [int(years[0].rev), int(years[1].rev)]
                        plt.bar(x_axis, [int(x) for x in labels])
                        # plt.text(2, int(year2.rev) + .25, str(Delta_1_year()) + '%', color=Colo)
                        # Under development. Associated with Delta and Color_change f-tions.
                        plt.xlabel('Periods')
                        plt.ylabel('Revenue')
                        plt.xticks(x_axis, x_axis)
                        plt.show()

                    if select_H_2 == 2:  # cogs
                        plt.style.use("bmh")
                        x_axis = np.arange(1, 3)
                        labels = [int(years[0].cogs), int(years[1].cogs)]
                        plt.bar(x_axis, [int(x) for x in labels])
                        # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                        # Under development. Associated with Delta and Color_change f-tions.
                        plt.xlabel('Periods')
                        plt.ylabel('Costs of goods')
                        plt.xticks(x_axis, x_axis)
                        plt.show()

                    if select_H_2 == 3:  # assets
                        plt.style.use("bmh")
                        x_axis = np.arange(1, 3)
                        labels = [int(years[0].assets), int(years[1].assets)]
                        plt.bar(x_axis, [int(x) for x in labels])
                        # plt.text(2, int(year2.assets) + .25, str(Delta_1_year()) + '%', color=Colo)
                        # Under development. Associated with Delta and Color_change f-tions.
                        plt.xlabel('Periods')
                        plt.ylabel('Assets')
                        plt.xticks(x_axis, x_axis)
                        plt.show()

                    if select_H_2 == 4:  # liabilities
                        plt.style.use("bmh")
                        x_axis = np.arange(1, 3)
                        labels = [int(years[0].liab), int(years[1].liab)]
                        plt.bar(x_axis, [int(x) for x in labels])
                        # plt.text(2, int(year2.liab) + .25, str(Delta_1_year()) + '%', color=Colo)
                        # Under development. Associated with Delta and Color_change f-tions.
                        plt.xlabel('Periods')
                        plt.ylabel('Liabilities')
                        plt.xticks(x_axis, x_axis)
                        plt.show()

                    if select_H_2 == 5:  # equity
                        plt.style.use("bmh")
                        x_axis = np.arange(1, 3)
                        labels = [int(years[0].equity), int(years[1].equity)]
                        plt.bar(x_axis, [int(x) for x in labels])
                        # plt.text(2, int(year2.equity) + .25, str(Delta_1_year()) + '%', color=Colo)
                        # Under development. Associated with Delta and Color_change f-tions.
                        plt.xlabel('Periods')
                        plt.ylabel('Equity')
                        plt.xticks(x_axis, x_axis)
                        plt.show()

                    if select_H_2 == 6:  # income
                        plt.style.use("bmh")
                        x_axis = np.arange(1, 3)
                        labels = [int(years[0].net), int(years[1].net)]
                        plt.bar(x_axis, [int(x) for x in labels])
                        # plt.text(2, int(year2.net) + .25, str(Delta_1_year()) + '%', color=Colo)
                        # Under development. Associated with Delta and Color_change f-tions.
                        plt.xlabel('Periods')
                        plt.ylabel('Net income')
                        plt.xticks(x_axis, x_axis)
                        plt.show()
                    end = input('Press any key to go back. If you want to quit, please enter "Q"')
                else:
                    break

            else:
                break
        elif select_menu == 2:

            # Functional programing
            import functions

            # Under development. Target: differentiate colors regarding the value
            '''def Second_color():
                if roe_percetange() or operating_profit_percetenge() or roa_percentage() < 5:
                    return "red"
                elif roe_percetange or operating_profit_percetenge() or roa_percentage() > 5 and roe_percetange or operating_profit_percetenge() or roa_percentage() < 10:
                    return "yellow"
                else:
                    return "green"
            pie_chart_colors = ['white', Second_color()]'''

            while end not in ("Q", "q"):
                print(
                    "please select pics\n 1 - current ratio analysis\n 2 - capital structure\n 3 - cash conversion\n 4 - profitability")
                select_H_Main = int(input("Please enter selection"))
                if select_H_Main == 1:
                    functions.current_ratio_pic()
                if select_H_Main == 2:
                    functions.capital_structure()
                if select_H_Main == 3:
                    functions.cash_conversion_cycle()
                if select_H_Main == 4:
                    functions.profitability()
                end = input("Enter ""Q"" if you wat to go back.\n Enter any key to select other option")
                if end in ('Q', 'q'):
                    break
        else:
            print("Wrong choice")
