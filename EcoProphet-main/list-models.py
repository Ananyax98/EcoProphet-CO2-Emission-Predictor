import google.generativeai as genai

# Configure API key (replace with your actual key)
genai.configure(api_key="YOUR_API_KEY")

# List available models
models = genai.list_models()

# Print model names
print("Available Gemini AI Models:")
for model in models:
    print(model.name)
