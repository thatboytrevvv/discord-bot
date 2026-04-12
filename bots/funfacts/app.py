import os
import random
import requests
from datetime import date, timedelta

# Discord webhook URL
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

facts = [
    # Animals
    "Octopuses have three hearts, nine brains, and blue blood.",
    "A group of flamingos is called a 'flamboyance.'",
    "Sea otters hold hands while sleeping so they don't drift apart.",
    "Cows have best friends and get stressed when separated from them.",
    "The mantis shrimp can punch with the force of a .22 caliber bullet.",
    "Tardigrades (water bears) can survive the vacuum of outer space.",
    "A single strand of spider silk is five times stronger than a strand of steel the same thickness.",
    "Dolphins have names for each other — unique signature whistles they use to call specific individuals.",
    "The heart of a blue whale is so large that a small child could swim through its arteries.",
    "Honey bees can recognize human faces.",
    "An octopus can taste with its arms — each sucker has thousands of chemical receptors.",
    "Wombat poop is cube-shaped, which prevents it from rolling away and helps mark territory.",
    "Axolotls can regenerate their brains, hearts, and limbs.",
    "Crows can remember human faces and hold grudges for years.",
    "Elephants are the only animals that can't jump, but they can communicate through vibrations in the ground felt through their feet.",

    # Space
    "There are more stars in the observable universe than grains of sand on all of Earth's beaches.",
    "A day on Venus is longer than a year on Venus — it takes 243 Earth days to rotate once but only 225 days to orbit the Sun.",
    "Neutron stars are so dense that a teaspoon of their material would weigh about 6 billion tons.",
    "The footprints on the Moon will likely remain there for 100 million years since there's no wind or water to erode them.",
    "Space is completely silent because there are no molecules to transmit sound.",
    "If you could fold a piece of paper 42 times, it would reach the Moon.",
    "Saturn's density is low enough that it would float if placed in a bathtub large enough to hold it.",
    "The Sun makes up 99.86% of all the mass in our solar system.",
    "There's a giant cloud of alcohol in space (Sagittarius B2) that spans 288 billion miles.",
    "One million Earths could fit inside the Sun.",
    "A year on Mercury is just 88 Earth days, but a single day (sunrise to sunrise) lasts 176 Earth days.",
    "The Voyager 1 spacecraft, launched in 1977, is the farthest human-made object from Earth — over 15 billion miles away.",
    "There are rogue planets that float through space without orbiting any star.",
    "Olympus Mons on Mars is the tallest known volcano in the solar system — nearly three times the height of Mount Everest.",

    # Human body
    "Your body produces about 25 million new cells each second.",
    "The human nose can detect over 1 trillion different scents.",
    "You produce enough saliva in your lifetime to fill two swimming pools.",
    "Human bones are stronger than steel — ounce for ounce, bone is stronger than steel.",
    "Your brain uses about 20% of your body's total energy, despite being only 2% of your body weight.",
    "Humans share about 60% of their DNA with bananas.",
    "The acid in your stomach is strong enough to dissolve metal — your stomach lining has to regenerate every few days to survive it.",
    "Your body contains about 37.2 trillion cells.",
    "Nerve impulses travel at speeds up to 250 mph.",
    "The human eye can distinguish approximately 10 million different colors.",

    # History
    "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid of Giza.",
    "Oxford University is older than the Aztec Empire — teaching began at Oxford around 1096, while the Aztec Empire was founded in 1428.",
    "Ancient Romans used crushed mouse brains as toothpaste.",
    "The shortest war in history lasted 38 to 45 minutes — between Britain and Zanzibar on August 27, 1896.",
    "During the 1800s, dentures were commonly made from the teeth of dead soldiers.",
    "The Great Fire of London in 1666 destroyed 13,200 houses but officially only 6 deaths were recorded.",
    "Vikings used the bones of slain animals to forge their weapons, believing it would give the weapons the spirit of the animal.",
    "Napoleon was once attacked by a horde of rabbits during a rabbit hunt organized for his amusement.",
    "The ancient Egyptians used slabs of stone as pillows.",
    "Woolly mammoths were still alive when the Great Pyramid of Giza was being built.",

    # Science
    "Hot water freezes faster than cold water under certain conditions — a phenomenon known as the Mpemba effect.",
    "A single bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "Bananas are naturally radioactive because they contain potassium-40.",
    "Glass is technically not a solid or a liquid — it's an amorphous solid.",
    "If you removed all the empty space from the atoms that make up every human on Earth, the entire population could fit into an apple.",
    "Honey never spoils — edible honey has been found in 3,000-year-old Egyptian tombs.",
    "Water can boil and freeze at the same time — it's called the 'triple point.'",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "A photon of light takes about 8 minutes to travel from the Sun to Earth, but it can take 100,000 years to travel from the Sun's core to its surface.",
    "Diamond rain falls on Saturn and Jupiter.",

    # Geography & Nature
    "There's a lake in Australia called Lake Hillier that is naturally bright pink.",
    "Russia has a larger surface area than Pluto.",
    "The Amazon Rainforest produces about 20% of the world's oxygen.",
    "There are more trees on Earth than stars in the Milky Way — roughly 3 trillion trees vs. 100-400 billion stars.",
    "The Dead Sea is so salty that nothing can sink in it — you float effortlessly.",
    "Canada has more lakes than the rest of the world combined.",
    "Mount Everest grows about 4 millimeters taller every year due to tectonic activity.",
    "There's enough water in Lake Superior to cover all of North and South America in one foot of water.",
    "Lightning strikes Earth about 100 times every second.",
    "The Sahara Desert is roughly the same size as the entire United States.",

    # Everyday & Pop Culture
    "The inventor of the Pringles can is buried in one — Fredric Baur's ashes were placed in a Pringles can per his request.",
    "A jiffy is an actual unit of time — it's 1/100th of a second.",
    "The average person walks the equivalent of five times around the Earth in their lifetime.",
    "The total weight of all the ants on Earth is roughly equal to the total weight of all the humans.",
    "It would take about 1.2 million mosquito bites to drain all the blood from a human body.",
    "The dot over the letters 'i' and 'j' is called a 'tittle.'",
    "A standard deck of shuffled cards has more possible arrangements than there are atoms on Earth.",
    "Bubble wrap was originally invented as wallpaper.",
    "The average cloud weighs about 1.1 million pounds.",
    "It rains diamonds on Neptune and Uranus.",

    # Food
    "Strawberries aren't actually berries, but bananas, avocados, and watermelons are.",
    "It takes about 70 licks to get to the center of a Tootsie Pop.",
    "Apples float in water because they are 25% air.",
    "Peanuts are one of the ingredients in dynamite.",
    "Carrots were originally purple before the 17th century, when the Dutch cultivated the orange variety.",
    "Chocolate was once used as currency by the Aztecs.",
    "Ketchup was sold as medicine in the 1830s.",
    "A single saffron flower yields only three threads of saffron, which is why it's the most expensive spice in the world.",
    "Cashews grow on the bottom of cashew apples.",
    "Lemons contain more sugar than strawberries.",

    # Technology
    "The first computer virus was created in 1983 and was called the 'Elk Cloner.'",
    "More people in the world have access to a mobile phone than to a toilet.",
    "The QWERTY keyboard was designed to slow typists down — early typewriters jammed if keys were pressed too quickly.",
    "The first message ever sent over the internet was 'LO' — it was supposed to be 'LOGIN' but the system crashed after two letters.",
    "A single Google search uses about 0.3 watt-hours of electricity — enough to power a 60-watt light bulb for 18 seconds.",
    "About 90% of the world's currency exists only in digital form.",
    "The first 1 GB hard drive, introduced in 1980, weighed about 550 pounds and cost $40,000.",
    "Nintendo was founded in 1889 as a playing card company.",
    "Email existed before the World Wide Web.",
    "The first alarm clock could only ring at 4 a.m.",
]


def get_random_fact():
    """Pick a fact based on today's date — deterministic, no storage needed.

    Uses the number of days since an epoch to walk through a shuffled
    copy of the facts list.  The shuffle is seeded so the order is
    fixed but non-obvious, and the list cycles once all facts are used.
    """
    epoch = date(2025, 1, 1)
    day_number = (date.today() - epoch).days

    # Seed a local RNG so the shuffle is always the same
    rng = random.Random(42)
    indices = list(range(len(facts)))
    rng.shuffle(indices)

    return facts[indices[day_number % len(facts)]]


def send_fact():
    """Send a random fun fact to Discord via webhook."""
    fact = get_random_fact()

    payload = {
        "embeds": [
            {
                "title": "🧠 Fun Fact of the Day",
                "description": fact,
                "color": 0x5865F2,
            }
        ]
    }

    response = requests.post(
        WEBHOOK_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 204:
        print(f"Successfully sent fact: {fact[:60]}...")
    else:
        print(f"Failed to send: {response.status_code} - {response.text}")


if __name__ == "__main__":
    send_fact()
