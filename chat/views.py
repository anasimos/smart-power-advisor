from rest_framework.decorators import api_view
from rest_framework.response import Response
from ai.services import AIService


@api_view(["POST"])
def chat(request):
    print("DATA:", request.data)

    message = request.data.get("message")

    if not message:
        return Response(
            {
                "error": "Please provide a 'message' field.",
                "received": request.data,
            },
            status=400,
        )

    reply = AIService.chat(message)

    return Response({
        "user": message,
        "assistant": reply,
    })