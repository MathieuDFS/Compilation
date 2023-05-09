# Projet Compilation
Projet scolaire de création d'un compilateur.

## Attendus théoriques
- [X] un lexer
- [X] un parser
- [X] un ast 
- [X] un visiteur
- [X] une documentation

## Idée du projet
Faire un compilateur pour un langage de programmation pour le wargaming. Ce langage sera desciptif et permettra d'initialiser une situation de jeu. Il permettra de décrire les flottes, les relations entre les factions et la carte.

## Grammaire
- _Program_ := _Initial_State_
- _Initial_State_ := (_Factions_)? (_Relations_)? (_Fleets_)? _Map_  
- _Factions_ := Factions: _Faction_*
- _Faction_ := - _identifier_
- _Relations_ := Relations: _Relation_*  
- _Relation_ := -_identifier_ - _identifier_ : _int_  
- _Fleets_ := Fleets: _Faction_Fleet_*  
- _Faction_Fleet_ := -_identifier_  fleet: _Flotilla_ * 
- _Flotilla_ := - _identifier_ : _Vessel_ _Vessel_*   
- _Vessel_ := - int _Vessel_Type_
- _Vessel_Type_ := croiseur | destroyer | sous-marin | porte-avion | torpilleur | bombardier | chasseur | transporteur
- _Map_ := -int*int  
- _Identifier_ := str

## Utilisation
Pour utiliser le compilateur, il faut lancer le script `main.py` avec en argument le fichier à compiler. (il est possible d'ajouter un second argument, cela activera le pretty printer et retournera le fichier réécrit avec ce nom).
```bash	
python3 main.py <file>
python3 main.py <file> <pretty_print_name>
python3 main.py example.txt
python3 main.py mon_programme.txt mon_programme
```

Il est aussi possible de l'exécuter directement depuis un IDE pour cela modifié la valeur IDE dans le fichier `main.py` à `True`. Et indiquer le nom du fichier à compiler dans la variable `filename`.