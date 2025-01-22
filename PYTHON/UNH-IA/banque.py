from experta import *

class EvaluationPret(KnowledgeEngine):

    @DefFacts()
    def initier_faits(self):
        yield Fact(revenu=0)
        yield Fact(age=0)
        yield Fact(duree_pret=0)
        yield Fact(montant_demande=0)
        yield Fact(ratio_dette_revenu=0)

    @Rule(Fact(revenu=P(lambda r: r < 2000)))
    def refuser_pret_revenu(self):
        print("Prêt refusé : Revenu mensuel insuffisant.")
        self.declare(Fact(eligibilite="refuse"))

    @Rule(Fact(revenu=P(lambda r: r >= 2000)), Fact(ratio_dette_revenu=P(lambda ratio: ratio > 0.4)))
    def refuser_pret_ratio(self):
        print("Prêt refusé : Ratio dette/revenu trop élevé.")
        self.declare(Fact(eligibilite="refuse"))

    @Rule(Fact(age=P(lambda age: age < 18)))
    def refuser_pret_age(self):
        print("Prêt refusé : Le client est mineur.")
        self.declare(Fact(eligibilite="refuse"))

    @Rule(Fact(montant_demande=P(lambda montant: montant > 50000)))
    def verification_approfondie(self):
        print("Vérification approfondie nécessaire : Montant demandé supérieur à 50 000€.")

    @Rule(Fact(duree_pret=P(lambda duree: duree > 10)), Fact(revenu=P(lambda r: r <= 5000)))
    def refuser_pret_duree(self):
        print("Prêt refusé : Durée du prêt trop longue avec un revenu insuffisant.")
        self.declare(Fact(eligibilite="refuse"))

    @Rule(Fact(revenu=P(lambda r: r >= 2000)),
          Fact(ratio_dette_revenu=P(lambda ratio: ratio <= 0.4)),
          Fact(age=P(lambda age: age >= 18)),
          Fact(duree_pret=P(lambda duree: duree <= 10) | Fact(revenu=P(lambda r: r > 5000))),
          NOT(Fact(eligibilite="refuse")))
    def accorder_pret(self):
        print("Prêt accordé.")
        self.declare(Fact(eligibilite="accorde"))

# Exemple d'utilisation
if __name__ == "__main__":
    moteur = EvaluationPret()
    moteur.reset()

    # Données du client
    moteur.declare(Fact(revenu=3000))
    moteur.declare(Fact(age=25))
    moteur.declare(Fact(duree_pret=8))
    moteur.declare(Fact(montant_demande=40000))
    moteur.declare(Fact(ratio_dette_revenu=0.3))

    moteur.run()
