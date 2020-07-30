---
title: Projet 8 - Créez une plate-forme pour amateurs de Nutella
subtitle: Parcours OpenClassrooms - Développeur d'application Python
author:
  - 'Étudiant : Guillaume OJARDIAS'
  - 'Mentor : Erwan KERIBIN'
  - 'Mentor évaluateur : Babacar SYLLA'
---
\renewcommand{\contentsname}{Sommaire}
\tableofcontents

# Présentation

## Objectif

- Trouver en un clic un produit de substitution

## Cahier des charges

- Fonctionnalités :
	- Avoir un compte utilisateur
	- Sauvegarder des substituts dans ses favoris
	- Faire une recherche dès la page d'accueil
\linebreak
- Design :
	- Esquisses de disposition des pages
	- Charte graphique
	- Utilisation du template Creative proposé par StartBootstrap

## Résultat final

- [http://projet-8.ojardias.io](http://projet-8.ojardias.io)

# Démarche de création

## Étapes du projet

- Création du projet Django
\linebreak
- Mise en place de le gestion des utilisateurs => `User` personnalisé
\linebreak
- Création des modèles de données (`Product` et `Category`)
- Insertion des produits dans la BDD (commande `init_db`)
\linebreak
- Mise en place du système de recherche des substituts
- Ajout de la fonctionnalité de mise en favoris
\linebreak
- Ajout des propositions lors de la recherche

## Code source

- Python + Django
\linebreak
- GitHub -> [Pur-Beurre](https://github.com/GuillaumeOj/Pur-Beurre)

## Arborescence du projet

```
|- config              #- Configuration du projet
|- homepage            ##
|- openfoodfacts        #
|- product              # Applications
|- search               #
|- users               ##
|- static              #- Fichiers statiques
|- templates           #- Templates généraux
|- tests               ##
    |- homepage         #
    |- openfoodfacts    #
    |- product          # Tests
    |- search           #
    |- users           ##
```

## Algorithme de recherche d'un substitut

- Filtre pour le calcul des catégories en commun
```python
q = Q(categories__in=product.categories.all()) & Q(
	nutriscore_grade__lt=product.nutriscore_grade))

```

- Requête pour obtenir les substituts
```python
substitutes = (Product.objects.annotate(
	common_categories=Count("categories", filter=q))
		.order_by("-common_categories", "nutriscore_grade")
		.exclude(code=product.code)
		.exclude(name=product.name)[:30])
```

## Tests sur la vue `auto_completion` de l'application `search` (1/3) :

- Mock de la class `Product` :

```python
class MockProduct:
	def __init__(self, products, substitutes=""):
		# Mock de l'attribut "objects"
		self.objects = MockProductManager(
			products, substitutes
		)
```

## Tests sur la vue `auto_completion` de l'application `search` (2/3) :

- Mock de la class `ProductManager` :

```python

class MockProductManager:
	def __init__(self, products, substitutes):
		self.products = products
		self.substitutes = substitutes

	{ ··· }

	# Mock la méthode
	def get_products_by_name(self, *args, **kwargs):
		return self.products
```

## Tests sur la vue `auto_completion` de l'application `search` (3/3) :

- Utilisation de `MockProduct` :

```python
def test_auto_completion_return_json(self):
	# Instantiation du Mock
	mock_product = MockProduct(self.products)
		.objects.get_products_by_name
	# Patch du Mock
	with patch("product.models.Product", mock_product):
	# Appel de la vue
	response = self.client.post(
		reverse("search:auto_completion"),
		data={"name": "nut"},
	)
	self.assertEqual(response.status_code, 200)
	self.assertTrue(loads(response.content)
		.get("products_names"))
```

# Bilan du projet

## Découpage du projet

- Perfectible
	- Changer le nom de `homepage`
	- Regrouper les templates
\linebreak
- Penser son découpage en amont
	- Changement en cours difficile
	- Facilité avec l'expérience

## Tests

- **Coverage** est un très bon outil
	- Utile pour mettre en relief les zones non testées
	- Attention à avoir un esprit critique
\linebreak
- Le **Test Driven Development**
	- Indispensable
	- Difficile pour un débutant
	- Viens avec le temps et l'expérience

## Django

- Nombreux outils disponibles *out of the box*
	- Users
	- Admin
	- API (non utilisé sur ce projet)
\linebreak
- Part de *magie* appréciée par certains
\linebreak
- Très puissant pour une utilisation poussée

## Fin

- Merci pour votre attention
