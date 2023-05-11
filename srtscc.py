import srt
import requests

# read in our srt/scc file
srt_file = "Uncut Gems (2019) (NetNaija.com).srt"
with open(srt_file, "r") as fp:
    content = fp.read()


srt_generator = srt.parse(content)
subtitle = next(srt_generator)
content = subtitle.content

for t in srt_generator:
    print(t.content)


url = "https://api.apilayer.com/bad_words?censor_character=censor_character"
#Not working as i expected it to.
# Got to explore other options for this
