from cli import CLI
from taxCalc import TaxCalc


def main():
    cl = CLI()
    choice = cl.greetingMenu()
    match choice:
        case _ if choice == 1:
            inp = cl.getInput(1)
            tc = TaxCalc(inp)
            print(f"Net Income: {tc.netIncome():.3f}")

        case _ if choice == 2:
            gross = cl.getInput(1)
            savings = cl.getInput(2)
            expenses = cl.getInput(3)
            tc = TaxCalc(gross, savings, expenses)
            print(f"Disposable: {tc.netAfterSE():.3f}")
            saved = tc.netAfterExpenses() / (1 - tc.savingRatio)
            print(f"Amount saved ({tc.savingRatio * 100:.3f}%): {saved:.3f}")
            print(
                f"Expenses as a % of net income (net: {tc.netIncome()}): {(tc.expenses / tc.netIncome())*100:.3f}"
            )
        case _ if choice == 3:
            gross = cl.getInput(1)
            savings = cl.getInput(2)
            tc = TaxCalc(gross, savings)
            print(f"Net after saving: {tc.netAfterSavings():.3f}")
            print(
                f"Amount saved ({tc.savingRatio * 100:.3f}%): {tc.netIncome() - tc.netAfterSavings():.3f}"
            )


if __name__ == "__main__":
    main()
