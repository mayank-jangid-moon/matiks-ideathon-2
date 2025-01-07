import numpy as np
import pandas as pd
import random

def generate_synthetic_data(output_file="synthetic_math_data.csv"):
    np.random.seed(42)
    user_ids = np.arange(1, 101)
    question_categories = ['Arithmetic', 'Algebra', 'Geometry', 'Logic']
    difficulty_levels = ['Easy', 'Medium', 'Hard']
    
    category_difficulty = {
        'Arithmetic': {'Easy': (30, 10), 'Medium': (50, 15), 'Hard': (70, 20)},
        'Algebra': {'Easy': (35, 12), 'Medium': (55, 18), 'Hard': (75, 25)},
        'Geometry': {'Easy': (40, 15), 'Medium': (60, 20), 'Hard': (85, 30)},
        'Logic': {'Easy': (30, 10), 'Medium': (45, 15), 'Hard': (65, 25)},
    }
    
    category_correctness_prob = {
        'Arithmetic': {'Easy': 0.8, 'Medium': 0.6, 'Hard': 0.4},
        'Algebra': {'Easy': 0.75, 'Medium': 0.55, 'Hard': 0.35},
        'Geometry': {'Easy': 0.7, 'Medium': 0.5, 'Hard': 0.3},
        'Logic': {'Easy': 0.75, 'Medium': 0.55, 'Hard': 0.45},
    }

    user_skill = {user: random.gauss(0.5, 0.2) for user in user_ids}

    rows = []
    for user in user_ids:
        for _ in range(50):
            category = random.choice(question_categories)
            difficulty = random.choice(difficulty_levels)
            
            time_mean, time_std = category_difficulty[category][difficulty]
            time_taken = np.random.normal(loc=time_mean, scale=time_std)
            time_taken = max(5, time_taken)
            
            attempts_lambda = 1 if difficulty == 'Easy' else 2 if difficulty == 'Medium' else 3
            attempts = np.random.poisson(lam=attempts_lambda)

            base_correctness_prob = category_correctness_prob[category][difficulty]
            adjusted_prob = min(1.0, max(0.0, base_correctness_prob + (user_skill[user] - 0.5) * 0.2))
            correctness = np.random.choice([1, 0], p=[adjusted_prob, 1 - adjusted_prob])

            rows.append({
                'UserID': user,
                'Category': category,
                'Difficulty': difficulty,
                'TimeTaken': max(5, time_taken),
                'Attempts': max(1, attempts),
                'Correctness': correctness
            })

    data = pd.DataFrame(rows)
    data.to_csv(output_file, index=False)
    print(f"Synthetic data saved to {output_file}")


generate_synthetic_data()
