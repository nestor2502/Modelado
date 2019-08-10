#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form/', offset = 0):
	args = {'offset': offset} if offset else{}

	response = requests.get(url, params = args) #se realiza la posicion

	if response.status_code == 200:
		payload = response.json()
		results = payload.get('results', [])

		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)
		next = raw_input("¿Continuar listando? [Y/N]").lower()
		if next == 'y':
			get_pokemons(offset=offset+20)

__name__ = '__main__'
if __name__ == '__main__':
	url = 'https://pokeapi.co/api/v2/pokemon-form/'
	get_pokemons()
    
	


