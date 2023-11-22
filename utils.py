from bs4 import BeautifulSoup


def change_response(content, proxy_url):
    soup = BeautifulSoup(content, "html.parser")
    for a_tag in soup.find_all("a"):
        a_tag["href"] = proxy_url
    return str(soup)


def verify_age_restrition(content, restricted_words, is_older):
    if not is_older:
        soup = BeautifulSoup(content, "html.parser")

        for word in restricted_words:
            if word.lower() in soup.text.lower():
                return False

    return True
