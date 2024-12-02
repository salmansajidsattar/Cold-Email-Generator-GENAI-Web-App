import re
from langchain_community.document_loaders import WebBaseLoader
from utils import Chain
from portfolio import Portfolio


def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    # Trim leading and trailing whitespace
    text = text.strip()
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def get_email(url_input,llm,portfolio):
    loader = WebBaseLoader(url_input)
    print("loader",loader)
    data = clean_text(loader.load().pop().page_content)
    print("data",data)
    portfolio.load_portfolio()
    jobs = llm.extract_data(data)
    print("jobs", jobs)
    for job in jobs:
        skills = job.get('skills', [])
        links = portfolio.query_links(skills)
        email = llm.write_mail(job, links)
        print("Final final",email)
        return email