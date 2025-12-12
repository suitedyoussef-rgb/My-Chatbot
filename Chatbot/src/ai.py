def ai():
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
        print(f"Error details: {e}")
#========================================================================|