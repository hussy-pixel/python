class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
    
flash = []
print("welcome to the aplication")

while(True):
    word = input("enter the name you want to add to flash card")
    meaning = input("enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 1 to break and 0 to continue"))
    
    if(option):
        break
print("\n your flashcards")
for i in flash:
    print(">", i)