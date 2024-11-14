import base64
from PIL import Image
from io import BytesIO
import gradio as gr


def encode_image_to_base64(image_path, max_width=150):
    # Open the image with Pillow
    with Image.open(image_path) as img:
        # Calculate the new height to maintain the aspect ratio
        width_percent = max_width / float(img.width)
        new_height = int((float(img.height) * float(width_percent)))
        
        # Resize the image
        resized_img = img.resize((max_width, new_height), Image.LANCZOS)
        
        # Save the resized image to a BytesIO object
        buffered = BytesIO()
        resized_img.save(buffered, format="PNG", optimize=True, quality=85)
        
        # Encode the resized image to Base64
        encoded_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
    return encoded_string


def encode_image_to_base64_2(image, max_width=300):
    # Resize the image to have a maximum width while preserving aspect ratio

    width_percent = (max_width / float(image.width))
    new_height = int((float(image.height) * float(width_percent)))
    resized_image = image.resize((max_width, new_height), Image.ANTIALIAS)
    
    # Encode the resized image to Base64
    buffered = BytesIO()
    resized_image.save(buffered, format="PNG", optimize=True, quality=85)
    encoded_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_string



def get_profile(username, Display_name, bio, following, followers, location, website,Joined ,Born):

    location_html = f"""<img src="https://i.imgur.com/6Mm6NuX.png" style="margin:0 5px 0 0;"> {location}""" if location else ""
    website_html = f"""<img src="https://i.imgur.com/XVx9dI2.png" style="margin:0 5px;"> <a href="YOUR_JOURNAL" style="color:#1DA1F2;text-decoration:none;">{website}</a>""" if website else ""
    
    profile = f"""<!--PROFILE-->
        <div style="padding:calc((134px / 2) + 10px) 15px 15px 15px;line-height:1.2;">

            <b style="font-size:18px;display:flex;align-items:center;">{Display_name}</b>
            <div style="color:#657786;">@{username}</div>
            <div style="margin:10px 0;">{bio}</div>

            <div style="margin:10px 0;display:flex;align-items:center;flex-wrap:wrap;">
                {location_html}
                {website_html}
                <img src="https://i.imgur.com/OtC7jsU.png" style="margin:0 5px;"> {Born}
                <span style="width:100%;height:5px;"></span>
                <img src="https://i.imgur.com/Tqoplgs.png" style="margin:0 5px 0 0;"> {Joined}
            </div>


            <b> {following} </b> <span style="direction: ltr; color:#657786;">Following</span>
            <b> {followers} </b> <span style="direction: ltr; color:#657786;">Followers</span>

        </div>"""
    return profile



def get_tweet_attached_images(images_paths):
    images_filterd = []
    n_images = 0
    for elem in images_paths:
        if elem:
            images_filterd.append(encode_image_to_base64(elem, 300) )
            n_images += 1
    

    # Single image 
    if n_images == 1:
        html_element = f"""<div style="background:url('data:image/png;base64,{images_filterd[0]}') center;background-size:cover;border:1px solid #E6ECF0;border-radius:20px;overflow:hidden;height:265px;margin:10px 0 0 0;"></div>"""

    elif n_images == 2:
        html_element = f"""<div style="border:1px solid #E6ECF0;border-radius:20px;overflow:hidden;height:265px;display:flex;justify-content:space-between;margin:10px 0 0 0;">
                    <div style="background:url('data:image/png;base64,{images_filterd[0]}') center;background-size:cover;height:100%;width:calc(50% - 1px);"></div>
                    <div style="background:url('data:image/png;base64,{images_filterd[1]}') center;background-size:cover;height:100%;width:calc(50% - 1px);"></div></div>"""
    
    elif n_images == 3:
        html_element = f"""<div style="border:1px solid #E6ECF0;border-radius:20px;overflow:hidden;height:265px;display:flex;flex-direction:column;justify-content:space-between;flex-wrap:wrap;margin:10px 0 0 0;">
                    <div style="background:base64,{images_filterd[0]}') center;background-size:cover;height:100%;width:calc(50% - 1px);margin:0 2px 0 0;"></div>
                    <div style="background:base64,{images_filterd[1]}') center;background-size:cover;width:calc(50% - 1px);height:calc(50% - 1px);"></div>
                    <div style="background:base64,{images_filterd[2]}') center;background-size:cover;width:calc(50% - 1px);height:calc(50% - 1px);"></div>
                </div>"""
    elif n_images == 4:
        html_element = f"""<div style="border:1px solid #E6ECF0;border-radius:20px;overflow:hidden;height:265px;display:flex;justify-content:space-between;flex-wrap:wrap;margin:10px 0 0 0;">
                    <div style="background:base64,{images_filterd[0]}') center;background-size:cover;width:calc(50% - 1px);height:calc(50% - 1px);margin:0 0 2px 0;"></div>
                    <div style="background:base64,{images_filterd[1]}') center;background-size:cover;width:calc(50% - 1px);height:calc(50% - 1px);margin:0 0 2px 0;"></div>
                    <div style="background:base64,{images_filterd[2]}') center;background-size:cover;width:calc(50% - 1px);height:calc(50% - 1px);"></div>
                    <div style="background:base64,{images_filterd[3]}') center;background-size:cover;width:calc(50% - 1px);height:calc(50% - 1px);"></div>
                </div>"""
    
    else:
        html_element = ""


    return html_element

