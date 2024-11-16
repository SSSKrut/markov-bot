import json
import random

class MarkovPredictor:
    def __init__(self, probabilities_file):
        with open(probabilities_file, 'r', encoding='utf-8') as f:
            self.probabilities = json.load(f)
        self.all_words = list(self.probabilities.keys())
    
    def predict_next(self, current_word, min_probability=0.0):
        next_words = self.probabilities.get(current_word)
        
        if next_words:
            filtered_words = {word: prob for word, prob in next_words.items() if prob >= min_probability}
            
            if filtered_words:
                chosen_word = random.choice(list(filtered_words.keys()))
                return chosen_word
            else:
                chosen_word = random.choice(list(next_words.keys()))
                return chosen_word
        else:
            chosen_word = random.choice(self.all_words)
            return chosen_word

def generate_sequence(start_word, num_words, predictor, min_probability=0.0):
    sequence = [start_word]
    current_word = start_word

    for _ in range(num_words - 1):
        next_word = predictor.predict_next(current_word, min_probability)
        sequence.append(next_word)
        current_word = next_word

    return ' '.join(sequence)

def main():
    predictor = MarkovPredictor('src/output_probabilities.json')
    
    start_word = input("Enter a starting word: ")
    num_words = int(input("Enter the number of words to generate: "))
    min_prob = float(input("Enter the minimum probability threshold (between 0 and 1): "))
    
    generated_text = generate_sequence(start_word, num_words, predictor, min_probability=min_prob)
    print("\nGenerated text:")
    print(generated_text)

if __name__ == "__main__":
    main()