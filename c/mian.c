#include <stdio.h>

int main() {
    // Déclaration d'une chaîne de caractères pour stocker le nom
    char nom[50];

    // Demande à l'utilisateur son nom
    printf("Entrez votre nom : ");
    
    // Utilisation de scanf pour lire le nom saisi par l'utilisateur
    scanf("%s", nom);

    // Affiche un message de bienvenue avec le nom saisi
    printf("Bienvenue, %s !\n", nom);

    // Termine le programme
    return 0;
}
