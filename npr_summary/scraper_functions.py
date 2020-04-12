import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
import textwrap


def Article_Summary(news_article, ratio):
    '''Makes a news article on NPR smaller'''

    # Retrieve page text
    url = news_article
    page = requests.get(url).text

    # Turn page into BeautifulSoup object to access HTML tags
    soup = BeautifulSoup(page)

    # Get headline
    headline = soup.find('h1').get_text()

    # Get text from all <p> tags.
    p_tags = soup.find_all('p')
    # Get the text from each of the “p” tags and strip surrounding whitespace.
    p_tags_text = [tag.get_text().strip() for tag in p_tags]

    # Filter out sentences that contain newline characters '\n' or don't contain periods.
    sentence_list = [
        sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]

    # Combine list items into string.
    article = ' '.join(sentence_list)

    # Make a summary of the article
    summary = summarize(article, ratio=ratio)

    '''# A clean output
    print(f'\nLength of original article: {len(article)}')
    print(f'Length of summary: {len(summary)}')
    print(f'Headline: {headline} \n')
    print(f'Article Summary:\n{textwrap.fill(summary, 120)}')'''

    return summary

