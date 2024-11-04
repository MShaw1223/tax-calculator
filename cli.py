class CLI:
    def greetingMenu(self) -> int:
        inputs = [
            "Get Net Income (Gross - tax and NIC)",
            "Get Net Income after savings and expenses",
            "Get Net Income after savings",
        ]
        sides = "- - -"

        largest_length = max(len(item) for item in inputs)

        print_times = largest_length // 4
        # with the second as longest (NI after S&E) print times = 10
        # thus 10//3 should be the amount of spaces added
        added_spaces = " " * (print_times // 3)

        terminating_line = (f"{sides} " * (print_times - 1)) + f"{sides}"

        print(terminating_line)

        for i in range(len(inputs)):
            padded_input = inputs[i].ljust(largest_length)
            print(f"{sides} {i+1}. {padded_input} {added_spaces}{sides}")

        print(terminating_line)

        choice = int(input("\nEnter Choice here: "))
        return choice

    def getInput(self, user_input) -> float:
        match user_input:
            case _ if user_input == 1:
                response = float(input("Enter Your Gross income: "))
                return response
            case _ if user_input == 2:
                response = float(input("Now your saving target (2% = 0.02): "))
                return response
            case _ if user_input == 3:
                response = float(input("Now enter your yearly expenses: "))
                return response
        return 0.0
