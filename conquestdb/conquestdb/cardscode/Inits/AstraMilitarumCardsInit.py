from .. import CardClasses


def astra_militarum_cards_init():
    faction = "Astra Militarum"
    astra_militarum_cards_array = [
        CardClasses.WarlordCard("Colonel Straken", "Each other soldier or warrior unit "
                                                   "you control at this planet gets "
                                                   "+1 ATK.", "Soldier. Catachan.",
                                faction, 2, 6, 2, 5,
                                "Bloodied.", 7, 7,
                                ["4x Straken's Command Squad", "2x Glorious Intervention",
                                 "1x Omega Zero Command", "1x Straken's Cunning"]
                                ),
        CardClasses.ArmyCard("Straken's Command Squad", "Interrupt: When this unit leaves "
                                                        "play, put a Guardsman token "
                                                        "into play at the same planet.",
                             "Soldier. Catachan.", 2, faction, "Signature",
                             2, 2, 1, False),
        CardClasses.SupportCard("Omega Zero Command", "Reaction: After you win a command "
                                                      "struggle, put a Guardsman token "
                                                      "into play at that planet.",
                                "Location.", 2, faction, "Signature", False),
        CardClasses.EventCard("Glorious Intervention", "Reaction: After a unit is assigned "
                                                       "damage by an attack, sacrifice a "
                                                       "Soldier or Warrior unit at the same "
                                                       "planet to prevent all of that "
                                                       "damage. Then, deal X damage to the "
                                                       "attacker. X is the sacrificed "
                                                       "unit's printed ATK value.",
                              "Tactic.", 1, faction, "Signature", 1, False),
        CardClasses.AttachmentCard("Straken's Cunning", "Attach to an army unit.\n"
                                                        "Attached unit gets +1 ATK.\n"
                                                        "Interrupt: When attached unit "
                                                        "leaves play, draw 3 cards.",
                                   "Skill.", 1, faction, "Signature", 3, False,
                                   type_of_units_allowed_for_attachment="Army",
                                   extra_attack=1),
        CardClasses.ArmyCard("Ratling Deadeye", "Ranged. (This unit attacks during the "
                                                "ranged skirmish at the beginning of"
                                                " a battle.)", "Scout. Abhuman.", 1,
                             faction, "Common", 1, 1, 1, False, ranged=True),
        CardClasses.ArmyCard("Cadian Mortar Squad", "Ranged. (This unit attacks during the "
                                                    "ranged skirmish at the beginning of"
                                                    " a battle.)\n"
                                                    "Reaction: After an army unit you "
                                                    "control at this planet leaves play, "
                                                    "ready this unit.", "Soldier. Cadia.",
                             3, faction, "Loyal", 1, 3, 2, False, ranged=True),
        CardClasses.ArmyCard("Sanctioned Psyker", "", "Psyker.", 2, faction, "Common",
                             0, 4, 2, False),
        CardClasses.ArmyCard("Leman Russ Battle Tank", "No Wargear Attachments.",
                             "Vehicle. Tank. Elite.", 5, faction, "Loyal",
                             4, 6, 4, False, wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Mordian Hellhound", "No Wargear Attachments.\n"
                                                  "Area Effect (1). (When this unit "
                                                  "attacks it may instead deal its "
                                                  "Area Effect damage to each enemy "
                                                  "unit at this planet.",
                             "Vehicle. Tank. Mordian.", 4, faction, "Common",
                             3, 3, 2, False, area_effect=1,
                             wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Assault Valkyrie", "No Wargear Attachments.\n Flying. (This "
                                                 "unit takes half damage from non-Flying "
                                                 "units.", "Vehicle. Transport.",
                             4, faction, "Common", 4, 4, 1, False,
                             wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Stalwart Ogryn", "Immune to enemy events.",
                             "Warrior. Abhuman.", 2, faction, "Common",
                             2, 2, 1, False),
        CardClasses.ArmyCard("Captain Markis", "Action: Sacrifice an Astra Militarum unit "
                                               "at this planet to exhaust a target "
                                               "non-warlord unit at this planet. "
                                               "(Limit once per phase.)",
                             "Soldier. Officer. Vostroya.",
                             3, faction, "Loyal", 2, 3, 2, True,
                             action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.ArmyCard("Enginseer Augur", "Interrupt: When this unit leaves play, "
                                                "search the top 6 cards of your deck for "
                                                "an Astra Militarum support card with "
                                                "printed cost 2 or lower. Put that card "
                                                "into play at your HQ, and place the "
                                                "remaining cards on the bottom of your deck "
                                                "in any order.", "Scholar. Tech-Priest.",
                             2, faction, "Common", 2, 2, 0, False),
        CardClasses.ArmyCard("Penal Legionnaire", "", "Conscript. Ally.",
                             0, faction, "Common", 1, 1, 0, False),
        CardClasses.ArmyCard("Infantry Conscripts", "This unit gets +2 ATK for each "
                                                    "support you control.", "Conscript.",
                             4, faction, "Common", 0, 5, 0, False),
        CardClasses.ArmyCard("Elysian Assault Team", "Interrupt: When a Soldier or Warrior "
                                                     "unit you control leaves play from a "
                                                     "planet, put this unit into play "
                                                     "from your hand at the same planet.",
                             "Soldier. Elysia.", 2, faction, "Common", 2, 1, 0, False),
        CardClasses.EventCard("Preemptive Barrage", "Combat Action: Target up to 3 Astra "
                                                    "Militarum units you control at the "
                                                    "same planet. Each targeted unit gains "
                                                    "Ranged until the end of the phase. "
                                                    "(Units with Ranged attack during the "
                                                    "ranged skirmish at the beginning "
                                                    "of the battle.)", "Tactic.", 1,
                              faction, "Loyal", 2, False, action_in_hand=True,
                              allowed_phases_in_hand="COMBAT"),
        CardClasses.EventCard("Suppressive Fire", "Combat Action: Exhaust a unit you "
                                                  "control to exhaust a target non-warlord "
                                                  "unit at the same planet.", "Tactic.",
                              0, faction, "Common", 1, False, action_in_hand=True,
                              allowed_phases_in_hand="COMBAT"),
        CardClasses.AttachmentCard("Hostile Environment Gear", "Attach to an army unit.\n"
                                                               "Attached unit gets +3 HP.",
                                   "Wargear. Armor.", 1, faction, "Common", 1, False,
                                   type_of_units_allowed_for_attachment="Army",
                                   extra_health=3),
        CardClasses.AttachmentCard("Bodyguard", "Attach to an army unit you control.\n"
                                                "Forced Reaction: After a unit you control "
                                                "is assigned damage by an attack at this "
                                                "planet, reassign 1 of that damage to "
                                                "attached unit.", "Condition.", 0,
                                   faction, "Loyal", 2, False,
                                   type_of_units_allowed_for_attachment="Army",
                                   must_be_own_unit=True),
        CardClasses.SupportCard("Imperial Bunker", "Limited. (Limit one Limited card "
                                                   "per round.)\n"
                                                   "Interrupt: When you deploy an Astra "
                                                   "Militarum unit, exhaust this support "
                                                   "to reduce that unit's cost by 1.",
                                "Location.", 1, faction, "Common", True,
                                applies_discounts=[True, 1, True],
                                is_faction_limited_unique_discounter=True, limited=True),
        CardClasses.SupportCard("Rockcrete Bunker", "If this card has 4 or more damage on "
                                                    "it, sacrifice it.\n"
                                                    "Reaction: After damage is assigned to "
                                                    "a unit you control, exhaust this "
                                                    "support to reassign 1 of that damage "
                                                    "to this support.", "Upgrade.", 1,
                                faction, "Loyal", False),
        CardClasses.SupportCard("Catachan Outpost", "Combat Action: Exhaust this support to "
                                                    "give a target unit +2 ATK for its "
                                                    "next attack this phase.", "Location.",
                                2, faction, "Common", False, action_in_play=True,
                                allowed_phases_in_play="COMBAT"),
        CardClasses.ArmyCard("Seraphim Superior Allegra", "Reaction: After this unit is "
                                                          "declared as an attacker, ready a "
                                                          "target support card you control.",
                             "Ecclesiarchy. Soldier.", 4, faction, "Loyal", 3, 4, 2, True),
        CardClasses.SupportCard("Holy Fusillade", "Reaction: After a combat round begins, "
                                                  "exhaust this support to resolve a "
                                                  "ranged skirmish at this battle.",
                                "Upgrade. Ecclesiarchy.", 1, faction, "Common", False),
        CardClasses.ArmyCard("Standard Bearer", "While you control a non-Astra Militarum warlord, you may deploy this "
                                                "unit from your hand as if it had Ambush.\n"
                                                "Reaction: After this unit enters play, ready an army "
                                                "unit you control at this planet.", "Soldier.",
                             3, faction, "Common", 2, 2, 1, False, action_in_hand=True,
                             allowed_phases_in_hand="COMBAT", ambush=True),
        CardClasses.ArmyCard("Interrogator Acolyte", "Interrupt: When this unit leaves play, draw 2 cards.",
                             "Soldier. Inquisitor.", 3, faction, "Loyal", 2, 2, 1, False),
        CardClasses.EventCard("Muster the Guard", "Deploy Action: Exhaust your warlord to reduce the cost of "
                                                  "each Astra Militarum unit you deploy this phase by 1.",
                              "Tactic. Maneuver.", 0, faction, "Common", 1, False,
                              action_in_hand=True, allowed_phases_in_hand="DEPLOY"),
        CardClasses.EventCard("Noble Deed", "Action: Sacrifice an Astra Militarum unit to deal damage equal to its "
                                            "printed ATK value to a target enemy army unit at the same planet.",
                              "Tactic.", 1, faction, "Common", 1, False,
                              action_in_hand=True, allowed_phases_in_hand="ALL"),
        CardClasses.ArmyCard("Iron Guard Recruits", "", "Conscript. Mordian.",
                             2, faction, "Common", 1, 2, 2, False),
        CardClasses.AttachmentCard("Dozer Blade", "Attached to a vehicle army unit.\n"
                                                  "Attached unit gets +2 HP.", "Hardpoint.",
                                   0, faction, "Common", 1, False,
                                   type_of_units_allowed_for_attachment="Army", required_traits="Vehicle",
                                   extra_health=2),
        CardClasses.SupportCard("Inquisitorial Fortress", "Action: Exhaust and sacrifice this support "
                                                          "to rout a target army unit.", "Location.",
                                2, faction, "Loyal", False, action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.ArmyCard("Mystic Warden", "FORCED REACTION: After a battle at this planet ends, "
                                              "sacrifice this unit.", "Psyker.",
                             0, faction, "Common", 2, 2, 0, False),
        CardClasses.EventCard("To Arms!", "Action: Ready a target support card.", "Tactic.",
                              0, faction, "Loyal", 2, False, action_in_hand=True, allowed_phases_in_hand="ALL"),
        CardClasses.AttachmentCard("Honorifica Imperialis", "Attach to an army unit.\n"
                                                            "While at a planet with an enemy warlord attached unit "
                                                            "gains Armorbane and Ranged.", "Wargear. Award.",
                                   2, faction, "Loyal", 2, False,
                                   type_of_units_allowed_for_attachment="Army"),
        CardClasses.ArmyCard("Steel Legion Chimera", "No Wargear Attachments.\n"
                                                     "Reaction: After a non-Vehicle unit you control at this "
                                                     "planet is assigned damage by an attack, prevent 1 of "
                                                     "that damage.", "Vehicle. Transport.",
                             3, faction, "Common", 2, 4, 1, False, wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Tallarn Raiders", "This unit gets +2 ATK while it is at a planet with a warlord.",
                             "Soldier. Tallarn.", 1, faction, "Common", 0, 2, 1, False),
        CardClasses.SupportCard("Staging Ground", "Action: Exhaust this support to deploy a unit"
                                                  " with printed cost 2 or lower at a planet",
                                "Location.", 1, faction, "Common", False,
                                action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.WarlordCard("Torquemada Coteaz", "Combat Action: Sacrifice a unit at this planet to give "
                                                     "this warlord +3 ATK for its next attack this phase. "
                                                     "(Limit once per attack).", "Soldier. Inquisitor.",
                                faction, 0, 8, 1, 6,
                                "Bloodied.", 8, 8,
                                ["4x Coteaz's Henchmen", "2x The Emperor Protects",
                                 "1x Formosan Black Ship", "1x The Glovodan Eagle"],
                                action_in_play=True, allowed_phases_in_play="COMBAT"
                                ),
        CardClasses.ArmyCard("Coteaz's Henchmen", "Interrupt: When this unit leaves play, ready your warlord",
                             "Soldier.", 2, faction, "Signature", 1, 3, 1, False),
        CardClasses.SupportCard("Formosan Black Ship", "Interrupt: When you sacrifice a non-token unit, exhaust "
                                                       "this support to put 2 Guardsman tokens into play at the "
                                                       "same planet as the sacrificed unit.", "Upgrade.",
                                1, faction, "Signature", False),
        CardClasses.AttachmentCard("The Glovodan Eagle", "Attach to your warlord.\n"
                                                         "Attached warlord gets +1 ATK.\n"
                                                         "Combat Action: Detach this card to have it become an army "
                                                         "unit with 1 ATK and 1 HP and the text: "
                                                         "“Action: Return this unit to your hand.”", "Familiar.",
                                   1, faction, "Signature", 3, True, action_in_play=True,
                                   allowed_phases_in_play="COMBAT", type_of_units_allowed_for_attachment="Warlord",
                                   must_be_own_unit=True, extra_attack=1),
        CardClasses.EventCard("The Emperor Protects", "Interrupt: When a unit you control leaves play from a "
                                                      "planet with your warlord, return that unit to your "
                                                      "hand instead.", "Tactic.",
                              0, faction, "Signature", 1, False),
        CardClasses.ArmyCard("Shrieking Basilisk", "No Wargear Attachments.\n"
                                                   "Ranged.\n"
                                                   "Reaction: After this unit damages an enemy unit, "
                                                   "exhaust a target support card.", "Vehicle. Artillery. Elite.",
                             6, faction, "Common", 3, 5, 3, False, wargear_attachments_permitted=False, ranged=True),
        CardClasses.EventCard("The Emperor's Warrant", "Combat Action: Exhaust a target enemy unit at a planet "
                                                       "without an enemy warlord. Then, deal damage equal to "
                                                       "that unit's ATK value to another target unit at that planet.",
                              "Tactic.", 2, faction, "Loyal", 2, False, action_in_hand=True,
                              allowed_phases_in_hand="COMBAT"),
        CardClasses.WarlordCard("Broderick Worr", "Army units that retreat from this planet are destroyed instead.\n"
                                                  "Each other Astra Militarum unit you control at a "
                                                  "Stronghold planet (green)"
                                                  " gets +1 ATK and gains, “Cannot retreat or be routed.”",
                                "Soldier. Commissar.", faction, 2, 6, 2, 5, "Bloodied.", 7, 7,
                                ["4x Anxious Infantry Platoon", "2x Summary Execution",
                                 "1x Forward Barracks", "1x Commissarial Bolt Pistol"]
                                ),
        CardClasses.ArmyCard("Anxious Infantry Platoon", "FORCED REACTION: After a combat round at this planet ends, "
                                                         "you may pay 1 resource. If you do not, retreat this unit.",
                             "Soldier.", 2, faction, "Signature", 3, 3, 1, False),
        CardClasses.SupportCard("Forward Barracks", "Reaction: After a combat round ends, if you control an "
                                                    "Astra Militarum unit at the planet where the battle is taking "
                                                    "place, put 1 Guardsman token into play at that planet.",
                                "Location.", 2, faction, "Signature", False),
        CardClasses.EventCard("Summary Execution", "Play only during a battle.\n"
                                                   "Combat Action: Sacrifice a unit at a planet with your warlord "
                                                   "to have that planet gain a Stronghold icon (green) until the "
                                                   "end of the battle. Then, draw 1 card.", "Tactic.",
                              0, faction, "Signature", 1, False, action_in_hand=True, allowed_phases_in_hand="COMBAT"),
        CardClasses.AttachmentCard("Commissarial Bolt Pistol", "Attach to a Commissar unit.\n"
                                                               "Attached unit gets +1 ATK.\n"
                                                               "Reaction: After an army unit you control at this "
                                                               "planet leaves play, deal 1 damage to a target army "
                                                               "unit at this planet.", "Wargear. Weapon.",
                                   1, faction, "Signature", 3, False, extra_attack=1, required_traits="Commissar"),
        CardClasses.ArmyCard("Sacaellum Shrine Guard", "While this unit is at a Stronghold planet (green) it gets"
                                                       " +1 ATK and +1 HP.", "Soldier. Sacaellum. Ally.",
                             1, faction, "Common", 1, 1, 1, False),
        CardClasses.SupportCard("Troop Transport", "Limited.\n"
                                                   "Action: Sacrifice this support to either put a Guardsman "
                                                   "token into play at a planet, or put 2 Guardsman tokens into "
                                                   "play at a Stronghold planet (green).", "Upgrade.",
                                0, faction, "Loyal", False, limited=True, action_in_play=True,
                                allowed_phases_in_play="ALL"),
        CardClasses.ArmyCard("Death Korps Engineers", "Action: Sacrifice this unit to destroy a "
                                                      "target exhausted support card.", "Soldier. Krieg.",
                             2, faction, "Common", 2, 3, 0, False, action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.ArmyCard("Vanguard Soldiers", "Interrupt: When this unit leaves play, "
                                                  "ready another target army unit you control.", "Soldier. Sacaellum.",
                             3, faction, "Loyal", 3, 3, 1, False),
        CardClasses.EventCard("Inspirational Fervor", "Reaction: After you win a battle at a "
                                                      "Stronghold planet (green), move up to 2 non-warlord units"
                                                      " you control at that planet to a target planet.", "Tactic.",
                              1, faction, "Common", 1, False),
        CardClasses.ArmyCard("Taurox APC", "No Wargear Attachments.\n"
                                           "Reaction: After a combat round at a Stronghold planet (green) ends, "
                                           "move this unit to that planet.", "Vehicle. Transport.",
                             2, faction, "Common", 2, 2, 1, False, wargear_attachments_permitted=False),
        CardClasses.AttachmentCard("M35 Galaxy Lasgun", "Attach to a non-warlord unit.\n"
                                                        "Attached unit gets +1 ATK and +1 HP.\n"
                                                        "Interrupt: When attached unit leaves play, return this "
                                                        "attachment to your hand.", "Wargear. Weapon.",
                                   1, faction, "Common", 1, False, extra_attack=1, extra_health=1,
                                   type_of_units_allowed_for_attachment="Army/Token/Synapse"),
        CardClasses.ArmyCard("Sacaellum's Finest", "Reaction: After you win a battle at a non-first Stronghold planet"
                                                   " (green), instead of triggering the planet's Battle ability, "
                                                   "put this unit into play from your hand at a Stronghold planet"
                                                   " (green).", "Soldier. Sacaellum.",
                             4, faction, "Loyal", 3, 4, 2, False),
        CardClasses.SupportCard("Cathedral of Saint Camila", "Combat Action: Exhaust this support to target up to 1 "
                                                             "non-Elite enemy army unit at each Stronghold planet"
                                                             " (green). Exhaust each targeted unit. "
                                                             "(Limit once per phase.)", "Location. Ecclesiarchy.",
                                3, faction, "Loyal", True, action_in_play=True, allowed_phases_in_play="COMBAT"),
        CardClasses.ArmyCard("Leman Russ Conqueror", "No Wargear Attachments.\n"
                                                     "Reaction: After this unit resolves an attack, it gets +3 ATK "
                                                     "until the end of the phase.", "Vehicle. Tank. Elite.",
                             6, faction, "Common", 3, 7, 3, False, wargear_attachments_permitted=False),
        CardClasses.EventCard("Bolster the Defense", "Combat Action: Put a support card into play from your hand with"
                                                     " printed cost equal to or lower than the highest"
                                                     " number of army unit you control at a planet.", "Tactic.",
                              0, faction, "Loyal", 2, False, action_in_hand=True, allowed_phases_in_hand="COMBAT"),
        CardClasses.AttachmentCard("Imperial Rally Point", "Attach to a Stronghold planet (green).\n"
                                                           "Reduce the cost of each Astra Militarum unit you deploy "
                                                           "at this planet by 1 (to a minimum of 1).", "Location.",
                                   1, faction, "Common", 1, False, planet_attachment=True, green_required=True),
        CardClasses.ArmyCard("Vostroyan Officer", "Each Elite unit you control at this planet gains "
                                                  "Immune to enemy events.", "Soldier. Vostroya.",
                             2, faction, "Common", 1, 3, 1, False),
        CardClasses.ArmyCard("Scion Strike Force", "Deep Strike (3), Ranged", "Soldier. Elite.",
                             5, faction, "Common", 3, 4, 2, False, deepstrike=3, ranged=True),
        CardClasses.EventCard("No Surprises", "Deploy Action: Destroy a target card in reserve.", "Tactic.",
                              1, faction, "Common", 1, False, action_in_hand=True, allowed_phases_in_hand="DEPLOY"),
        CardClasses.ArmyCard("Firstborn Battalion", "While you control 3 or more support cards this "
                                                    "unit gains Mobile and Ranged.", "Soldier. Vostroya.",
                             4, faction, "Loyal", 3, 4, 2, False),
        CardClasses.SupportCard("Clearcut Refuge", "Action: Exhaust this support to give a target unit +X HP until"
                                                   " the end of the phase. X is the highest printed cost among units"
                                                   " you control.", "Location", 1, faction, "Common", True,
                                action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.WarlordCard("Grigory Maksim", "While a unit you control is being dealth damage, support cards "
                                                  "may be used as shield cards with 1 shield icon. If the shielded "
                                                  "card is a Tank, that support card has 2 shield icons instead.",
                                "Soldier. Vostroya.",
                                faction, 1, 7, 1, 6, "Bloodied.", 7, 7,
                                ["4x Maksim's Squadron", "1x Clearing the Path",
                                 "2x Keep Firing!", "1x Searchlight"]),
        CardClasses.ArmyCard("Maksim's Squadron", "No Wargear Attachments.\n"
                                                  "Interrupt: When you use a shield card to "
                                                  "prevent this unit from taking "
                                                  "damage, that card gains 1 shield icon.", "Vehicle. Tank. Vostroya.",
                             3, faction, "Signature", 2, 3, 1, False, wargear_attachments_permitted=False),
        CardClasses.SupportCard("Clearing the Path", "Reaction: After you win a battle at a planet with your warlord, "
                                                     "put an Astra Militarum support card from your discard pile"
                                                     " into play at your HQ.", "Stratagem.",
                                2, faction, "Signature", False),
        CardClasses.EventCard("Keep Firing!", "Combat Action: Ready a target Tank unit you control.", "Tactic.",
                              1, faction, "Signature", 1, False, action_in_hand=True, allowed_phases_in_hand="ALL"),
        CardClasses.AttachmentCard("Searchlight", "Attached unit gains 1 command icon.\n"
                                                  "Exhaust your warlord to move attached unit to another planet.\n"
                                                  "Action: Exhaust your warlord to move attached "
                                                  "unit to another planet.", "Hardpoint.",
                                   1, faction, "Signature", 3, False, extra_command=1, required_traits="Vehicle",
                                   must_be_own_unit=True, action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.ArmyCard("Enginseer Mechanic", "Reaction: After a Vehicle unit you control at this planet is "
                                                   "assigned damage, exhaust this unit to prevent up to"
                                                   " 2 of that damage.", "Scholar.",
                             3, faction, "Common", 1, 6, 1, False),
        CardClasses.ArmyCard("Griffon Escort", "No Wargear Attachments.\n"
                                               "Reaction: After this unit enters play, put 2 Guardsman tokens into "
                                               "play at this planet.", "Vehicle. Tank.",
                             4, faction, "Loyal", 2, 4, 1, False, wargear_attachments_permitted=False),
        CardClasses.AttachmentCard("Hot-Shot Laspistol", "Attach to an army unit you control.\n"
                                                         "Attached unit gets +2 ATK.\n"
                                                         "Damage cannot be removed from units at the same planet"
                                                         " as attached unit.", "Weapon. Wargear.",
                                   1, faction, "Common", 1, False, type_of_units_allowed_for_attachment="Army",
                                   must_be_own_unit=True, extra_attack=2),
        CardClasses.ArmyCard("Catachan Tracker", "Increase the Deep Strike value of each card you opponent"
                                                 " controls at this planet by 2.", "Soldier. Catachan.",
                             3, faction, "Common", 2, 3, 1, False),
        CardClasses.EventCard("Death Serves the Emperor", "Interrupt: When a Vehicle unit you control is destroyed, "
                                                          "gain resources equal to its printed cost. Max 1 per round.",
                              "Tactic.", 0, faction, "Common", 1, False),
        CardClasses.ArmyCard("Mars Alpha Exterminator", "No Wargear Attachments.\n"
                                                        "Reaction: After this unit is declared as an attacker, "
                                                        "destroy either a target army unit with printed cost 2 or "
                                                        "lower at this planet or a target token unit at this planet.",
                             "Vehicle. Tank. Elite.", 6, faction, "Loyal", 4, 6, 2, False,
                             wargear_attachments_permitted=False),
        CardClasses.SupportCard("Jungle Trench", "Combat Action: Exhaust this support to prevent 1 damage from each "
                                                 "attack made by a non-warlord unit this combat round.", "Location.",
                                2, faction, "Loyal", False, action_in_play=True, allowed_phases_in_play="COMBAT"),
        CardClasses.ArmyCard("23rd Mechanised Battalion", "No Attachments. Cannot be targeted.\n"
                                                          "Reaction: After the second combat round ends at this "
                                                          "planet, if there is at least one enemy unit, retreat this "
                                                          "unit to put 4 Guardsman tokens into play at this planet. "
                                                          "Then deal 5 damage to this unit.", "Corps. Transport.",
                             5, faction, "Loyal", 1, 12, 3, False, no_attachments=True),
        CardClasses.ArmyCard("Armored Fist Squad", "No Wargear attachments.\n"
                                                   "This unit gets +2 HP while it is at a planet with a warlord.\n"
                                                   "Interrupt: When this unit retreats, exhaust a non-warlord unit "
                                                   "at this planet.\n", "Vehicle. Tank. Transport.",
                             2, faction, "Common", 2, 2, 1, False, wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Catachan Devils Patrol", "Interrupt: When a unit you control is chosen as a defender, "
                                                       "deploy this unit from your hand at the same planet. Then "
                                                       "your opponent must choose to either deal 2 damage to the "
                                                       "attacker or cancel the remainder of the attack.",
                             "Soldier. Catachan.", 2, faction, "Common", 2, 2, 1, False),
        CardClasses.ArmyCard("Celestian Amelia", "Reaction: After an enemy unit is declared as an attacker at this "
                                                 "planet, while that unit is attacking, reduce all damage taken by "
                                                 "other Astra Militarum units you control to 1. "
                                                 "(Limit once per phase.)", "Soldier. Martyr. Ecclesiarchy.",
                             3, faction, "Loyal", 3, 3, 1, True),
        CardClasses.ArmyCard("Commissar Somiel", "Reaction: After an Astra Militarum Transport unit you control leaves "
                                                 "play, put a Guardsman token into play at your HQ.",
                             "Soldier. Officer. Commissar.", 2, faction, "Loyal", 1, 2, 2, True),
        CardClasses.ArmyCard("Devoted Hospitaller", "While you control a Commissar unit, you cannot deploy this unit.\n"
                                                    "Reaction: After this unit enters play, place 2 faith among army "
                                                    "units you control. Then you may exhaust an enemy army unit at "
                                                    "this planet and deal damage equal to its ATK value to this unit.",
                             "Novice. Ecclesiarchy.", 2, faction, "Loyal", 1, 2, 1, False),
        CardClasses.ArmyCard("Dominion Eugenia", "While this unit has faith, it gains Armorbane.\n"
                                                 "Reaction: After another Astra Militarum Ecclesiarchy unit you "
                                                 "control at this planet is declared as an attacker, place 1 faith "
                                                 "on this unit and the attacker.", "Soldier. Officer. Ecclesiarchy.",
                             4, faction, "Loyal", 3, 4, 3, True),
        CardClasses.ArmyCard("Eloquent Confessor", "While this unit has faith, it gets +1 ATK.\n"
                                                   "Combat Reaction: After a non-warlord unit moves or enters play "
                                                   "at this planet, pay 1 faith to exhaust it.",
                             "Priest. Ecclesiarchy.", 2, faction, "Common", 2, 2, 1, False),
        CardClasses.ArmyCard("Evangelizing Ships", "Combat Action: Pay 1 faith to put a Guardsman token into play at a "
                                                   "non-green planet. Then your opponent moves this unit to a planet "
                                                   "of his choice. (Limit once per phase.)",
                             "Transport. Ecclesiarchy.", 2, faction, "Loyal", 1, 3, 1, False,
                             action_in_play=True, allowed_phases_in_play="COMBAT"),
        CardClasses.ArmyCard("Exalted Celestians", "While this unit has faith and is not a defender, it cannot be "
                                                   "dealt damage.\n"
                                                   "Reaction: After this unit exhausts, place 1 faith on it.",
                             "Soldier. Ecclesiarchy.", 2, faction, "Common", 2, 2, 1, False),
        CardClasses.ArmyCard("Fanatical Sister Repentia", "Interrupt: When this unit uses Shield with Faith, double "
                                                          "the number of faith on it.",
                             "Soldier. Martyr. Ecclesiarchy.", 3, faction, "Common", 4, 2, 1, False),
        CardClasses.ArmyCard("Heavy Flamer Retributor", "While this unit has faith, it cannot be routed.\n"
                                                        "Reaction: After this unit resolves its attack, deal 1 "
                                                        "damage to a number of different enemy units at this "
                                                        "planet equal to faith on this unit.",
                             "Soldier. Ecclesiarchy.", 3, faction, "Common", 3, 2, 2, False),
        CardClasses.ArmyCard("Holy Battery", "No Wargear Attachments.\n"
                                             "While at a planet with a unit with faith you control, this "
                                             "unit gets +1 ATK.\n"
                                             "Reaction: After you use a shield card on this unit, place 1 faith on it.",
                             "Tank. Vostroya. Vehicle.", 2, faction, "Loyal", 2, 2, 1, False,
                             wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Hydra Flak Tank", "No Wargear Attachments.\n"
                                                "This unit deals double damage to enemy Flying or Mobile units.\n"
                                                "Reaction: After a unit moves to or from this planet, "
                                                "deal it 1 damage. (Limit once per phase.)", "Vehicle. Tank. Krieg.",
                             3, faction, "Common", 2, 3, 1, False, wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Krieg Armoured Regiment", "No Wargear Attachments.\n"
                                                        "Reaction: After this unit leaves play, place it at the "
                                                        "bottom of your deck to Rally 6 a Tank, Vehicle or Krieg "
                                                        "unit with a different name, put it into play "
                                                        "at the same planet.", "Vehicle. Tank. Elite.",
                             6, faction, "Loyal", 5, 6, 2, False, wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Patron Saint", "Deep Strike (3).\n"
                                             "Reaction: After you deploy or Deep Strike this unit, remove up to 3 "
                                             "damage from Astra Militarum army units and Ecclesiarchy units you "
                                             "control. Then place faith equal to the damage removed among "
                                             "army units you control.\n", "Saint. Elite. Ecclesiarchy.",
                             5, faction, "Loyal", 4, 5, 2, False, deepstrike=3),
        CardClasses.ArmyCard("Pattern IX Immolator", "No Wargear Attachments.\n"
                                                     "Command Action: Deal X damage among enemy non-warlord units at "
                                                     "this planet and place X faith among army units at this planet. "
                                                     "X is the number of command struggles your opponent won this "
                                                     "phase minus 1. (Limit once per phase.)",
                             "Vehicle. Tank. Ecclesiarchy.", 3, faction, "Common", 3, 3, 1, False,
                             action_in_play=True, allowed_phases_in_play="COMMAND"),
        CardClasses.ArmyCard("Penitent Engine", "No Wargear Attachments.\n"
                                                "Reaction: After an attack resolved by a unit you control at this "
                                                "planet does not destroy the defender, place 1 faith on this unit "
                                                "and it gets +1 ATK for its next attack this phase.",
                             "Vehicle. Martyr. Ecclesiarchy.", 3, faction, "Loyal", 2, 3, 1, False,
                             wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Sacred Rose Immolator", "No Wargear Attachments.\n"
                                                      "Reaction: After this unit resolves its attack or moves to a "
                                                      "planet, place 1 faith on it. Then deal 1 damage to up to "
                                                      "2 different enemy units at this planet. "
                                                      "(Limit twice per round.)", "Vehicle. Transport. Ecclesiarchy.",
                             3, faction, "Common", 1, 3, 1, False, wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Saint Erika", "If you don't control faith, destroy this unit.\n"
                                            "Forced Reaction: After a non-Elysia, non-Saint Astra Militarum army unit "
                                            "enters your discard pile from this planet, pay 1 faith to return that "
                                            "unit to your hand.", "Saint. Martyr. Ecclesiarchy.",
                             3, faction, "Loyal", 5, 5, 1, True),
        CardClasses.ArmyCard("Siege Regiment Manticore", "No Wargear Attachments.\n"
                                                         "Reaction: After the ranged skirmish at an adjacent planet "
                                                         "ends, exhaust this unit to deal 3 damage to an enemy "
                                                         "non-warlord unit at that planet.",
                             "Vehicle. Artillery. Krieg.", 4, faction, "Common", 3, 4, 1, False,
                             wargear_attachments_permitted=False),
        CardClasses.ArmyCard("Tenacious Novice Squad", "While this unit has faith, it gets +1 ATK and +1 HP.\n"
                                                       "Reaction: After a warlord commits to this planet, place 1 "
                                                       "faith on an army unit at this planet.",
                             "Soldier. Ecclesiarchy.", 1, faction, "Common", 1, 1, 1, False),
        CardClasses.ArmyCard("Undying Saint", "Lumbering.\n"
                                              "Cannot be damaged by Area Effect.\n"
                                              "Reaction: After the deploy phase begins, if this unit is in your "
                                              "discard pile, put it into play at a target non-first planet "
                                              "(ignore this restriction if your opponent has the initiative).",
                             "Martyr. Ecclesiarchy.", 1, faction, "Loyal", 2, 1, 1, False, lumbering=True),
        CardClasses.ArmyCard("Vengeful Seraphim", "While this unit has faith, it gains Flying.\n"
                                                  "Reaction: After an Ecclesiarchy unit you control at this planet "
                                                  "is destroyed, this unit gets +1 ATK and +1 HP until the end "
                                                  "of the phase. Then you may pay 1 faith to ready this unit. "
                                                  "(Limit once per phase.)", "Soldier. Ecclesiarchy.",
                             3, faction, "Common", 3, 2, 1, False),
        CardClasses.ArmyCard("Zealous Cantus", "Reaction: After an Ecclesiarchy or Grey Knights card enters your "
                                               "discard pile, place 1 faith on an army unit. "
                                               "(Limit twice per faith.)", "Soldier. Ecclesiarchy.",
                             3, faction, "Common", 3, 3, 1, False),
        CardClasses.AttachmentCard("Banner of the Sacred Rose", "Limited.\n"
                                                                "Attach to a unit you control.\n"
                                                                "Interrupt: When you deploy an Ecclesiarchy unit, "
                                                                "exhaust this attachment to reduce the cost by 1 plus "
                                                                "the number of green planets in your opponent's "
                                                                "victory display.", "Standard. Ecclesiarchy.",
                                   1, faction, "Loyal", 2, True, limited=True, must_be_own_unit=True),
        CardClasses.AttachmentCard("Blade of the Crimson Oath", "Attach to a non-warlord unit.\n"
                                                                "Attached unit gets +2 ATK and +2 HP.\n"
                                                                "Interrupt: When your opponent triggers an ability "
                                                                "that discards a card from your hand, put 2 Guardsman "
                                                                "tokens into play at a planet to put this card from "
                                                                "your hand into play attached to a unit.",
                                   "Relic. Wargear. Weapon.", 1, faction, "Loyal", 2, True,
                                   type_of_units_allowed_for_attachment="Army/Synapse/Token.",
                                   extra_attack=2, extra_health=2),
        CardClasses.AttachmentCard("Departmento Munitorum Aid", "Attach to a Vehicle army unit.\n"
                                                                "Attached unit gets +1 HP.\n"
                                                                "Action: Exhaust this attachment and remove 1 "
                                                                "damage from attached unit to retreat it.",
                                   "Maintenance.", 0, faction, "Loyal", 2, False, extra_health=1,
                                   required_traits="Vehicle", type_of_units_allowed_for_attachment="Army",
                                   action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.AttachmentCard("Revered Heavy Flamer", "Deep Strike (0).\n"
                                                           "Attach to an army unit.\n"
                                                           "Attached unit gets +2 ATK.\n"
                                                           "Reaction: After your opponent uses a shield card on a "
                                                           "unit at this planet, place 1 faith on an army unit at "
                                                           "this planet.", "Wargear. Weapon. Ecclesiarchy.",
                                   1, faction, "Common", 1, False, type_of_units_allowed_for_attachment="Army",
                                   extra_attack=2, deepstrike=0),
        CardClasses.AttachmentCard("Sanctified Bolter", "Attach to an army unit you control.\n"
                                                        "Attached unit gets +1 ATK and +1 HP.\n"
                                                        "Reaction: After a ranged skirmish at this planet begins, "
                                                        "or an enemy non-warlord unit moves from another planet to "
                                                        "this planet, place 2 faith among army units at this planet.",
                                   "Wargear. Weapon.", 1, faction, "Loyal", 1, False, extra_attack=1, extra_health=1,
                                   type_of_units_allowed_for_attachment="Army", must_be_own_unit=True),
        CardClasses.AttachmentCard("Seal of the Ebon Chalice", "Attach to an army unit. Attached unit gets +1 HP.\n"
                                                               "Interrupt: When attached unit takes damage from a "
                                                               "unit with a higher printed cost, deal to that unit "
                                                               "damage equal to the difference between the "
                                                               "units' printed costs.", "Award. Ecclesiarchy.",
                                   1, faction, "Loyal", 2, False, extra_health=1,
                                   type_of_units_allowed_for_attachment="Army"),
        CardClasses.AttachmentCard("Until Justice is Done", "Attach to an enemy army unit.\n"
                                                            "Increase damage dealt to attached unit by 1.\n"
                                                            "Reaction: After an Ecclesiarchy unit you control is "
                                                            "assigned damage by an attack, put this card from your "
                                                            "hand into play attached to the attacker.\n",
                                   "Vow. Ecclesiarchy.", 2, faction, "Common", 1, False, must_be_enemy_unit=True,
                                   type_of_units_allowed_for_attachment="Army"),
        CardClasses.EventCard("Our Last Stand", "Action: Place 1 faith on each Astra Militarum unit you control at the "
                                                "first planet. If that planet shares a common type with two planets in "
                                                "your opponent's victory display your warlord gains: Interrupt:\" "
                                                "When this unit is assigned damage, reduce that damage by 1 (min 1)."
                                                "\" until the end of the battle. Max 1 per round.",
                              "Prayer. Ecclesiarchy.", 0, faction, "Loyal", 2, False,
                              action_in_hand=True, allowed_phases_in_hand="ALL"),
        CardClasses.EventCard("Wrathful Retribution", "Reaction: After an enemy unit moves to, or enters play at, "
                                                      "a planet where a battle is taking place, place faith equal "
                                                      "to its printed cost among army units you control. "
                                                      "Then ready a non-Elite unit with faith.",
                              "Prayer. Ecclesiarchy.", 1, faction, "Loyal", 2, False),
        CardClasses.SupportCard("Holy Crusade", "Each other non-signature card in your deck must be Ecclesiarchy.\n"
                                                "Action: Exhaust this support to place 2 faith among "
                                                "units you control.", "Pledge.", 1, faction, "Loyal", False,
                                action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.SupportCard("Munitorum Support", "Once per round you may deploy a card on this support as "
                                                     "if it were in your hand.\n"
                                                     "Reaction: After you deploy this support, place a M35 Galaxy "
                                                     "Lasgun, a Hot-Shot Laspistol, a Bodyguard, a Seal of the "
                                                     "Ebon Chalice, and a Defense Battery on this card.", "Pledge.",
                                1, faction, "Common", False),
        CardClasses.SupportCard("Senatorum Directives", "Reaction: After a Catachan unit you control is assigned "
                                                        "damage, put a Guardsman token into play at the same planet. "
                                                        "You may then reassign one of that damage to it."
                                                        " (Limit once per battle.)", "Pledge.",
                                1, faction, "Loyal", False),
        CardClasses.SupportCard("Agra's Preachings", "Limited.\n"
                                                     "Reaction: After your opponent wins a battle, exhaust this "
                                                     "support and target a planet with an enemy unit to rally 6 "
                                                     "a non-Elite Astra Militarum unit, attach it to that planet. "
                                                     "When the combat phase ends, deploy that unit at that planet "
                                                     "and reduce its cost by 2. If you can't, discard it.",
                                "Decree. Ecclesiarchy.", 1, faction, "Common", True, limited=True),
        CardClasses.SupportCard("Blood of Martyrs", "Interrupt: When an Astra Militarum unit you control is destroyed, "
                                                    "exhaust this support and target up to 3 army units at the same "
                                                    "planet. Move any faith on that unit to the targeted units and "
                                                    "they get +1 ATK for their next attack this phase. Then if the "
                                                    "destroyed card is a Martyr, draw 1 card.",
                                "Decree. Ecclesiarchy.", 1, faction, "Loyal", False),
        CardClasses.SupportCard("Cardinal Agra Decree", "While you control faith, each Vostroya unit you control "
                                                        "gets +1 ATK.\n"
                                                        "Interrupt: When this card enters your discard pile, "
                                                        "draw a card and place 1 faith on an army unit.",
                                "Decree. Ecclesiarchy.", 0, faction, "Loyal", True),
        CardClasses.SupportCard("Convent Prioris Advisor", "Reaction: After a Vostroya unit moves to a planet, place "
                                                           "1 faith on it. Then you may sacrifice this support to "
                                                           "place 1 faith on that unit and Rally 6 a support, add "
                                                           "it to your hand.", "Advisor. Ecclesiarchy.",
                                0, faction, "Loyal", True),
        CardClasses.SupportCard("Embarked Squads", "Command Action: Exhaust this support to have a target, "
                                                   "non-Upgrade, Vehicle unit you control gain the Upgrade and "
                                                   "Transport traits and \"Interrupt: When this unit retreats, put "
                                                   "2 Guardsman tokens into play at the same planet. "
                                                   "(Limit once per phase.)\" until the end of the round.",
                                "Location.", 0, faction, "Loyal", False),
        CardClasses.SupportCard("Holy Chapel", "Action: Exhaust and Sacrifice this support to put 4 faith among "
                                               "Astra Militarum or Space Marines army units.",
                                "Location. Ecclesiarchy.", 1, faction, "Common", False,
                                action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.WarlordCard("Canoness Vardina", "Action: Place 2 faith among army units you control. If your "
                                                    "warlord is at a planet with an enemy warlord, place 3 instead. "
                                                    "(Limit once per round)", "Officer. Ecclesiarchy.",
                                faction, 2, 6, 2, 6,
                                "Bloodied.\n"
                                "Action: Place 2 faith among Ecclesiarchy army units at this planet. "
                                "(Limit once per game.)", 7, 7,
                                ["2x Faith Denies Death", "4x Sororitas Command Squad",
                                 "1x Supreme Appearance", "1x Transcendent Blessing"]),
        CardClasses.EventCard("Faith Denies Death", "Reaction: After an army unit with faith is assigned damage, "
                                                    "pay 1 faith to prevent up to 5 of that damage.",
                              "Prayer. Ecclesiarchy.", 0, faction, "Signature", 1, False),
        CardClasses.ArmyCard("Sororitas Command Squad", "Reaction: After you prevent damage assigned to this unit "
                                                        "by a non-warlord unit, deal damage equal to the prevented "
                                                        "damage to that enemy unit. (Limit once per phase.)",
                             "Soldier. Ecclesiarchy.", 3, faction, "Signature", 3, 3, 1, False),
        CardClasses.SupportCard("Supreme Appearance", "Action: Exhaust and sacrifice this support to exhaust each "
                                                      "non-warlord unit. Use this ability only if you control "
                                                      "no Ranged units.", "Miracle.", 1, faction, "Signature", False,
                                action_in_play=True, allowed_phases_in_play="ALL"),
        CardClasses.AttachmentCard("Transcendent Blessing", "Attach to a non-warlord unit.\n"
                                                            "Attached unit gets +1 ATK and +1 HP.\n"
                                                            "Interrupt: When attached unit leaves play, pay 1 "
                                                            "faith to attach this card to an eligible unit.",
                                   "Blessing.", 0, faction, "Signature", 3, False, extra_health=1, extra_attack=1,
                                   type_of_units_allowed_for_attachment="Army/Synapse/Token"),
        CardClasses.WarlordCard("Saint Celestine", "Combat Action: Pay faith equal to the printed cost of a "
                                                   "non-Elite unit in your hand to put it into play at this planet. "
                                                   "If that unit is still in play at the end of the phase, "
                                                   "discard it and draw a card. (Limit once per phase.)",
                                "Saint. Ecclesiarchy.", faction, 2, 7, 2, 5,
                                "Bloodied.\n"
                                "Interrupt: When your warlord would be defeated by taking damage, remove all damage "
                                "from it instead. Then deal it 5 damage. (Limit once per game.)", 7, 7,
                                ["1x Armour of Saint Katherine", "4x Heralding Cherubim",
                                 "2x Miraculous Intervention", "1x Order of the Crimson Oath"],
                                action_in_play=True, allowed_phases_in_play="COMBAT"),
        CardClasses.AttachmentCard("Armour of Saint Katherine", "Attach to your warlord.\n"
                                                                "Reduce all damage dealth to attached unit to 3.\n"
                                                                "Reaction: After attached unit takes damage, place "
                                                                "1 faith on it.", "Wargear. Armor.",
                                   0, faction, "Signature", 3, True, type_of_units_allowed_for_attachment="Warlord",
                                   must_be_own_unit=True),
        CardClasses.ArmyCard("Heralding Cherubim", "Reaction: After your warlord commits to a planet, place 1 "
                                                   "faith on this unit. Then you may move this unit to a planet "
                                                   "adjacent to your warlord.", "Herald. Ecclesiarchy.",
                             2, faction, "Signature", 2, 2, 1, False),
        CardClasses.EventCard("Miraculous Intervention", "Reaction: After a combat round begins at a planet, commit "
                                                         "your warlord to that planet and place 2 faith on it. Then "
                                                         "you may pay 1 resource to put Guardsman tokens into play "
                                                         "at that planet until you control at least as many units as "
                                                         "your opponent at that planet.", "Prayer. Ecclesiarchy.",
                              1, faction, "Signature", 1, False),
        CardClasses.SupportCard("Order of the Crimson Oath", "While at the first planet, your warlord gets +2 HP.\n"
                                                             "Reaction: After your opponent wins a battle, Rally 6 "
                                                             "a unit, add it to your hand. Then place 2 faith among "
                                                             "army units you control.", "Location. Ecclesiarchy.",
                                0, faction, "Signature", False)
    ]
    return astra_militarum_cards_array
