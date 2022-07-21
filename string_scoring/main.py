from fastapi import FastAPI
from rapidfuzz import fuzz, process
from string_scoring.models import (RequestPairString, ResponseScoring, ResponseUser,
                                   ResponsePairString, RequestScoring)

app = FastAPI(description='App to estimate likehood of strings')


@app.post('/two_string')
async def root1(strings: RequestPairString):
    score = fuzz.ratio(strings.string1, strings.string2)
    response = ResponsePairString(
        id=strings.id,
        score=score

    )
    return response


@app.post('/scoring')
async def root2(request: RequestScoring):
    user = request.user.concatenate()
    candidates = [x.concatenate() for x in request.candidates]

    result = process.extract(
        query=user,
        choices=candidates,
        limit=request.limit
    )
    response_users = [ResponseUser(concat=concat, score=score, index=ind) for concat, score, ind in result]
    return ResponseScoring(users=response_users)
