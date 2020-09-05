from alert_bot import start_bot
from argparse import ArgumentParser

def main() -> None: 
    parser = ArgumentParser(
            description="",
            usage="utelal.py -s")

    parser.add_argument(
            "--start", "starts bot"
            )

if __name__ == "__main__":
    main()
