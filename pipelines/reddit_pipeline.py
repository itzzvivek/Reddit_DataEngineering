from dags.reddit_dag import extract
from etls.reddit_etl import connect_reddit, extract_posts
from utils.constants import SECRET, CLIENT_ID


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    #connection to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    #exraction
    post = extract_posts(instance, subreddit, time_filter, limit)
    #transformation
    #loading to csv