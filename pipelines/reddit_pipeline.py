def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    #connection to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    #exraction
    #transformation
    #loading to csv