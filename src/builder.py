import re
import json
from collections import defaultdict

def read_and_build_markov_chain(file_path, output_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read()

        sentences = re.split(r'[.!?]+', content)

        markov_chain = defaultdict(list)

        for sentence in sentences:
            # Tokenize the sentence into words, commas, and double dashes
            words = re.findall(r'\w+|--|[,]', sentence)
            # Build the Markov chain
            for i in range(len(words)-1):
                current_word = words[i]
                next_word = words[i+1]
                markov_chain[current_word].append(next_word)
                
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(markov_chain, outfile, ensure_ascii=False, indent=4)

        print(f"Markov chain saved to {output_path}")

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = 'voina-i-mir.txt'
    output_path = 'markov_chain.json'
    read_and_build_markov_chain(file_path, output_path)