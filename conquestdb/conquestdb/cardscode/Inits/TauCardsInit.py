from .. import CardClasses


def tau_cards_init():
    faction = "Tau"
    tau_cards_array = [
        CardClasses.WarlordCard("Commander Shadowsun", "Reaction: After this warlord commits to "
                                                       "a planet, put a Tau attachment with printed "
                                                       "cost 2 or lower or "
                                                       "\"Shadowsun's Stealth Cadre\" "
                                                       "from your hand or discard pile into play "
                                                       "attached to an eligible unit at this planet.",
                                "Soldier. Shas'o.", faction, 1, 7, 1, 5, "Bloodied.", 7, 7,
                                ["4x Shadowsun's Stealth Cadre", "1x Communications Relay",
                                 "2x Squadron Redeployment", "1x Command-link Drone"], cycle_info="Core Set"),
        CardClasses.ArmyCard("Shadowsun's Stealth Cadre", "This card may enter play as an attachment "
                                                          "with the text \"Attach to a non-Vehicle "
                                                          "army unit. Attached unit gets "
                                                          "+2 ATK and +2 HP.\"", "Soldier. Pilot.",
                             2, faction, "Signature", 2, 2, 1, False, cycle_info="Core Set"),
        CardClasses.SupportCard("Communications Relay", "Interrupt: When your opponent triggers an "
                                                        "ability that targets a unit you control with "
                                                        "1 or more attachments, exhaust this support "
                                                        "to cancel its effects.", "Upgrade.",
                                1, faction, "Signature", False, cycle_info="Core Set"),
        CardClasses.EventCard("Squadron Redeployment", "Action: Exhaust an army unit with 1 or more "
                                                       "attachments to move it to a target planet.",
                              "Tactic.", 0, faction, "Signature", 1, False, action_in_hand=True,
                              allowed_phases_in_hand="ALL", cycle_info="Core Set"),
        CardClasses.AttachmentCard("Command-link Drone", "Attach to a unit.\n"
                                                         "Attached unit gets +1 ATK.\n"
                                                         "Action: Pay 1 RESOURCE to attach this card "
                                                         "to a different unit.", "Drone.",
                                   0, faction, "Signature", 3, False, action_in_play=True,
                                   allowed_phases_in_play="ALL", extra_attack=1, cycle_info="Core Set"),
        CardClasses.ArmyCard("Recon Drone", "Limited.", "Drone. Ally.", 0, faction, "Loyal",
                             0, 1, 2, False, limited=True, cycle_info="Core Set"),
        CardClasses.ArmyCard("Vior'la Marksman", "Ranged.", "Scout. Shas'la.", 1, faction, "Common",
                             1, 2, 1, False, ranged=True, cycle_info="Core Set"),
        CardClasses.ArmyCard("Carnivore Pack", "Interrupt: When this unit is destroyed, "
                                               "gain 3 RESOURCE.", "Warrior. Kroot.",
                             3, faction, "Common", 3, 3, 0, False, cycle_info="Core Set"),
        CardClasses.ArmyCard("Vash'ya Trailblazer", "Mobile.", "Scout. Pilot.",
                             2, faction, "Common", 1, 1, 2, False, mobile=True, cycle_info="Core Set"),
        CardClasses.ArmyCard("Fire Warrior Elite", "Interrupt: When an enemy unit would declare an "
                                                   "attack against a unit you control at this planet, "
                                                   "declare this unit as the defender instead.",
                             "Soldier. Shas'la.", 3, faction, "Common", 1, 5, 0, False, cycle_info="Core Set"),
        CardClasses.ArmyCard("Fire Warrior Strike Team", "This unit gets +1 ATK "
                                                         "for every attachment on it.",
                             "Soldier. Shas'la.", 4, faction, "Common", 1, 5, 1, False, cycle_info="Core Set"),
        CardClasses.ArmyCard("Crisis Battle Guard", "Mobile.", "Soldier. Pilot. Elite.",
                             5, faction, "Loyal", 3, 5, 3, False, mobile=True, cycle_info="Core Set"),
        CardClasses.ArmyCard("Earth Caste Technician", "Reaction: After this unit enters play, "
                                                       "search the top 6 cards of your deck for an "
                                                       "attachment or Drone card. Reveal it, add it "
                                                       "to your hand, and place the remaining cards "
                                                       "on the bottom of your deck in any order.",
                             "Scholar. Ally.", 1, faction, "Common", 1, 1, 1, False, cycle_info="Core Set"),
        CardClasses.ArmyCard("Gun Drones", "You may deploy this card as a Drone attachment with the "
                                           "text, \"Attach to a non-Vehicle army unit."
                                           "Attached unit gains Area Effect (2).\"", "Drone.",
                             2, faction, "Loyal", 2, 2, 1, False, cycle_info="Core Set"),
        CardClasses.ArmyCard("Stingwing Swarm", "Ranged.", "Warrior. Vespid.", 4, faction, "Common",
                             3, 3, 1, False, ranged=True, cycle_info="Core Set"),
        CardClasses.ArmyCard("Fireblade Kais'vre", "Interrupt: When you use a Tau card as a shield card "
                                                   "at this planet, it gains 1 shield icon.",
                             "Soldier. Hero.", 3, faction, "Loyal", 2, 3, 2, True, cycle_info="Core Set"),
        CardClasses.ArmyCard("Experimental Devilfish", "No Wargear Attachments.\n"
                                                       "Reaction: After this unit commits to a "
                                                       "planet, ready it.", "Vehicle. Transport.",
                             3, faction, "Common", 4, 2, 1, False,
                             wargear_attachments_permitted=False, cycle_info="Core Set"),
        CardClasses.EventCard("Even the Odds", "Action: Move a target attachment to another eligible "
                                               "unit controlled by the same player.", "Tactic.",
                              1, faction, "Common", 1, False, action_in_hand=True,
                              allowed_phases_in_hand="ALL", cycle_info="Core Set"),
        CardClasses.EventCard("Calculated Strike", "Action: Destroy a target Limited card.",
                              "Tactic.", 1, faction, "Common", 1, False, action_in_hand=True,
                              allowed_phases_in_hand="ALL", cycle_info="Core Set"),
        CardClasses.EventCard("Deception", "Deploy Action: Return a target non-Elite army "
                                           "unit to its owner's hand.", "Tactic.",
                              2, faction, "Loyal", 2, False, action_in_hand=True,
                              allowed_phases_in_hand="DEPLOY", cycle_info="Core Set"),
        CardClasses.AttachmentCard("Repulsor Impact Field", "Attach to an army unit."
                                                            "Limit 1 per unit.\n"
                                                            "Reaction: After attached unit is damaged "
                                                            "by an attack, deal 2 damage to the "
                                                            "attacker.", "Wargear.",
                                   2, faction, "Loyal", 2, False,
                                   type_of_units_allowed_for_attachment="Army", limit_one_per_unit=True,
                                   cycle_info="Core Set"),
        CardClasses.AttachmentCard("Ion Rifle", "Attach to an army unit.\n"
                                                "Attached unit gets +3 ATK.", "Wargear. Weapon.",
                                   1, faction, "Common", 1, False,
                                   type_of_units_allowed_for_attachment="Army", extra_attack=3, cycle_info="Core Set"),
        CardClasses.SupportCard("Frontline Launch Bay", "Limited.\n"
                                                        "Interrupt: When you deploy a Tau unit, exhaust "
                                                        "this support to reduce that unit's cost by 1.",
                                "Location.", 1, faction, "Common", True,
                                applies_discounts=[True, 1, True],
                                is_faction_limited_unique_discounter=True, limited=True, cycle_info="Core Set"),
        CardClasses.SupportCard("Ambush Platform", "Interrupt: When you deploy an attachment, "
                                                   "reduce its cost by 1.\n"
                                                   "Combat Action: Exhaust this support to deploy "
                                                   "an attachment from your hand.",
                                "Upgrade.", 2, faction, "Common", False, action_in_play=True,
                                allowed_phases_in_play="COMBAT", cycle_info="Core Set"),
        CardClasses.ArmyCard("Pathfinder Shi Or'es", "Action: Discard an attachment on this unit to ready it."
                                                     " (Limit once per phase.)", "Scout.",
                             3, faction, "Loyal", 3, 3, 1, True, action_in_play=True, allowed_phases_in_play="ALL",
                             war_pack_info="The Great Devourer"),
        CardClasses.SupportCard("Repair Bay", "Deploy Action: Exhaust this support to place a Drone or Pilot "
                                              "card from your discard pile on top of your deck.", "Location.",
                                1, faction, "Common", False, action_in_play=True, allowed_phases_in_play="DEPLOY",
                                war_pack_info="The Great Devourer"),
        CardClasses.ArmyCard("Air Caste Courier", "While you control a non-Tau warlord, this unit gains Flying.\n"
                                                  "Combat Action: Exhaust this unit to move an attachment from a unit"
                                                  " you control at this planet to another eligible unit you control.",
                             "Scout. Pilot.", 2, faction, "Common", 1, 3, 1, False, action_in_play=True,
                             allowed_phases_in_play="COMBAT", war_pack_info="Legions of Death"),
        CardClasses.ArmyCard("Piranha Hunter", "Mobile.\n"
                                               "No Wargear Attachments.\n"
                                               "Reaction: After this unit moves from one planet to another, "
                                               "draw 1 card.", "Vehicle. Speeder.",
                             3, faction, "Common", 2, 2, 0, False, wargear_attachments_permitted=False, mobile=True,
                             war_pack_info="The Howl of Blackmane"),
        CardClasses.ArmyCard("Aun'ui Prelate", "Ambush.\n"
                                               "FORCED REACTION: After this unit resolves its attack, "
                                               "move it to your HQ.\n"
                                               "Reaction: After you deploy this unit, each other Tau unit \n"
                                               "you control at this planet gets +1 ATK until the end of the phase.",
                             "Soldier. Ethereal.", 4, faction, "Loyal", 4, 3, 0, False, ambush=True,
                             action_in_hand=True, allowed_phases_in_hand="COMBAT",
                             war_pack_info="The Howl of Blackmane"),
        CardClasses.SupportCard("Homing Beacon", "Limited.\n"
                                                 "Reaction: After a unit you control moves to your HQ, "
                                                 "exhaust this support to gain 1 or draw 1 card.", "Upgrade.",
                                1, faction, "Common", False, limited=True, war_pack_info="The Howl of Blackmane"),
        CardClasses.ArmyCard("Bork'an Recruits", "This unit gets +2 ATK while it is at a planet with a warlord.",
                             "Soldier.", 2, faction, "Common", 2, 2, 1, False, war_pack_info="The Scourge"),
        CardClasses.EventCard("Kauyon Strike", "Combat Action: Move 1 or more Ethereal units "
                                               "you control to a target planet.", "Tactic.",
                              1, faction, "Loyal", 2, False,
                              action_in_hand=True, allowed_phases_in_hand="COMBAT", war_pack_info="The Scourge"),
        CardClasses.AttachmentCard("Blacksun Filter", "Attach to an army unit.\n"
                                                      "After an enemy warlord commits to the same "
                                                      "planet as attached unit, gain 1 RESOURCE.", "Wargear.",
                                   0, faction, "Common", 1, False, type_of_units_allowed_for_attachment="Army",
                                   war_pack_info="The Scourge"),
        CardClasses.WarlordCard("Aun'shi", "Each Tau unit you control at this planet gains Armorbane.\n"
                                           "FORCED REACTION: After this warlord resolves its attack,"
                                           " move it to your HQ.", "Ethereal. Soldier.", faction,
                                2, 7, 1, 5, "Bloodied.", 7, 7,
                                ["4x Ethereal Envoy", "1x Aun'shi's Sanctum",
                                 "1x Honor Blade", "2x Ethereal Wisdom"],
                                war_pack_info="Gift of the Ethereals"),
        CardClasses.ArmyCard("Ethereal Envoy", "FORCED REACTION: After this unit resolves its attack, "
                                               "move it to your HQ.", "Ethereal. Soldier.",
                             1, faction, "Signature", 1, 3, 1, False, war_pack_info="Gift of the Ethereals"),
        CardClasses.SupportCard("Aun'shi's Sanctum", "Action: Exhaust this support to ready a target unit at a "
                                                     "planet with 1 or more Ethereal units you control.", "Location.",
                                2, faction, "Signature", True, action_in_play=True, allowed_phases_in_play="ALL",
                                war_pack_info="Gift of the Ethereals"),
        CardClasses.AttachmentCard("Honor Blade", "Attach to an Ethereal unit.Attached unit gains, “Each other Tau "
                                                  "unit you control at this planet gets +1 ATK.”", "Wargear. Weapon.",
                                   1, faction, "Signature", 3, False, required_traits="Ethereal",
                                   war_pack_info="Gift of the Ethereals"),
        CardClasses.EventCard("Ethereal Wisdom", "Action: Until the end of the phase, a target Tau unit you control "
                                                 "gets +1 ATK and gains the Ethereal trait.", "Tactic.",
                              0, faction, "Signature", 1, False, action_in_hand=True, allowed_phases_in_hand="ALL",
                              war_pack_info="Gift of the Ethereals"),
        CardClasses.ArmyCard("Sa'cea XV88 Broadside", "This unit gain Area Effect (2) "
                                                      "while it has 1 or more attachments.",
                             "Soldier. Pilot. Elite.", 6, faction, "Loyal", 4, 6, 3, False,
                             war_pack_info="Zogwort's Curse"),
        CardClasses.EventCard("Tense Negotiations", "Action: Exhaust your warlord to trigger the Battle "
                                                    "ability at the same planet as your warlord.", "Tactic."
                              , 1, faction, "Common", 1, False, action_in_hand=True, allowed_phases_in_hand="ALL",
                              war_pack_info="Zogwort's Curse"),
        CardClasses.AttachmentCard("Heavy Marker Drone", "Attach to an enemy army unit.\n"
                                                         "Double damage dealt to attached unit.", "Drone.",
                                   1, faction, "Loyal", 2, False, type_of_units_allowed_for_attachment="Army",
                                   must_be_enemy_unit=True, war_pack_info="Zogwort's Curse"),
        CardClasses.ArmyCard("Fire Warrior Grenadiers", "For each Ethereal unit you control at this planet, "
                                                        "this unit gets +2 ATK and gains 1 command icon.",
                             "Soldier. Shas'la.", 3, faction, "Common", 2, 2, 0, False,
                             war_pack_info="The Threat Beyond"),
        CardClasses.SupportCard("Ksi'm'yen Orbital City", "Combat Action: Exhaust this support to move an Ethereal"
                                                          " unit from your HQ to a target planet. "
                                                          "Then, ready that unit.", "Location.",
                                2, faction, "Loyal", False, action_in_play=True, allowed_phases_in_play="COMBAT",
                                war_pack_info="The Threat Beyond"),
        CardClasses.ArmyCard("Vior'la Warrior Cadre", "This unit gains Ranged while you control an"
                                                      " Ethereal unit at this planet.", "Soldier. Shas'la.",
                             4, faction, "Common", 4, 3, 1, False, war_pack_info="Descendants of Isha"),
        CardClasses.EventCard("For the Tau'va", "Action: Exhaust your warlord to ready each unit "
                                                "you control with 1 or more attachments.", "Tactic. Maneuver.",
                              2, faction, "Common", 1, False, action_in_hand=True, allowed_phases_in_hand="ALL",
                              war_pack_info="Descendants of Isha"),
        CardClasses.WarlordCard("Commander Starblaze", "You may include common Astra Militarum cards in your deck, "
                                                       "but cannot include other cards from a non-Tau faction.\n"
                                                       "Reaction: After this warlord commits to a planet, move 1 "
                                                       "Astra Militarum unit you control from an "
                                                       "adjacent planet to this planet.", "Shas'o. Soldier.",
                                faction, 2, 6, 2, 5, "Bloodied.", 7, 7,
                                ["4x Ardent Auxiliaries", "1x Starblaze's Outpost",
                                 "2x Bond of Brotherhood", "1x Searing Burst Cannon"],
                                war_pack_info="Decree of Ruin"),
        CardClasses.ArmyCard("Ardent Auxiliaries", "Reaction: After this unit commits to a planet, if you control an "
                                                   "Astra Militarum unit at this planet, ready this unit.", "Soldier.",
                             2, faction, "Signature", 2, 2, 1, False,
                             war_pack_info="Decree of Ruin"),
        CardClasses.SupportCard("Starblaze's Outpost", "Action: Exhaust this support and return an Astra Militarum "
                                                       "army unit at a planet to your hand to put a Tau unit "
                                                       "with equal or lower printed cost into play from your "
                                                       "hand at the same planet.", "Location.",
                                2, faction, "Signature", True, action_in_play=True, allowed_phases_in_play="ALL",
                                war_pack_info="Decree of Ruin"),
        CardClasses.EventCard("Bond of Brotherhood", "Action: Until the end of the phase, each Tau unit you control"
                                                     " at a target planet gets +2 HP and each Astra Militarum"
                                                     " unit you control at the targeted planet gets +2 ATK.", "Tactic.",
                              2, faction, "Signature", 1, False, action_in_hand=True, allowed_phases_in_hand="ALL",
                              war_pack_info="Decree of Ruin"),
        CardClasses.AttachmentCard("Searing Burst Cannon", "Attach to a unit.\n"
                                                           "Interrupt: When attached unit damages an enemy unit by an"
                                                           " attack, if no shield card was used during this"
                                                           " attack, double the damage taken.", "Wargear. Weapon.",
                                   1, faction, "Signature", 3, False, war_pack_info="Decree of Ruin"),
        CardClasses.ArmyCard("Prudent Fire Warriors", "Interrupt: When this unit leaves play, attach each attachment "
                                                      "on it to a target eligible unit at this planet.", "Soldier.",
                             2, faction, "Common", 2, 3, 0, False, war_pack_info="Boundless Hate"),
        CardClasses.ArmyCard("Exploratory Drone", "Reaction: After a non-Tau unit is deployed at this planet,"
                                                  " move this unit to an adjacent planet.", "Drone.",
                             1, faction, "Loyal", 0, 2, 1, False, war_pack_info="Boundless Hate"),
        CardClasses.AttachmentCard("Auxiliary Armor", "Attach to an army unit.\n"
                                                      "Attached unit gets +2 ATK and +1 HP.\n"
                                                      "If attached unit is a non-Tau unit, it gains 1 command icon.",
                                   "Wargear. Armor.", 2, faction, "Loyal", 2, False,
                                   type_of_units_allowed_for_attachment="Army", extra_attack=2, extra_health=1,
                                   war_pack_info="Boundless Hate"),
        CardClasses.ArmyCard("Prototype Crisis Suit", "Reaction: After you deploy this unit, search the top 9 cards "
                                                      "of your deck for up to 2 Tau attachments, each with printed "
                                                      "cost 2 or lower. Put each eligible attachment into play "
                                                      "attached to this unit. Then, shuffle the remaining cards "
                                                      "into your deck.", "Pilot. Elite.",
                             5, faction, "Common", 4, 4, 2, False, war_pack_info="Deadly Salvage"),
        CardClasses.EventCard("Mont'ka Strike", "Combat Action: Exhaust each ready Soldier unit you control at a "
                                                "target planet to deal damage equal to their combined printed"
                                                " ATK value to an enemy army unit at the targeted planet.", "Tactic.",
                              2, faction, "Common", 1, False, action_in_hand=True, allowed_phases_in_hand="COMBAT",
                              war_pack_info="Deadly Salvage"),
        CardClasses.SupportCard("Sae'lum Enclave", "Limited.\n"
                                                   "Interrupt: When you deploy a non-Tau unit, exhaust this support "
                                                   "to reduce that unit's cost by 2.", "Location.",
                                1, faction, "Loyal", True, limited=True, war_pack_info="Deadly Salvage"),
        CardClasses.ArmyCard("Auxiliary Overseer", "For each non-Tau unit you conrol at this planet,"
                                                   " this unit gets +1 ATK.", "Soldier.",
                             2, faction, "Loyal", 1, 3, 1, False, war_pack_info="What Lurks Below"),
        CardClasses.AttachmentCard("Drone Defense System", "Attach to a Pilot or Vehicle unit.\n"
                                                           "Combat Action: Exhaust attached unit to deal 2 damage to"
                                                           " each exhausted enemy unit at this planet.", "Hardpoint.",
                                   1, faction, "Common", 1, False, required_traits="Vehicle/Pilot",
                                   type_of_units_allowed_for_attachment="Army", action_in_play=True,
                                   allowed_phases_in_play="COMBAT", war_pack_info="What Lurks Below"),
        CardClasses.ArmyCard("Sae'lum Pioneer", "While this unit is at a Material planet (red), it gains: "
                                                "+2 resources when command struggle won at this planet.",
                             "Scout. Ally.", 3, faction, "Common", 2, 2, 1, False,
                             war_pack_info="Wrath of the Crusaders"),
        CardClasses.SupportCard("Colony Shield Generator", "Interrupt: When a support card you control would be "
                                                           "targeted, exhaust this support to have this card "
                                                           "be targeted instead (ignoring targeting restrictions).",
                                "Upgrade.", 0, faction, "Common", False, war_pack_info="Wrath of the Crusaders"),
        CardClasses.ArmyCard("Kroot Hunter", "Reaction: After you deploy this unit at a "
                                             "Material planet (red), gain 1 RESOURCE.", "Scout. Ally.",
                             1, faction, "Common", 2, 2, 0, False,
                             war_pack_info="The Final Gambit"),
        CardClasses.EventCard("War of Ideas", "Interrupt: When a command struggle resolves at a planet, "
                                              "exhausted army units you control count their command "
                                              "icons during that command struggle.", "Tactic.",
                              0, faction, "Common", 1, False, war_pack_info="The Final Gambit"),
        CardClasses.ArmyCard("Kroot Guerrilla", "Reaction: After a battle a this planet begins, gain 1 RESOURCE.",
                             "Warrior. Kroot.", 3, faction, "Common", 2, 3, 1, False,
                             war_pack_info="Jungles of Nectavus"),
        CardClasses.ArmyCard("XV8-05 Enforcer", "Reaction: After damage from an attack by this unit has been assigned,"
                                                " reassign any amount of that damage to another enemy "
                                                "unit at this planet. (Limit once per attack.)", "Soldier. Pilot.",
                             4, faction, "Common", 4, 4, 1, False, war_pack_info="Jungles of Nectavus"),
        CardClasses.ArmyCard("Grav Inhibitor Drone", "Each unit with printed cost 2 or lower at this planet cannot "
                                                     "attack while a unit with printed cost 3 or higher at"
                                                     " this planet is ready.", "Drone.",
                             1, faction, "Common", 0, 4, 0, False, war_pack_info="Unforgiven"),
        CardClasses.AttachmentCard("Missile Pod", "Attach to a Pilot or Vehicle unit you control."
                                                  "Deploy Action: Sacrifice this attachment to deal 3 damage to a "
                                                  "target enemy army unit in your opponent's HQ or destroy a target "
                                                  "support card.", "Hardpoint.", 2, faction, "Common", 1, False,
                                   must_be_own_unit=True, required_traits="Pilot/Vehicle", action_in_play=True,
                                   allowed_phases_in_play="DEPLOY", war_pack_info="Unforgiven"),
        CardClasses.ArmyCard("Sniper Drone Team", "Ranged.\n"
                                                  "Reaction: After the ranged skirmish at this planet ends, "
                                                  "ready this unit.", "Soldier. Drone.",
                             4, faction, "Loyal", 2, 5, 2, False, ranged=True, war_pack_info="Slash and Burn"),
        CardClasses.EventCard("Tactical Withdrawal", "Deep Strike (0).\n"
                                                     "Reaction: After you Deep Strike this event, move any number"
                                                     " of units you control at this planet to an adjacent planet.",
                              "Tactic.", 0, faction, "Loyal", 2, False, deepstrike=0, war_pack_info="Slash and Burn"),
        CardClasses.ArmyCard("Herald of the Tau'va", "Each Elite unit you control at this planet gains Mobile.\n"
                                                     "FORCED REACTION: After this unit resolves its attack,"
                                                     " move it to your HQ.", "Soldier. Ethereal.",
                             2, faction, "Common", 1, 3, 1, False, war_pack_info="Searching for Truth"),
        CardClasses.SupportCard("Beleaguered Garrison", "Each card you control in reserve is counted as a command "
                                                        "icon at its planet when resolving command struggles.",
                                "Location.", 1, faction, "Common", True, war_pack_info="Searching for Truth"),
        CardClasses.ArmyCard("XV25 Stealth Squad", "Deep Strike (3).\n"
                                                   "You may Deep Strike this card as an Action "
                                                   "during the combat phase.", "Soldier. Pilot. Elite.",
                             5, faction, "Common", 5, 3, 0, False, deepstrike=3,
                             war_pack_info="Against the Great Enemy"),
        CardClasses.AttachmentCard("Kroot Hunting Rifle", "Deep Strike (0).\n"
                                                          "Attach to an army unit you control.\n"
                                                          "Reaction: After attached unit destroys an enemy unit "
                                                          "by an attack, gain 1 RESOURCE.", "Wargear. Kroot.",
                                   2, faction, "Common", 1, False, deepstrike=0,
                                   type_of_units_allowed_for_attachment="Army", must_be_own_unit=True,
                                   war_pack_info="Against the Great Enemy"),
        CardClasses.ArmyCard("Raging Krootox", "No Attachments.\n"
                                               "Combat Action: This unit gets +X ATK until the end of ths phase."
                                               " X is the number of RESOURCE in your resource pool. "
                                               "(Limit once per phase.)",
                             "Creature. Kroot. Elite.", 5, faction, "Loyal", 2, 6, 0, False,
                             no_attachments=True, action_in_play=True, allowed_phases_in_play="COMBAT",
                             war_pack_info="The Warp Unleashed"),
        CardClasses.EventCard("Hunter's Ploy", "Reaction: After the headquarters phase begins, each player gains "
                                               "RESOURCE equal to the highest printed cost among units he controls.",
                              "Tactic.", 0, faction, "Common", 1, False, war_pack_info="The Warp Unleashed"),
        CardClasses.ArmyCard("Commander Bravestorm",
                             "Reaction: After you attach a non-Drone attachment to a unit at this planet, "
                             "draw a card.", "Soldier. Pilot. Shas'o.",
                             3, faction, "Loyal", 2, 4, 1, True, war_pack_info="By Imperial Decree"),
        CardClasses.ArmyCard("Escort Drone",
                             "You may deploy this card as a Wargear attachment with the text "
                             "\"Attach to an army unit. Attached unit gains +2 ATK and +1 HP. "
                             "Interrupt: When attached unit leaves play detach this card to have "
                             "it become an army unit.\"", "Drone.",
                             1, faction, "Loyal", 2, 1, 1, False, war_pack_info="A Mask Falls Off"),
        CardClasses.ArmyCard("Frontline Counsellor",
                             "Interrupt: When another unit you control is routed or moves from a planet, "
                             "move this unit to that planet. (Limit once per phase.)\n"
                             "Forced Reaction: After this unit resolves its attack, move it to your HQ.",
                             "Soldier. Ethereal.", 2, faction, "Common", 2, 1, 2, False,
                             war_pack_info="The Laughing God"),
        CardClasses.ArmyCard("Gue'vesa Overseer", "This unit is an Astra Militarum unit in addition to Tau.\n"
                                                  "Reaction: After this unit enters play, a non-Tau army unit at "
                                                  "an adjacent planet gets +1 ATK and another gets +1 HP until the "
                                                  "end of the game. (Each unit can be at a different planet.)",
                             "Soldier.", 2, faction, "Common", 1, 3, 1, False, war_pack_info="Overrun"),
        CardClasses.ArmyCard("Kroot Hounds",
                             "No Attachments.\n"
                             "Reaction: After a Kroot unit you control damages an enemy unit by an attack at "
                             "this planet, exhaust this unit to deal 2 damage to that enemy unit.",
                             "Creature. Kroot.", 2, faction, "Common", 3, 3, 0, False, no_attachments=True,
                             war_pack_info="Breaching the Veil"),
        CardClasses.ArmyCard("Rampaging Knarloc",
                             "No Attachments.\n"
                             "While you have 4 RESOURCE or more, reduce all damage taken by this unit to 3.\n"
                             "Reaction: After this unit is declared as a defender, exhaust it "
                             "to deal 4 damage to the attacker.", "Creature. Kroot. Elite.",
                             5, faction, "Loyal", 4, 7, 0, False, no_attachments=True, war_pack_info="Overrun"),
        CardClasses.ArmyCard("Scavenging Kroot Rider",
                             "Reaction: After this unit enters play, attach an eligible attachment from your "
                             "discard pile to this unit and exhaust a target enemy limited support card.",
                             "Kroot.", 2, faction, "Common", 3, 3, 0, False, war_pack_info="The Laughing God"),
        CardClasses.ArmyCard("Shas'el Lyst",
                             "While this unit is ready, as an additional cost to target units you control at this "
                             "planet, your opponent must pay 1 RESOURCE.\n"
                             "Interrupt: When your opponent triggers an ability that discards a card from your hand "
                             "or routs a unit you control, put this unit from your hand into play at a planet.",
                             "Soldier. Hero.", 2, faction, "Loyal", 2, 3, 1, True,
                             war_pack_info="Defenders of the Faith"),
        CardClasses.ArmyCard("Trap Laying Hunter", "Interrupt: When this unit is chosen as a defender, "
                                                   "your opponent must choose to either deal 3 damage to the "
                                                   "attacker or exhaust a unit he controls at the same planet. "
                                                   "(Limit once per combat round.)", "Warrior. Kroot.",
                             3, faction, "Common", 4, 2, 0, False, war_pack_info="Aligned Stars"),
        CardClasses.AttachmentCard("Arrangement at Elova IV",
                                   "Attach to a Tau army unit you control.\n"
                                   "Attached unit gains, \"Reaction: When your opponent wins a command struggle at "
                                   "a planet with one or more Tau units you control, gain 1 RESOURCE.\"",
                                   "Negotiation.", 0, faction, "Loyal", 2, True, must_be_own_unit=True,
                                   type_of_units_allowed_for_attachment="Army", unit_must_match_faction=True,
                                   war_pack_info="Breaching the Veil"),
        CardClasses.AttachmentCard("Data Analyzer",
                                   "Attach to an army unit.\n"
                                   "Attached unit gets +1 HP.\n"
                                   "Interrupt: When a unit is assigned damage by an attack at this planet, reassign "
                                   "1 of that damage to another unit controlled by the same player at this planet.",
                                   "Wargear. Experimental.", 2, faction, "Loyal", 2, True,
                                   type_of_units_allowed_for_attachment="Army", extra_health=1,
                                   war_pack_info="A Mask Falls Off"),
        CardClasses.AttachmentCard("Fusion Cascade Defiance",
                                   "Attach to an army unit.\n"
                                   "Attached unit gets +1 ATK and +1 HP.\n"
                                   "Reaction: After this card enters or leaves play, deal 1 damage to a target "
                                   "unit at this planet.", "Wargear.", 1, faction, "Loyal", 2, False,
                                   type_of_units_allowed_for_attachment="Army", extra_health=1, extra_attack=1,
                                   war_pack_info="A Mask Falls Off"),
        CardClasses.AttachmentCard("Positional Relay",
                                   "Attach to an army unit.\n"
                                   "Attached unit gets +1 ATK and +1 HP.\n"
                                   "Action: Exhaust this attachment to Rally X an attachment, add it to your hand. "
                                   "X equals the number of attachments you control.",
                                   "Wargear. Experimental.", 1, faction, "Loyal", 2, False,
                                   type_of_units_allowed_for_attachment="Army", extra_health=1, extra_attack=1,
                                   action_in_play=True, allowed_phases_in_play="ALL", war_pack_info="A Mask Falls Off"),
        CardClasses.EventCard("Breach and Clear",
                              "If all effects of this event are cancelled, gain 2 RESOURCE.\n"
                              "Action: Exhaust a target army unit. Then you may sacrifice an attachment to exhaust "
                              "another target army unit at the same planet.", "Tactic.",
                              2, faction, "Loyal", 2, False, action_in_hand=True, allowed_phases_in_hand="ALL",
                              war_pack_info="A Mask Falls Off"),
        CardClasses.EventCard("Consumed by the Kindred",
                              "Action: Exhaust a Kroot unit and sacrifice another non-Vehicle unit to gain "
                              "RESOURCE equal to the sacrificed unit's printed cost.", "Tactic. Kroot.",
                              0, faction, "Common", 1, False, action_in_hand=True, allowed_phases_in_hand="ALL",
                              war_pack_info="Enemy Territory"),
        CardClasses.EventCard("Guerrilla Tactics",
                              "Command Action: Choose a planet with an enemy unit. Your opponent loses RESOURCE "
                              "equalt to the resource bonus and must discard cards equal to the card bonus. "
                              "Then move a Kroot army unit you control at that planet to the first planet.",
                              "Tactic. Kroot.", 1, faction, "Loyal", 2, False,
                              action_in_hand=True, allowed_phases_in_hand="COMMAND", war_pack_info="Aligned Stars"),
        CardClasses.EventCard("Optimized Landing",
                              "Interrupt: When you deploy a non-Drone army unit, reduce its cost by X (Max 2). "
                              "X is the amount of attachments you control. (Max 1 per round.)",
                              "Tactic.", 0, faction, "Loyal", 1, False, war_pack_info="For the Enclaves"),
        CardClasses.SupportCard("Bork'an Sept",
                                "Reaction: After you deploy this support, search your deck for a non-signature "
                                "non-hardpoint Tau attachment, reveal it, add it to your hand and shuffle your deck.",
                                "Pledge.", 0, faction, "Loyal", False, war_pack_info="Chronicles of Heroes"),
        CardClasses.SupportCard("Dal'yth Sept",
                                "While there are two or more tokens on this support, you may use it from play as a "
                                "shield card with 4 shield icons.\n"
                                "Reaction: After your opponent captures a planet, put a token on this support.",
                                "Pledge.", 0, faction, "Loyal", False, war_pack_info="Chronicles of Heroes"),
        CardClasses.SupportCard("Vior'la Sept",
                                "If there are 3 or more tokens on this support, sacrifice it.\n"
                                "Reaction: After the phase command ends, put a Defense Battery into play from the "
                                "card collection at a planet without Defense Battery you control and put a "
                                "token on this support.", "Pledge.", 1, faction, "Loyal", False,
                                war_pack_info="Chronicles of Heroes"),
        CardClasses.SupportCard("Smuggler's Den",
                                "Action: Exhaust this support and pay 1 RESOURCE to return a target non-Drone "
                                "attachment you control to your hand and gain resources equal to the printed cost "
                                "of the attachment.", "Location.", 1, faction, "Loyal", True,
                                action_in_play=True, allowed_phases_in_play="ALL", war_pack_info="Enemy Territory"),
        CardClasses.WarlordCard("Aun'Len",
                                "Reaction: After the deploy phase ends, have a player trigger the battle ability "
                                "of a target planet with a unit you control. "
                                "(You cannot target the same planet twice.)", "Prophet.", faction, 2, 6, 2, 6,
                                "Bloodied.\nAction: Trigger the battle ability of this planet. "
                                "(Limit once per game.)", 7, 7,
                                ["1x Forward Outpost", "4x Pathfinder Team",
                                 "1x Rail Rifle", "2x Tempting Ceasefire"], war_pack_info="For the Enclaves"),
        CardClasses.SupportCard("Forward Outpost",
                                "Combat Action: Exhaust this support to give a non-Drone army unit "
                                "Sweep (2) for its next attack this phase.", "Location.", 1, faction, "Signature",
                                False, action_in_play=True, allowed_phases_in_play="COMBAT",
                                war_pack_info="For the Enclaves"),
        CardClasses.ArmyCard("Pathfinder Team", "Reaction: After this planet battle ability is triggered, "
                                                "exhaust this unit to draw a card.",
                             "Soldier.", 2, faction, "Signature", 2, 3, 1, False,
                             war_pack_info="For the Enclaves"),
        CardClasses.AttachmentCard("Rail Rifle",
                                   "Attach to your warlord.\n"
                                   "Reaction: After your warlord resolves an attack, retreat it to deal 1 damage "
                                   "to a target unit at this planet.", "Weapon.", 1, faction, "Signature", 3, False,
                                   must_be_own_unit=True, type_of_units_allowed_for_attachment="Warlord",
                                   war_pack_info="For the Enclaves"),
        CardClasses.EventCard("Tempting Ceasefire",
                              "Deploy Action: Each player secretly chooses a number on the command dial, reveal it and "
                              "draw that many cards. Then if you set a lower number, take the difference in RESOURCE "
                              "from your opponent. If not he takes the difference in RESOURCE from the token bank. "
                              "If equal draw a card. Max 1 per round.", "Tactic.",
                              0, faction, "Signature", 1, False, action_in_hand=True, allowed_phases_in_hand="DEPLOY",
                              war_pack_info="For the Enclaves"),
        CardClasses.WarlordCard("Farsight",
                                "Your attachment cards are considered to have Deep Strike (0).\n"
                                "Reaction: After you Deep Strike a card, gain 2 RESOURCE. (Limit once per phase.)",
                                "Shas'o.", faction, 2, 7, 2, 5,
                                "Bloodied.\nYour attachment cards are considered to have Deep Strike (0).", 7, 7,
                                ["2x Daring Assault", "4x Farsight Vanguard",
                                 "1x Support Fleet", "1x The Dawn Blade"],
                                war_pack_info="For the Enclaves"),
        CardClasses.EventCard("Daring Assault",
                              "The effects of this event cannot be cancelled.\n"
                              "Action: Draw a card. Then you may move each card in reserve you control to a "
                              "different planet.", "Tactic.", 0, faction, "Signature", 1, False,
                              action_in_hand=True, allowed_phases_in_hand="ALL", war_pack_info="For the Enclaves"),
        CardClasses.ArmyCard("Farsight Vanguard",
                             "Reaction: After this unit is declared as an attacker or defender, choose a unit "
                             "you control. Move a non-Drone attachment you control between this unit and the "
                             "chosen unit. (Limit once per phase.)", "Soldier.",
                             2, faction, "Signature", 2, 2, 1, False, war_pack_info="For the Enclaves"),
        CardClasses.SupportCard("Support Fleet",
                                "This support cannot be targeted nor discarded.\n"
                                "After you play this support, Rally 16 for up to 4 attachments, place them on this "
                                "support. Then shuffle your deck.\n"
                                "Reaction: After the deploy phase begins, transfer a card from this support "
                                "to your hand.", "Fleet.", 1, faction, "Signature", False,
                                war_pack_info="For the Enclaves", preparation=True),
        CardClasses.AttachmentCard("The Dawn Blade",
                                   "Attach to your warlord.\n"
                                   "Attached unit gets Sweep (1).\n"
                                   "Combat Action: Exhaust this attachment to either Deep Strike an attachment or "
                                   "move a card in reserve you control to another planet.",
                                   "Weapon.", 0, faction, "Signature", 3, True,
                                   must_be_own_unit=True, type_of_units_allowed_for_attachment="Warlord",
                                   war_pack_info="For the Enclaves"),
        CardClasses.WarlordCard("Shaper Agnok",
                                "Interrupt: When your opponent wins a command struggle at a planet with one or "
                                "more Kroot units you control, gain 1 RESOURCE or draw 1 card.", "Kroot.",
                                faction, 2, 7, 2, 5, "Bloodied.", 7, 7,
                                ["4x Agnok's Shadows", "2x Behind Enemy Lines",
                                 "1x Evolutionary Adaptation", "1x Vanguard Pack"],
                                war_pack_info="Promise of War"),
        CardClasses.ArmyCard("Agnok's Shadows",
                             "Combat Action: Exhaust this unit to have a target non-warlord unit at this planet "
                             "get -2 ATK until the end of the phase, then move this unit to an adjacent planet.",
                             "Warrior. Kroot.", 2, faction, "Signature", 2, 3, 0, False,
                             action_in_play=True, allowed_phases_in_play="COMBAT", war_pack_info="Promise of War"),
        CardClasses.EventCard("Behind Enemy Lines",
                              "Combat Action: Deploy a Kroot unit at a target planet. Then exhaust a target non-Elite "
                              "enemy army unit at this planet.", "Tactic. Kroot.", 1, faction, "Signature", 1, False,
                              action_in_hand=True, allowed_phases_in_hand="ALL", war_pack_info="Promise of War"),
        CardClasses.SupportCard("Evolutionary Adaptation",
                                "Deploy Action: Exhaust this support to choose a unit in your opponent's discard pile "
                                "and remove it from the game to give a target Kroot army unit a keyword (and all "
                                "associated values) printed on the removed unit until the end of the round.",
                                "Upgrade.", 0, faction, "Signature", False,
                                action_in_play=True, allowed_phases_in_play="DEPLOY", war_pack_info="Promise of War"),
        CardClasses.AttachmentCard("Vanguard Pack",
                                   "Limited.\nAttach to a planet.\n"
                                   "Reaction: After an enemy unit is deployed at this planet, exhaust it. Then "
                                   "your opponent may give you 1 RESOURCE to return this attachment to your hand.",
                                   "Stratagem. Kroot.", 0, faction, "Signature", 3, False, limited=True,
                                   planet_attachment=True, war_pack_info="Promise of War")
    ]
    return tau_cards_array
