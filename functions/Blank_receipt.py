def print_header():
    print("CASH RECEIPT")


def print_dashes():
    print("------------------------------")


def print_body():
    print("Charged to____________________\nReceived by___________________")


def print_footer():
    print("© SoftUni")


def print_receipt():
    print_header()
    print_dashes()
    print_body()
    print_dashes()
    print_footer()


if __name__ == "__main__":
    print_receipt()