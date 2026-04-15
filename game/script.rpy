# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define nk = Character ("Nukumizu", color=("#4E8B38"))
define ya = Character ("Yanami", color=("#244377"))
define hs = Character ("Sosuke", color=("#9B3835"))


# El juego comienza aquí.

label start:
    #intro siscon

    "???" "Estoy tan orgullosa de ti,{w=.2} {i}Oniichan.{/i}"

    "???" "Debes de estar cansado."

    "???" "Haz trabajado muy duro."

    "???" "Asi que dejame cuidar de ti, ¿esta bien~?"

    scene cafeteria
    with fade

    "Ah, esto se pone cada vez mejor."

    "Que buena hermana es Kurumi, la manera en la que se preocupaba por su hermano mayor es increible."

    "¡Y estoy a punto de llegar al climax de la historia!"

    "Estas escenas de refuerzo pueden durar hasta veinte paginas, ¡y cada una es mejor que la anterior!"

    "{i}No puedo esperar a que-{nw=.3}-{/i}"

    #fin de la intro siscon

    "???" "¡No puedes hacer eso, Sosuke!"

    "???" "¡¿Te vas a quedar aqui sin hacer nada al respecto?! ¡No puedes estar perdiendo el tiempo aqui!"

    "Mi tren de pensamiento es interrumpido por gritos providentes de una mesa cercana"

    "{i}Parece que los tortolos vinieron a discutir.{/i} {p}No es de mi incumbencia."

    "Me iba a levantar para conseguir algo de soda de melon para volver a mi lectura, pero me volvi a sentar rapidamente tras darme cuenta quienes eran la pareja ruidosa."

    "Esos dos llevaban el uniforme de mi escuela, {i}y para colmo,{/i} eran compañeros de mi clase."

    "{i}{b}Anna Yanami{/b} y {b}Hakamada Sosuke.{/b}{/i}"

    "Personas que se pueden describir como populares y atractivas."

    scene cgcafeteria1
    with fade

    ya "¡Tienes que detener a Karen antes de que se vaya! ¿¡Acaso no te importa de que sea transferida a Inglaterra!?"

    hs "Ya nos despedimos del otro, no hay nada que pueda hacer-{nw=.3}-"

    ya "¿¡Y acaso tomaste su palabra en serio!? ¡Obviamente significa que te necesita cerca!"

    "Karen... creo que esa era la chica que transfirieron no hace mucho. Hizo todo un escandalo cuando llego."

    "{i}Espera, ¿ya se va de nuevo? Todo esto esta pasando demasiado rapido.{/i}"

    hs "¿Como sabes lo que ella quizo decir-{nw=.3}-"

    ya "¡Por que se lo qe se siente!"

    ya "¿No lo entiendes? Asi me siento todo el tiempo, Sosuke..."
    return
