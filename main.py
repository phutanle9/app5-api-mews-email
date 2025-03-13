import requests
from send_email import send_email

api_key = "7f280d9389184fdd99c22cbce8a66742"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-02-13&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    # Use empty string if title or description is None
    body = body + (article['title'] or "") + "\n" + (article["description"] or "") + "\n\n"

# Encode body in UTF-8
body = body.encode("utf-8")

# Send email if body is not empty
if body:
    send_email(message=body)
