import requests


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}

    res = requests.get(gh_api_repo_search_url, params=parameters)

    status_code = res.status_code
    # status_code = 500
    if status_code != 200:
        raise RuntimeError(
            f"An error occurred. Status code was: {status_code}")
    else:
        res_json = res.json()["items"]
        return res_json


if __name__ == "__main__":
    languages = ["Python", "Javascript", "Ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
