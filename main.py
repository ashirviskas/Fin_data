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
                print("Enter number of comparative periods\n 2 year\n 3 year\n 4 year")
                select_H_Main = int(input("Please enter"))
                if select_H_Main == 2:
                    attrs = input_attrs('Enter first period data: ')
                    year1 = Year(*attrs)
                    attrs = input_attrs('Enter second period data: ')
                    year2 = Year(*attrs)

                    while end not in ("Q", "q"):
                        print(
                            "please select\n 1 - revenues\n 2 - cogs\n 3 - assets\n 4 - liabilities\n 5 - equity\n 6 - net income")
                        select_H_2 = int(input("Please enter selection"))
                        if select_H_2 == 1:
                            def Delta_1_year():
                                delta = (int(year2.rev) - int(year1.rev)) / int(year1.rev) * 100
                                return round(delta, 2)


                            plt.style.use("bmh")  # revenue
                            x_axis = np.arange(1, 3)
                            labels = [int(year1.rev), int(year2.rev)]
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
                            labels = [int(year1.cogs), int(year2.cogs)]
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
                            labels = [int(year1.assets), int(year2.assets)]
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
                            labels = [int(year1.liab), int(year2.liab)]
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
                            labels = [int(year1.equity), int(year2.equity)]
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
                            labels = [int(year1.net), int(year2.net)]
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

                if select_H_Main == 3:

                    attrs = input_attrs('Enter first period data: ')
                    year1 = Year(*attrs)
                    attrs = input_attrs('Enter second period data: ')
                    year2 = Year(*attrs)
                    attrs = input_attrs('Enter third period data: ')
                    year3 = Year(*attrs)
                    end = input("")

                    while end not in ("Q", "q"):
                        print(
                            "please select\n 1 - revenues\n 2 - cogs\n 3 - assets\n 4 - liabilities\n 5 - equity\n 6 - net income")
                        select_H_3 = int(input("Please enter selection"))


                        def Delta_2_year():
                            delta = (int(year2.rev) - int(year1.rev)) / int(year1.rev) * 100
                            return round(delta, 2)


                        if select_H_3 == 1:  # revenues
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 4)
                            labels = [int(year1.rev), int(year2.rev), int(year3.rev)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Revenue')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_3 == 2:  # cogs
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 4)
                            labels = [int(year1.cogs), int(year2.cogs)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Costs of goods')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_3 == 3:  # assets
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 4)
                            labels = [int(year1.assets), int(year2.assets), int(year3.assets)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.liab) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Assets')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_3 == 4:  # liabilities
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 4)
                            labels = [int(year1.liab), int(year2.liab), int(year3.liab), int(year4.liab)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Liabilities')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_3 == 5:  # equity
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 4)
                            labels = [int(year1.equity), int(year2.equity), int(year3.equity), int(year4.equity)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.equity) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Equity')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_3 == 6:  # income
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 4)
                            labels = [int(year1.net), int(year2.net), int(year3.net), int(year4.net)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.assets) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Net income')
                            plt.xticks(x_axis, x_axis)
                            plt.show()
                        end = input("Press any key to go back. If you want to quit, please enter ""Q""")
                    else:
                        break

                if select_H_Main == 4:
                    attrs = input_attrs('Enter first period data: ')
                    year1 = Year(*attrs)
                    attrs = input_attrs('Enter second period data: ')
                    year2 = Year(*attrs)
                    attrs = input_attrs('Enter third period data: ')
                    year3 = Year(*attrs)
                    attrs = input_attrs('Enter third period data: ')
                    year4 = Year(*attrs)
                    end = input("")

                    while end not in ("Q", "q"):
                        print(
                            "please select\n 1 - revenues\n 2 - cogs\n 3 - assets\n 4 - liabilities\n 5 - equity\n 6 - net income")
                        select_H_4 = int(input("Please enter selection"))


                        def Delta_2_year():
                            delta = (int(year2.rev) - int(year1.rev)) / int(year1.rev) * 100
                            return round(delta, 2)


                        if select_H_4 == 1:  # revenues
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 5)
                            labels = [int(year1.rev), int(year2.rev), int(year3.rev), int(year4.rev)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Revenue')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_4 == 2:  # cogs
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 5)
                            labels = [int(year1.cogs), int(year2.cogs), int(year3.cogs), int(year4.cogs)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Costs of goods')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_4 == 3:  # assets
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 5)
                            labels = [int(year1.assets), int(year2.assets), int(year3.assets), int(year4.assets)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.liab) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Assets')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_4 == 4:  # liabilities
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 5)
                            labels = [int(year1.liab), int(year2.liab), int(year3.liab), int(year4.liab)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.cogs) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Liabilities')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_4 == 5:  # equity
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 5)
                            labels = [int(year1.equity), int(year2.equity), int(year3.equity), int(year4.equity)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.equity) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Equity')
                            plt.xticks(x_axis, x_axis)
                            plt.show()

                        if select_H_4 == 6:  # income
                            plt.style.use("bmh")
                            x_axis = np.arange(1, 5)
                            labels = [int(year1.net), int(year2.net), int(year3.net), int(year4.net)]
                            plt.bar(x_axis, [int(x) for x in labels])
                            # plt.text(2, int(year2.assets) + .25, str(Delta_1_year()) + '%', color=Colo)
                            plt.xlabel('Periods')
                            plt.ylabel('Net income')
                            plt.xticks(x_axis, x_axis)
                            plt.show()
                        end = input("Press any key to go back. If you want to quit, please enter ""Q""")
                    else:
                        break

                end = input("Press any key to go back. If you want to quit, please enter ""Q""")
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
