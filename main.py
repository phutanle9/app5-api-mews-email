import requests

url= "https://newsapi.org/v2/everything?q=tesla&from=2025-02-13&sortBy=publishedAt&apiKey=7f280d9389184fdd99c22cbce8a66742"

request = requests.get(url)
content= request.json()

for article in content['articles']:
    print(article['title'])
    print(article["description"])