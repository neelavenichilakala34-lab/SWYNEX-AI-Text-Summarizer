from huggingface_hub import InferenceClient
def summarize_text(text):
    client=InferenceClient(provider="auto")
    prompt =f"""
Summarize the following text in 3 to 5 simple sentences.
keep the important information and make the summary easy to understand
text:
{text}
"""
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response.choices[0].message.content
print("====================================")
print("         AI TEXT SUMMARIZER")
print("====================================")
text=input("\nEnter your text:\n")
if len(text.strip())<20:
    print("\nPlease enter a longer paragraph.")
else:
        print("\nGenerating summary...\n")
        summary=summarize_text(text)
        print("---------AI SUMMARY---------")
        print(summary)
        print("----------------------------")