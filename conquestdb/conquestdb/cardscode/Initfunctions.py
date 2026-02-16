from .Inits import ChaosCardsInit, NeutralCardsInit, OrksCardsInit, PlanetCardsInit, \
    DarkEldarCardsInit, EldarCardsInit, TauCardsInit, SpaceMarinesCardsInit, AstraMilitarumCardsInit, \
    TyranidsCardsInit, NecronsCardsInit, TokensCardsInit, ApokaErrataCardsInit


def init_player_cards():
    space_marines_card_array = SpaceMarinesCardsInit.space_marines_cards_init()
    astra_militarum_card_array = AstraMilitarumCardsInit.astra_militarum_cards_init()
    orks_card_array = OrksCardsInit.orks_cards_init()
    chaos_card_array = ChaosCardsInit.chaos_cards_init()
    dark_eldar_card_array = DarkEldarCardsInit.dark_eldar_cards_init()
    eldar_card_array = EldarCardsInit.eldar_cards_init()
    tau_card_array = TauCardsInit.tau_cards_init()
    tyranids_card_array = TyranidsCardsInit.tyranids_cards_init()
    necrons_card_array = NecronsCardsInit.necrons_cards_init()
    neutral_card_array = NeutralCardsInit.neutral_cards_init()
    tokens_card_array = TokensCardsInit.tokens_cards_init()
    card_array = space_marines_card_array + astra_militarum_card_array + orks_card_array + chaos_card_array + \
        dark_eldar_card_array + eldar_card_array + tau_card_array + tyranids_card_array + \
        necrons_card_array + neutral_card_array + tokens_card_array
    for i in range(len(card_array)):
        if card_array[i].check_for_a_trait("Pledge"):
            card_array[i].quantity = 1
        elif card_array[i].get_loyalty() == "Signature" and card_array[i].get_card_type() != "Warlord":
            for j in range(len(card_array)):
                if card_array[j].get_card_type() == "Warlord":
                    sig_squad = card_array[j].get_signature_squad()
                    found_card = False
                    for k in range(len(sig_squad)):
                        card_name = sig_squad[k][3:]
                        if card_name == card_array[i].get_name():
                            found_card = True
                            card_array[i].quantity = int(sig_squad[k][0])
                            break
                    if found_card:
                        break
    return card_array


def init_planet_cards():
    planet_cards_array = PlanetCardsInit.planet_cards_init()
    return planet_cards_array


def init_apoka_errata_cards():
    apoka_errata_cards_array = ApokaErrataCardsInit.apoka_errata_cards_init()
    return apoka_errata_cards_array
