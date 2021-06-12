# About the Script

I use three modules, openai, speech_recognition and pyttsx3. Together they work to take in text and input it into whatever GPT-3 set up you’ve got going on. 
I primarily use it to chat.I’m sharing this because I really don’t see all that many ‘basic’ scripts using the openai library and it was kind of annoyingly obtuse to 
get this running. I spent around a day just to get this working, which added up to a lot of questions to a poor and confused API that was sick of me by the time I was
done.(Seriously, that was really cool. GPT-3 got bored of me asking the same question on completely different prompts.) Learned quite a decent amount, not a big python 
guy, but I think the script runs well and takes tweaks fluently.


# Notes

## Running the script

### Installation

Install the required libraries through pip, by running 'pip install -r requirements.txt' the file is in the repo

## Running the script

Run a terminal and navigate to the repo file and run 'python Speech-to-text-to-Speech.py' It will ask you to speak. Do so and wait a bit for it to process. Boom.
RESULTS!

## Variables

The only Variable you're probably interested in should be **'myPrompt'** and the **'{SpeechText}'** string inside of it. You can change the prompt, but definitely look at how
I laid it out. The API reacts a bit differently here and I think that's due to a lack of punctuation and on top of that, some issues with new lines. So the best way
I found for this to work was the way I got it laid out, aka 'Human:{SpeechText} \nAI:' That way GPT-3 just picks it up from the point of interest.

### IMPORTANT NOTE! 

## This script will not run without an API key from openai.com

## Some things I’d like to develop further:

1.) The speech to text system is not great at taking in commas and periods. It really misses a lot of the nuance that this AI seems to thrive on. So any recommendations on libraries are welcome.

2.) Hopefully I find a more calming voice than Microsoft Sam (Despite his nostalgic value). If anyone recommends some solution for that, it would be awesome.

3.) Some visuals would be nice, maybe see if I can make API calls with the AI results and get a sentiment grading on it and represent that in the graphic (frowny face/smile etc. etc.)

Feel free to share any tips and to fork/use this freely.
