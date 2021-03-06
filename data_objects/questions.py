import logging
from dataclasses import dataclass
from typing import Tuple

logger = logging.getLogger(__name__)


@dataclass
class Question:
    question: str
    options: Tuple[str, str, str, str]
    answer: int
    index: int = 0
    extra_text: str = ""


def construct_questions():

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
                 options=("Speak and be not silent", "Shut up", "Sing me a song", "Take your place in the Citadel "
                                                                                  "Guard"),
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

        Question(question="What did Isildur bring from N??menor and set up at Erech?",
                 options=("A black stone", "A watchtower", "A temple", "A ship"),
                 answer=0),

        Question(question="With whom did Gimli quarrel about Galadriel?",
                 options=("Hama", "Th??oden", "??omer", "??owyn"),
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
                 options=("Lugdush", "Snaga", "Grishn??kh", "Ugl??k"),
                 answer=3),

        Question(question="\"I am not altogether on anybody's side, because nobody - ...\"?",
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

        Question(question="Who stood before the Black Gates, with the D??nedain about them, right at the front of the "
                          "allies?",
                 options=("The Sons of Elrond", "Gandalf and Aragorn", "Imrahil and ??omer", "Pippin and Merry"),
                 answer=0),

        Question(question="Finish the line that Legolas sang at the Cormallen: "
                          "\"To the Sea, to the Sea! The White Gulls "
                          "are crying, The wind is blowing ...\"",
                 options=("and my spirit is crying", "and the white foam is flying",
                          "and I know not where I'm going", "and Middle-earth is dying"),
                 answer=1),

        Question(question="Where did King Aragorn say that Beregond should live, now that all was settled?",
                 options=("Emyn Arnen", "Osgiliath", "Henneth Annun", "Cair Andros"),
                 answer=0),

        Question(question="Where did Merry and Pippin find themselves after their escape from the Orcs?",
                 options=("Rohan", "Lothl??rien", "Orthanc", "Fangorn"),
                 answer=3),

        Question(question="From what were Treebeard's pillows made?",
                 options=("Sheepskin", "Leaves", "Earth", "Grass"),
                 answer=3),

        Question(question="In which peak of the Misty Mountains was Durin's Tower?",
                 options=("Mount Gundabad", "Caradhras", "Fanuidhol", "Celebdil"),
                 answer=3),

        Question(question="Who was Th??oden's banner-bearer?",
                 options=("Herufara", "Eothain", "Grimbrand", "Guthlaf"),
                 answer=3),

        Question(question="Who, on the battlefield, realised that ??owyn still lived?",
                 options=("Amroth", "Aragorn", "Imrahil", "Erestor"),
                 answer=2),

        Question(question="Trolls have what color blood?",
                 options=("Black", "Green", "Red", "Khaki"),
                 answer=0),

        Question(question="What protected Merry and Pippin from being slain by the rider whose horse jumped over them?",
                 options=("They were hidden under their Elf cloaks", "They were hidden by Grishn??kh",
                          "He missed them in the dark", "Mount Gundabad"),
                 answer=0),

        Question(question="To the base of which mountain did Treebeard carry the hobbits?",
                 options=("Mindolluin", "Menegroth", "Methedras", "Mount Gundabad"),
                 answer=2),

        Question(question="Aragorn was surprised to hear of the Ents as he thought they were ...?",
                 options=("A tale from the Elder Days", "A legend of Rohan",
                          "A rumour out of the Wilderland", "A story told by the Elves of Mirkwood"),
                 answer=1),

        Question(question="What are the great pillars flanking the river Anduin called?",
                 options=("The Argonauts", "The Argonath", "The Argonom", "The Argoplum"),
                 answer=1),

        Question(question="Name the 'grey hills' through which Sam and Frodo had to find a route alone",
                 options=("Grey Mountains", "Misty Mountains", "Emyn Muil", "Cairngorms"),
                 answer=2),

        Question(question="What did ??omer call hobbits?",
                 options=("Dwarves", "Halflings", "Perian", "Snaga"),
                 answer=1),

        Question(question="Why do Pippin and Merry sit on Treebeard's table?",
                 options=("The chairs are all Ent-sized and too big for them", "There are no chairs in his Enthouse",
                          "The chairs are all covered with bundles of plants", "All the chairs are broken"),
                 answer=1),

        Question(question="What, according to Gandalf, was the only thing that would ensure victory in the coming war?",
                 options=("Use of the Ring", "The valour of the Men of Gondor", "The armies of Rohirrim",
                          "All the Free People of the West working together"),
                 answer=0),

        Question(question="Who built Meduseld?",
                 options=("Brego son of Eorl", "Eorl the Young", "Th??oden son of Thengel", "The Stewards of Gondor"),
                 answer=0),

        Question(question="What do men now call the region where the Entwives had their gardens?",
                 options=("The Dead Marshes", "The Brown Lands", "The Old Forest", "The Grey Mountains"),
                 answer=1),

        Question(question="What did Gandalf say lay beneath the 'great smoke' that Legolas saw?",
                 options=("Fire and death", "Battle and war", "Wizardry and destruction", "Treachery and fighting"),
                 answer=1),

        Question(question="What did Gimli choose when offered any gift from King Th??oden's Armoury?",
                 options=("An axe and chain-mail", "A sword and scabbard", "A knife and sheath", "A cap and shield"),
                 answer=3),

        Question(question="Of what did Galadriel warn Legolas in her message?",
                 options=("Mind the Gap of Rohan", "Beware the Sae", "Take care when crossing the Isen",
                          "Watch out for Oliphaunts"),
                 answer=1),

        Question(question="Who did gr??ma truly serve while counsellor the Th??oden?",
                 options=("Saruman", "Sauron", "The Nazg??l", "Ugl??k"),
                 answer=0),

        Question(question="How old was Pippin when he became a soldier of Gondor?",
                 options=("33", "50", "25", "28"),
                 answer=3),

        Question(question="What did Aragorn call Th??oden, when speaking of his body returning to Rohan?",
                 options=("Th??oden the Slayer", "Th??oden the Renewed", "Th??oden the Horse-Lord",
                          "Th??oden the Renowned"),
                 answer=3),

        Question(question="Into what should Bilbo have put the Ring, to leave it for Frodo?",
                 options=("A pouch", "A handkerchief", "An envelope", "A rag"),
                 answer=2),

        Question(question="What is the name of the hill that is about half way between Bree and Rivendell?",
                 options=("Stormdale", "Hailpeak", "Snow gully", "Weathertop"),
                 answer=3),

        Question(question="Name the husband of Lobelia Sackville-Baggins",
                 options=("Oscar", "Otho", "Lotho", "Nemo"),
                 answer=1),

        Question(question="What name do the hobbits use for the constellation we call the Plough?",
                 options=("The Hoe", "The Trowel", "The Sickle", "The Shovel"),
                 answer=2),

        Question(question="What ring did Galadriel wear?",
                 options=("Nenya", "Narya", "Varya", "Venya"),
                 answer=0),

        Question(question="Who feared 'to stay behind bars, until use and old age accept them'?",
                 options=("??omer", "??owyn", "Saruman", "Bilbo"),
                 answer=1),

        Question(question="How did Merry secretly join the army riding to Minas Tirith?",
                 options=("Under a rider's cloak", "Following on foot", "On his pony", "In the baggage van"),
                 answer=0),

        Question(question="Who brought the first news of the assault on Osgiliath to Minas Tirith?",
                 options=("Faramir", "Beregond", "Gandalf", "The Prince of Dol Amroth"),
                 answer=2),

        Question(question="How many Ents left the Entmoot and marched on Isengard?",
                 options=("About fifty", "Several hundred", "Only twenty or so", "Several dozen"),
                 answer=0),

        Question(question="What did the head of the great battering ram look like?",
                 options=("A leering Orc", "A ravening wolf", "A great mailed fist", "A snarling Troll"),
                 answer=1),

        Question(question="How many times did the great battering ram strike the gates of Minas Tirith?",
                 options=("Once", "Twice", "Thrice", "Four times"),
                 answer=2),

        Question(question="What did Gandalf conclude would  happen if Isengard and Mordor fought each other?",
                 options=("The victor would emerge stronger than either and free from doubt",
                          "The victor would turn his attention on Gondor and be merciless",
                          "The loser would try to make an alliance with the Men of Minas Tirith and corrupt them",
                          "The victor would make fair seem foul and foul seem fair"),
                 answer=0),

        Question(question="Who was gr??ma's father?",
                 options=("Gl??in", "Gr??ma", "Grond", "Galmod"),
                 answer=3),

        Question(question="What title did Merry and Pippin claim at the ruined gates of Isengard",
                 options=("Gatekeepers", "Way-watchers", "Doorwardens", "Caretakers"),
                 answer=2),

        Question(question="When he returned to Minas Tirith, what did Faramir do with his company from Henneth Annun?",
                 options=("Sent them to guard Cair Andros", "Left them to watch the road from Minas Morgul",
                          "Left them at Henneth Annun to ambush more Oliphaunts",
                          "Sent them to strengthen the garrison at the fords of Osgiliath"),
                 answer=3),

        Question(question="What did Gh??n-buri-Gh??n say before he vanished?",
                 options=("\"Day is coming!\"", "\"Darkness is breaking\"", "\"Wind is changing!\"",
                          "\"Stone-houses are burning!\""),
                 answer=2),

        Question(question="Who apart from ??owyn did Th??oden ask to see, as he lay dying?",
                 options=("Theodred", "Gandalf", "??omer", "Pippin"),
                 answer=2),

        Question(question="What frightened Frodo most in the Mirror of Galadriel?",
                 options=("An eye", "His death", "The ruin of the Shire", "Bilbo wandering lost"),
                 answer=0),

        Question(question="What gift did Galadriel give Boromir, when the Company left Lothl??rien?",
                 options=("A sword", "A shield", "A belt of gold", "A silver brooch"),
                 answer=2),

        Question(question="What did ??omer rename Aragorn?",
                 options=("Fastfoot", "Wingfoot", "Lightfoot", "Sorefoot"),
                 answer=1),

        Question(question="Merry said to Th??oden that he would run to battle eve if ...",
                 options=("He had to crawl", "He had to be rolled in a barrel",
                          "He ran his feet off", "It took a year and a day"),
                 answer=2),

        Question(question="What was Denethor's purpose in questioning Pippin so closely?",
                 options=("To try to find out about the Ring", "To insult Gandalf",
                          "He could use \"even his grief as a cloak\"", "To pass a boring morning"),
                 answer=2),

        Question(question="How far were the host of Rohan from Pelennor, when they left the hidden valley?",
                 options=("Seven miles", "Ten miles", "Seven furlongs", "Seven leagues"),
                 answer=3),

        Question(question="What decorated the gift Galadriel gave Sam, when he left Lothl??rien?",
                 options=("The 'G' rune", "A flower", "A tree", "The 'S' rune"),
                 answer=0),

        Question(question="To where did ??omer ask Aragorn to return the horses he lent him?",
                 options=("Gondor", "Isengard", "Meduseld", "Tol Brandir"),
                 answer=2),

        Question(question="What was the name of the Entwife that Fangorn loved?",
                 options=("Fentathren", "Finduilas", "Fingalad", "Fimbrethil"),
                 answer=3),

        Question(question="Who was last of the Company to enter the Paths of the Dead, and the most afraid?",
                 options=("Arod, the horse of Rohan", "Gimli", "Legolas", "Halbarad"),
                 answer=1),

        Question(question="How far did the army of Rohan ride on their first day's journey from Edoras?",
                 options=("Two leagues", "Twenty leagues", "Twelve leagues", "Two hundred leagues"),
                 answer=2),

        Question(question="What newcomers did Gandalf say they would see before the arrival of the Rohirrim?",
                 options=("Aragorn and his kinsmen, the Rangers of the north",
                          "Fugitives from Cair Andros", "The hosts of Morgul", "The Corsairs of Umbar"),
                 answer=1),

        Question(question="Who did the city watchmen believe were in the ships sailing up the Anduin?",
                 options=("Pirates", "Orcs", "Ghosts", "Corsairs"),
                 answer=3),

        Question(question="What gift did Galadriel give Frodo, when the Company left Lothl??rien?",
                 options=("A sword", "A golden belt", "A crystal vial", "A ring"),
                 answer=2),

        Question(question="What was the name of the horse that ??omer lent to Legolas?",
                 options=("Shadowfax", "Snowmane", "Elendil", "Arod"),
                 answer=3),

        Question(question="Who went ahead of the Company to find the way around the rapids?",
                 options=("Aragorn and Legolas", "Aragorn and Boromir", "Boromir and Legolas", "Gimli and Legolas"),
                 answer=0),

        Question(question="Where did Same and Frodo land their boat after leaving the Company?",
                 options=("On Tol Brandir", "On the slopes of Amon Lhaw", "On Path Galen", "On the Emyn Muil"),
                 answer=1),

        Question(question="Who said \"I would cut off your head, beard and all, Master Dwarf, if it stood but a little "
                          "higher from the ground\"?",
                 options=("Saruman", "Wormtongue", "??omer", "Boromir"),
                 answer=2),

        Question(question="At the Prancing Pony, what did Nob use to make a nice imitation of Frodo's head?",
                 options=("A coconut", "A brown woolen mat", "A cushion", "A hedgehog"),
                 answer=1),

        Question(question="What did Frodo shout out when he was stabbed, at Weathertop?",
                 options=("Namarie!", "O Elbereth! Gilthoniel!", "Elen sila lumenn!", "Luthien Tin??viel!"),
                 answer=1),

        Question(question="What were the yellow winter flowers called that grew on Cerin Amroth, in L??rien?",
                 options=("Rosie", "Diamond", "Primula", "Elanor"),
                 answer=3),

        Question(question="Mr Butterbur accused Frodo of breaking up his crocks with his ...?",
                 options=("High notes", "Juggling", "Acrobatics", "Shenanigans"),
                 answer=2),

        Question(question="What broken object did Strider show Frodo, in the parlour of the Prancing Pony?",
                 options=("His leg", "His knife", "His backpack", "His sword"),
                 answer=3),

        Question(question="Who was 'the fairest maiden that has ever been ...'?",
                 options=("Amina", "??owyn", "Luthien", "Arwen"),
                 answer=0,
                 extra_text="According to the books it's Luthien though"),

        Question(question="Which Ent almost caught Saruman when they attacked Isengard?",
                 options=("Brightbark", "Beechbone", "Leaflock", "Quickbeam"),
                 answer=3),

        Question(question="What colours did Faramir's company wear in Ithilien?",
                 options=("Red and black", "Black and blue", "Green and brown", "Grey"),
                 answer=2),

        Question(question="Who did Sam describe as 'Hard as diamonds, soft as moonlight'?",
                 options=("Gandalf", "Elrond", "Galadriel", "Celeborn"),
                 answer=2),

        Question(question="How were the hobbits saved from Grishn??kh?",
                 options=("Ugl??k found them", "They lost him in the dark", "A Rider killed him", "Pippin killed him"),
                 answer=2),

        Question(question="Complete the phrase \"Sheep get like ...\"",
                 options=("Shepherds", "Grass", "Dogs", "Barrels"),
                 answer=0),

        Question(question="What Elven name does Legolas call Ents?",
                 options=("Ornedrim", "Galadhrim", "Onodrim", "Erynhoth"),
                 answer=2),

        Question(question="What colour was Th??oden's shield?",
                 options=("Gold", "Green", 'White', 'Red'),
                 answer=0),

        Question(question="What type of weather was it, as the body of Th??oden was taken to the city?",
                 options=('Bright sunshine', 'Thick fog', 'Howling a gale', 'Rain'),
                 answer=3),

        Question(question="What do Hill-Trolls do to their enemies?",
                 options=('Scalp them', 'Bite their throats', 'Trample them', 'Poison them'),
                 answer=1),

        Question(question="What had Treebeard forgotten that hobbits do?",
                 options=('They sit down to eat', 'They comb their hair', 'They lie down to sleep',
                          'The bathe their feet'),
                 answer=2),

        Question(question='What relation was ??owyn to ??omer?',
                 options=('Wife', 'Sister', 'Cousin', 'None'),
                 answer=1),

        Question(question='How many men of the Outlands rode to the defence of Minas Tirith, before the siege?',
                 options=('One hundred thousand', 'Ten thousand', 'Three thousand', 'Five hundred'),
                 answer=2),

        Question(question='What was the \'Silent Street\' called in the Hallows of Minas Tirith?',
                 options=('Rath Dinen', 'Rathloriel', 'Rath Vorondil', 'Rath Numen'),
                 answer=0),

        Question(question='Who was Aragorn\'s standard-bearer?',
                 options=('Hama', 'Herugrim', 'H??rin', 'Halbarad'),
                 answer=3),

        Question(question="What does Quickbeam do whenever he sees a rowan-tree?",
                 options=('He waters its roots and chants a poem', 'He stops and sings to it',
                          'He laughs and claps his hands', 'He caresses it and says something in Entish'),
                 answer=1),

        Question(question="How often was a mayor elected in Michel Delving?",
                 options=('Once a week', 'Every 7 years', 'When the standing one could no longer stand', 'Annually'),
                 answer=1),

        Question(question="At the Long-expected Party Bilbo wished, thirdly, to make...?",
                 options=('A cake', 'A complaint', 'A song and dance', 'An announcement!'),
                 answer=3),

        Question(question="Where did Strider say that he and the hobbits should heard for, when they left Bree?",
                 options=('Weathertop', 'Dale', 'Isengard', 'Bombadil\'s house'),
                 answer=0),

        Question(question="What is a Silmaril?",
                 options=("A crystal ball", 'A necklace', 'A pudding', 'A jewel'),
                 answer=3),

        Question(question="Whilst trying to cross Caradhras, what did Frodo notice Legolas wearing on his feet?",
                 options=('Boots', 'Sandals', 'Light shoes', 'Nothing'),
                 answer=2),

        Question(question="What did Boromir shout as he went to the rescue of Gandalf on the narrow bridge, in Moria?",
                 options=('Minas Tirith!', 'Osgiliath!', 'Faramir!', 'Gondor!'),
                 answer=3),

        Question(question="Who did Aragorn refuse to take to the Paths of the Dead?",
                 options=('??owyn', '??omer', 'Gr??ma', 'Merry'),
                 answer=0),

        Question(question="What did Th??oden call Minas Tirith?",
                 options=('Mundeli', 'Oldburg', 'Mundburg', 'Oldbury'),
                 answer=2),

        Question(question="When Gandalf said that he would allow only one more \"but\" "
                          "tonight what did Pippin then ask "
                          "about?",
                 options=("Aragorn's use of the Palantir of Orthanc", "Gollum",
                          'When Merry and the Rohirrim would arrive',
                          'Shelob'),
                 answer=1),

        Question(question="What gift did Galadriel give Legolas when the Company left Lothl??rien?",
                 options=('A sword', 'A gold belt', 'A bow and arrows', 'Good advice'),
                 answer=2),

        Question(question="How many men did ??omer lose in the battle near Entwood",
                 options=('15', '25', '2', '30'),
                 answer=0),

        Question(question="What happened to Leaflock the Ent - Had he ...?",
                 options=("Wandered out of Treebeard's land, looking for the Entwives",
                          "Hidden himself deep in the darkest depths of Fangorn",
                          "Been badly injured by axe-wielding Orcs",
                          "Brown sleepy, almost tree-ish"),
                 answer=3),

        Question(question="Which Ent stood 'as still as a door-tree', at the foot of the stairs to Orthanc?",
                 options=('Fastpole', 'Quickbeam', 'Hastyrod', 'Hurrystalk'),
                 answer=1),

        Question(question="How does Pippin react when Gandalf arrives at the ruins of Isengard?",
                 options=('He rubs his eyes and imagines he must be dreaming',
                          'He tries to jump up from the rock he is sitting on, but falls over his own feet',
                          'He pinches himself to see if he is awake',
                          'He tries to call out, but can\'t'),
                 answer=3),

        Question(question="Who taught Pippin his duties as a soldier of Gondor?",
                 options=('Faramir', 'Beregond', 'Ioreth', 'Bergil'),
                 answer=1),

        Question(question="With what was Treebeard's bed covered?",
                 options=('Leaves and cut grass', 'Sheepskin and other animal pelts',
                          'Dried grass and bracken', 'Reeds and pine needles'),
                 answer=2),

        Question(question="What was the Dwarven name for Celebdil, the Silvertine?",
                 options=('Gabilgathol', 'Bundushath??r', 'Kibil-n??la', 'Zirakzigil'),
                 answer=3),

        Question(question="Why was ??omer not present to greet the Company, when they arrived at Meduseld?",
                 options=('He was dead', 'He was imprisoned', 'He had been captured by Orcs', 'He was in bed'),
                 answer=1),

        Question(question="Who did Pippin watch leaving Minas Tirith, as he sat with Beregond?",
                 options=('Gandalf', 'The old, women and children', 'The errand-riders', 'An army'),
                 answer=1),

        Question(question="By what name was Dwimorberg known in Rohan?",
                 options=('The Lonely Mountain', 'The Black Mountain', 'The Haunted Mountain', 'The Dead Mountain'),
                 answer=2),

        Question(question="Who helped Merry join the Rohirrim in their ride to Minas Tirith?",
                 options=('Thengel', 'Hama', 'Theodred', 'Dernhelm'),
                 answer=3),

        Question(question="What was the first thing Merry said when Aragorn revived him, in the House of Healing?",
                 options=('"Oh good, a real bed"', '"What day is it?"', '"I am hungry"', '"Strider, how splendid!"'),
                 answer=2),

        Question(question="Whilst in parley with the Mouth of Sauron, what did Gandalf call the Dark Lord?",
                 options=('Base Master of Treachery', 'Low Lord of Loathing', 'Tricksy', 'The King of Deceit'),
                 answer=0),

        Question(question="What did Gandalf put on the heads of Frodo and Sam, for the feast on the Field of "
                          "Cormallen?",
                 options=('Winged helms', 'Wreaths of scarlet flowers', 'Small golden coronets', 'Circlets of Silver'),
                 answer=3),

        Question(question="What was the purpose of the gift Frodo received, on leaving Lothl??rien?",
                 options=('To bring good luck', 'To hide him from evil eyes', 'To prolong his strength',
                          'A light in dark places'),
                 answer=3),

        Question(question="How many horses did the Three Hunters borrow from ??omer?",
                 options=('3', '4', '2', '1'),
                 answer=2),

        Question(question="How does Pippin interrupt the Entmoot when it first starts?",
                 options=('He hiccups loudly', 'He belches', 'He yawns', 'He coughs politely'),
                 answer=2),

        Question(question="Who the Th??oden name as his heir when he rode off to battle?",
                 options=('??owyn', '??omer', 'Gandalf', 'Aragorn'),
                 answer=1),

        Question(question="Where was the home of 'old Forlong the Fat'?",
                 options=('Ithilien', 'Lossarnach', 'Imloth Melui', 'Dol Amroth'),
                 answer=1),

        Question(question="To where did Aragorn bid the Dead follow him?",
                 options=('Pelargir', 'Dol Amroth', 'Minas Tirith', 'Umbar'),
                 answer=0),

        Question(question="What was the name of the hill refuge prepared for the women and children of Rohan?",
                 options=('Meduseld', 'Isengard', 'Dunharrow', 'Helm\'s Deep'),
                 answer=2),

        Question(question="What did the hobbits say Isengard looked like, as it filled with water?",
                 options=('A volcanic crater, all smoke and fumes',
                          'A huge flat saucepan, all steaming and bubbling',
                          'A large bathtub, all vapours and mists',
                          'A gian puddle, all muddy and slimy'),
                 answer=1),

        Question(question="What was the chief city of Gondor, abandoned at the time of the War of the Ring.",
                 options=('Arnor', 'Ann??minas', 'Osgiliath', 'Henneth Annun'),
                 answer=2),

        Question(question="Who crowned Aragorn?",
                 options=('Frodo', 'Gandalf', 'Faramir', 'Himself'),
                 answer=1),

        Question(question="What did Frodo tell Wormtongue he could have if he stayed in teh Shire, and did not follow "
                          "Saruman?",
                 options=('A nice little hole to live in', 'Rest and food', 'A holiday',
                          'Time to appease his sins by planting potatoes'),
                 answer=1),

        Question(question="What did the Men of Gondor call 'sweet galenas'?",
                 options=('Pipe-weed', 'Small white flowers', 'A damson pudding', 'A short sword'),
                 answer=0),

        Question(question="What did the hobbits do that amused the Ents at the Entmoot?",
                 options=('The bowed', 'They shook hands with Treebeard', 'The were \'hasty\' in leaving Entmoot',
                          'They ate some of their supply of lembas'),
                 answer=0),

        Question(question="Who did the people of Rohan trust to lead them in the absence of Th??oden?",
                 options=('??owyn', '??omer', 'Hama', 'Helm'),
                 answer=0),

        Question(question="How many servants carried Faramir to his pyre?",
                 options=('Four', 'Six', 'Ten', 'One dozen'),
                 answer=1),

        Question(question="What is Galadriel's first reaction when Frodo offers her the Ring?",
                 options=('She takes it', 'She laughs', 'She walks away from him', 'She cries'),
                 answer=1),

        Question(question="What did Gimli ask as a gift from Galadriel?",
                 options=('A kiss', 'A strand of hair', 'A picture', 'Gold'),
                 answer=1),

        Question(question="What was the name of the horse that ??omer lent to Aragorn?",
                 options=('Hasufel', 'Shadowfax', 'Snowmane', 'Elendil'),
                 answer=0),

        Question(question="Into how many Farthings was the Shire divided?",
                 options=('1', '2', '3', '4'),
                 answer=3),

        Question(question="How did Bilbo claim to have spent his fifty first birthday?",
                 options=('Under a table', 'In a barrel', 'Against a lamp-post', 'Over the hill'),
                 answer=1),

        Question(question="Into what did Frodo hope Gandalf would turn Sam?",
                 options=('A grass snake', 'A mewlip', 'A spotted toad', 'A dead-end'),
                 answer=2),

        Question(question="What did Boromir lose at Tharbad?",
                 options=('His food', 'His horse', 'His sword', 'His way'),
                 answer=1),

        Question(question="After the boat journey, where di Aragorn hope to visit for a guiding sign?",
                 options=('Lothl??rien', 'Amon Hen', 'Henneth Annun', 'Fangorn'),
                 answer=1),

        Question(question="How was Frodo's plan to continue alone spoiled?",
                 options=('They had guessed he would go, and threw a farewell party for him',
                          'The whole Company came with him',
                          "Aragorn tied him to a tree so he couldn't go",
                          'Sam came back in time to go with him'),
                 answer=3),

        Question(question="What was Th??oden's sword called?",
                 options=("Aiglos", "Glamdring", "Herugrim", "Anduril"),
                 answer=2),

        Question(question="How did Wormtongue arrive at Isengard",
                 options=("On foot with some Dunlendings", "Carried by some Huorns",
                          "In a small cart pulled by a donkey", "On an old tired horse"),
                 answer=3),

        Question(question="What is the meaning of Rath Celerdain?",
                 options=("Long Street", "The Lampwrights Street", "Osgiliath Road", "The Baker's Street"),
                 answer=1),

        Question(question="What sort of creature stunned Beregond in the final battle at the Black Gate?",
                 options=("M??makil", "Orcs", "Hill-Troll", "Uruk-hai"),
                 answer=2),

        Question(question="Who brought the Sceptre of Ann??minas to Minas Tirith?",
                 options=("Galadriel", "C??rdan", "Radagast", "Elrond"),
                 answer=3),

        Question(question="What did Bilbo leave for Adelard Took?",
                 options=("A horse", "An umbrella", "A shoe shine kit", "A doormat"),
                 answer=1),

        Question(question="What is Tin??viel, in the Common Speech?",
                 options=("Lark", "Nightingale", "Cuckoo", "Thrush"),
                 answer=1),

        Question(question="When on Caradhras, to whom did Gandalf say \"if Elves could fly over mountain, they might "
                          "fetch the Sun to save us\"?",
                 options=("Gimli", "Legolas", "Aragorn", "Frodo"),
                 answer=1),

        Question(question="When Aragon leapt to Gandalf's defence on the Moria bridge, whose name did Aragorn call "
                          "out?",
                 options=("Narsil!", "Elendil!", "Arwen!", "Eru"),
                 answer=1),

        Question(question="What choices did Th??oden give gr??ma when his treachery was discovered?",
                 options=("Prison or death", "Exile or death", "To ride to war or exile", "To ride to war or prison"),
                 answer=2),

        Question(question="Who said he could lay Pippin on his back or stand him on his head?",
                 options=("Merry", "Faramir", "Gandalf", "Bergil"),
                 answer=3),

        Question(question="To where did Aragon summon the dead?",
                 options=('The Stone of Erech', 'Pelargir', "Minas Tirith", "Meduseld"),
                 answer=0),

        Question(question="Who said that his death lay beyond the door to the Paths of the Dead?",
                 options=("Aragorn", "Legolas", "Gimli", "Halbarad"),
                 answer=3),

        Question(question="Which horse did Merry ride from Edoras to Minas Tirith?",
                 options=("Stybba", "Windfola", "Snowmane", "Shadowfax"),
                 answer=1),

        Question(question="What does Gandalf say must be done, as \"soon there will be battle on the fields\"?",
                 options=("A sortie must be made", "All the wounded should be evacuated to Lossarnach",
                          "The gate of Minas Tirith be shut and barred",
                          "The city walls have to be held until the Rohirrim arrive"),
                 answer=0),

        Question(question="Who found Merry when he fell over, as he followed a shadow outside the Prancing Pony?",
                 options=("Gandalf", "Nob", "Hob", "Bob"),
                 answer=1),

        Question(question="How many Black Riders came upon the hobbits at Weathertop?",
                 options=('3', '4', '5', '6'),
                 answer=2),

        Question(question="Where did the Fellowship stop briefly, in their flight from the gate of Moria?",
                 options=("The Dimrill Dale", "The Silverlode valley", "Druin's Dale", "The mere of Moria"),
                 answer=0),

        Question(question="Sam said that not even his uncle .... who, could do a trick like crossing the rope bridge?",
                 options=("Sandy", "Ted", "Andy", "Bill"),
                 answer=2),

        Question(question="Who first peeped into the Mirror of Galadriel?",
                 options=("Frodo", "Merry", "Galadriel", "Sam"),
                 answer=3),

        Question(question="What had been left in Galadriel's care, to pass to Aragorn?",
                 options=("Anduril", "A green stone set in a brooch", "A banner", "A crown"),
                 answer=1),

        Question(question="Who, alone of the Fellowship, did the Elves demand should enter L??rien blindfolded?",
                 options=("Frodo", "Aragorn", "Boromir", "Gimli"),
                 answer=3),

        Question(question="Who wanted to see Elf-magic?",
                 options=("Frodo", "Boromir", "Sam", "Aragorn"),
                 answer=2),

        Question(question="According to Celeborn, who remembered things the wise should know?",
                 options=("Wizards", "Dwarfs", "Old wives", "Trees"),
                 answer=2),

        Question(question="What was the response of the dead to Aragorn's summons?",
                 options=("A horn blew", "A great cry", "A wind blew the torches out", "Their king appeared"),
                 answer=2),

        Question(question="How was Faramir struck down?",
                 options=("Hewn down by Orcs", "Stabbed by Southron spears",
                          "His horse was killed by an axeman", "Shot with a deadly dart"),
                 answer=3),

        Question(question="What weapons did the Easterlings prefer in battle?",
                 options=("Scimitars", "Spears", "Axes", "Daggers"),
                 answer=2),

        Question(question="Who slew Ugl??k?",
                 options=("Aragorn", "??omer", 'Merry', 'Pippin'),
                 answer=1),

        Question(question="Why did Treebeard take more kindly to Elves than to others?",
                 options=("Because they lived in the woods and cared for the trees",
                          "Because the Elves cured the Ents of dumbness long ago",
                          "Because the Elves were as long-lived as the Ents",
                          "Because the Elves would not harm the trees of Fangorn Forest"),
                 answer=1),

        Question(question="Where did Gandalf go, once rescued, after destroying the Balrog?",
                 options=("Caras Galadhon", "Rhosgobel, the house of Radagast",
                          "To Thranduil's Halls in Mirkwood", "Rivendell"),
                 answer=0),

        Question(question="What name did Aragorn cry out, as Gandalf rode Shadowfax from Edoras?",
                 options=("The White Rider!", "The Grey Pilgrim", "Mithrandir!", "Stormcrow!"),
                 answer=0),

        Question(question="Who did Pippin meet as he fled the Hallows, looking for Gandalf?",
                 options=("The Prince of Dol Amroth", "Beregond", "H??rin of the Keys",
                          "The warden of the Houses of Healing"),
                 answer=1),

        Question(question="In the song about the Battle of the Pelennor Fields, who was referred ot as"
                          " \"Thengling mighty\"?",
                 options=("Grimbold", "Hirluin", "Forlong", "Th??oden"),
                 answer=3),

        Question(question="What did Gandalf advise Th??oden should be done first?",
                 options=("To attack Mordor", "To build defences", "The destroy the threat of Saruman",
                          "To punish gr??ma"),
                 answer=2),

        Question(question="Who did Pippin call \"a fine old fellow\"?",
                 options=("Gandalf", "Th??oden", "Denethor", "Fatty Bolger"),
                 answer=1),

        Question(question="Of what did Gandalf warn the hobbits, when he left Isengard for Helm's Deep?",
                 options=("Stay our of the Huorn-wood", "Keep an eye out for gr??ma", "Keep away from Orthanc",
                          "Keep their eyes and ears open and their mouths shut"),
                 answer=2),

        Question(question="Who was Aragorn's father?",
                 options=("Aredhel", "Arathorn", "Imrahil", "Celeborn"),
                 answer=1),

        Question(question="Who fell in love with a fair Elf main, in the song that Aragorn sang on Weathertop?",
                 options=("Elrond", "Amroth", "Beren", "F??anor"),
                 answer=2),

        Question(question="What is the missing word: 'A ... Gilthoniel'?",
                 options=("Varda", "Elbereth", "Galadriel", "Berethil"),
                 answer=1),

        Question(question="What star was most beloved by the elves?",
                 options=("The North Star", "The Polar Star", "E??rendil", "Sirius"),
                 answer=2),

        Question(question="What gifts did Galadriel give Merry and Pippin, when the Company left Lothl??rien?",
                 options=("Bows and arrows", "Silver belts clasped with gold", "New pipes", "Swords"),
                 answer=1),

        Question(question="For how many leagues did the Three Hunters pursue the Orcs on foot?",
                 options=('5', '15', '45', '105'),
                 answer=2),

        Question(question="How many horses did ??omer lose in the battle near Entwood?",
                 options=('15', '12', '9', '30'),
                 answer=1),

        Question(question="What is the term for a young Ent?",
                 options=("An Entsprout", "An Entette", "An Entern", "An Enting"),
                 answer=3),

        Question(question="How does Gandalf summon the horses to carry the party from Fangorn to Edoras?",
                 options=("He lifts his hand and calls aloud in a great voice",
                          "He snaps his fingers and stamps hi feet",
                          "He whistles", "He claps loudly twice"),
                 answer=2),

        Question(question="Who proclaimed his titles, as the Company swept past the Pillars of the Argonath?",
                 options=("Boromir", "Legolas", "Gimli", "Aragorn"),
                 answer=3),

        Question(question="What was the name of the horse that Gandalf took from Th??oden?",
                 options=("Shadowfax", "Snowmane", "Bill", "Fleet of Foot"),
                 answer=0),

        Question(question="What reward did Merry promise Pippin for his bravery?",
                 options=("Almost a chapter a Bilbo's book", "A medal from Elrond",
                          "Three cheers from the hobbits in the Shire", "A purse of gold from Aragorn"),
                 answer=0),

        Question(question="Who worked the gems on the standard that Aragorn raised on teh foremost ship?",
                 options=("Galadriel", "Celebr??an", "Arwen", "Goldberry"),
                 answer=2),

        Question(question="Who did Galadriel describe as 'Queen of the Stars'?",
                 options=("Nimrodel", "Celebr??an", "Varda", "Arwen"),
                 answer=2),

        Question(question="How does the Ent Quickbeam get his name?",
                 options=("He says 'yes' to an elder Ent before he has finished his question",
                          "He walks everywhere quicker than the other Ents",
                          "He likes to stand in the open fields in the sun",
                          "He smiles and laughs at everyone"),
                 answer=0),

        Question(question="Who cried \"Death! Ride, ride to ruin and the world's ending!\"?",
                 options=("Erkenbrand", "Treebeard", "Aragorn", "??omer"),
                 answer=3),

        Question(question="Who stood next to Beregond in the front rank of the men of Gondor, outside the Black Gates?",
                 options=("Bergil", "Angbor", "Pippin", "Imrahil"),
                 answer=2),

        Question(question="Of what did Sam hope to get a glimpse in the peaceful days in Cormallen?",
                 options=("A cat of Queen Beruthiel", "A dragon", "An oliphaunt", "A scion of the Oldest Tree"),
                 answer=2),

        Question(question="Who took command of the City defence, when Denethor would not leave Faramir's bedside?",
                 options=("Imrahil", "Golasgil, lord of Anfalas", "Gandalf", "Forlong the Fat, Lord of Lossarnach"),
                 answer=2),

        Question(question="How many stars were there on the standard, borne on Aragorn's ship?",
                 options=("5", '7', '9', '6'),
                 answer=1),

        Question(question="By the banks of which river did the Company share a farewell feast with Celeborn and "
                          "Galadriel?",
                 options=("River Running", "Silverlode", "Baranduin", "Celebrant"),
                 answer=1),

        Question(question="At what age did Frodo come into his inheritance?",
                 options=("18", "25", "33", "42"),
                 answer=2),

        Question(question="Who came through the window, 'shears, grass clippings and all'?",
                 options=("Gandalf", "Frodo", "Tom Bombadil", "Sam"),
                 answer=3),

        Question(question="Complete the last line of Frodo's song \"For though it was day, to her surprise...\"",
                 options=("They all went back to bed", "The moon got up instead!",
                          "She said \"Right said Fred!\"", "Where's my ale and bread?"),
                 answer=0),

        Question(question="How far the Th??oden say it was from Edoras to Minas Tirith?",
                 options=("Five hundred leagues", "Fifty leagues", "A hundred leagues and two",
                          "A thousand leagues"),
                 answer=2),

        Question(question="What did Gandalf think had hastened the start of Sauron's assault of Minas Tirith?",
                 options=("Aragorn's use of the Palantir of Orthanc", "His return as Gandalf the White",
                          "The rousing of the Ents and destruction of Isengard",
                          "The victor of Rohirrim at Helm's Deep"),
                 answer=0),

        Question(question="Who told Th??oden that the weather was changing, as Gh??n-buri-Gh??n had said?",
                 options=("Widfara", "Wulfhelm", "Deorlaf", "Guthwine"),
                 answer=0),

        Question(question="To whom had the 'forgotten people' made the oath they later broke?",
                 options=("Arvedui", "Sauron", "Isildur", "Elrond"),
                 answer=2),

        Question(question="What did ??owyn give Merry before he left Dunharrow?",
                 options=("A sword", "A leather jerkin", "A cup", "Food for the journey"),
                 answer=1),

        Question(question="Denethor said there were two follies: -to send the Ring to Mordor in the hands of \""
                          "a witless halfling\", and...?",
                 options=("To trust in the wisdom of Gandalf",
                          "To try to send the Ring over the sea into the Ancient west",
                          "To use the Ring", "To place hope in the strength of arms"),
                 answer=2),

        Question(question="Who was banner bearer to the King of the Mark?",
                 options=("Elrond", "Guthlaf", "Gamling", "Eorl"),
                 answer=1),

        Question(question="Whom did the Warden in the House of Healing describe as 'very tough in the fibre'?",
                 options=("Hobbits", "Faramir", "??owyn", "Bergil"),
                 answer=0),

        Question(question="What did Gandalf say he would do regarding the terms the Mouth of Sauron offered?",
                 options=("Consider them, in his own time", "Reject them utterly", "Negotiate",
                          "Refer the decision to Aragorn"),
                 answer=1),

        Question(question="When peering into the Mirror of Galadriel, whom did Sam see cutting down trees?",
                 options=("Gaffer Gamgee", "Farmer Cotton", "Strange Men", "Ted Sandyman"),
                 answer=3),

        Question(question="What name did Galadriel give Aragorn, on his departure from Lothl??rien?",
                 options=("Strider", "D??nedain", "Anduril", "Elessar"),
                 answer=3),

        Question(question="What was King Th??oden's most precious horse called?",
                 options=("Shadowfax", "Bill", "Hasufel", "Roheryn"),
                 answer=0),


        Question(question="Which Elf blindfolded the Fellowship in Lothl??rien?",
                 options=("Haldir", "Rumil", "Orophin", "Nimrodel"),
                 answer=0),

        Question(question="What did Same first want to do, after peering into the Mirror of Galadriel?",
                 options=("Tell Frodo about it", "Go home", "Get on with the quest", "Touch the water"),
                 answer=1),

        Question(question="Who was Galadriel's daughter?",
                 options=("Arwen", "Celebr??an", "Nimrodel", "Finduilas"),
                 answer=1),

        Question(question="Where did the Captain of the West stop for a day on their return from the Fields of "
                          "Cormallen?",
                 options=("Emyn Muil", "Parth Galen", "Tol Brandir", "Osgiliath"),
                 answer=3),

        Question(question="When the new Tree was planted in the Court of the Fountain, what happened to the old one?",
                 options=("It was burned", "It was given to the Anduin", "It was laid to rest in Rath Dinen",
                          "It was mulched for compost for the new Tree"),
                 answer=2),

        Question(question="What is the next line: \"The Road goes ever on and on ...\"?",
                 options=("Like Bilbo's never ending song", "Like dreams beneath a summer sun",
                          "Down from the door where it began", "And from his doom he ran and ran"),
                 answer=2),

        Question(question="What name did Gandalf call the Balrog?",
                 options=("Flame of Arnor", "Flame of Shadow", "Fire of Sauron", "Flame of Ud??n"),
                 answer=3),

        Question(question="Who was the first Elf to welcome Frodo, in the eaves of L??rien?",
                 options=("Haldir", "H??rin", "Huan", "Hob"),
                 answer=0),

        Question(question="Who added a verse about fireworks to Gandalf's lament?",
                 options=("Frodo", "Bilbo", "Aragorn", "Sam"),
                 answer=3),

        Question(question="What relation was ??owyn to Th??oden?",
                 options=("Daughter", "Sister", "Wife", "Niece"),
                 answer=3),

        Question(question="What did Legolas desire from the Isengard doorwardens?",
                 options=("Cheese", "Sausages", "Wine", "Salad"),
                 answer=2),

        Question(question="How did Gandalf greet Pippin at the ruins of Isengard?",
                 options=("\"Hello Pippin! This is a pleasant surprise!\"",
                          "\"Get up, you tom-fool of a Took!\"",
                          "\"Pippin, stop nelly-podging around and tell me where Treebeard is!\"",
                          "\"Peregrin Took! What are you doing here?\""),
                 answer=1),
    ]

    return without_indices


def load_questions():
    questions = list()
    for ii, q in enumerate(construct_questions()):
        q.index = ii
        questions.append(q)

    print(f'We are working with {len(questions)} questions')
    return questions
