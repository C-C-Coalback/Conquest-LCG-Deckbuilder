from ..CardClasses import PlanetCard


def planet_cards_init():
    planet_array = [
        PlanetCard("Plannum",
                   "Battle Ability: Move a non-warlord unit "
                   "you control to a planet of your choice.",
                   1, 1, False, True, True, "Traxis"),
        PlanetCard("Atrox Prime", "Battle: Deal 1 damage "
                                  "to each enemy unit at a target HQ or adjacent planet.",
                   1, 1, True, True, False, "Traxis"),
        PlanetCard("Barlus", "Battle: Discard 1 card at "
                             "random from your opponent's hand.",
                   2, 0, False, False, True, "Traxis"),
        PlanetCard("Elouith", "Battle: Search the top 3 cards of your deck for a card. "
                              "Add it to your hand, and place the remaining cards "
                              "on the bottom of your deck in any order.", 2, 0, False, True, False, "Traxis"),
        PlanetCard("Carnath", "Battle: Trigger the Battle ability "
                              "of another planet in play",
                   1, 1, True, True, False, "Traxis"),
        PlanetCard("Tarrus", "Battle: If you control fewer units than your opponent, "
                             "gain 3 resources or draw 3 cards.", 1, 1, True, False, True, "Traxis"),
        PlanetCard("Osus IV", "Battle: "
                              "Take 1 resource from your opponent.", 0, 2, False, False, True, "Traxis"),
        PlanetCard("Ferrin", "Battle: Rout a target non-warlord unit.",
                   0, 2, True, False, False, "Traxis"),
        PlanetCard("Y'varn", "Battle: Each player puts a unit into play "
                             "from his hand at his HQ.",
                   0, 1, True, True, True, "Traxis"),
        PlanetCard("Iridial", "Battle: Remove all damage from a target unit.",
                   1, 0, True, True, True, "Traxis"),
        PlanetCard("Anshan",
                   "Battle: Rally 6 a unit with printed cost 3 or lower, put it "
                   "into play at this planet.",
                   1, 1, True, True, False, "Gardis",
                   commit_text="Commit: For each player, have them draw 1 card or gain 1 resource."),
        PlanetCard("Beckel",
                   "Battle: Name a card. Look at your opponent's hand."
                   " If there is a card by that name, gain 1 resource.",
                   1, 0, True, True, True, "Gardis",
                   commit_text="Forced Commit: Deal 1 damage to a unit you control at this planet."),
        PlanetCard("Erida",
                   "Battle: Sacrifice an army unit to draw 2 cards and gain 2 "
                   "resources.", 0, 1, True, True, True, "Gardis",
                   commit_text="Forced Commit: Handsize is set to 8 this round."),
        PlanetCard("Excellor",
                   "Battle: Switch the location of two army units of the same "
                   "player.", 1, 1, False, True, True, "Gardis",
                   commit_text="Commit: Place 1 faith on an army unit."),
        PlanetCard("Jalayerid",
                   "Battle: Deal 1 damage to a target enemy unit at each "
                   "adjacent planet and each enemy HQ.",
                   0, 2, True, False, False, "Gardis",
                   commit_text="Commit: Deal 1 damage to a non-warlord unit at this planet."),
        PlanetCard("Jaricho",
                   "Battle: Resolve a battle at another non-first planet where no "
                   "battle is taking place. (Can only be triggered during the combat phase.)",
                   1, 1, True, False, True, "Gardis",
                   commit_text="Forced Commit: Reveal a card from your hand."),
        PlanetCard("Munos",
                   "Battle: Return a target army unit and each attachment on it "
                   "to its owner's hand. Then the unit's owner gains resources equal to the "
                   "unit cost.", 0, 2, False, False, True, "Gardis",
                   commit_text="Commit: Look at the top card of your deck, you may place it on the "
                               "bottom of your deck."),
        PlanetCard("Navida Prime",
                   "Battle: Copy the Battle Ability of a planet in a victory display.",
                   2, 0, False, False, True, "Gardis",
                   commit_text="Commit: Copy the Commit Ability of an adjacent planet."),
        PlanetCard("Nectavus XI",
                   "Battle: Resolve a command struggle at a planet. While resolving "
                   "it, control of each unit at that planet is switched with your opponent.",
                   1, 1, True, True, False, "Gardis",
                   commit_text="Commit: Remove 1 damage from an army unit at this planet."),
        PlanetCard("Vargus",
                   "Battle: Move 1 damage from a unit to another. If that other unit "
                   "is destroyed as a result of this effect, gain 1 resource.",
                   2, 0, False, True, False, "Gardis",
                   commit_text="Commit: Gain 1 resource (or 2 if your warlord is bloodied)."),
        PlanetCard("Zarvoss Foundry",
                   "Battle: Rally 8 a support or attachment card, put it into play at your HQ or "
                   "attached to an eligible target.",
                   1, 0, True, True, True, "Veros"),
        PlanetCard("Xenos World Tallin",
                   "Battle: Target a planet. Your opponent must move an army unit he controls to that planet. "
                   "Then you may move an army unit you control to that planet.",
                   1, 1, False, True, True, "Veros"),
        PlanetCard("Mangeras",
                   "Battle: Remove up to 4 damage among cards you control.",
                   1, 1, True, True, False, "Veros"),
        PlanetCard("Kunarog The Slave Market",
                   "Battle: Put 2 token units (of any kind) into play exhausted at a target planet.",
                   0, 2, True, False, False, "Veros"),
        PlanetCard("Ironforge",
                   "Battle: You may move an army unit to your HQ. Then an army unit in your HQ gets "
                   "+2 ATK and +2 HP until the end of the game.",
                   2, 0, False, False, True, "Veros"),
        PlanetCard("Frontier World Jaris",
                   "Battle: If you have fewer cards in hand than your opponent, draw 3 cards.",
                   0, 1, True, True, True, "Veros"),
        PlanetCard("Daprian's Gate",
                   "Battle: Exhaust an army unit. That unit cannot ready during the next headquarters phase.",
                   0, 2, False, False, True, "Veros"),
        PlanetCard("Craftworld Lugath",
                   "Battle: Switch this planet, if it is not the first planet, with another one or copy "
                   "the Battle ability of an adjacent planet.",
                   2, 0, False, True, False, "Veros"),
        PlanetCard("Contaminated World Adracan",
                   "Battle: Deal 1 damage to up to 5 units at a target planet. Then, you may infest it.",
                   1, 1, True, True, False, "Veros"),
        PlanetCard("Bhorsapolis The Decadent",
                   "Battle: Put a non-Elite unit into play from your discard pile or your hand at the last "
                   "planet or your HQ.", 1, 1, True, False, True, "Veros"),
        PlanetCard("Wounded Scream",
                   "Battle: Gain 2 resources and draw 1 card. Then you may have this card's textbox be "
                   "considered blank.", 1, 1, True, True, True, "The Breach"),
        PlanetCard("Tool of Abolition",
                   "Battle: Deal 2 damage to an army unit and exhaust it or remove 2 damage from a unit "
                   "and ready it.", 1, 1, True, True, False, "The Breach"),
        PlanetCard("The Frozen Heart",
                   "Battle: Trigger the battle ability of a planet in your or your opponent's victory display.",
                   1, 0, True, True, True, "The Breach"),
        PlanetCard("Petrified Desolations",
                   "Battle: Remove 1 damage from up to 3 units, or deal 1 damage to up to 2 units.",
                   0, 2, True, False, False, "The Breach"),
        PlanetCard("Immortal Sorrows",
                   "Battle: Your warlord gains Brutal or Armorbane.",
                   1, 1, True, True, False, "The Breach"),
        PlanetCard("Hell's Theet",
                   "Battle: A target army unit gets +3 HP or place 5 faith among units you control.",
                   1, 1, False, True, True, "The Breach"),
        PlanetCard("Freezing Tower",
                   "Battle: Move an army unit with a printed cost of 3 or lower you control to a target "
                   "planet or rout a target army unit.",
                   0, 2, False, False, True, "The Breach"),
        PlanetCard("Clipped Wings",
                   "Battle: Draw a card or discard your hand to draw 4 cards.",
                   1, 1, True, False, True, "The Breach"),
        PlanetCard("Beheaded Hope",
                   "Battle: Return an army unit you control to your hand to gain 3 resources or deploy an "
                   "army unit, reducing its cost by 2.",
                   2, 0, False, False, True, "The Breach"),
        PlanetCard("Baneful Veil",
                   "Battle: Trigger the battle ability of an adjacent left or right planet.",
                   2, 0, False, True, False, "The Breach"),
        PlanetCard("Xorlom",
                   "Forced Battle: Rout an army unit you control.",
                   0, 2, False, False, True, "Nepthis"),
        PlanetCard("Selphini VII",
                   "Forced Battle: Your opponent may move a damage from a unit to another, then remove another damage.",
                   1, 1, True, True, False, "Nepthis"),
        PlanetCard("New Vulcan",
                   "Forced Battle: Move your warlord to the last planet. Then exhaust it.",
                   1, 1, False, True, True, "Nepthis"),
        PlanetCard("Hissan XI",
                   "Forced Battle: Have your opponent target another planet in play, you must trigger the battle "
                   "ability of that planet.", 2, 0, False, True, False, "Nepthis"),
        PlanetCard("Gareth Prime",
                   "Forced Battle: Your opponent may move a target army unit you control to a planet "
                   "of his choice.", 1, 0, True, True, True, "Nepthis"),
        PlanetCard("Erekiel",
                   "Forced Battle: Your opponent chooses: place up to 4 faith among units he controls, or do it "
                   "at the beginning of the next deploy phase.",
                   2, 0, False, False, True, "Nepthis"),
        PlanetCard("Diamat",
                   "Forced Battle: Deal 2 indirect damage among units you control.",
                   1, 1, True, False, True, "Nepthis"),
        PlanetCard("Coradim",
                   "Forced Battle: Sacrifice an army unit.",
                   0, 2, True, False, False, "Nepthis"),
        PlanetCard("Belis",
                   "Forced Battle: Discard a card.",
                   1, 1, True, True, True, "Nepthis"),
        PlanetCard("Agerath Minor",
                   "Forced Battle: Your opponent draws a card and gains 1 resource.",
                   1, 1, True, True, False, "Nepthis"),
        PlanetCard("Radex",
                   "Battle: Exhaust a target non-Elite army unit to have it gain a keyword among Mobile, Flying, "
                   "Armorbane, Sweep (3) or Retaliate (4).",
                   0, 1, True, True, True, "Sargos"),
        PlanetCard("Langeran",
                   "Battle: Have a target army unit or support lose its textbox until the end of the next round.",
                   1, 1, True, True, False, "Sargos"),
        PlanetCard("Josoon",
                   "While Captured: owner gains 1 resource each deploy phase.\n"
                   "Battle: Exhaust a target army unit. Then move it to an adjacent planet.",
                   2, 0, False, True, False, "Sargos"),
        PlanetCard("Ice World Hydras IV",
                   "Battle: Reveal the top card of your deck until you reveal a unit, you may deploy it at a "
                   "planet reducing its cost by 1. Then shuffle your deck.",
                   2, 0, False, False, True, "Sargos"),
        PlanetCard("Heletine",
                   "Battle: Look at the top 4 cards of your deck. Place up to 4 at the bottom in any order. "
                   "Then, gain 1 resource.", 1, 1, True, False, True, "Sargos"),
        PlanetCard("Fortress World Garid",
                   "While captured: the first shield card the owner plays each round gains 1 shield.\n"
                   "Battle: Draw 3 cards. Then discard a card.",
                   0, 2, True, False, False, "Sargos"),
        PlanetCard("Fenos",
                   "Army units cannot enter play at this planet during the combat phase.\n"
                   "Battle: Deal 2 damage among up to two target units.",
                   1, 1, False, True, True, "Sargos"),
        PlanetCard("Essio",
                   "Increase cost to deploy Elite units at this planet by 2.\n"
                   "Battle: Discard up to 2 cards, for each card discarded draw 2 cards or gain 2 resources.",
                   1, 1, True, True, False, "Sargos"),
        PlanetCard("Daemon World Ivandis",
                   "While captured: owner's warlord gets +2 HP.\n"
                   "Battle: Remove up to 3 damage from a unit, then you may turn your warlord to its hale side.",
                   0, 2, False, False, True, "Sargos"),
        PlanetCard("Chiros The Great Bazaar",
                   "Each warlord at this planet gets +1 ATK.\n"
                   "Battle: Look at the planets removed from the game. Reveal one to trigger its battle ability.",
                   1, 0, True, True, True, "Sargos")
    ]
    return planet_array
