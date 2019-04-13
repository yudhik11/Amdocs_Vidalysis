import requests
from pygments import highlight, lexers, formatters
import json, sys


def get_video_id(name):
    url=requests.get("https://api.videoindexer.ai/trial/Accounts/c09ddeac-e37a-4f39-92b4-e03a724532ea/Videos?accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBY2NvdW50SWQiOiJjMDlkZGVhYy1lMzdhLTRmMzktOTJiNC1lMDNhNzI0NTMyZWEiLCJBbGxvd0VkaXQiOiJGYWxzZSIsIkV4dGVybmFsVXNlcklkIjoiMTAyNDgyNDcwMDg5NTk1ODEzNjk2IiwiVXNlclR5cGUiOiJHb29nbGUiLCJpc3MiOiJodHRwczovL3d3dy52aWRlb2luZGV4ZXIuYWkvIiwiYXVkIjoiaHR0cHM6Ly93d3cudmlkZW9pbmRleGVyLmFpLyIsImV4cCI6MTU1NTA1Nzc1OCwibmJmIjoxNTU1MDUzODU4fQ.pDAueQxuoNaG_znoUxSX59JGs4TQsqUw6lI6ohoBzYk")
    resp=url.json()
    # print(resp)
    i=0
    vid_id=-1
    for i in range(0, len(resp['results'])):
        if name== resp['results'][i]['name']:
            vid_id=resp['results'][i]['id']
    return (vid_id)

def videx(name):
    id=get_video_id(name)
    url = "https://api.videoindexer.ai/trial/Accounts/c09ddeac-e37a-4f39-92b4-e03a724532ea/Videos/"+id+"/Index?reTranslate=False&accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBY2NvdW50SWQiOiJjMDlkZGVhYy1lMzdhLTRmMzktOTJiNC1lMDNhNzI0NTMyZWEiLCJBbGxvd0VkaXQiOiJGYWxzZSIsIkV4dGVybmFsVXNlcklkIjoiMTAyNDgyNDcwMDg5NTk1ODEzNjk2IiwiVXNlclR5cGUiOiJHb29nbGUiLCJpc3MiOiJodHRwczovL3d3dy52aWRlb2luZGV4ZXIuYWkvIiwiYXVkIjoiaHR0cHM6Ly93d3cudmlkZW9pbmRleGVyLmFpLyIsImV4cCI6MTU1NTA1Nzc1OCwibmJmIjoxNTU1MDUzODU4fQ.pDAueQxuoNaG_znoUxSX59JGs4TQsqUw6lI6ohoBzYk"
    url = requests.get(url)
    # print(url.json())


    formatted_json = json.dumps(url.json(), indent=4)
    #colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    print(formatted_json)

if __name__ == '__main__':
    # if len(sys.argv) == 2:
    #     # print(get_video_id())
    inp=input('Video name:\n')
    # else:
    videx(inp)
