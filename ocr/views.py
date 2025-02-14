from django.http import JsonResponse
from .utils import extract_text
import os


def ocr_view(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        image_path = f"/tmp/{image.name}"

        with open(image_path, "wb") as f:
            f.write(image.read())

        text = extract_text(image_path)
        os.remove(image_path)

        return JsonResponse({"text": text})

    return JsonResponse({"error": "Invalid request"}, status=400)
