import spotipy
import sys

def main():
	username = sys.argv[1]
	scope = 'playlist-read-collaborative'
	token = spotipy.util.prompt_for_user_token(username, scope, client_id ='aed32e0354914a3798094ab32b8ffb21', client_secret = '40cdb111d55b4c58a7cbff203f234fe8', redirect_uri = 'http://startbackpacking.org/')
	if token:
		
	else:
		print("Can't get token for ", username)
		print("Make sure correct spotify username is entered")

if __name__ == '__main__':
	main()