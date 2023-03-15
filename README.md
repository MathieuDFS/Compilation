# Projet Compilation
Projet scolaire de création d'un compilateur

## Attendus théoriques
- [X] un lexer
- [ ] un parser
- [ ] un ast
- [ ] un visiteur
- [ ] une documentation

## Idée du projet

Faire un compilateur pour un langage de programmation pour le wargaming.

## Todo list
- exemple de programme à compiler
- un lexer
- un parser
- Construite un AST
- Analyseur contextuel

Faire l'essemble de ces étapes pour un langage de programmation simple. Puis le complexifier incrementalement.

## Grammaire
- _program_ := _etat_inital_  _actions_  
- _etat_inital_ := (_factions_)? (_relations_)? (_flottes_)? _terrain_  
- _factions_ := Factions (- _identifier_)*  
- _relations_ := Relations (- _relation_faction_)*  
- _relation_faction_ := _identifier_ - _identifier_ :int  
- _flottes_ := Fleets _flotte_faction_*  
- _flotte_faction_ := _identifier_  fleet : (_flotille_ )* 
- _flotille_ = - _identifier_ : _navires_ _navires_*   
- _navires_ = - - int _batiment_
- _batiment_ = croiseur | destroyer | sous-marin | porte-avion | torpilleur | bombardier | chasseur | transporteur
- _terrain_ := -int * int  
