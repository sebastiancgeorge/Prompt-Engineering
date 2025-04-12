import openai

openai.api_key = "your-api-key-here"

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Examples of different prompt styles
if __name__ == "__main__":
    prompts = {
        "zero_shot": "Translate the following English sentence to French: 'I love AI.'",
        "few_shot": """Translate English to French:
        English: Hello
        French: Bonjour
        English: How are you?
        French: Comment ça va?
        English: I love AI.
        French:""",
        "role_based": "You are a professional French translator. Translate 'I love AI' into French.",
        "instructional": "Please translate 'I love AI' into French."
    }

    for style, prompt in prompts.items():
        print(f"\n--- {style.replace('_', ' ').title()} Prompt ---")
        print("Prompt:", prompt)
        print("Response:", get_response(prompt))
