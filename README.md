set OPEN_API_KEY=""

openai tools fine_tunes.prepare_data -f gift_recommendations_prompts_completions.json

openai api fine_tunes.create -t gift_recommendations_prompts_completions_prepared.jsonl -m curie

openai api  completions.create -m model_fine_tunes -p "Sport gift for someone from 10 - 30 years old?"
