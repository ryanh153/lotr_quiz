from dataclasses import dataclass
from typing import Tuple


@dataclass
class Question:
    question: str
    options: Tuple[str, str, str, str]
    answer: int
    index: int = 0


without_indices = [
    Question(question="On which day did Aragorn and the Captains arrive at the walls of Minas Tirith, after the "
                      "War of the Ring?",
             options=("Midsummer's eve", "The Eve of May", "The first day of Spring", "The first of April"),
             answer=1),

    Question(question="On what day did the Fair Folk out of the north arrive at the Gates of Minas Tirith?",
             options=("The Eve of Midsummer", "The first of April", "22nd September", "25th December"),
             answer=0),

    Question(question="How were the leftover hobbits taken away from the Long-expected Party?",
             options=("In barrels", "In vans", "On toboggans", "In wheelbarrows"),
             answer=3),

    Question(question="What was Denethor's first command to Pippin?",
             options=("Speak and be not silent", "Shut up", "Sing me a song", "Take your place in the Citadel Guard"),
             answer=0),

    Question(question="Which of the Fellowship rode with Aragorn on the Paths of the Dead",
             options=("Frodo and Sam", "Merry and Pippin", "Gandalf and Boromir", "Legolas and Gimli"),
             answer=3),

    Question(question="How did Throne upset Merry at the Muster of Rohan?",
             options=("He released him from his service", "He refused to listen to his tales",
                      "He took his sword from him", "He forgot he was there"),
             answer=0),

    Question(question="Which great horse did Gandalf summon to Fangorn?",
             options=("Snowmane", "Firefoot", "Narothal", "Shadowfax"),
             answer=3),

    Question(question="What reward did Gandalf accept for his services to Rohan?",
             options=("Gold", "To be made a Rider of Rohan", "Shadowfax", "A sword"),
             answer=2),

    Question(question="Who showed Pippin around Minas Tirith?",
             options=("Beregond", "Bergil", "Faramir", "Denethor"),
             answer=1),

    Question(question="Who said to Sam \"You nassty filthy little sneak\"?",
             options=("Gollum", "Bill Ferny", "Frodo", "Snaga"),
             answer=0),

    Question(question="What did Denethor say he felt, having sent Boromir to Rivendell, rather than Faramir?",
             options=("Stir not the bitterness in the cup I mixed for myself",
                      "Do I not already know the bitter harvest I have sown, and must reap?",
                      "Long have I felt the bitter sting of my folly",
                      "Do not remind me of the bitter herbs I have gathered to my breast"),
             answer=0),

    Question(question="What did Isildur bring from Númenor and set up at Erech?",
             options=("A black stone", "A watchtower", "A temple", "A ship"),
             answer=0),

    Question(question="With whom did Gimli quarrel about Galadriel?",
             options=("Hama", "Théoden", "Éomer", "Éowyn"),
             answer=2),

    Question(question="What was the name of the door that led to the Hallows of Minas Tirith?",
             options=("Fen Thurin", "Nan Tathren", "Fennas Nogothrim", "Fen Hollen"),
             answer=3),

    Question(question="What was the crown made from in the standard of Elendil, that Aragorn raised on his ship?",
             options=("Mithril and gold", "Ithildin and copper", "Silver and gold", "Mithril and jet"),
             answer=0),

    Question(question="What colour was the banner of Dol Amorth?",
             options=("Blue", "Silver", "Gold", "White"),
             answer=0),

    Question(question="Who was lieutenant of Morgul?",
             options=("Grond", "Gothmog", "Golfimbul", "Gollum"),
             answer=1),

    Question(question="What did Galadriel wish for, when asked by Frodo?",
             options=("To be a simple Elf maiden", "The Ring", "The defeat of Sauron",
                      "That the One Ring had never been wrought"),
             answer=3),

    Question(question="Who led the final attempt by the Orcs to escape from the Riders of Rohan?",
             options=("Lugdush", "Snaga", "Grishnákh", "Uglúk"),
             answer=3),

    Question(question="\"I am not altogether on anybody's side, be nobody - ...\"?",
             options=("Tends the woods and the trees as I do", "Remembers the old Ents anymore",
                      "Thinks about the Entwives like I do", "Is altogether on my side"),
             answer=3),

    Question(question="How does Gandalf find his way down after the Battle of the Peak?",
             options=("He climbs down the mountainside", "Shadowfax finds him and carries him to safety",
                      "He is carried down by Gwaihir the Windlord", "He is rescued by Treebeard"),
             answer=2),

    Question(question="Why had the Oathbreakers come to the Stone of Erech?",
             options=("To fight", "To seize the Company", "To worship at the Stone",
                      "To fulfill their oath and have peace"),
             answer=3),

    Question(question="What 'men of a new sort' did Ingold describe as assaulting Rammas Echor?",
             options=("Broad and grim, bearded like Dwarves", "Short and squat, with painted faces",
                      "Tall and strong, with braided hair", "Dark and hideous, with bones in their noses"),
             answer=0),

    Question(question="What colour was the tree on the standard of Aragorn's ship, at the Harlond?",
             options=("White", "Red", "Silver", "Green"),
             answer=0),

    Question(question="Who was first to volunteer to take the One Ring to Mordor?",
             options=("Bilbo", "Frodo", "Sam", "Legolas"),
             answer=0),

    Question(question="In what year did the white wolves invade the Shire, during the fell winter?",
             options=("1398", "1311", "1358", "1325"),
             answer=1),

    Question("Who created the runic system that was used on Balin's tombstone?",
             options=("Daeron", "Orophin", "Celebrimbor", "Nimrodel"),
             answer=0),

    Question(question="Who stood before the Black Gates, with the Dúnedain about them, right at the front of the "
                      "allies?",
             options=("The Sons of Elrond", "Gandalf and Aragorn", "Imrahil and Éomer", "Pippin and Merry"),
             answer=0),

    Question(question="Finish the line that Legolas sang at the Cormallen: \"To the Sea, to the Sea! The White Gulls "
                      "are crying, The wind is blowing ...\"",
             options=("and my spirit is crying", "and the white foam is flying",
                      "and I know not where I'm going", "and Middle-earth is dying"),
             answer=1),

    Question(question="Where did King Aragorn say that Beregond should live, now that all was settled?",
             options=("Emyn Arnen", "Osgiliath", "Henneth Annun", "Cair Andros"),
             answer=0),

    Question(question="Where did Merry and Pippin find themselves after their escape from the Orcs?",
             options=("Rohan", "Lothlórien", "Orthanc", "Fangorn"),
             answer=3),

    Question(question="From what were Treebeard's pillows made?",
             options=("Sheepskin", "Leaves", "Earth", "Grass"),
             answer=3),

    Question(question="In which peak of the Misty Mountains was Durin's Tower?",
             options=("Mount Gundabad", "Caradhras", "Fanuidhol", "Celebdil"),
             answer=3)
]

questions = list()
for ii, q in enumerate(without_indices):
    q.index = ii
    questions.append(q)
