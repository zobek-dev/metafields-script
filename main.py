import requests
import time
import json

# Configuración de la autenticación y la URL de la tienda
api_key = '34b78d117a087315253794492dfa3757'
password = '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'
store_url = 'https://disena-sustentable-chile.myshopify.com'

products_ids=[]
metafields_ids=[]

def get_all_product_ids():
  url = f'{store_url}/admin/api/2023-04/products.json?limit=250'
  
  headers = {
    'Content-Type': 'application/json',
  }
  
  response = requests.get(url, auth=(api_key, password), headers=headers)
  
  if response.status_code == 200:
    products = response.json()['products']
    product_ids = [product['id'] for product in products]
    return product_ids
  else:
    print(f'Error al obtener la lista de productos: {response.text}')
    return None
  
def get_product_metafield_id(id):
  # value = '[{"brand":"Alchemy","url":"https://www.shop-alchemy.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Coreana","url":"https://www.coreanachile.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Bambusa","url":"https://www.bambusa.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Benamor","url":"https://www.benamor1925.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Ecoshampoo","url":"https://www.ecoshampoo.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Evolve Beauty","url":"https://www.caretobeauty.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Labcconte","url":"https://www.labcconte.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Nerea Skincare","url":"https://www.nereaskincare.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Qullantu","url":"https://www.qullantu.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Newen","url":"https://www.newencosmetica.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"The Organik Formula","url":"https://www.theorganikformula.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"All Bnat","url":"https://www.allbnat.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Casita Rimu","url":"https://www.casitarimu.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Cuwu Eco Solucion","url":"https://www.cuwu.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Ecobee Soluciones","url":"https://www.ecobeechile.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Envuelbee","url":"https://www.envuelbee.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Fue","url":"https://www.fue.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Hokka","url":"https://www.hokka.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Klean Kanteen","url":"https://www.kleankanteen.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Late!","url":"https://www.late.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Maria Jose Design","url":"https://mariajosevasquezdesign.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Muka","url":"https://www.muka.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Puur","url":"https://www.puurbottle.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Tapperbee","url":"https://www.tapper-bee.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Amor Mio","url":null,"instagram":"https://www.instagram.com/amrescatetextil/","facebook":null,"tiktok":null},{"brand":"Botela","url":"https://www.botela.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Caranca","url":"https://www.caranca.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Domei","url":"https://www.domeizapatos.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Dask","url":"https://www.dask.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Gadol","url":"https://www.gadolchile.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Joyas Textiles","url":"https://www.unibles.com/joyastextiles","instagram":null,"facebook":null,"tiktok":null},{"brand":"Manda","url":"https://www.mandaactive.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Maria Jesus Jofre","url":"https://www.mariajesusjofre.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Ngo Shoes","url":"https://www.ngo-shoes.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Paulamar","url":"https://www.paulamar.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Plastica","url":"https://www.cl.plastica.com","instagram":null,"facebook":null,"tiktok":null},{"brand":"Suri de Chile","url":"https://www.suridechile.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Blu Blu","url":"https://www.blublu.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Nanou","url":"https://www.nanou.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Sofia de la Reguera","url":"https://www.sofiadelareguera.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Ekomar","url":"https://www.ekomar.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"Demente","url":"https://www.dmds.cl","instagram":null,"facebook":null,"tiktok":null},{"brand":"lasandresoap","url":null,"instagram":"https://www.instagram.com/lasandresoap/","facebook":null,"tiktok":null}]'

  url=f'{store_url}/admin/api/2023-04/products/{id}/metafields.json'
  headers = {
    'Content-Type': 'application/json',
  }
  
  time.sleep(1)
  response = requests.get(url, auth=(api_key, password), headers=headers)

  if response.status_code == 200:
    metafields = response.json()['metafields']
    print(metafields)
    metafield_id = metafields['key']
    print(metafield_id)
    # metafields_ids.append(metafield_id)
    # print(metafields_ids)
    return
  else:
    print(f'Error al obtener la lista de productos: {response.text}')
    return None

product_ids = get_all_product_ids()

for id in product_ids:
  get_product_metafield_id(id)

print(metafields_ids)


#  url = f'{store_url}/admin/api/2023-04/metafields/{metafield_id}.json

# print(len(product_ids))
# if product_ids:
#   print('Lista de ID de productos:')
#   for product_id in product_ids:
#     print(product_id)



# Actualizar un metafield existente en un producto específico
# def update_product_metafield(metafield_id, value):
#     url = f'{store_url}/admin/api/2023-04/metafields/{metafield_id}.json'
    
#     metafield_data = {  
#         'metafield': {
#             'value': value,
#             'value_type': 'json'
#         }
#     }
    
#     headers = {
#         'Content-Type': 'application/json',
#     }
    
#     response = requests.put(url, auth=(api_key, password), headers=headers, json=metafield_data)
    
#     if response.status_code == 200:
#         print('Metafield actualizado exitosamente')
#     else:
#         print(f'Error al actualizar el metafield: {response.text}')

# # ID del metafield que deseas actualizar
# metafield_id = 'TU_METAFIELD_ID'

# # Nuevo valor para el metafield
# new_value = 'NUEVO_VALOR'

# update_product_metafield(metafield_id, new_value)


