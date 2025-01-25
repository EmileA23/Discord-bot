import discord 

def etiqueta_reciclar():
    embed = discord.Embed(
        title = "¿Que es el reciclaje?",
        description= "Aqui aprenderemos sobre el reciclaje y tips para reciclar",
        color= 0x00aaff
    )
    embed.add_field(
        name= "La importancia del reciclaje:",
        value= "El reciclaje es importante por que debemos hacernos cargo de nuestros desechos",
        inline= False
    )
    

    embed.set_thumbnail(
        url= "https://i.postimg.cc/FsWwRW5t/recliclar.png"
    )
    return embed

def etiqueta_reducir():
    embed = discord.Embed(
        title = "¿Que es reducir?",
        description= "Aqui aprenderemos por que es importante reciclar y te daremos algunos tips para ayudar al planeta ",
        color= 0x00aaff
    )
    embed.add_field(
        name= "La importancia de reducir:",
        value= "Reducir ayuda a que alla menos basura en el mundo la cual daña a la tierra",
        inline= False
    )
    
    embed.set_thumbnail(
        url= "https://i.postimg.cc/fbRcLNXZ/reducir.jpg"
    )
    return embed


def etiqueta_reutilizar():
    embed = discord.Embed(
        title = "¿Que es reutilizar?",
        description= "Te enseñaremos la importancia de reutilizar y en que ayuda al planeta",
        color= 0x00aaff
    )
    embed.add_field(
        name= "La importancia de reutilizar:",
        value= "Al reutilizar puedes crear cosas muy bonitas como un porta lapices de un panda con una botella de soda aparte ayudas a salvar a la tierra",
        inline= False
    )
    
    embed.set_thumbnail(
        url= "https://i.postimg.cc/QCfBvB4T/Reutilizar.jpg"
    )
    return embed