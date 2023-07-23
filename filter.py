import re

playlistComponents = []

f = open("playlist.m3u", "r", encoding="utf-8")
nf = open("filteredPlaylist.m3u", "w", encoding="utf-8")

metaPattern = re.compile("^#(EXTINF|EXTVLCOPT|KODIPROP).*")
urlPattern = re.compile("^http[\S]+")

channel = ""
for line in f.read().split("\n"):
    if (metaPattern.match(line)):
        channel = channel + line + "\n"
    elif (urlPattern.match(line)):
        channel = channel + line + "\n"
        if channel not in playlistComponents:
            playlistComponents.append(channel)
        channel = ""
    else:
        playlistComponents.append(line + "\n")

nf.writelines(playlistComponents)
