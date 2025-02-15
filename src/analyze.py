import argparse
from calculate import *

# Add in options for output to file
parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="Print verbose details", action="store_true")
parser.add_argument("-V", "--version", help="Print current version number", action="store_true")
args = parser.parse_args()


def formatInputString(msg: str) -> str:
    return msg.lower().replace(" ","")

def main() -> None:
    input = formatInputString("Test String")
    ciphertext = Ciphertext(input)
    print(f"Index of Coincidence: {ciphertext.calculateIndexOfCoincidence()}")
    print(f"Character Frequency: {ciphertext.calculateCharacterFrequency()}")
    print(f"Character Frequency by Percentage: {ciphertext.calculateCharacterFrequencyByPercentage()}")

if __name__ == "__main__":
    main()