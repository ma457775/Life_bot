import discord
import random
from discord.ext import commands
import os
import requests
import pyttsx3
from model import get_class
print(os.listdir("Memes"))  
print(os.listdir("Memes-en"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

robot = pyttsx3.init()
voces = robot.getProperty('voices')
robot.setProperty('voice', voces[1].id)

def voice(texto:str):
    robot.say(texto)
    robot.runAndWait()

consejys = [
    "Ahorra energía: Apaga luces y electrodomésticos cuando no los uses.",
    "Usa bombillas LED: Consumen menos electricidad y duran más tiempo.",
    "Reduce el consumo de agua: Cierra el grifo mientras te cepillas los dientes o lavas los platos.",
    "Recicla correctamente: Separa vidrio, plástico, papel y residuos orgánicos.",
    "Reutiliza todo lo posible: Usa botellas reutilizables, bolsas de tela y recipientes de vidrio.",
    "Evita el desperdicio de comida: Compra solo lo necesario y reutiliza sobras en nuevas recetas.",
    "Consume productos locales y de temporada: Reducen la huella de carbono del transporte.",
    "Reduce el consumo de carne: La producción de carne genera emisiones altas de CO₂ y consume mucha agua.",
    "Opta por envases biodegradables: Evita productos con demasiado plástico.",
    "Haz compostaje: Convierte los desechos orgánicos en abono para plantas.",
    "Usa transporte público o comparte coche: Reduce emisiones y ahorra combustible.",
    "Camina o usa bicicleta: Es más ecológico y saludable.",
    "Mantén tu vehículo en buen estado: Un coche bien mantenido consume menos combustible.",
    "Opta por vehículos eléctricos o híbridos: Si es posible, elige opciones con menor impacto ambiental.",
    "Digitaliza documentos: Reduce el uso de papel imprimiendo solo cuando sea necesario.",
    "Desconecta cargadores y dispositivos: Evita el consumo de energía fantasma.",
    "Usa materiales reciclados: Compra cuadernos, bolígrafos y otros artículos ecológicos.",
    "Planta árboles y cuida las áreas verdes: Los árboles ayudan a reducir el CO₂ y mejoran el aire.",
    "Participa en limpiezas comunitarias: Ayuda a recoger basura en parques y playas.",
    "Educa y sensibiliza: Comparte estos consejos con familiares y amigos para fomentar un impacto positivo.",
    "Instala paneles solares: Una inversión que reduce la factura de electricidad y la huella de carbono.",
    "Cosecha agua lluvia: Úsala para riego o limpieza en el hogar.",
    "Compra ropa sostenible: Prefiere textiles orgánicos o de segunda mano.",
    "Repara en lugar de desechar: Da una segunda vida a tus objetos.",
    "Reduce el uso de aire acondicionado: Ventila naturalmente siempre que sea posible.",
    "Prefiere electrodomésticos con etiqueta de eficiencia energética.",
    "Descongela el refrigerador regularmente para que funcione mejor.",
    "Usa aplicaciones para compartir bicicleta o patinete eléctrico.",
    "No uses pajillas plásticas: Prefiere metálicas o de bambú.",
    "Apoya marcas comprometidas con la sostenibilidad.",
    "Reutiliza agua de la lavadora para pisos o sanitarios.",
    "Siembra un huerto en casa: Reduce el transporte de alimentos.",
    "Evita imprimir correos electrónicos innecesarios.",
    "Cierra bien puertas y ventanas para ahorrar calefacción.",
    "Comparte libros o utiliza bibliotecas en vez de comprar nuevos.",
    "Usa detergentes y productos de limpieza biodegradables.",
    "Deshazte de baterías y electrónicos en puntos de recolección especiales.",
    "Participa en campañas de reciclaje escolar o laboral.",
    "Evita usar ascensor si puedes subir por escaleras.",
    "Promueve hábitos ecológicos en redes sociales."
]

factsy = [
    "Save energy: Turn off lights and appliances when not in use.",
    "Use LED bulbs: They consume less electricity and last longer.",
    "Reduce water consumption: Turn off the tap while brushing your teeth or washing dishes.",
    "Recycle properly: Separate glass, plastic, paper, and organic waste.",
    "Reuse as much as possible: Use reusable bottles, cloth bags, and glass containers.",
    "Avoid food waste: Buy only what is necessary and reuse leftovers in new recipes.",
    "Consume local and seasonal products: They reduce the carbon footprint of transportation.",
    "Reduce meat consumption: Meat production generates high CO₂ emissions and consumes a lot of water.",
    "Opt for biodegradable packaging: Avoid products with excessive plastic.",
    "Compost: Turn organic waste into fertilizer for plants.",
    "Use public transportation or carpool: Reduce emissions and save fuel.",
    "Walk or use a bicycle: It is more eco-friendly and healthier.",
    "Keep your vehicle in good condition: A well-maintained car consumes less fuel.",
    "Choose electric or hybrid vehicles: If possible, opt for lower environmental impact options.",
    "Digitize documents: Reduce paper usage by printing only when necessary.",
    "Unplug chargers and devices: Avoid phantom energy consumption.",
    "Use recycled materials: Buy eco-friendly notebooks, pens, and other supplies.",
    "Plant trees and take care of green areas: Trees help reduce CO₂ and improve air quality.",
    "Participate in community cleanups: Help collect trash in parks and beaches.",
    "Educate and raise awareness: Share these tips with family and friends to encourage a positive impact.",
    "Install solar panels: An investment that reduces electricity bills and your carbon footprint.",
    "Harvest rainwater: Use it for irrigation or cleaning at home.",
    "Buy sustainable clothing: Choose organic textiles or second-hand items.",
    "Repair instead of throwing away: Give your objects a second life.",
    "Reduce air conditioning use: Ventilate naturally whenever possible.",
    "Prefer appliances with an energy efficiency label.",
    "Defrost your refrigerator regularly to improve efficiency.",
    "Use bike-sharing or electric scooter apps.",
    "Avoid plastic straws: Choose metal or bamboo ones.",
    "Support brands committed to sustainability.",
    "Reuse washing machine water for floors or toilets.",
    "Grow a home garden: Reduce food transportation.",
    "Avoid printing unnecessary emails.",
    "Close doors and windows properly to save heating.",
    "Share books or use libraries instead of buying new ones.",
    "Use biodegradable detergents and cleaning products.",
    "Dispose of batteries and electronics at special collection points.",
    "Participate in recycling campaigns at school or work.",
    "Avoid using the elevator if you can take the stairs.",
    "Promote eco-friendly habits on social media."
]




@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    # Comandos disponibles
    commands_list = '''
    Hi please select your lenguage with the command !english or !spanish
    '''
    channel = bot.get_channel(1331770000083517452)
    voice(commands_list)
    await channel.send(commands_list)

@bot.command()
async def spanish(ctx):
    mensaje = f'Hola, ¡soy un bot {bot.user}!, puedes utilizar el comando !memes para ver memes para aprender sobre los problemas de el cambio cliamtico y como evitarlo o el comando !consejos para poder ver uno de los 40 consejos al azar, puedes utilizar el comando !github para tener el link para ver el código de este bot, puedes utilizar el comando !version para ver la versión de este bot, ¡gracias!'
    voice(mensaje)
    await ctx.send(mensaje)

@bot.command()
async def english(ctx):
    message = f'Hi, I am bot {bot.user}!, you can use the command !ENmemes to see the memes to learn about the problems of the climate change and how not to do it or you can use de command !tips so you can see one of the 40 tips in a random way , you can use the command !github so you can get the link to see this code of this bot, you can use the command !version so you can see the version of this bot, thank you!'
    voice(message)
    await ctx.send()

@bot.command()
async def memes(ctx):
    img_name = random.choice(os.listdir("Memes"))
    with open(f'Memes/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def ENmemes(ctx):
    img_name = random.choice(os.listdir("Memes-en"))
    with open(f'Memes/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def consejos(ctx):
    consejxs = random.choice(consejys)
    print(consejxs)
    await ctx.send(consejxs)
    voice(consejxs)
    

@bot.command()
async def facts(ctx):
    factsx = random.choice(factsy)
    print(factsx)
    await ctx.send(factsx)
    voice(factsx)

@bot.command()
async def github(ctx):
    await ctx.send(f"")

@bot.command()
async def version(ctx):
    await ctx.send(f"1.1")


bot.run("")
