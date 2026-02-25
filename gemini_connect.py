from google import genai




client = genai.Client(api_key='AIzaSyCeMeOHyqKMLvt5cg0i38Do6BwCb3J7vhU')

def get_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    return (response.text)
