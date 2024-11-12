
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

carte_murmure = [
        ["🚪", "🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "🌀", " ", " ", " ", " ", " ", " ", " ", " ", "💨", "💨", " "," ", "🌀", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "💨", "👁️‍🗨️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "👁️‍🗨️", "💨", "🌫️", "🌀", "💨", "🚪", "🚪", "🚪"],
        ["🚪", "💨", "🌀", "💨", "💨", " ", " ", " ", " ", " ", " ", " ", "🌀", "💨", "💨", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "🌀", "🌫️", "👁️‍🗨️", "👁️‍🗨️", " ", " ", " ", " ", " ", " ", " ", "🌫️", "🌀", "🌫️", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "🌫️", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "💨", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "💨", "🌀", " ", " ", "🌀", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🚪", "🚪", "🚪", "🚪"],
        ["🚪", "💨", "👁️‍🗨️", "🌀", "🌀", "👁️‍🗨️", "💨", "🌀", "🚪", " ", " ", " ", " ", " ", " ", " ", "🚪"],
        ["🚪", "💨", "💨", " ", " ", "💨", " ", " ", "🚪", " ", " ", " ", " ", " ", "🚪"],
        ["🚪", "🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪","🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪", "🚪"],
    ]


descriptionsM = {
    "🌀": "Vous êtes dans une salle de murmure, pièce très sombre vous parvenez à entendre des voix vous entourent.",
    "👁️‍🗨️": "Vous êtes dans une salle de l'œil, vous ne voyer rien mais .. on vous voit ! et on vois Elias l'énorme clébard.",
    "💨": "Vous êtes dans une salle de vent, des raffales de vents viennent sur vous et laisse entendre des murmures terrifiantes.",
    "🌫️": "Vous êtes dans une salle de brume, une brume épaisse vous entoure et vous empêche de voir à plus de 2 mètres.",
    

}

position_joueur = [2, 2]
