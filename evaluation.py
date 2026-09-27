from main import summarize_text

test_cases = [
    {
        "name": "News Text",
        "text": "Artificial intelligence is changing many industries. Companies use AI to automate tasks, analyze data, improve customer service, and support decision making."
    },
    {
        "name": "Educational Text",
        "text": "Photosynthesis is the process by which green plants use sunlight, carbon dioxide, and water to produce glucose and oxygen."
    },
    {
        "name": "Short Text",
        "text": "AI is useful."
    }
]

print("================================")
print("AI TEXT SUMMARIZER EVALUATION")
print("================================")

for test in test_cases:
    print(f"\nTest Case: {test['name']}")
    print("Input:", test["text"])

    if len(test["text"].strip()) < 20:
        print("Result: Input is too short for a useful summary.")
    else:
        print("Summary:")
        print(summarize_text(test["text"]))