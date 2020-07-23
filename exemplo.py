from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz

API = IQ_Option('login', 'senha')
API.connect()
API.change_balance('PRACTICE') # PRACTICE / REAL

while True:
	if API.check_connect() == False:
		print('Erro ao se conectar')
		API.connect()
	else:
		print('Conectado com sucesso!')
		break
	
	time.sleep(1)


def perfil(): # Função para capturar informações do perfil
	perfil = json.loads(json.dumps(API.get_profile_ansyc()))
	
	return perfil
	
	'''
		name
		first_name
		last_name
		email
		city
		nickname
		currency
		currency_char 
		address
		created
		postal_index
		gender
		birthdate
		balance		
	'''
    
def timestamp_converter(x): # Função para converter timestamp
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	
	return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]
	
x=perfil()
print("Nome: ",(x['name']),)
print("Balanço atual: ",(API.get_balance()),)

par = 'EURUSD'

API.start_candles_stream(par, 60, 1)
time.sleep(1)



while True:
	vela = API.get_realtime_candles(par, 60)
	for velas in vela:
		print(vela[velas]['close'])
	time.sleep(1)
API.stop_candles_stream(par, 60)

