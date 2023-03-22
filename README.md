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
- Faire un pretty printer (qui réécrit le programme proprement)
- Analyseur contextuel

Faire l'essemble de ces étapes pour un langage de programmation simple. Puis le complexifier incrementalement.

## Grammaire
- _Program_ := _Initial_State_  _actions_  
- _Initial_State_ := (_Factions_)? (_Relations_)? (_Fleets_)? _terrain_  
- _Factions_ := Factions: _Faction_*
- _Faction_ := - _identifier_
- _Relations_ := Relations: _Relation_*  
- _Relation_ := -_identifier_ - _identifier_ : _int_  
- _Fleets_ := Fleets: _Faction_Fleet_*  
- _Faction_Fleet_ := _identifier_  fleet: _Flotilla_ * 
- _Flotilla_ := - _identifier_ : _Vessel_ _Vessel_*   
- _Vessel_ := - int _Vessel_Type_
- _Vessel_Type_ := croiseur | destroyer | sous-marin | porte-avion | torpilleur | bombardier | chasseur | transporteur
- _Terrain_ := -int*int  
