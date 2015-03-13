

def songData(art, ti):
	"""
		This function has a dependency you need to install.
		You'll need to install pyechonest. the easiest way to do this
		is to use setuptools and run the command "easy_install pyechonest"
	
	"""
	from pyechonest import config, song
	config.ECHO_NEST_API_KEY="J52LGDHNBUF5VOJDA";
	
	results = song.search(artist = art, title = ti);
	song_result = results[0];
	if song_result is None:
		print "Song not found.";
		return -1;
	return 	song_result.audio_summary['tempo'];

