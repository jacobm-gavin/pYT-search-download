##pytube or yt-dlp
from youtube_search import YoutubeSearch
import os


def main():
    query = input("Enter the search query: ")
    results = YoutubeSearch(query, max_results=5).to_dict()
    resultsList = []
    for i in results:
        resultsList.append({f"{i['title']:<70} || {i['channel']:<70} || {i['duration']}": f"https://www.youtube.com/watch?v={i['id']}" })
    for i, video in enumerate(resultsList):
        print(f"{i}: {list(video.keys())[0]}") 

    choice = int(input("Enter the number of the video you want to download: "))
    download(list(resultsList[choice].values())[0])
    lint()
        
def lint():
    for file in os.listdir("/Users/jmgavin/Audio"):
        if "_" in file:
            os.rename(f"/Users/jmgavin/Audio/{file}", f"/Users/jmgavin/Audio/{file.replace('_', ' ')}")

def download(link: str) -> bool:
    os.system(f"yt-dlp {link} -x --audio-format mp3  --embed-thumbnail --embed-metadata -P ~/Audio --restrict-filenames")
    return
main()
