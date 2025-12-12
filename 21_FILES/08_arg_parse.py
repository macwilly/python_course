import argparse
def main():
    parser = argparse.ArgumentParser(description="Simple Calculater")

    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("num2", type=float, help="The second number")
    parser.add_argument("operation", choices=["add","sub", "mult", "div"], type=str, help="Operation to perform")

    args = parser.parse_args()

    match args.operation:
        case "add":
            print(f"The sum of {args.num1} and {args.num2} is {args.num1+ args.num2}")
        case "sub":
            print(f"The sum of {args.num1} and {args.num2} is {args.num1 - args.num2}")
        case "mult":
            print(f"The product of {args.num1} and {args.num2} is {args.num1 * args.num2}")
        case "div":
            print(f"The product of {args.num1} and {args.num2} is {args.num1 / args.num2}")
        case _:
            # Since the choices are set we never get into the default as case
            print("Invalid operation")


if __name__ == "__main__":
    main()