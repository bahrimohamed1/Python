from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0
        self.platform_status = "active"

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        card1_score = card1.attack_power + card1.health + card1.rating
        card2_score = card2.attack_power + card2.health + card2.rating

        if card1_score >= card2_score:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.cards.values(),
            key=lambda card: (-card.calculate_rating(), card.name),
        )

        leaderboard = []
        for card in sorted_cards:
            leaderboard.append(
                {
                    "id": card.card_id,
                    "name": card.name,
                    "rating": card.calculate_rating(),
                    "record": f"{card.wins}-{card.losses}",
                }
            )
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        if total_cards == 0:
            avg_rating = 0
        else:
            total_rating = sum(card.calculate_rating()
                               for card in self.cards.values())
            avg_rating = round(total_rating / total_cards)

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": self.platform_status,
        }
