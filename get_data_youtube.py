from googleapiclient.discovery import build

def get_video_id_from_url(url):
    # Extract the video ID from the URL
    if "watch?v=" in url:
        return url.split("watch?v=")[-1]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")

def get_comments_from_video(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=100
    )
    
    while request:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        request = youtube.commentThreads().list_next(request, response)
    
    return comments

# Thay thế bằng URL video và API Key của bạn
video_url = 'https://www.youtube.com/watch?v=y_pe3ldKB9A'
api_key = 'AIzaSyCRrUqdycCYrBGSQsmci-FLuKTPidFDKlI'

# Lấy ID video từ URL
video_id = get_video_id_from_url(video_url)

# Lấy bình luận từ ID video
comments = get_comments_from_video(video_id, api_key)

# In các bình luận
for comment in comments:
    print(comment)
