import boto3 

ACCESS_KEY = ''
SECRET_KEY = ''



client = boto3.client(
    'rekognition',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

def get_path():
    from tkinter.filedialog import askopenfilename
    targetPath=askopenfilename()
    print("targetPath:%s"%targetPath)
    return targetPath

def obtener_bytes_imagen(ruta_imagen):
    with open(ruta_imagen,'rb') as imagen:
        #print(imagen.read())
        return imagen.read()

def create_collection(collection_id): 
    client=boto3.client('rekognition')
    #Create a collection
    try: 
        print('Creating collection:' + collection_id)
        response=client.create_collection(CollectionId=collection_id)
        print('Collection ARN: ' + response['CollectionArn'])
        print('Status code: ' + str(response['StatusCode']))
        print('Done...')
    except:
        print("Colección ya creada")
        

def describe_collection(collection_id):
    client=boto3.client('rekognition')
    response = client.describe_collection(CollectionId=collection_id)
    print(response)
    
def add_face(collection,ruta_imagen,id):
    bytes= obtener_bytes_imagen(ruta_imagen)
    client=boto3.client('rekognition')
    response = client.index_faces(
        CollectionId=collection,
        DetectionAttributes=[],
        ExternalImageId=id,
        Image = {'Bytes': bytes})
    print('Se agregó correctamente el rostro de: ',response['FaceRecords'][0]['Face']['ExternalImageId'])

def listar_faces(collection):
    client=boto3.client('rekognition')
    response = client.list_faces(
        CollectionId= collection,
        MaxResults=30)
    #print(response['Faces'])
    for i in response['Faces']:
        print ( "FaceId: ", i['FaceId'], "   corresponde a: ", i['ExternalImageId']) 
        
def delete_faces(lista):
    print("borrando")
    client=boto3.client('rekognition')
    response = client.delete_faces(
    CollectionId='First_collection',
    FaceIds=lista)
    
#CREAR UNA COLECCIÓN, SOLO EJECUTAR UNA VEZ, LUEGO COMENTAR AMBAS LÍNEAS   
collection_name = str(input("Ingrese el nombre de la colección:  "))
create_collection(collection_name)

#EJECUTAR CADA VEZ QUE SE QUIERA AGREGAR UN ROSTRO, PRIMERO ESCOGER LA IMAGEN 
#Y LUEGO PROPORCIONAR UN NOMBRE
nombre_colleccion = 'DemoCollecion'
ruta_imagen = get_path()
nombre = input('Ingrese el nombre de la persona:  ')
add_face(nombre_colleccion,ruta_imagen,nombre)
#PARA LISTAR LOS ROSTROS DE LA COLECCIÓN.
listar_faces(nombre_colleccion)