def get_tweet(Display_name, username, profile_image_64,tweet1, likes_1, retweets_1, comments_1,date_1, img1_1, img1_2, img1_3, img1_4):
    # get_tweet_attached_images([img1_1, img1_2, img1_3, img1_4])
    tweet = f"""        <!--TEXT TWEET - COPY PASTE AS MANY TIMES AS NEEDED-->
        <div style="padding:15px;border-bottom:1px solid #E6ECF0;display:flex;justify-content:space-between;flex-wrap:wrap;">
           
            <!--TWEET ICON-->
            <div style="width:49px;height:49px;margin:0;background:#1DA1F2 url('data:image/png;base64,{profile_image_64}') center;background-size:cover;border-radius:100%;"></div>
            
                <!--TWEET CONTENT-->
                <div style="width:calc(100% - 49px - 10px);">

                <!--TWEET HEADER-->
                <div style="display:flex;align-items:center;">
                    <b>{Display_name}</b>
                    <span style="color:#657786;margin:0 0 0 5px;">
                        @{username} · {date_1}
                    </span><br>
                    <img src="https://i.imgur.com/vFdgDXR.png" style="margin:0 0 0 auto;">
                </div>

                {tweet1}
                {get_tweet_attached_images([img1_1, img1_2, img1_3, img1_4])}
            
                <!--TWEET FOOTER-->
                <div style="display:flex;align-items:center;justify-content:center;color:#657786;font-size:12px;margin:10px 0 0 0;">
                    <img src="https://i.imgur.com/Z5VDZyK.png"> <div style="margin:0 auto 0 5px;">{comments_1}</div>
                    <img src="https://i.imgur.com/ZxkplxW.png"> <div style="margin:0 auto 0 5px;">{retweets_1}</div>
                    <img src="https://i.imgur.com/HgY5iJG.png"> <div style="margin:0 auto 0 5px;">{likes_1}</div>
                    <img src="https://i.imgur.com/vxZ6Zh9.png" style="margin:0 auto 0 0;">
                </div>

                    </div>

        </div>  """
    return tweet

def PinnedTweet(Display_name, username, profile_image_64,tweet1, likes_1, retweets_1, comments_1,date_1, img1_1, img1_2, img1_3, img1_4):

    tweet = f"""

       <div style="padding:15px;margin:0 0 10px 0;border-bottom:1px solid #E6ECF0;box-shadow:0 10px 0 0 #E6ECF0;display:flex;justify-content:space-between;flex-wrap:wrap;">

                <!--PINNED HEADER-->
                <div style="width:100%;margin:0 0 5px 40px;font-size:11px;color:#657786;display:flex;align-items:center;">
                    <img src="https://i.imgur.com/5bxnRkd.png" style="margin:0 5px 0 0;"> Pinned 
                </div>

            <!--TWEET ICON-->
            <div style="width:49px;height:49px;margin:0;background:#1DA1F2 url('data:image/png;base64,{profile_image_64}') center;background-size:cover;border-radius:100%;"></div>

                <!--TWEET CONTENT-->
                <div style="width:calc(100% - 49px - 10px);">

                <!--TWEET HEADER-->
                <div style="display:flex;align-items:center;">
                    <b>{Display_name}</b>
                    <span style="color:#657786;margin:0 0 0 5px;">
                        @{username} · {date_1}
                    </span><br>
                    <img src="https://i.imgur.com/vFdgDXR.png" style="margin:0 0 0 auto;">
                </div>

                {tweet1}

                <!--TWEET FOOTER-->
                <div style="display:flex;align-items:center;justify-content:center;color:#657786;font-size:12px;margin:10px 0 0 0;">
                    <img src="https://i.imgur.com/Z5VDZyK.png"> <div style="margin:0 auto 0 5px;">{comments_1}</div>
                    <img src="https://i.imgur.com/ZxkplxW.png"> <div style="margin:0 auto 0 5px;">{retweets_1}</div>
                    <img src="https://i.imgur.com/HgY5iJG.png"> <div style="margin:0 auto 0 5px;">{likes_1}</div>
                    <img src="https://i.imgur.com/vxZ6Zh9.png" style="margin:0 auto 0 0;">
                </div>

                    </div>

        </div>

        """
    return tweet

