import random
import requests

def entertain(name):
    while True:    
        print("Here is what I can do:")
        print("1-Number guessing game")
        print("2-Magic 8-Ball")
        print("3-Rock-Paper-Scissors")
        print("4-Tell me a joke")
        print("5-Tell me a story")
        print("6-Dice roll game")
        print("7-Fun Fact")
        print("8-Pokemon Info Game")
        print("")
        
        choice = input(" ")

        # =========================
        # 1. Number Guessing Game
        # =========================
        if choice == "1":
            while True: # Outer loop for playing multiple rounds of the game
                r = random.randint(1, 100)
                guess1 = input("enter guess or X to exit: ")

                if guess1.lower() == "x":
                    break
                try:
                    guess = int(guess1)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if guess > r:
                    print("too high, try again")

                elif guess < r:
                    print("Too low, try again")

                else:
                    print("correct")
                    print("continue?")
                    answer = input("(yes/no to play again, or X to exit game): ")

                    if answer.lower() == "yes":
                        continue
                    else:
                        break # Breaks out of the inner guessing loop

        # =========================
        # 2. Magic 8-Ball
        # =========================
        if choice == "2":
            while True:
                liste = [
                    "It is certain.", "Without a doubt.", "Yes - definitely.",
                    "Most likely.", "Outlook good.", "Yes.",
                    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                    "Cannot predict now.", "Concentrate and ask again.",
                    "Don’t count on it.", "My reply is no.", "Outlook not so good.", "Very doubtful."
                ]

                print("Ask a yes/no question (or X to stop):")
                question = input("")

                if question.lower() == "x":
                    break

                print(random.choice(liste))

        # =========================
        # 3. Rock Paper Scissors
        # =========================
        if choice == "3":
            print(f"Welcome {name} to Rock-Paper-Scissors") # Fixed f-string syntax

            while True:
                choices = ["rock", "paper", "scissors"]
                comp = random.choice(choices)
                guess = input("rock, paper or scissors (press x to break): ")

                if guess.lower() == "x":
                    break

                if guess == comp:
                    print("It's a tie!")
                    print("computer's choice:", comp)

                elif guess == "rock" and comp == "scissors":
                    print("YOU win!")
                    print("computer's choice:", comp)

                elif guess == "rock" and comp == "paper":
                    print("You lose!")
                    print("computer's choice:", comp)

                elif guess == "paper" and comp == "rock":
                    print("YOU win!")
                    print("computer's choice:", comp)

                elif guess == "paper" and comp == "scissors":
                    print("YOU lose!")
                    print("computer's choice:", comp)

                elif guess == "scissors" and comp == "rock":
                    print("YOU lose!")
                    print("computer's choice:", comp)

                elif guess == "scissors" and comp == "paper":
                    print("YOU win!")
                    print("computer's choice:", comp)

                else:
                    print("invalid choice")

        # =========================
        # 4. Jokes Section
        # =========================
        if choice == "4":
            jokes = [
                "Why don’t programmers like nature? Too many bugs.",
                "Why do Python developers wear glasses? Because they can’t C.",
                "I told my computer I needed a break… and it said 'No problem, I’ll go to sleep.'",
                "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself.",
                "Why did the function break up with the loop? It felt trapped.",
                "Why did the computer go to the doctor? It had a virus!",
                "I tried to catch some fog… I mist.",
                "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                "Why don't skeletons fight each other? They don’t have the guts.",
                "Why was the math book sad? Too many problems.",
                "Why did the scarecrow win an award? He was outstanding in his field.",
                "Why don't eggs tell jokes? They’d crack each other up.",
                "Why do cows have hooves instead of feet? Because they lactose.",
                "Why did the bicycle fall over? It was two-tired.",
                "Why did the stadium get hot? All the fans left.",
                "Why don’t oysters donate to charity? Because they’re shellfish.",
                "What do you call fake spaghetti? An impasta.",
                "Why did the tomato blush? It saw the salad dressing!",
                "Why can't a nose be 12 inches long? Because then it would be a foot.",
                "Why don't scientists trust atoms? They make up everything."
            ]

            while True:
                joke = random.choice(jokes)
                print(joke)
                answer12 = input("Another joke? (yes/no): ")

                if answer12.lower() != "yes":
                    break

        # =========================
        # 5. Stories Section
        # =========================
        
        if choice == "5":

            stories = [
    """Lina found a tiny glowing stone.
She kept it in her pocket.
At night it lit up her whole room.
She realized it glowed stronger when she smiled.
So she decided to smile every day.""",

    """A cat named Oreo loved climbing trees.
One day he climbed too high.
He meowed loudly for help.
A kind boy brought a ladder.
Oreo jumped into his arms happily.""",

    """Sam planted a single seed in a cup.
He watered it every morning.
A week later a tiny sprout appeared.
Sam cheered like it won a trophy.
The plant grew as tall as his window.""",

    """Mira lost her red balloon.
She searched the whole park.
Suddenly it floated back down.
A child caught it and returned it.
Mira shared the balloon as a thank-you.""",

    """A puppy followed a butterfly.
It ran across the garden happily.
The butterfly landed on its nose.
The puppy froze in surprise.
Then they both ran off again.""",

    """Ali built a paper boat.
He placed it gently on the water.
It floated better than he expected.
A small wave pushed it far.
Ali clapped and made another boat.""",

    """Nora baked cookies for her friends.
She burned the first batch.
The second batch was perfect.
Her friends loved them.
Nora realized mistakes make you better.""",

    """A robot woke up alone in a lab.
It pressed a button labeled 'play'.
Soft music filled the room.
The robot danced happily.
Scientists found it and laughed.""",

    """A shy girl found a stray kitten.
She fed it every day.
The kitten followed her everywhere.
She named it Snow.
They both became less lonely.""",

    """A boy found a shiny coin.
He wished for ice cream.
A vendor appeared around the corner.
He bought his favorite flavor.
He kept the coin as a lucky charm.""",

    """Sara drew a rainbow on the street.
Rain started falling.
Her drawing washed away.
But the real rainbow appeared in the sky.
Sara smiled at the magic.""",

    """A tiny turtle was scared of swimming.
Its mother encouraged it gently.
It slowly entered the water.
It discovered it could swim well.
The turtle never feared again.""",

    """Omar loved stars.
He watched them every night.
One night a shooting star appeared.
He made a wish silently.
The next day his dream came true.""",

    """A bird fell from its nest.
A girl picked it up carefully.
She returned it to the nest.
The mother bird chirped loudly.
The girl felt like a hero.""",

    """A snowman felt lonely.
Children returned the next day.
They added new buttons and a scarf.
The snowman looked happy again.
He enjoyed the laughter around him.""",

    """Lily collected seashells.
She found a glowing one.
It hummed softly in her hand.
She kept it close as a treasure.
It always reminded her of the sea.""",

    """A mouse dreamed of being brave.
One day a storm scared all animals.
The mouse guided them to shelter.
Everyone thanked the mouse.
It finally felt brave.""",

    """A small robot cleaned the city.
People never noticed it.
One day it broke down.
Kids fixed it together.
The robot beeped happily.""",

    """A kite got stuck in a tree.
Two brothers tried pulling it.
Their dog barked and helped.
The kite finally came down.
They flew it together.""",

    """A lonely cloud drifted across the sky.
It looked for other clouds.
Then it found hundreds of them.
They formed a big fluffy family.
The cloud never drifted alone again.""",

    """A little boy talked to flowers.
People laughed at him.
But the flowers bloomed beautifully.
His garden became the prettiest.
Everyone asked for his secret.""",

    """A giraffe wanted to see the ocean.
It walked for days.
Finally it reached the shore.
Waves splashed its long legs.
The giraffe felt peaceful.""",

    """Two cats argued over a fish.
They fought until both were tired.
A dog walked by and grabbed it.
The cats stared at each other.
They never argued again.""",

    """A star fell into a river.
A girl found it glowing.
She placed it in a jar.
At night it lit her room.
The star returned to the sky by morning.""",

    """A parrot learned a new word.
It repeated it all day.
Everyone laughed at its excitement.
The parrot felt proud.
It kept learning new words.""",

    """A little dragon couldn’t breathe fire.
It practiced every day.
One day it sneezed and made sparks.
Its friends cheered loudly.
The dragon finally believed in itself.""",

    """A snail entered a race.
Everyone thought it would lose.
It kept going slowly.
The others got tired.
The snail won proudly.""",

    """A squirrel lost its acorn.
It searched all morning.
A bird dropped it from a tree.
The squirrel danced with joy.
It stored the acorn safely.""",

    """A penguin loved sliding on ice.
It raced with its friends.
It always came last.
But it never stopped smiling.
Everyone loved its spirit.""",

    """A young fox wanted to howl.
It tried every night.
Eventually it made a loud howl.
The forest echoed it back.
The fox felt powerful.""",

    """A boy built a sandcastle.
Waves destroyed it.
He built a bigger one.
The waves destroyed that too.
He laughed and built another.""",

    """A fish dreamed of the sky.
It jumped as high as it could.
One day a big wave lifted it.
It saw the sky clearly.
The fish felt happy.""",

    """Two rabbits found a carrot.
They shared it equally.
Both stayed full.
Both stayed friends.
Sharing made everything better.""",

    """A girl found a lost puppy.
She fed it and cleaned it.
She searched for its owner.
No one claimed it.
She adopted it with joy.""",

    """A robot learned to draw.
Its drawings were shaky.
Kids encouraged it.
Soon it drew beautiful pictures.
The robot decorated the classroom.""",

    """A cow wanted to jump.
It practiced secretly.
One day it finally jumped high.
Everyone clapped.
The cow felt proud.""",

    """A tiny bird sang loudly.
The forest laughed.
But the song reached the sky.
Clouds danced with the melody.
The forest stopped laughing.""",

    """A boy wrote his first poem.
He was shy to show it.
His teacher read it quietly.
She said it was beautiful.
The boy wrote many more.""",

    """A turtle and rabbit raced.
Rabbit ran too fast and slipped.
Turtle kept going slowly.
It reached the finish line first.
Rabbit congratulated turtle.""",

    """A bee got stuck in a flower.
A butterfly pulled it out.
They became friends.
They visited flowers together.
The bee felt grateful.""",

    """A fox lost its shadow.
It searched everywhere.
At sunset it finally saw it.
The shadow danced with it.
The fox laughed happily.""",

    """A frog loved dancing.
It danced in the rain.
Animals gathered to watch.
The frog felt proud.
It danced every rainy day.""",

    """A starfish wanted to explore.
It crawled across the beach.
A wave carried it far.
It landed in a tide pool.
It found new friends there.""",

    """A baby elephant feared thunder.
Its mother hugged it tightly.
The thunder slowly faded.
The elephant felt safe.
It slept peacefully.""",

    """A boy lost his toy car.
He searched everywhere.
His sister found it for him.
He thanked her with a hug.
They played together happily.""",

    """A butterfly landed on a book.
A girl followed it silently.
It stopped on a sunflower.
The girl drew it quickly.
The butterfly flew away gently.""",

    """A kitten couldn’t climb a couch.
It tried again and again.
Finally it climbed up.
It slept proudly on the cushion.
Its owner smiled warmly.""",

    """A little robot felt lonely.
It walked around the house.
It heard laughter in a room.
Kids invited it to play.
The robot felt loved."""
]
            while True:

                story = random.choice(stories)

                print (story)

                answer123 = input("Another?(yes/no): ")

                if answer123.lower() == "yes":
                    continue
                else:
                    break

