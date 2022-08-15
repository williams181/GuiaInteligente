#abrindo arquivo texto
PATH = "data\\flickr8k\\input"

with open(PATH+"Flickr8k.token.txt") as f:
    data = f.read()
	
# chave contínua do dicionário como image_id e valor como lista de legendas.
descriptions = dict()

try:
    for el in data.split("\n"):
        tokens = el.split()
        image_id , image_desc = tokens[0],tokens[1:]

        # removendo .jpg do id da imagem
        image_id = image_id.split(".")[0]

        image_desc = " ".join(image_desc)
        
        # verifica se image_id já está presente ou não
        if image_id in descriptions:
            descriptions[image_id].append(image_desc)
        else:
            descriptions[image_id] = list()
            descriptions[image_id].append(image_desc)
except Exception as e: 
    print("Exception got :- \n",e)

descriptions["1000268201_693b08cb0e"]


