import csv
import json

# Read the CSV file and store the gift recommendations in a list
gift_recommendations = []
with open('gift_recommendations.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        age, hobby, gift = row
        gift_recommendations.append({'age': age, 'hobby': hobby, 'gift': gift})

# Generate prompt and completion pairs for each gift recommendation
prompt_completion_pairs = []
for gift in gift_recommendations:
    prompt = f"What is a good {gift['hobby']} gift for someone {gift['age']}?"
    completion = f"A good {gift['hobby']} gift for someone {gift['age']} is {gift['gift']}."
    prompt_completion_pairs.append({'prompt': prompt, 'completion': completion})

# Export the prompt and completion pairs to a JSON file
with open('gift_recommendations_prompts_completions.json', 'w') as file:
    json.dump(prompt_completion_pairs, file)
