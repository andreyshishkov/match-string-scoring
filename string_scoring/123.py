from rapidfuzz import process
from string_scoring.models import User, RequestScoring


u1 = User(first_name='Andrey', last_name='Shishkov', address='Krasnodar')
u2 = User(first_name='Ivan', last_name='Kochetenko', address='Krasnodar')
u3 = User(first_name='Andreyka', last_name='sheshkov', address='Krasnodar krashaya')

request = RequestScoring(
    user=u1,
    candidates=[u2, u3]
)

request = RequestScoring(
    user=u1,
    candidates=[u2, u3]
)

user = request.user.concatenate()
candidates = [x.concatenate() for x in request.candidates]

result = process.extract(
        query=user,
        choices=candidates,
        limit=request.limit
    )
print(result)
