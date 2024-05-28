# INHA in short : introduction
Ce projet est un essai réalisé au cours du printemps 2024, en tant que monitrice étudiante au service de l'informatique documentaire (SID) de l'INHA. Plus particulièrement, il a été effectué dans le cadre de la rédaction de notices pour les catalogues de ventes numrisés à mettre en ligne sur la bibliothèque numérique de l'INHA. 
# Problématiques et objectifs 
Les catalogues de ventes ont souvent des titres longs et descriptifs, et encore plus quand il s’agit de recueils factices. Pour les afficher de manière plus lisible sur la page des résultats de recherche sur la bibliothèque numérique, ils sont raccourcis.
## Méthode : 
- Agrégation des titres des recueils factices avec le séparateur « \[suivi de] » 
- Titre raccourcis : généralement on garde le début du titre, pour avoir une idée représentative du contenu de la vente, le nom du collectionneur, d’artistes importants s’il y en a. La date est extraite et mise en forme selon la forme suivante : \[vente du N° du jour, mois, année]. Les contenus supprimés sont placés entre crochets. Par exemple :
| Titre long | Titre court |
|---------|----------|
|Catalogue des vases, colonnes, tables de marbres rares, figures de bronze, porcelaines de choix, laques, meubles précieux, pendules, lustres, bras & lanternes de bronze doré d'or mat : bijoux & autres effets importants qui composent le cabinet de feu M. le duc d'Aumont. Par P. F. Julliot fils, & A. J. Paillet. La vente se fera le 12 décembre 1782, à quatre heures précises de relevée, & jours suivants, en son hôtel, place Louis XV|Catalogue des effets précieux qui composent le cabinet de feu M. le duc d'Aumont \[...] : \[vente du 12 au 21 décembre 1782]|

## Idées 
- Expérimenter une automatisation à la fois du processus d’agrégation et de titres résumés
- Créer une petite interface graphique qui soit capable, quand on lui donne un ou plusieurs titre de catalogues de ventes, de les agréger ensemble (s'il s'agit d'un recueil factice) et de générer une version abrégée (destinée à un affichage plus clair sur la page des résultats de recherche sur la bibliothèque numérique)
