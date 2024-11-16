import json
from collections import Counter

def calculate_probabilities(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        markov_data = json.load(f)
    
    probability_dict = {}
    
    for word, followers in markov_data.items():
        follower_counts = Counter(followers)
        total_followers = sum(follower_counts.values())
        
        follower_probabilities = {}
        for follower, count in follower_counts.items():
            probability = count / total_followers
            follower_probabilities[follower] = probability
        
        sorted_probabilities = dict(
            sorted(
                follower_probabilities.items(),
                key=lambda item: item[1],
                reverse=True
            )
        )
        
        probability_dict[word] = sorted_probabilities
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(probability_dict, f, ensure_ascii=False, indent=4)
    
calculate_probabilities('src/markov_chain.json', 'output_probabilities.json')