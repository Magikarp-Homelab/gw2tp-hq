# tp-hq

## notes:

* get all item ids (64'526)
* set  a baseline since item info/metadata isn't updaten often
* update price info over event hub

* add recipe id to object if it exists
* mf recipes aren't available, maybe query wiki for those at a later point

flow:
get item id -> search recipe -> make object -> persist
get item tp price -> trigger event/persist
map recipes out -> persist <- this shit hard

## item object
* id : number
* name : string
* icon : string

* type : string
    * depending on type, the item has more fields
* rarity : string
* level : number

* flags : []string
    * notable flags:
      * AccountBound (on acquire)
      * SoulBound (on acquire)
      * 


## notable endpoints
* items, https://wiki.guildwars2.com/wiki/API:2/items
* recipes search, https://wiki.guildwars2.com/wiki/API:2/recipes/search
* recipes, https://wiki.guildwars2.com/wiki/API:2/recipes