def Repost(Display_name, username, profile_image_64,tweet1, likes_1, retweets_1, comments_1,date_1, img1_1, img1_2, img1_3, img1_4):

   tweet = f"""        <!--TEXT TWEET - COPY PASTE AS MANY TIMES AS NEEDED-->
        <div style="padding:15px;border-bottom:1px solid #E6ECF0;display:flex;justify-content:space-between;flex-wrap:wrap;">
            <div style="width:100%;margin:0 0 5px 40px;font-size:11px;color:#657786;display:flex;align-items:center;">
                    <img src="https://i.imgur.com/ZxkplxW.png" style="margin:0 5px 0 0;"> reposted 
                </div>
            <!--TWEET ICON-->
            <div style="width:49px;height:49px;margin:0;background:#1DA1F2 url('data:image/png;base64,{profile_image_64}') center;background-size:cover;border-radius:100%;"></div>

                <!--TWEET CONTENT-->
                <div style="width:calc(100% - 49px - 10px);">

                <!--TWEET HEADER-->
                <div style="display:flex;align-items:center;">
                    <b>{Display_name}</b>
                    <span style="color:#657786;margin:0 0 0 5px;">
                        @{username} · {date_1}
                    </span><br>
                    <img src="https://i.imgur.com/vFdgDXR.png" style="margin:0 0 0 auto;">
                </div>

                {tweet1}
                {get_tweet_attached_images([img1_1, img1_2, img1_3, img1_4])}
            
                <!--TWEET FOOTER-->
                <div style="display:flex;align-items:center;justify-content:center;color:#657786;font-size:12px;margin:10px 0 0 0;">
                    <img src="https://i.imgur.com/Z5VDZyK.png"> <div style="margin:0 auto 0 5px;">{comments_1}</div>
                    <img src="https://i.imgur.com/ZxkplxW.png"> <div style="margin:0 auto 0 5px;">{retweets_1}</div>
                    <img src="https://i.imgur.com/HgY5iJG.png"> <div style="margin:0 auto 0 5px;">{likes_1}</div>
                    <img src="https://i.imgur.com/vxZ6Zh9.png" style="margin:0 auto 0 0;">
                </div>

                    </div>

        </div>  """ 
   return tweet