#---------------------------------------------------------------------------------------------------
        if choice == "6":
                
            print("Welcome to the Dice Roll Game!")

            while True:
           
                dice = random.randint(1,6)

                print(dice)

                print("again(Yes/No)")
                answer1223 = input("")

                if answer1223.lower() == "yes":
                    continue

                else:
                    break
                
#----------------------------------------------------------------------------------:
            
        if choice == "7":

            while True:

                facts = ["Water expands when it freezes.",
        "Light travels at about 299,792 kilometers per second.",
        "The human body contains around 37 trillion cells.",
        "Earth revolves around the Sun once every 365.25 days.",
        "DNA is shaped like a double helix.",
        "Sound travels faster in water than in air.",
        "The speed of sound in air is about 343 meters per second.",
        "Jupiter is the largest planet in our solar system.",
        "The Sun is a medium-sized yellow star.",
        "Carbon is the fourth most abundant element in the universe.",
        "Lightning is hotter than the surface of the Sun.",
        "Photosynthesis converts carbon dioxide into oxygen and glucose.",
        "The ozone layer protects Earth from harmful UV radiation.",
        "The Milky Way galaxy contains over 100 billion stars.",
        "A day on Venus is longer than a year on Venus.",
        "Atoms are mostly empty space.",
        "Neutrons have no electric charge.",
        "Protons determine an element’s atomic number.",
        "The human brain has about 86 billion neurons.",
        "Oxygen is the most abundant element in Earth's crust.",
        "The Moon causes Earth's ocean tides.",
        "Einstein’s E=mc² relates energy to mass.",
        "Black holes have gravity so strong that not even light can escape.",
        "Mars has the largest volcano in the solar system, Olympus Mons.",
        "Ice is less dense than liquid water.",
        "Earth’s magnetic field protects us from solar wind.",
        "Bacteria can survive extreme environments, even space.",
        "The universe is about 13.8 billion years old.",
        "Helium was first discovered on the Sun before Earth.",
        "A prism splits white light into a spectrum of colors.",
        "Viruses are not technically alive.",
        "The human heart beats about 100,000 times per day.",
        "Whales are mammals, not fish.",
        "Plants release oxygen during photosynthesis.",
        "Electricity travels at nearly the speed of light.",
        "The periodic table organizes elements by atomic number.",
        "An octopus has three hearts.",
        "Carbon dioxide is a greenhouse gas.",
        "DNA stands for deoxyribonucleic acid.",
        "The boiling point of water decreases at higher altitudes.",
        "The human body is about 60% water.",
        "Gravity is weaker on the Moon than on Earth.",
        "Diamonds are made of carbon atoms arranged in a crystal lattice.",
        "The Earth’s core is mostly iron and nickel.",
        "Rainbows appear when sunlight is refracted through water droplets.",
        "Antibiotics kill bacteria but not viruses.",
        "A light-year measures distance, not time.",
        "Neptune has the strongest winds in the solar system.",
        "Earth’s atmosphere is about 78% nitrogen.",
        "The Andromeda Galaxy is the nearest major galaxy to the Milky Way.",
        "Radio waves have the longest wavelength in the electromagnetic spectrum.",
        "Ultraviolet light has shorter wavelengths than visible light.",
        "Chlorophyll gives plants their green color.",
        "Coral reefs are made of tiny animals called polyps.",
        "The human skeleton has 206 bones.",
        "Blood is red due to the iron in hemoglobin.",
        "Venus rotates in the opposite direction of most planets.",
        "There are 118 known elements on the periodic table.",
        "The largest organ in the human body is the skin.",
        "Salt lowers the freezing point of water.",
        "Sound cannot travel through a vacuum.",
        "Meteorites are rocks from space that land on Earth.",
        "Atoms consist of protons, neutrons, and electrons.",
        "Hydrogen is the lightest element.",
        "The Pacific Ocean is the largest ocean on Earth.",
        "Electric current is measured in amperes.",
        "Newton’s third law states that every action has an equal and opposite reaction.",
        "Cells are the basic units of life.",
        "The pH scale measures acidity or alkalinity.",
        "Our Sun will eventually become a red giant star.",
        "An ecosystem includes all living and nonliving components of an area.",
        "A supernova is a powerful explosion of a dying star.",
        "The Moon reflects sunlight; it doesn’t produce its own light.",
        "The Great Barrier Reef is the largest living structure on Earth.",
        "Iron rusts when it reacts with oxygen and water.",
        "Carbon is the basis of all known life forms.",
        "Water has a high specific heat capacity.",
        "The Milky Way is a barred spiral galaxy.",
        "Viruses can mutate rapidly.",
        "An atom’s nucleus contains nearly all its mass.",
        "The atmosphere gets thinner with altitude.",
        "Fossils provide evidence of past life forms.",
        "Saturn’s rings are mostly made of ice and rock.",
        "Electricity is the flow of electrons.",
        "Pluto is classified as a dwarf planet.",
        "Microwaves excite water molecules to heat food.",
        "Magnets have north and south poles.",
        "Earth’s rotation causes day and night.",
        "The largest organ inside the body is the liver.",
        "Lava becomes igneous rock when it cools.",
        "Tides are highest during a full moon and new moon.",
        "A black hole’s boundary is called the event horizon.",
                
       ]
                fact = random.choice(facts)

                print (fact)
                

                print("Continue?")
                answer = input("Yes/NO: ")

                if answer.lower() == "yes":
                    continue

                if answer.lower() == "no":
                    break

                
                    
#-----------------------------------------------------------------------------------
                
        if choice == "8":
            
            while True:


                pok = input("Enter Pokemon or x to stop: ").lower()
                
                if pok.lower() == "x":
                    break
                try:
                    url = f"https://pokeapi.co/api/v2/pokemon/{pok}"

                    response = requests.get(url)

                    if response.status_code !=200:
                        print("Pokemon not found")
                        continue


                    data = response.json()

                    height = data["height"]/10
                    weight = data["weight"]/10
                    id = data["id"]
                    

                    print("Here are the stats of ",pok,":")
                    print("")
                    print("Height(cm):",height,)
                    print("Weight(Kg):",weight,)
                    print("Id:",id,)


                    answer = input("Again(yes/no): ")

                    if answer.lower() == "yes":
                        continue

                    if answer.lower() == "no":
                        break
                except (requests.exceptions.RequestException, KeyError):
                    print("An error occurred. Please try again.")