from .. import CardClasses


"""
CardClasses.PlanetCard("Anshan",
                       "Commmit Ability: For each player, have them draw 1 card "
                       "or gain 1 resource.\n\n"
                       "Battle Ability: Rally 6 a unit with printed cost 3 or lower, put it "
                       "into play at this planet.",
                       1, 1, True, True, False, "Anshan"),
CardClasses.PlanetCard("Beckel",
                       "Forced Commit Ability: Deal 1 damage to a unit you control at this "
                       "planet.\n\nBattle Ability: Name a card. Look at your opponent's hand."
                       " If there is a cardby that name, gain 1 resource.",
                       1, 0, True, True, True, "Beckel"),
CardClasses.PlanetCard("Erida",
                       "Forced Commit Ability: Handsize is set to 8 this round.\n\n"
                       "Battle Ability: Sacrifice an army unit to draw 2 cards and gain 2 "
                       "resources.", 0, 1, True, True, True, "Erida"),
CardClasses.PlanetCard("Excellor",
                       "Commit Ability: Place 1 faith on an army unit.\n\n"
                       "Battle Ability: Switch the location of two army units of the same "
                       "player.", 1, 1, False, True, True, "Excellor"),
CardClasses.PlanetCard("Jalayerid",
                       "Commmit Ability: Deal 1 damage to a non-warlord unit at this planet.\n\n"
                       "Battle Ability: Deal 1 damage to a target enemy unit at each "
                       "adjacent planet and each enemy HQ.",
                       0, 2, True, False, False, "Jalayerid"),
CardClasses.PlanetCard("Jaricho",
                       "Forced Commit Ability: Reveal a card from your hand.\n\n"
                       "Battle Ability: Resolve a battle at another non-first planet where no "
                       "battle is taking place. (Can only be triggered during the combat phase.)",
                       1, 1, True, False, True, "Jaricho"),
CardClasses.PlanetCard("Munos",
                       "Commit Ability: Look at the top card of your deck, you may place it on the "
                       "bottom of your deck.\n\n"
                       "Battle Ability: Return a target army unit and each attachment on it "
                       "to its owner's hand. Then the unit's owner gains resources equal to the "
                       "unit cost.", 0, 2, False, False, True, "Munos"),
CardClasses.PlanetCard("Navida Prime",
                       "Commit Ability: Copy the Commit Ability of an adjacent planet.\n\n"
                       "Battle Ability: Copy the Battle Ability of a planet in a victory display.",
                       2, 0, False, False, True, "Navida_Prime"),
CardClasses.PlanetCard("Nectavus XI",
                       "Commit Ability: Remove 1 damage from an army unit at this planet.\n\n"
                       "Battle Ability: Resolve a command struggle at a planet. While resolving "
                       "it, control of each unit at that planet is switched with your opponent.",
                       1, 1, True, True, False, "Nectavus_XI"),
CardClasses.PlanetCard("Vargus",
                       "Commit Ability: Gain 1 resource (or 2 if your warlord is bloodied).\n\n"
                       "Battle Ability: Move 1 damage from a unit to another. If that other unit "
                       "is destroyed as a result of this effect, gain 1 resource.",
                       2, 0, False, True, False, "Vargus"),
"""


def planet_cards_init():
    planet_array = [CardClasses.PlanetCard("Plannum",
                                           "Battle Ability: Move a non-warlord unit "
                                           "you control to a planet of your choice.",
                                           1, 1, False, True, True,"Plannum"),
                    CardClasses.PlanetCard("Atrox Prime", "Battle Ability: Deal 1 damage "
                                                          "to each enemy unit at a target HQ or adjacent planet.",
                                           1, 1, True, True, False,"Atrox_Prime"),
                    CardClasses.PlanetCard("Barlus", "Battle Ability: Discard 1 card at "
                                                     "random from your opponent's hand.",
                                           2, 0, False, False, True, "Barlus"),
                    CardClasses.PlanetCard("Elouith", "Battle Ability: Search the top 3 cards of your deck for a card. "
                                                      "Add it to your hand, and place the remaining cards "
                                                      "on the bottom of your deck in any order.", 2, 0, False, True,
                                           False, "Elouith"),
                    CardClasses.PlanetCard("Carnath", "Battle Ability: Trigger the Battle ability "
                                                      "of another planet in play",
                                           1, 1, True, True, False, "Carnath"),
                    CardClasses.PlanetCard("Tarrus", "Battle Ability: If you control fewer units than your opponent, "
                                                     "gain 3 resources or draw 3 cards.", 1, 1, True, False, True,
                                           "Tarrus"),
                    CardClasses.PlanetCard("Osus IV", "Battle Ability: "
                                                      "Take 1 resource from your opponent.", 0, 2, False, False, True,
                                           "Osus_IV"),
                    CardClasses.PlanetCard("Ferrin", "Battle Ability: Rout a target non-warlord unit.",
                                           0, 2, True, False, False, "Ferrin"),
                    CardClasses.PlanetCard("Y'varn", "Battle Ability: Each player puts a unit into play "
                                                     "from his hand at his HQ.",
                                           0, 1, True, True, True, "Y'varn"),
                    CardClasses.PlanetCard("Iridial", "Battle Ability: Remove all damage from a target unit.",
                                           1, 0, True, True, True, "Iridial"),
                    CardClasses.PlanetCard("FINAL CARD", "", -1, -1, False, False, False, "NO IMAGE")]
    return planet_array
