questions = [
    {
        "question": "Which part of Amoeba helps in capturing food?",
        "options": ["Cilia", "Flagella", "Pseudopodia", "Tentacles"],
        "answer": 2
    },
    {
        "question": "Which organ produces bile juice?",
        "options": ["Gall bladder", "Liver", "Pancreas", "Stomach"],
        "answer": 1
    },
    {
        "question": "Which of the following is not a ruminant?",
        "options": ["Cow", "Goat", "Horse", "Deer"],
        "answer": 2
    },
    {
        "question": "Which enzyme in saliva breaks down starch?",
        "options": ["Pepsin", "Trypsin", "Amylase", "Lipase"],
        "answer": 2
    },
    {
        "question": "In plants, which process converts sunlight into food?",
        "options": ["Respiration", "Transpiration", "Photosynthesis", "Digestion"],
        "answer": 2
    }
]

score = 0

for i, q in enumerate(questions):
    print(f"\nQ{i+1}: {q['question']}")
    for idx, opt in enumerate(q['options']):
        print(f"  {idx + 1}. {opt}")
    try:
        ans = int(input("Your answer (1-4): ")) - 1
        if ans == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Nope, it's {q['options'][q['answer']]}")
    except:
        print("⚠️ Invalid input. Skipping question.")

print(f"\n🎯 Final Score: {score}/{len(questions)}")
if score == len(questions):
    print("🏆 Perfect! You’re a Nutrition Master.")
elif score >= 3:
    print("👍 Good job! Keep reviewing.")
else:
    print("📚 Time to revisit the Nutrition chapters.")