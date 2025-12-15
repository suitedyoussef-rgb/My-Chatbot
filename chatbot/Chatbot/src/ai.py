def AI_Chatbot():
    import google.generativeai as genai
    import os
    
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("GEMINI_API_KEY environment variable not set.")
            return
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel("gemini-2.5-flash")

        while True:
                
            prompt = input("\n\nAsk anything or type 'exit' to exit: \n")

            if prompt.lower() == "exit":
                print("\n=========================================================|\n")
                break

            response = model.generate_content(prompt)       
                
            print("\n\nAI: ",response.text)
    except Exception as e:
        print(f"An error occurred with the AI model. Please check your API key and configuration.")
#========================================================================|

def image_generator():
    import requests
    while True:
        user_prompt = input("\n\nEnter a description for your AI image (or type 'exit' to quit):\n\n---> ")
        if user_prompt.lower() == "exit":
            print("Exiting the program.")
            break
        if not user_prompt.strip():
            print("You cannot send empty prompts.")
            continue

        safe_prompt = user_prompt.strip().replace(" ", "_")
        image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}"

        response = requests.get(image_url)
        if response.status_code == 200:
            print("You can open this image URL:", image_url)
        else:
            print("Failed to generate image. Status code:", response.status_code)