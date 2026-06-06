import discord
import random
from unidecode import unidecode
from difflib import get_close_matches
intents = discord.Intents.default()
intents.message_content = True
File_name="Your_database"
client = discord.Client(intents=intents)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.80)
    return matches[0] if matches else None
def find_copy(File_name, tekst):
      with open (File_name, "r") as file:  
        lines = file.readlines()  
        file_content = '\n'.join(lines)
        if tekst in file_content:
            return 0
        else:
            best_match = find_best_match(tekst, lines)
            if best_match is not None:
                print(f"Best match'{tekst}': {best_match}")
                return 0
            else:
                return 1
def Draw_line(File_name):
    with open(File_name, 'r') as file:
        linie = file.readlines()
    if not linie:
        return None,None
    Line_number = random.randint(0, len(linie) - 1)
    Quote = linie[Line_number].strip() 

    return Quote, Line_number
def add_to_file(File_name, tekst):
    with open(File_name, "a") as file:
        Base_text=find_copy(File_name, tekst)
        if Base_text==1: 
          file.write("\n"+tekst)
          print("Save succes")
          return True
        if Base_text==0:
          print("Save falure")
          return False
        else:
          print("Database error")
          return False

@client.event
async def on_ready():
    print(f'Log as {client.user}')

@client.event
async def on_message(message):



    if message.content.startswith('!add'):
      komenda, *wiadomosc = message.content.split(' ', 1)
      if wiadomosc:  
            tekst = ''.join(wiadomosc)
            odpowiedz_bazy=add_to_file(File_name, tekst)
            if odpowiedz_bazy==True:
              response = f'Saved as: "{tekst}"'
              await message.channel.send(response)
            if odpowiedz_bazy==False:
              response = tekst+" already in database"
              await message.channel.send(response)

    if message.author == client.user:
        return

    if message.content.lower().startswith('!bo'):
        if len(message.mentions) > 0:
            user = message.mentions[0]
        else:
            user = message.author
        
        if user==message.author:
           Quote, Line_number = Draw_line(File_name)
           response = f' reason:  #{Line_number}: {Quote}'
           await message.channel.send(response)
        if user==message.mentions[0]:
           Quote, Line_number = Draw_line(File_name)
           response = f'{user.mention}Im very sorry, but my client is unable to take part in this activity because: #{Line_number}: {Quote}'
           await message.channel.send(response)
 
BOT_TOKEN = 'Your bot token'
client.run(BOT_TOKEN)