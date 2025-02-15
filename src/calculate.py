class Text:
    def __init__(self, msg: str) -> None:
        self.msg = msg    


    def calculateIndexOfCoincidence(self) -> float:
        result: float = 0.0
        n = len(self.msg)
        characterFrequency: dict[str, int] = self.calculateCharacterFrequency()
        
        for character in characterFrequency:
            result += ((characterFrequency.get(character) * (characterFrequency.get(character)-1))/(n*(n-1)))
        return result
    


    def calculateCharacterFrequency(self) -> dict[str, int]:
        characterFrequency: dict[str, int] = {}
        for character in self.msg:
            if character in characterFrequency.keys():
                characterFrequency[character] += 1
            else:
                characterFrequency[character] = 1
        return characterFrequency



    def calculateCharacterFrequencyByPercentage(self) -> dict[str, float]:
        characterFrequencyByPercentage: dict[str, float] = {}
        characterFrequency: dict[str, int] = self.calculateCharacterFrequency()
        for character in characterFrequency.keys():
            characterFrequencyByPercentage[character] = characterFrequency[character]/len(self.msg)
        return characterFrequencyByPercentage



class Ciphertext(Text):
    pass


class Plaintext(Text):
    pass
    

