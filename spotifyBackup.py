import spotipy
import sys
import spotipy.util as util



def main():

	SPOTIFYSONGLIMIT = 10000

	# Set up token info for saved songs
	username = sys.argv[1]
	scope = 'user-library-read'
	token = spotipy.util.prompt_for_user_token(username, scope, client_id ='aed32e0354914a3798094ab32b8ffb21', client_secret = '40cdb111d55b4c58a7cbff203f234fe8', redirect_uri = 'http://startbackpacking.org')
	if token:
		# Create spotify object
		spSaved = spotipy.Spotify(auth = token)
		# Get all savedSongs in dictionary {song name: song artist}
		savedSongs = {}
		for i in range(int (SPOTIFYSONGLIMIT/50)):
			currentFifty = spSaved.current_user_saved_tracks(50, i*50)
			if len(currentFifty["items"]) == 0:
				break
			for song in range(len(currentFifty['items'])):
				savedSongs [currentFifty['items'][song]['track']['name']] = currentFifty['items'][song]['track']['artists'][0]['name']
		# Print all saved songs in text file
		savedSongsFile = open("Saved Songs.txt",'w', encoding="utf-8")
		for song in savedSongs:
			savedSongsFile.write(song + " - " + savedSongs[song] + "\n")
	else:
		print("Can't get token for ", username)
		print("Make sure correct spotify username is entered")

	print("\nSaved songs backup complete :)\n")

	# Set up token info for playlists
	scope = 'playlist-read-collaborative'
	token = spotipy.util.prompt_for_user_token(username, scope, client_id ='aed32e0354914a3798094ab32b8ffb21', client_secret = '40cdb111d55b4c58a7cbff203f234fe8', redirect_uri = 'http://startbackpacking.org')
	if token:
		spPlaylists = spotipy.Spotify(auth = token)
		playlists = spPlaylists.user_playlists(username)
		for playlist in playlists['items']:
			playlistFile = open(playlist["name"], 'w', encoding="utf-8")
			for i in range(int(SPOTIFYSONGLIMIT/100)):
				currentOneHundred = spPlaylists.user_playlist_tracks(username, playlist["id"], offset = i*100)
				if (len(currentOneHundred["items"]) == 0):
					break
				for track in currentOneHundred['items']:
					playlistFile.write(track['track']['name'] + " - " + track['track']['artists'][0]['name'] + "\n")
			print ("Playlist " + playlist["name"] + " backup complete :)")


	else:
		print("Can't get token for ", username)
		print("Make sure correct spotify username is entered")		

if __name__ == '__main__':
    if len(sys.argv) > 1:
	    main()
    else:
        print ("Make sure to enter your spotify username/ID after python spotifyBackup.py")
        sys.exit()