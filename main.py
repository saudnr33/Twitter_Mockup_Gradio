import gradio as gr
import base64
from twitter_mockup import get_twitter_html






def show_component(counter):
    counter += 1
    counter = min(5, counter)
    update_rule = [gr.update(visible= i < counter) for i in range(5)]
    update_rule.append(counter)
    return update_rule
def hide_component(counter):
    counter += -1
    counter = max(1, counter)
    update_rule = [gr.update(visible= i < counter) for i in range(5)]
    update_rule.append(counter)
    return update_rule


with gr.Blocks() as demo:
    
    #State variable
    counter = gr.State(1)

    with gr.Row():
        generate_button = gr.Button("Generate Twitter Mockup")

    with gr.Row():

        with gr.Column():

            html_page = gr.HTML()
        
        with gr.Column():

            with gr.Accordion("Mockup Settings"):
                with gr.Row():
                    with gr.Column():
                        profile_img = gr.Image(label="Upload Profile Image", type="filepath", value = "assets/3174071699665935867.png")
                    with gr.Column():
                        header_img = gr.Image(label="Upload Header Image", type="filepath", value="assets/header_kafd.jpg")
                with gr.Row():
                    with gr.Column():
                        with gr.Row():
                            Display_name = gr.Textbox(label= "Name", value="Saud Alrasheed")
                            username = gr.Textbox(label = "Username", value="saudnr33")
                            bio = gr.Textbox(label = "Bio", value="Computer Vision Engineer and Padel Player")
                        with gr.Row():
                            following = gr.Textbox(label= "Following", value="348")
                            followers = gr.Textbox(label = "Followers", value="417")
                            location = gr.Textbox(label = "Location", value="Riyadh, Saudi Arabia")
                            Born = gr.Textbox(label ="Born" , value = "Born July 28" )
                            Joined =gr.Textbox(label= "Joind", value="Joined February 2024")  

                        with gr.Row():
                            website = gr.Textbox(label = "Website", value="saudalrasheed.com")
                with gr.Row():
                    with gr.Column():
                        with gr.Row():
                            add_tweet = gr.Button("Add Tweet")
                            delete_tweet = gr.Button("Remove Tweet")
                            add_Reposted = gr.Button("Add Reposted")
                            delete_Reposted = gr.Button("Remove Reposted")
                        with gr.Row():
                            with gr.Column():
                                accordion1 = gr.Accordion("Pinned Tweet ", visible=True)
                                with accordion1:
                                    with gr.Row():
                                        Tweet1 = gr.Textbox(label= "Tweet", value="I'm tweeting, tweet tweet.")
                                        checkbox1 = gr.Checkbox(label = "Add Tweet?", value=True)
                                        
                                    with gr.Row():
                                        comments_1 = gr.Textbox(label= "Comments", value="17")
                                        retweets_1 = gr.Textbox(label= "Retweets", value="36")
                                        likes_1 = gr.Textbox(label= "Likes", value="167")
                                        date_1 = gr.Textbox(label= "Date", value="May 09")

                                    with gr.Row():
                                        with gr.Column():
                                            img1_1 = gr.Image(label="Image 1", type="filepath", value="assets/header_kafd.jpg", interactive= True)
                                            img1_2 = gr.Image(label="Image 1", type="filepath", interactive= True, visible= False) # hide now for future use
                                        with gr.Column():
                                            img1_3 = gr.Image(label="Image 1", type="filepath", interactive= True)
                                            img1_4 = gr.Image(label="Image 1", type="filepath", interactive= True, visible=False) # hide now for future use

                                accordion2 = gr.Accordion("Tweet 2", visible=False)
                                with accordion2:
                                    with gr.Row():
                                        Tweet2 = gr.Textbox(label= "Tweet", placeholder="I'm tweeting, tweet tweet.")
                                        checkbox2 = gr.Checkbox(label = "Add Tweet?", value=False)
                                    with gr.Row():
                                        comments_2 = gr.Textbox(label= "Comments", placeholder="17")
                                        retweets_2 = gr.Textbox(label= "Retweets", placeholder="36")
                                        likes_2 = gr.Textbox(label= "Likes", placeholder="167")
                                        date_2 = gr.Textbox(label= "Date", value="May 09")

                                    with gr.Row():
                                        with gr.Column():
                                            img2_1 = gr.Image(label="Image 1", type="filepath", interactive= True)
                                            img2_2 = gr.Image(label="Image 3", type="filepath", interactive= True, visible= False) # hide now for future use
                                        with gr.Column():
                                            img2_3 = gr.Image(label="Image 2", type="filepath", interactive= True)
                                            img2_4 = gr.Image(label="Image 4", type="filepath", interactive= True, visible=False) # hide now for future use


                                accordion3 = gr.Accordion("Tweet 3", visible=False)
                                with accordion3:
                                    with gr.Row():
                                        Tweet3 = gr.Textbox(label= "Tweet", placeholder="I'm tweeting, tweet tweet.")
                                        checkbox3 = gr.Checkbox(label = "Add Tweet?", value=False)
                                    with gr.Row():
                                        comments_3 = gr.Textbox(label= "Comments", placeholder="17")
                                        retweets_3 = gr.Textbox(label= "Retweets", placeholder="36")
                                        likes_3 = gr.Textbox(label= "Likes", placeholder="167")
                                        date_3 = gr.Textbox(label= "Date", value="May 09")

                                    with gr.Row():
                                        with gr.Column():
                                            img3_1 = gr.Image(label="Image 1", type="filepath", interactive= True)
                                            img3_2 = gr.Image(label="Image 3", type="filepath", interactive= True, visible= False) # hide now for future use
                                        with gr.Column():
                                            img3_3 = gr.Image(label="Image 2", type="filepath", interactive= True)
                                            img3_4 = gr.Image(label="Image 4", type="filepath", interactive= True, visible=False) # hide now for future use


                                accordion4 = gr.Accordion("Tweet 4", visible=False)
                                with accordion4:
                                    with gr.Row():
                                        Tweet4 = gr.Textbox(label= "Tweet", placeholder="I'm tweeting, tweet tweet.")
                                        checkbox4 = gr.Checkbox(label = "Add Tweet?", value=False)
                                    with gr.Row():
                                        comments_4 = gr.Textbox(label= "Comments", placeholder="17")
                                        retweets_4 = gr.Textbox(label= "Retweets", placeholder="36")
                                        likes_4 = gr.Textbox(label= "Likes", placeholder="167")
                                        date_4 = gr.Textbox(label= "Date", value="May 09")

                                    with gr.Row():
                                        with gr.Column():
                                            img4_1 = gr.Image(label="Image 1", type="filepath", interactive= True)
                                            img4_2 = gr.Image(label="Image 3", type="filepath", interactive= True, visible= False) # hide now for future use
                                        with gr.Column():
                                            img4_3 = gr.Image(label="Image 2", type="filepath", interactive= True)
                                            img4_4 = gr.Image(label="Image 4", type="filepath", interactive= True, visible=False) # hide now for future use

                                accordion5 = gr.Accordion("Tweet 5", visible=False)
                                with accordion5:
                                    with gr.Row():
                                        Tweet5 = gr.Textbox(label= "Tweet", placeholder="I'm tweeting, tweet tweet.")
                                        checkbox5 = gr.Checkbox(label = "Add Tweet?", value=False)
                                    with gr.Row():
                                        comments_5 = gr.Textbox(label= "Comments", placeholder="17")
                                        retweets_5 = gr.Textbox(label= "Retweets", placeholder="36")
                                        likes_5 = gr.Textbox(label= "Likes", placeholder="167")
                                        date_5 = gr.Textbox(label= "Date", value="May 09")

                                    with gr.Row():
                                        with gr.Column():
                                            img5_1 = gr.Image(label="Image 1", type="filepath", interactive= True)
                                            img5_2 = gr.Image(label="Image 3", type="filepath", interactive= True, visible= False) # hide now for future use
                                        with gr.Column():
                                            img5_3 = gr.Image(label="Image 2", type="filepath", interactive= True)
                                            img5_4 = gr.Image(label="Image 4", type="filepath", interactive= True, visible=False) # hide now for future use
                    with gr.Row():
                        with gr.Column():
                            accordion6 = gr.Accordion("Repoost Tweet ", visible=False)
                            with accordion6:
                                with gr.Row():
                                    REprofile_img = gr.Image(label="Upload Profile Image", type="filepath", value = "assets/yMneXppa_400x400.jpg")
                                    REDisplay_name = gr.Textbox(label= "Name", value="Fahad Alshaya")
                                    REusername = gr.Textbox(label = "Username", value="FahadAls")
                                    repost1 = gr.Textbox(label= "Tweet", value="I'm tweeting, tweet tweet.")
                                    checkrepost = gr.Checkbox(label = "Repost?", value=False)
                                        
                                with gr.Row():
                                    repostcomments_1 = gr.Textbox(label= "Comments", value="17")
                                    repostretweets_1 = gr.Textbox(label= "Retweets", value="36")
                                    repostlikes_1 = gr.Textbox(label= "Likes", value="167")
                                    repostdate_1 = gr.Textbox(label= "Date", value="May 09")
                                    
                                with gr.Row():
                                    with gr.Column():
                                        repostimg1_1 = gr.Image(label="Image 1", type="filepath", value="assets/header_kafd.jpg", interactive= True)
                                        repostimg1_2 = gr.Image(label="Image 1", type="filepath", interactive= True, visible= False) # hide now for future use
                                    with gr.Column():
                                        repostimg1_3 = gr.Image(label="Image 1", type="filepath", interactive= True)
                                        repostimg1_4 = gr.Image(label="Image 1", type="filepath", interactive= True, visible=False) # hide now for future use


    generate_button.click(get_twitter_html, inputs=[profile_img, Display_name, username, bio, header_img, following, followers, location, website, Joined ,Born,
                                                    checkbox1 ,Tweet1, comments_1,date_1, likes_1, retweets_1,img1_1, img1_2, img1_3, img1_4,
                                                    checkbox2, Tweet2, comments_2,date_2, likes_2, retweets_2,img2_1, img2_2, img2_3, img2_4, 
                                                    checkbox3, Tweet3, comments_3,date_3, likes_3, retweets_3,img3_1, img3_2, img3_3, img3_4, 
                                                    checkbox4, Tweet4, comments_4,date_4, likes_4, retweets_4,img4_1, img4_2, img4_3, img4_4, 
                                                    checkbox5, Tweet5, comments_5,date_5,likes_5, retweets_5,img5_1, img5_2, img5_3, img5_4,
                                                    REprofile_img,REDisplay_name,REusername,checkrepost,repost1,repostcomments_1,repostretweets_1,repostlikes_1,repostdate_1,repostimg1_1,
                                                    repostimg1_2,repostimg1_3,repostimg1_4], outputs=html_page)
    add_tweet.click(show_component,inputs =[counter],  outputs=[accordion1, accordion2, accordion3, accordion4, accordion5 , counter])
    delete_tweet.click(hide_component,inputs = [counter],  outputs=[accordion1, accordion2, accordion3, accordion4, accordion5 , counter])
    add_Reposted.click(show_component,inputs =[counter],outputs=[accordion6,counter])
    delete_Reposted.click(hide_component , inputs = [counter],outputs=[accordion6,counter])
demo.launch()

