from alert_bot import start_bot
from argparse import ArgumentParser

def main() -> None: 
    parser = ArgumentParser(
            description="",
            usage="utelal.py start"
            )
    
    subparser = parser.add_subparsers(dest="command")
    subparser.add_parser(
            "start", help="starts bot"
            )

    args = parser.parse_args()
    if args.command == "start":
        start_bot()
    else:
        parser.print_usage()

if __name__ == "__main__":
    main()
