import random
from colorama import init, Fore, Back, Style
from pycenter import center
from pystyle import Anime, Colorate, Colors, Center, System, Write
import time
from discord import Webhook, RequestsWebhookAdapter
import string




class build:
  def __init__(self, imagepath: str, scale: int) -> None:
    self.path = imagepath
    self.scale = scale

    return self.run()

  def run(self) -> None:
    img = self.mkimage(path=self.path)
    pixels = self.mkpixels(img=img)
    ascii = self.mkascii(pixels=pixels)

    with open(self.npath, mode="w", encoding='utf-8') as f:
      f.write(ascii)
    
    return None

  def mkimage(self, path: str) -> object:
    img = Image.open(path)
    width, height = img.size

    self.nwidth = round(width / self.scale)

    img = img.resize((self.nwidth, round(height / (self.scale * 2))))

    return img.convert('L')

  def mkpixels(self, img: object) -> str:
    pixels = img.getdata()

    pixels = [self.chars[pixel//25] for pixel in pixels]
    return ''.join(pixels).replace('.',' ')

  def mkascii(self, pixels: str) -> str:
    ascii = [pixels[index:index + self.nwidth] for index in range(0, len(pixels), self.nwidth)]
    nascii = []
    for line in ascii:
      if line.strip():
        nascii.append(line)
    return "\n".join(nascii)

  @property
  def npath(self) -> str:
    return ".".join(self.path.split(".")[:-1]) + ".txt"

  @property
  def chars(self) -> str:
    return ["§","/","#","&","@","$","%","*","!",":","."]



ascii = """
 /$$   /$$ /$$   /$$                          /$$$$$$                     
| $$$ | $$|__/  | $$                         /$$__  $$                    
| $$$$| $$ /$$ /$$$$$$    /$$$$$$   /$$$$$$  | $$  \__/  /$$$$$$  /$$$$$$$ 
| $$ $$ $$| $$|_  $$_/   /$$__  $$ /$$__  $$ | $$ /$$$$ /$$__  $$| $$__  $$
| $$  $$$$| $$  | $$    | $$  \__/| $$  \ $$ | $$|_  $$| $$$$$$$$| $$  \ $$
| $$\  $$$| $$  | $$ /$$| $$      | $$  | $$ | $$  \ $$| $$_____/| $$  | $$
| $$ \  $$| $$  |  $$$$/| $$      |  $$$$$$/ |  $$$$$$/|  $$$$$$$| $$  | $$
|__/  \__/|__/   \___/  |__/       \______/  \______/  \_______/|__/  |__/
                                                                          
"""[1:]


Logo = '''
                    @@@@@@@@@@@@@@@@                    
               &@@@@@@@@@@@@@@@@@@@@@@@@&               
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            
         &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&         
       &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&       
     :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:     
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
   @@@@@@@@@@@@@@@@@@% @@@@@@@@@@ *@@@@@@@@@@@@@@@@@@   
  @@@@@@@@@@@@@@                        @@@@@@@@@@@@@@  
 &@@@@@@@@@@@@%                          !@@@@@@@@@@@@& 
 @@@@@@@@@@@@!                             @@@@@@@@@@@@ 
@@@@@@@@@@@@$                              !@@@@@@@@@@@@
@@@@@@@@@@@@                                &@@@@@@@@@@@
@@@@@@@@@@@         &@@@$      !@@@@         @@@@@@@@@@@
@@@@@@@@@@@        &@@@@@      @@@@@@        &@@@@@@@@@@
@@@@@@@@@@@        $@@@@@      @@@@@&        %@@@@@@@@@@
@@@@@@@@@@*                                  :@@@@@@@@@@
 @@@@@@@@@*                                  :@@@@@@@@@ 
 &@@@@@@@@@       :@&              &&:       &@@@@@@@@& 
  @@@@@@@@@@@&       &@@@@@@@@@@@@@       &@@@@@@@@@@@  
   @@@@@@@@@@@@@@@* @@@@@@@@@@@@@@@@ !&@@@@@@@@@@@@@@   
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
     :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:     
       &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&       
         &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&         
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@            
               &@@@@@@@@@@@@@@@@@@@@@@@@&               
                    @@@@@@@@@@@@@@@@    
                    
                    Press [Enter]                
'''[1:]




System.Size(140, 40)
System.Title("NitroGen")
System.Clear()
Anime.Fade(Center.Center(Logo), Colors.blue_to_green, Colorate.Vertical, interval=0.025, enter=True)

def gen():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(ascii)))
  print("\n"*5)
  
  link = input('Webhook url: ')
  amount = int(input('How many code to generate: '))
  for i in range(amount):
      time.sleep(5)
      code = 'https://discord.gift/' + "".join(random.choices(string.ascii_letters + string.digits, k=16))
      print("Code Generated !" + code)
      webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
      webhook.send(code)
gen()
        
    