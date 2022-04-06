## use http requests
## copilot had no idea what to do here whatsoever
import json
import typing
import urllib.error
import urllib.parse
import urllib.request
from email.message import Message

class Response(typing.NamedTuple):
    body: str
    headers: Message
    status: int
    error_count: int = 0

    def json(self) -> typing.Any:
        try:
            output = json.loads(self.body)
        except json.JSONDecodeError:
            output = ""
        return output

def get(url: str):
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json"},
        method="GET"
        )

    print("Sending", req.method, "request", url)
    try:
        with urllib.request.urlopen(req) as httpresponse:
            response = Response(
                headers=httpresponse.headers,
                status=httpresponse.status,
                body=httpresponse.read().decode(
                    httpresponse.headers.get_content_charset("utf-8")
                ),
            )
    except urllib.error.HTTPError as e:
        response = Response(
            body=str(e.reason),
            headers=e.headers,
            status=e.code,
            error_count=1,
        )

    print("Response Status", response.status)
    if response.error_count >= 1:
        print("Response Error", response.body)
    return response

def getTrivia(amount: int = 25):
    questions = get("https://trivia-art.herokuapp.com/api/questions?amount={}".format(amount))

    print(questions.json())


    
getTrivia(35)