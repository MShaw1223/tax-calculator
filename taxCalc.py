class TaxCalc:
    def __init__(
        self,
        gross,
        savingRatio=0.0,
        expenses=0.0,
        is_blind=False,
        married_and_over_89=False,
    ):
        self.gross = gross
        self.savingRatio = savingRatio
        self.expenses = expenses
        # Define allowances and thresholds
        self.PAV = 12_570  # Personal Allowance
        self.BLIND_ALLOWANCE = 3_070 if is_blind else 0
        self.MARRIED_REBATE = 1_108 if married_and_over_89 else 0
        self.INCOME_LIMIT = 100_000  # Income limit for allowance reduction
        # Tax bands and rates
        self.BR_LIMIT = 37_700
        self.HR_LIMIT = 125_140
        self.BASIC_RATE = 0.2
        self.HIGHER_RATE = 0.4
        self.ADDITIONAL_RATE = 0.45
        # NI thresholds and rates
        self.WPT = 242  # Weekly Primary Threshold
        self.UEL = 967  # Weekly Upper Earnings Limit
        self.LOWER_NI_RATE = 0.08
        self.UPPER_NI_RATE = 0.02
        # Calculate personal allowance after potential reduction
        self.personal_allowance = self.calculate_personal_allowance()
        self.taxable = max(0, self.gross - self.personal_allowance)

    def calculate_personal_allowance(self) -> float:
        allowance = self.PAV + self.BLIND_ALLOWANCE
        if self.gross > self.INCOME_LIMIT:
            reduction = (self.gross - self.INCOME_LIMIT) / 2
            allowance = max(0, allowance - reduction)
        return allowance

    def grossIncomeTax(self) -> float:
        tax = 0.0
        if self.taxable <= self.BR_LIMIT:
            tax += self.taxable * self.BASIC_RATE
        else:
            tax += self.BR_LIMIT * self.BASIC_RATE
            # Tax for income within higher rate band
            if self.taxable <= self.HR_LIMIT:
                tax += (self.taxable - self.BR_LIMIT) * self.HIGHER_RATE
            else:
                tax += (self.HR_LIMIT - self.BR_LIMIT) * self.HIGHER_RATE
                # Tax for income within additional rate band
                tax += (self.taxable - self.HR_LIMIT) * self.ADDITIONAL_RATE
        return tax

    def nationalInsurance(self) -> float:
        weekly = self.taxable / 52
        if weekly <= self.WPT:
            return 0.0
        elif weekly <= self.UEL:
            return self.taxable * self.LOWER_NI_RATE  # earning<=UEL
        else:
            lower_band_amount = self.UEL - self.WPT
            lower_contribution = lower_band_amount * self.LOWER_NI_RATE
            upper_amount = (self.gross / 52) - self.UEL
            upper_earnings_contribution = upper_amount * self.UPPER_NI_RATE
            return 52 * (lower_contribution + upper_earnings_contribution)

    def netIncome(self) -> float:
        IT = self.grossIncomeTax()
        NI = self.nationalInsurance()
        net = self.gross - (IT + NI)
        return net

    def netAfterSavings(self) -> float:
        net_income = self.netIncome()
        return net_income * (1 - self.savingRatio)

    def netAfterExpenses(self) -> float:
        net_income = self.netIncome()
        income_less_expenses = net_income - self.expenses
        return income_less_expenses

    def netAfterSE(self) -> float:
        after_expenses = self.netAfterExpenses()
        disposable = after_expenses * (1 - self.savingRatio)
        return disposable
