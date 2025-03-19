from rest_framework.views import APIView
from rest_framework.response import Response
from fuzzywuzzy import process, fuzz

from .faqs import FAQ

class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get("message", "").lower().strip()
        print(f"Received message: {user_message}")


        greetings = ["hello", "hi", "good day", "hey", "what’s up", "greetings"]
        if user_message in greetings:
            return Response({"message": "Hello! Welcome to TuneCycle 🎶. How can I assist you with music leasing or recommendations?"})

        # Find the best match in FAQ keys
        best_match, score = process.extractOne(user_message, FAQ.keys(), scorer=fuzz.partial_ratio)

        if score > 60:
            print(f"Matched question: {best_match} (Score: {score})")
            return Response({"message": FAQ[best_match]})

        return Response({"message": "I'm here to help with music leasing and recommendations! Can you clarify your request?"})
