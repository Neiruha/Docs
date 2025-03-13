import openai

class OpenAIClient:
    def __init__(self):
        self.api_key = None
        self.client = None  # Новый клиент

    def set_api_key(self, api_key):
        self.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)  # Создаём клиент

    def get_response(self, prompt):
        if not self.client:
            raise ValueError("API key is not set. Please set the API key before making a request.")

        response = self.client.chat.completions.create(  # Новый синтаксис!
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
