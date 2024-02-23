class WordCount():
    def __init__(self):
        self.wordcount = {}
        self.words = []
    
    def split(self, text):
        self.words = text.split()
    
    def counter(self):
        for word in self.words:
            self.wordcount[word] = self.wordcount.get(word, 0) + 1
    
    def show_wordcount(self):
        print("List of words that appear in the text, and their respective number of apparitions: ")
        for k, v in self.wordcount.items():
            print(f"{k} : {v}")

            
text1 = WordCount()

text1.split("uno dos dos tres tres tres")
text1.counter()
text1.show_wordcount()