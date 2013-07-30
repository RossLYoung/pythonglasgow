from requests import get, ConnectionError


def get_members():

    try:
        members = get("https://api.github.com/orgs/python-glasgow/members").json()
        if 'message' in members and members['message'].startswith("API Rate Limit Exceeded"):
            print "GITHUB RATE LIMIT."
            raise StopIteration
    except ConnectionError:
        raise StopIteration

    for member in members:
        try:
            yield get(member['url']).json()
        except (ValueError, TypeError):
            continue