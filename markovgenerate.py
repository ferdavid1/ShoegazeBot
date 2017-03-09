# rename this main.py after lyric bank is generated
import markovify

# Get raw text as string.
with open("shoegaze_lyrics_bank.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)


# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(80) + '\n')