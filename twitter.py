def tweet_finder(lat, long, radius):

    '''
    This function takes the coordinates of a location and a radius, and returns the five most recent
    tweets from within that radius of the location with the username of the tweeter.
    '''
    
    # Import tweepy library
    import tweepy

    # Set auth
    auth = tweepy.OAuthHandler("NhwEslehY264mPa0owS6i4BZU","zzuVEQsOSOovoHXZ965Me4HKlt0VMiH87ruztaTo71cPH9VIYK")
    auth.set_access_token("2282751926-Avzs0JEIg0WIePxJO7y0meUYlQj2gR8uMfrnF6q","ePKPPikAAChk6W5dNnQPLTUOcOxNBzGHknI9DpO9aQXig")

    # Set twitter API
    twitter_api = tweepy.API(auth)

    # Search twitter
    tweets = twitter_api.search  (geocode = '{},{},{}'.format(lat,long,radius))

    for tweet in tweets:
        print tweet.user.name.encode("utf-8") + ": " + tweet.text.encode("utf-8")

tweet_finder(51.5,-0.15,'15km')
