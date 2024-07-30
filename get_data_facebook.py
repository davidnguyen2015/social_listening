import requests

def get_post_id_from_url(url, access_token):
    api_url = f"https://graph.facebook.com/v13.0/?id={url}&access_token={access_token}"
    response = requests.get(api_url)
    data = response.json()
    return data['id']

def get_comments_from_post(post_id, access_token):
    api_url = f"https://graph.facebook.com/v13.0/{post_id}/comments?access_token={access_token}"
    comments = []
    while True:
        response = requests.get(api_url)
        data = response.json()
        print(data)
        comments.extend(data['data'])
        if 'paging' in data and 'next' in data['paging']:
            api_url = data['paging']['next']
        else:
            break
    return comments

# Thay thế bằng URL bài đăng và Access Token của bạn
post_url = 'https://www.facebook.com/JustinBieber/posts/10159627484088888?_rdc=1&_rdr'
access_token = 'EAAEvES0IfyoBO3oBMBFhvptHvVMiI58Td4aZBAXnJBPFOouO9tLs9MAQAMZA3LuaQtDlt5e0ZAuOwvrC76ScZBZBfLBdnsNU6AZBf5NHN0Q2Skp8XQLJBQV2BsLXUawxnOteoADxWYahv7faY5fJe4Ki9RyvqK6xbAwLZCro3Sw9LJriXXhKk5KmNPlOUsEtTAJi8dLNYdD03clytzyZB3GyOuJ5IsLa16tthqoBYGo6TspXLtYMt0DQ'

# Lấy ID bài đăng từ URL
post_id = get_post_id_from_url(post_url, access_token)

# Lấy bình luận từ ID bài đăng
comments = get_comments_from_post(post_id, access_token)

# In các bình luận
for comment in comments:
    print(comment['message'])
