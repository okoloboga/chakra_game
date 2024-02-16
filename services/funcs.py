import time
from math import log2

from database.database import users_db
from lexicon.lexicon import LEXICON_MULTS

def add_power(user_id: int, previos: str, next: str, mod: int):
    users_db[user_id]['chakra'][next]  += users_db[user_id]['chakra'][previos] // mod
    users_db[user_id]['chakra'][previos] = users_db[user_id]['chakra'][previos] % mod

def wait_process(user_id: int):

    users_db[user_id]['time_1'] = time.time()
    steps = (users_db[user_id]['time_1'] - users_db[user_id]['time_0']) * users_db[user_id]['speed']
    users_db[user_id]['time_0'] = users_db[user_id]['time_1']

    users_db[user_id]['chakra']['dharana'] += steps

    if   users_db[user_id]['chakra']['dharana'] >= 13:
         add_power(user_id, 'dharana', 'dhyana', 13)

    if users_db[user_id]['chakra']['dhyana'] >= 13:
         add_power(user_id, 'dhyana', 'samadhi', 13)

    if users_db[user_id]['chakra']['samadhi'] >= 13:
         add_power(user_id, 'samadhi', 'muladhara', 13)
    
    if users_db[user_id]['chakra']['muladhara'] >= 5:
         add_power(user_id, 'muladhara', 'svadhishthana', 5)

    if users_db[user_id]['chakra']['svadhishthana'] >= 7:
         add_power(user_id, 'svadhishthana', 'manipura', 7)
        
    if users_db[user_id]['chakra']['manipura'] >= 11:
         add_power(user_id, 'manipura', 'anahata', 11)

    if users_db[user_id]['chakra']['anahata'] >= 13:
         add_power(user_id, 'anahata', 'vishuddha', 13)
         
    if users_db[user_id]['chakra']['vishuddha'] >= 17:
         add_power(user_id, 'vishuddha', 'ajna', 17)

    if users_db[user_id]['chakra']['ajna'] >= 3:
         add_power(user_id, 'ajna', 'sahasrara' , 3)
    
    if users_db[user_id]['chakra']['sahasrara'] >= 1001:
         users_db[user_id]['nirvana'] += 1

# Сокращение тысяч и миллионов
def to_k_m(param: str, user_id: int) -> str:
     if users_db[user_id][param] < 1000:
          will = users_db[user_id][param]
     elif 1000 <= users_db[user_id][param] < 10**6:
          will = str("{:.1f}".format(users_db[user_id][param] / 1000)) + "K"
     elif 10**6 <= users_db[user_id][param] < 10**9:
          will = str("{:.1f}".format(users_db[user_id][param] / 10**6)) + "M"
     elif 10**9 <= users_db[user_id][param] < 10**12:
          will = str("{:.1f}".format(users_db[user_id][param] / 10**9)) + "B"
     elif 10**12 <= users_db[user_id][param] < 10**15:
          will = str("{:.1f}".format(users_db[user_id][param] / 10**12)) + "T"
     return will

# Основное сообщение процесса
def main_process_answer(user_id: int):
     
     emp = ['▫️']
     
     dha = ['🛐' for _ in range(int(users_db[user_id]['chakra']['dharana']))]
     for _ in range(12 - int(users_db[user_id]['chakra']['dharana'])):
          dha.append('▫️')

     dhy = ['☸️' for _ in range(int(users_db[user_id]['chakra']['dhyana']))]
     for _ in range(12 - int(users_db[user_id]['chakra']['dhyana'])):
          dhy.append('▫️')
     
     sam = ['☯️' for _ in range(int(users_db[user_id]['chakra']['samadhi']))]
     for _ in range(12 - int(users_db[user_id]['chakra']['samadhi'])):
          sam.append('▫️')

     mul = ['❤️' for _ in range(int(users_db[user_id]['chakra']['muladhara']))]
     for _ in range(4 - int(users_db[user_id]['chakra']['muladhara'])):
          mul.append('▫️')

     sva = ['🧡' for _ in range(int(users_db[user_id]['chakra']['svadhishthana']))]
     for _ in range(6 - int(users_db[user_id]['chakra']['svadhishthana'])):
          sva.append('▫️')

     man = ['💛' for _ in range(int(users_db[user_id]['chakra']['manipura']))]
     for _ in range(10 - int(users_db[user_id]['chakra']['manipura'])):
          man.append('▫️')

     ana = ['💚' for _ in range(int(users_db[user_id]['chakra']['anahata']))]
     for _ in range(12 - int(users_db[user_id]['chakra']['anahata'])):
          ana.append('▫️')

     vis = ['💠' for _ in range(int(users_db[user_id]['chakra']['vishuddha']))]
     for _ in range(16 - int(users_db[user_id]['chakra']['vishuddha'])):
          vis.append('▫️')

     ajn = ['🧿' for _ in range(int(users_db[user_id]['chakra']['ajna']))]
     for _ in range(2 - int(users_db[user_id]['chakra']['ajna'])):
          ajn.append('▫️')

     sah = str('💟 ' + str(int(to_k_m('sahasrara', user_id))))
     speed = str(int(log2(users_db[user_id]['speed'])))
     
     will = to_k_m('will', user_id)

     answer=str('▫️▫️🕉<b>СОЗЕРЦАЙ</b> 🕉▫️▫️▫️\n'
               f"▫️▫️▫️👁Воля👁 <b>{will}</b>▫️▫️▫️\n"
               f"▫️▫️🌀Скорость🌀 <b>{speed}</b>▫️▫️▫️\n\n"
               f"{''.join(dha)}\n{''.join(dhy)}\n{''.join(sam)}\n{''.join(mul)}\n{''.join(sva)}\n"
               f"{''.join(man)}\n{''.join(ana)}\n{''.join(vis)}\n{''.join(ajn)}\n{''.join(sah)}\n\n"
               '<b>12</b>🛐➡️☸️   <b>12</b>☸️➡️☯️   <b>12</b>☯️➡️❤️\n\n'
               '<b>4</b>❤️➡️🧡     <b>6</b>🧡➡️💛     <b>10</b>💛➡️💚\n\n'
               '<b>12</b>💚➡️💠   <b>16</b>💠➡️🧿   <b>2</b>🧿➡️💟')

     return answer

# Жатва Чакр
def mantra_process(user_id: int, chakra: str):

     if chakra == 'will':
          if users_db[user_id]['will'] >= users_db[user_id]['speed']:
              users_db[user_id]['will'] -= users_db[user_id]['speed']
              users_db[user_id]['speed'] *= 2
     
     else:
          mult = LEXICON_MULTS[chakra]
          if users_db[user_id]['chakra'][chakra] >= 1:
               users_db[user_id]['will'] += int(mult * users_db[user_id]['chakra'][chakra])
               users_db[user_id]['chakra'][chakra] = 0
     