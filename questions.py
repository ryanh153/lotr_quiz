from dataclasses import dataclass
from typing import Tuple


@dataclass
class Question:
    question: str
    options: Tuple[str, str, str, str]
    answer: int
    index: int = 0
    extra_text: str = ""


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
             answer=3),

    Question(question="Who was Théoden's banner-bearer?",
             options=("Herufara", "Eothain", "Grimbrand", "Guthlaf"),
             answer=3),

    Question(question="Who, on the battlefield, realised that Éowyn still lived?",
             options=("Amroth", "Aragorn", "Imrahil", "Erestor"),
             answer=2),

    Question(question="Trolls have what color blood?",
             options=("Black", "Green", "Red", "Khaki"),
             answer=0),

    Question(question="What protected Merry and Pippin from being slain by the rider whose horse jumped over them?",
             options=("They were hidden under their Elf cloaks", "They were hidden by Grishnákh",
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

    Question(question="What did Éomer call hobbits?",
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
             options=("Brego son of Eorl", "Eorl the Young", "Théoden son of Thengel", "The Stewards of Gondor"),
             answer=0),

    Question(question="What do men now call the region where the Entwives had their gardens?",
             options=("The Dead Marshes", "The Brown Lands", "The Old Forest", "The Grey Mountains"),
             answer=1),

    Question(question="What did Gandalf say lay beneath the 'great smoke' that Legolas saw?",
             options=("Fire and death", "Battle and war", "Wizardry and destruction", "Treachery and fighting"),
             answer=1),

    Question(question="What did Gimli choose when offered any gift from King Théoden's Armoury?",
             options=("An axe and chain-mail", "A sword and scabbard", "A knife and sheath", "A cap and shield"),
             answer=3),

    Question(question="Of what did Galadriel warn Legolas in her message?",
             options=("Mind the Gap of Rohan", "Beware the Sae", "Take care when crossing the Isen",
                      "Watch out for Oliphaunts"),
             answer=1),

    Question(question="Who did gríma truly serve while counsellor the Théoden?",
             options=("Saruman", "Sauron", "The Nazgûl", "Uglúk"),
             answer=0),

    Question(question="How old was Pippin when he became a soldier of Gondor?",
             options=("33", "50", "25", "28"),
             answer=3),

    Question(question="What did Aragorn call Théoden, when speaking of his body returning to Rohan?",
             options=("Théoden the Slayer", "Théoden the Renewed", "Théoden the Horse-Lord", "Théoden the Renowned"),
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
             options=("Éomer", "Éowyn", "Saruman", "Bilbo"),
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

    Question(question="Who was gríma's father?",
             options=("Glóin", "Gríma", "Grond", "Galmod"),
             answer=3),

    Question(question="What title did Merry and Pippin claim at the ruined gates of Isengard",
             options=("Gatekeepers", "Way-watchers", "Doorwardens", "Caretakers"),
             answer=2),

    Question(question="When he returned to Minas Tirith, what did Faramir do with his company from Henneth Annun?",
             options=("Sent them to guard Cair Andros", "Left them to watch the road from Minas Morgul",
                      "Left them at Henneth Annun to ambush more Oliphaunts",
                      "Sent them to strengthen the garrison at the fords of Osgiliath"),
             answer=3),

    Question(question="What did Ghân-buri-Ghân say before he vanished?",
             options=("\"Day is coming!\"", "\"Darkness is breaking\"", "\"Wind is changing!\"",
                      "\"Stone-houses are burning!\""),
             answer=2),

    Question(question="Who apart from Éowyn did Théoden ask to see, as he lay dying?",
             options=("Theodred", "Gandalf", "Éomer", "Pippin"),
             answer=2),

    Question(question="What frightened Frodo most in the Mirror of Galadriel?",
             options=("An eye", "His death", "The ruin of the Shire", "Bilbo wandering lost"),
             answer=0),

    Question(question="What gift did Galadriel give Boromir, when the Company left Lothlórien?",
             options=("A sword", "A shield", "A belt of gold", "A silver brooch"),
             answer=2),

    Question(question="What did Éomer rename Aragorn?",
             options=("Fastfoot", "Wingfoot", "Lightfoot", "Sorefoot"),
             answer=1),

    Question(question="Merry said to Théoden that he would run to battle eve if ...",
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

    Question(question="What decorated the gift Galadriel gave Sam, when he left Lothlórien?",
             options=("The 'G' rune", "A flower", "A tree", "The 'S' rune"),
             answer=0),

    Question(question="To where did Éomer ask Aragorn to return the horses he lent him?",
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

    Question(question="What gift did Galadriel give Frodo, when the Company left Lothlórien?",
             options=("A sword", "A golden belt", "A crystal vial", "A ring"),
             answer=2),

    Question(question="What was the name of the horse that Éomer lent to Legolas?",
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
             options=("Saruman", "Wormtongue", "Éomer", "Boromir"),
             answer=2),

    Question(question="At the Prancing Pony, what did Nob use to make a nice imitation of Frodo's head?",
             options=("A coconut", "A brown woolen mat", "A cushion", "A hedgehog"),
             answer=1),

    Question(question="What did Frodo shout out when he was stabbed, at Weathertop?",
             options=("Namarie!", "O Elbereth! Gilthoniel!", "Elen sila lumenn!", "Luthien Tinúviel!"),
             answer=1),

    Question(question="What were the yellow winter flowers called that grew on Cerin Amroth, in Lórien?",
             options=("Rosie", "Diamond", "Primula", "Elanor"),
             answer=3),

    Question(question="Mr Butterbur accused Frodo of breaking up his crocks with his ...?",
             options=("High notes", "Juggling", "Acrobatics", "Shenanigans"),
             answer=2),

    Question(question="What broken object did Strider show Frodo, in the parlour of the Prancing Pony?",
             options=("His leg", "His knife", "His backpack", "His sword"),
             answer=3),

    Question(question="Who was 'the fairest maiden that has ever been ...'?",
             options=("Amina", "Éowyn", "Luthien", "Arwen"),
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

    Question(question="How were the hobbits saved from Grishnákh?",
             options=("Uglúk found them", "They lost him in the dark", "A Rider killed him", "Pippin killed him"),
             answer=2),

    Question(question="Complete the phrase \"Sheep get like ...\"",
             options=("Shepherds", "Grass", "Dogs", "Barrels"),
             answer=0),

    Question(question="What Elven name does Legolas call Ents?",
             options=("Ornedrim", "Galadhrim", "Onodrim", "Erynhoth"),
             answer=2),

    Question(question="What colour was Théoden's shield?",
             options=("Gold", "Green", 'White', 'Red'),
             answer=0),

    Question(question="What type of weather was it, as the body of Théoden was taken to the city?",
             options=('Bright sunshine', 'Thick fog', 'Howling a gale', 'Rain'),
             answer=3),

    Question(question="What do Hill-Trolls do to their enemies?",
             options=('Scalp them', 'Bite their throats', 'Trample them', 'Poison them'),
             answer=1),

    Question(question="What had Treebeard forgotten that hobbits do?",
             options=('They sit down to eat', 'They comb their hair', 'They lie down to sleep', 'The bathe their feet'),
             answer=2),

    Question(question='What relation was Éowyn to Éomer?',
             options=('Wife', 'Sister', 'Cousin', 'None'),
             answer=1),

    Question(question='How many men of the Outlands rode to the defence of Minas Tirith, before the siege?',
             options=('One hundred thousand', 'Ten thousand', 'Three thousand', 'Five hundred'),
             answer=2),

    Question(question='What was the \'Silent Street\' called in the Hallows of Minas Tirith?',
             options=('Rath Dinen', 'Rathloriel', 'Rath Vorondil', 'Rath Numen'),
             answer=0),

    Question(question='Who was Aragorn\'s standard-bearer?',
             options=('Hama', 'Herugrim', 'Húrin', 'Halbarad'),
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
             options=('Éowyn', 'Éomer', 'Gríma', 'Merry'),
             answer=0),

    Question(question="What did Théoden call Minas Tirith?",
             options=('Mundeli', 'Oldburg', 'Mundburg', 'Oldbury'),
             answer=2),

    Question(question="When Gandalf said that he would allow only one more \"but\" tonight what did Pippin then ask "
                      "about?",
             options=("Aragorn's use of the Palantir of Orthanc", "Gollum", 'When Merry and the Rohirrim would arrive',
                      'Shelob'),
             answer=1),

    Question(question="What gift did Galadriel give Legolas when the Company left Lothlórien?",
             options=('A sword', 'A gold belt', 'A bow and arrows', 'Good advice'),
             answer=2),

    Question(question="How many men did Éomer lose in the battle near Entwood",
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
             options=('Gabilgathol', 'Bundushathûr', 'Kibil-nâla', 'Zirakzigil'),
             answer=3),

    Question(question="Why was Éomer not present to greet the Company, when they arrived at Meduseld?",
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

    Question(question="What did Gandalf put on the heads of Frodo and Sam, for the feast on the Field of Cormallen?",
             options=('Winged helms', 'Wreaths of scarlet flowers', 'Small golden coronets', 'Circlets of Silver'),
             answer=3),

    Question(question="What was the purpose of the gift Frodo received, on leaving Lothlórien?",
             options=('To bring good luck', 'To hide him from evil eyes', 'To prolong his strength',
                      'A light in dark places'),
             answer=3),

    Question(question="How many horses did the Three Hunters borrow from Éomer?",
             options=('3', '4', '2', '1'),
             answer=2),

    Question(question="How does Pippin interrupt the Entmoot when it first starts?",
             options=('He hiccups loudly', 'He belches', 'He yawns', 'He coughs politely'),
             answer=2),

    Question(question="Who the Théoden name as his heir when he rode off to battle?",
             options=('Éowyn', 'Éomer', 'Gandalf', 'Aragorn'),
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
             options=('Arnor', 'Annúminas', 'Osgiliath', 'Henneth Annun'),
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

    Question(question="Who did the people of Rohan trust to lead them in the absence of Théoden?",
             options=('Éowyn', 'Éomer', 'Hama', 'Helm'),
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

    Question(question="What was the name of the horse that Éomer lent to Aragorn?",
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
             options=('Lothlórien', 'Amon Hen', 'Henneth Annun', 'Fangorn'),
             answer=1),

    Question(question="How was Frodo's plan to continue alone spoiled?",
             options=('They had guessed he would go, and threw a farewell party for him',
                      'The whole Company came with him',
                      "Aragorn tied him to a tree so he couldn't go",
                      'Sam came back in time to go with him'),
             answer=3),

    Question(question="What was Théoden's sword called?",
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
             options=("Mûmakil", "Orcs", "Hill-Troll", "Uruk-hai"),
             answer=2),

    Question(question="Who brought the Sceptre of Annúminas to Minas Tirith?",
             options=("Galadriel", "Círdan", "Radagast", "Elrond"),
             answer=3),

    Question(question="What did Bilbo leave for Adelard Took?",
             options=("A horse", "An umbrella", "A shoe shine kit", "A doormat"),
             answer=1),

    Question(question="What is Tinúviel, in the Common Speech?",
             options=("Lark", "Nightingale", "Cuckoo", "Thrush"),
             answer=1),

    Question(question="When on Caradhras, to whom did Gandalf say \"if Elves could fly over mountain, they might "
                      "fetch the Sun to save us\"?",
             options=("Gimli", "Legolas", "Aragorn", "Frodo"),
             answer=1),

    Question(question="When Aragon leapt to Gandalf's defence on the Moria bridge, whose name did Aragorn call out?",
             options=("Narsil!", "Elendil!", "Arwen!", "Eur!"),
             answer=1),

    Question(question="What choices did Théoden give gríma when his treachery was discovered?",
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

    Question(question="Who, alone of the Fellowship, did the Elves demand should enter Lórien blindfolded?",
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
]

questions = list()
for ii, q in enumerate(without_indices):
    q.index = ii
    questions.append(q)


print(f'We are working with {len(questions)} questions')
