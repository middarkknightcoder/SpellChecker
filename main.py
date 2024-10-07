from spellchecker import SpellChecker



class SpellCheckerApp:
    
    def __init__(self):
        self.spell = SpellChecker()   # We are create object of the Spellchecker class for used in over class
     
    def SpellCorrection(self,text):
        words = text.split()    # Spliting a text into words
        correct_words = []
        
        for w in words:
            correct_word  = self.spell.correction(w)
 
            if(correct_word != w.lower() and correct_word != None):
                correct_words.append(correct_word)
            else:
                correct_words.append(w)
         
        if(len(correct_words) == 0):
            return text
        else:
            return " ".join(correct_words)
    
    def run(self):
        
        print("***** Welcome in SpellChecker ! ******")

        while(True):
            
            text = input("Enter Text Which you want to correction : ")
            
            if(text == "Exit"):
                print("Clossing SpellChecker Application ......")
                break
        
            correct_text = self.SpellCorrection(text)
            print(f"Correction Text is -->  {correct_text}")
        
            print("\n")
            print("If you want to close the App write --> Exit")
            

if __name__ == "__main__":
    SpellCheckerApp().run()
            
                
        
        