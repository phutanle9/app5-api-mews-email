import requests
from send_email import send_email

# Your News API Key
api_key = "7f280d9389184fdd99c22cbce8a66742"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-02-15&sortBy=publishedAt&apiKey=7f280d9389184fdd99c22cbce8a66742"

# Request data from the News API
request = requests.get(url)

# Check if the request was successful
if request.status_code == 200:
    content = request.json()

    if "articles" in content:
        # Initialize the body for the email
        body = ""
        for article in content["articles"]:
            title = article.get('title', '') or ''
            description = article.get('description', '') or ''
            body += f"{title}\n{description}\n\n"

        # Check if body is not empty before sending an email
        if body.strip():  # Check if body has content
            send_email(message=body)
        else:
            print("No content to send in the email.")
    else:
        print("No articles found in the response.")
else:
    print(f"Failed to fetch data. Status code: {request.status_code}")
