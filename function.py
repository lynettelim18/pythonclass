def fahr_to_kelvin (temp):
	return ((temp -32)* (5/9) + 273.15)
	
def kelvin_to_celsius(temp_k):
	return temp_k - 273.15

def fahr_to_celsius (temp_f):
	temp_k = fahr_to_kelvin(temp_f)
	result = kelvin_to_celsius (temp_k)
	return result
	
	
print('freezing pt H2O in kelvin: ', fahr_to_kelvin (32))
print('freezing pt H2O in celcuis: ', kelvin_to_celsius (0))	
print('freezing pt H2O in celcuis starting from fahr: ', fahr_to_celsius (32))	