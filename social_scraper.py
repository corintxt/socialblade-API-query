# Module imports
import requests
import pandas as pd


# Retrieve ID and TOKEN from environment variables
ID = os.getenv('ID')
TOKEN = os.environ.get('TOKEN')


# Retrieve Twitter data for a given username (30 days by default)
def get_socialblade_data(user):
    twit_user = user
    client_id = ID
    token = TOKEN
    
    query_url = f'https://matrix.sbapis.com/b/twitter/statistics?query={twit_user}&clientid={client_id}&token={token}'
    x = requests.get(query_url)
    
    if x.status_code==200:
        print(f"Got data for {user}")
        resp = x.json()
        # call process_response() function on data object
        processed_data = process_response(resp)
        return processed_data        
    else:
        print(f"Query for [{user}] returned status {x.status_code}")


# Use pandas to format response object into dataframe
def process_response(resp):
    user_data = resp['data']['id']
    df = pd.DataFrame(resp['data']['daily']).sort_values(by='date').copy()
    
    df['username'] = user_data['username']
    df['display_name'] = user_data['display_name']
    
    # Reorganize columns
    df = df[['username','display_name','date', 'followers', 'following', 'tweets']]
    
    # Calculate follower change
    df['change'] = df.followers.diff()
    df['percent_change'] = df.followers.pct_change()
    print(f"Compiled data for {user_data['username']}")
    return df


# Save dataframe to CSV in directory (e.g. political alignment)
def write_to_csv(df, directory, username):
    df.to_csv(f'{directory}/{username}.csv', index=False)
    print(f'Saved {username} to csv.')