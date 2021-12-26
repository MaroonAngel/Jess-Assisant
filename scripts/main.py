import sys
sys.path.insert(0, 'E:\My Stuff\Portfolio\Other\Jess\Jarvis_AI\JarvisAI\JarvisAI');
import JarvisAI
import os
import re
import pprint
import random
import warnings

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")

obj = JarvisAI.JarvisAssistant(sync=False, token='adc0a911a43f8b5edce4b44f4c8762', disable_msg=False,
                               load_chatbot_model=False, high_accuracy_chatbot_model=False,
                               chatbot_large=False, backend_tts_api='pyttsx3')


def t2s(text):
    obj.text2speech(text)


def start():
    print("> Listening for name...")
    while True:        
        status, command = obj.hot_word_detect()
        if status:
            print(command)
        if status:
            while True:
                # use any one of them
                print(">> Awaiting input...")
                res = obj.mic_input()
                res = res.lower()
                # res = obj.mic_input_ai(debug=True)
                
                if re.search("shut down|turn off|shutdown", res):
                    t2s("Sure thing! Bye!")
                    print("Shutting down.")
                    exit()
                    break;

                if re.search("jokes|joke|Jokes|Joke", res):
                    joke_ = obj.tell_me_joke('en', 'neutral')
                    print(joke_)
                    t2s(joke_)
                    break;

                elif re.search('setup|set up', res):
                    setup = obj.setup()
                    print(setup)
                    break;

                elif re.search('google photos', res):
                    photos = obj.show_google_photos()
                    print(photos)
                    break;

                elif re.search('local photos', res):
                    photos = obj.show_me_my_images()
                    print(photos)
                    break;

                elif re.search('weather|temperature', res):
                    city = res.split(' ')[-1]
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    t2s(weather_res)
                    break;

                elif re.search('news', res):
                    news_res = obj.news()
                    pprint.pprint(news_res)
                    t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
                    t2s(news_res[0])
                    t2s(news_res[1])
                    break;

                elif re.search('tell me about', res):
                    topic = res[14:]
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    t2s(wiki_res)
                    break;

                elif re.search('date', res):
                    date = obj.tell_me_date()
                    print(date)
                    print(t2s(date))
                    break;

                elif re.search('time', res):
                    time = obj.tell_me_time()
                    print(time)
                    t2s(time)
                    break;

                elif re.search('open', res):
                    domain = res.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    print(open_result)
                    break;

                elif re.search('launch', res):
                    dict_app = {
                        'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                        'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
                    }

                    app = res.split(' ', 1)[1]
                    path = dict_app.get(app)
                    if path is None:
                        t2s('Application path not found')
                        print('Application path not found')
                    else:
                        t2s('Launching: ' + app)
                        obj.launch_any_app(path_of_app=path)
                    break;

                elif re.search('hello|hi', res):
                    print('Hi')
                    t2s('Hi')
                    break;

                elif re.search('how are you', res):
                    li = ['good', 'fine', 'great']
                    response = random.choice(li)
                    print(f"I am {response}")
                    t2s(f"I am {response}")
                    break;

                elif re.search('your name|who are you', res):
                    print("I am your personal assistant")
                    t2s("I am your personal assistant")
                    break;

                elif re.search('what can you do', res):
                    li_commands = {
                        "open websites": "Example: 'open youtube.com",
                        "time": "Example: 'what time it is?'",
                        "date": "Example: 'what date it is?'",
                        "launch applications": "Example: 'launch chrome'",
                        "tell me": "Example: 'tell me about India'",
                        "weather": "Example: 'what weather/temperature in Mumbai?'",
                        "news": "Example: 'news for today' ",
                    }
                    ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
                    I can open websites for you, launch application and more. See the list of commands-"""
                    print(ans)
                    pprint.pprint(li_commands)
                    t2s(ans)
                    break;
                    
                elif re.search('tech news', res):
                    obj.show_me_some_tech_news()
                    break;

                elif re.search('tech videos', res):
                    obj.show_me_some_tech_videos()
                    break;

                elif re.search(r"^add *.+ list$", res):
                    obj.create_new_list(res)
                    break;

                elif re.search(r"^show *.+ list$", res):
                    obj.show_me_my_list()
                    break;

                elif re.search(r"^delete *.+ list$", res):
                    obj.delete_particular_list(res)
                    break;

                else:
                    # chatbot_response = obj.chatbot_base(input_text=res)  # comment this line if you want to use chatbot large
                    # chatbot_response = obj.chatbot_large(input_text=res) # uncomment this line to use large model for heavy/complex tasks

                    print("-- Didn't understand. Going back to waiting... --")
                    t2s("kay.")
                    break;
                    
        else:
            continue


if __name__ == "__main__":
    if not os.path.exists("configs/config.ini"):
        print(os.listdir())
        res = obj.setup()
        if res:
            print("Settings Saved. Restart your Assistant")
    else:
        start()
