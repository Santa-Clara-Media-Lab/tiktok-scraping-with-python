from TikTokApi import TikTokApi
import pandas as pd

# collect videos from a given user. 
# THe "user_videos" object is now a list of 100 video dictionaries and only a few stats will be relevant which can be extracted with following function
 
api = TikTokApi() 
  
user_videos = api.byUsername(washingtonpost, count=100)

def simple_dict(tiktok_dict):
  to_return = {}
  to_return["user_name"] = tiktok_dict["author"]["uniqueId"]
  to_return["user_id"] = tiktok_dict["author"]["id"]
  to_return["video_id"] = tiktok_dict["id"]
  to_return["video_desc"] = tiktok_dict["desc"]
  to_return["video_time"] = tiktok_dict["createTime"]
  to_return["video_length"] = tiktok_dict["video"]["duration"]
  to_return["video_link"] = "https://www.tiktok.com/@{}/video/{}?lang=en".format(to_return["user_name"], to_return["video_id"])
  to_return["n_likes"] = tiktok_dict["stats"]["diggCount"]
  to_return["n_shares"] = tiktok_dict["stats"]["shareCount"]
  to_return["n_comments"] = tiktok_dict["stats"]["commentCount"]
  to_return["n_plays"] = tiktok_dict["stats"]["playCount"]

  return to_return

# Then, we can go from the API-outputted "user_videos" list to a nice, clean table

user_videos = [simple_dict(v) for v in user_videos]
user_videos_df = pd.DataFrame(user_videos)
user_videos_df.to_csv("{}_videos.csv".format(username),index=False)