def get_twitter_html(
                    profile_image = None, 
                    Display_name = "Saud Alrasheed", 
                    username="saudnr33", 
                    bio = "Computer Vision Engineer and Padel Player", 
                    header_image = None, 
                    following = 00, 
                    followers = 00, 
                    location = None, 
                    website =  "saudalrasheed.com", 
                    Joined  = None,
                    Born = None ,
                    checkbox1 = False , Tweet1 = None, comments_1 = None,date_1 = None, likes_1 = None, retweets_1 = None,img1_1 = None, img1_2 = None, img1_3 = None, img1_4 = None, 
                    checkbox2 = False, Tweet2 = None, comments_2 = None,date_2 = None,likes_2 = None, retweets_2 = None,img2_1 = None, img2_2 = None, img2_3 = None, img2_4 = None, 
                    checkbox3 = False, Tweet3 = None, comments_3 = None,date_3 = None, likes_3 = None, retweets_3 = None,img3_1 = None, img3_2 = None, img3_3 = None, img3_4 = None, 
                    checkbox4 = False, Tweet4 = None, comments_4 = None,date_4 = None, likes_4 = None, retweets_4 = None,img4_1 = None, img4_2 = None, img4_3 = None, img4_4 = None, 
                    checkbox5 = False, Tweet5 = None, comments_5 = None,date_5 = None, likes_5 = None, retweets_5 = None,img5_1 = None, img5_2 = None, img5_3 = None, img5_4 = None,
                    REprofile_img = None,
                    REDisplay_name = None ,
                    REusername = None ,
                    checkrepost = False , repost1 = None , repostcomments_1 = None , repostretweets_1 = None , repostlikes_1 = None , repostdate_1 = None ,repostimg1_1 = None , repostimg1_2 =None
                    ,repostimg1_3 = None , repostimg1_4 = None ):
    REprofile_img_64 = REprofile_img
    if REprofile_img is not None :
        REprofile_img_64 = encode_image_to_base64(REprofile_img, 150)
    profile_image_64 = profile_image
    header_image_64 = header_image
    if profile_image is not None: 
        profile_image_64 = encode_image_to_base64(profile_image, 150)
    if header_image is not None :
        header_image_64 = encode_image_to_base64(header_image, 500)
    
    
    ### Build HTML

    twitter_html = f"""
    <!DOCTYPE html>
    <html>
<head>
    <meta charset="UTF-8">
</head>
    <lj-raw><div style="width:600px;margin:0 auto;background:#fff;border:1px solid #E6ECF0;color:#14171A;font-family:Open Sans,trebuchet ms,sans-serif;font-size:14px;line-height:1.5;">


        <!--HEADER-->
        <div style="direction: ltr; height:200px;background:#1DA1F2 url('data:image/png;base64,{header_image_64}') center;background-size:cover;display:flex;align-items:flex-end;">
            <div style="width:134px;height:134px;margin:0 0 calc((134px / 2) * -1) 15px;background:#1DA1F2 url('data:image/png;base64,{profile_image_64}') center;background-size:cover;border-radius:100%;border:2px solid #fff;box-sizing:border-box;"></div>

            <b style="background:#1DA1F2;color:#fff;margin:0 15px -54px auto;padding:0 25px;height:39px;line-height:39px;border-radius:30px;">Follow</b>
        
        </div>

        <div style="direction: ltr;">


        <!--PROFILE-->
        {get_profile(username, Display_name, bio, following, followers, location, website , Joined ,Born)}


        <!--VIEWING-->
        <div style="display:flex;align-items:center;text-align:center;height:52px;border-bottom:1px solid #E6ECF0;">

           <b style="height:49px;line-height:52px;width:100%;border-bottom:3px solid #1DA1F2;color:#1DA1F2;">Posts</b>
            <b style="width:100%;">Replies</b>
            <b style="width:100%;">Highlights</b>
            <b style="width:100%;">Articles</b>
            <b style="width:100%;">Media</b>
            <b style="width:100%;">Likes</b>

        </div>



      

        {PinnedTweet(Display_name, username, profile_image_64, Tweet1, likes_1, retweets_1, comments_1,date_1, img1_1, img1_2, img1_3, img1_4) if checkbox1  else ""}
        {get_tweet(Display_name, username, profile_image_64, Tweet2, likes_2, retweets_2, comments_2,date_2, img2_1, img2_2, img2_3, img2_4) if checkbox2 else ""}
        {get_tweet(Display_name, username, profile_image_64, Tweet3, likes_3, retweets_3, comments_3,date_3, img3_1, img3_2, img3_3, img3_4) if checkbox3 else ""}
        {Repost(REDisplay_name, REusername, REprofile_img_64, repost1, repostlikes_1, repostretweets_1, repostcomments_1,repostdate_1, repostimg1_1, repostimg1_2, repostimg1_3, repostimg1_4) if checkrepost  else ""}
        {get_tweet(Display_name, username, profile_image_64, Tweet4, likes_4, retweets_4, comments_4,date_4, img4_1, img4_2, img4_3, img4_4) if checkbox4 else ""}
        {get_tweet(Display_name, username, profile_image_64, Tweet5, likes_5, retweets_5, comments_5,date_5, img5_1, img5_2, img5_3, img5_4) if checkbox5 else ""}



    </div>

    </div></lj-raw>
    </html>
    """


    encoded_content = base64.b64encode(twitter_html.encode()).decode()

    html_content = f"""
    <iframe src="data:text/html;base64,{encoded_content}" style="width:100%; height:1200px; border:none;"></iframe>
    """
    return html_content