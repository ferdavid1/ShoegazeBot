def Shoegaze():
	# rename this main.py after lyric bank is generated
	import markovify

	# Get raw text as string.
	with open("shoegaze_lyrics_bank.txt", encoding='ISO-8859-1') as f:
	    text = f.read()

	# Build the model.
	text_model = markovify.NewlineText(text)

	statement = text_model.make_short_sentence(80)

	return statement