print(''''
                   ..oo$00ooo..                    ..ooo00$oo..
                .o$$$$$$$$$'                          '$$$$$$$$$o.
             .o$$$$$$$$$"             .   .              "$$$$$$$$$o.
           .o$$$$$$$$$$~             /$   $\              ~$$$$$$$$$$o.
         .{$$$$$$$$$$$.              $\___/$               .$$$$$$$$$$$}.
        o$$$$$$$$$$$$8              .$$$$$$$.               8$$$$$$$$$$$$o
       $$$$$$$$$$$$$$$              $$$$$$$$$               $$$$$$$$$$$$$$$
      o$$$$$$$$$$$$$$$.             o$$$$$$$o              .$$$$$$$$$$$$$$$o
      $$$$$$$$$$$$$$$$$.           o{$$$$$$$}o            .$$$$$$$$$$$$$$$$$
     ^$$$$$$$$$$$$$$$$$$.         J$$$$$$$$$$$L          .$$$$$$$$$$$$$$$$$$^
     !$$$$$$$$$$$$$$$$$$$$oo..oo$$$$$$$$$$$$$$$$$oo..oo$$$$$$$$$$$$$$$$$$$$$!
     {$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$}
     6$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$?
     '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
      o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o
       $$$$$$$$$$$$$$;'~`^Y$$$7^''o$$$$$$$$$$$o''^Y$$$7^`~';$$$$$$$$$$$$$$$
       '$$$$$$$$$$$'       `$'    `'$$$$$$$$$'     `$'       '$$$$$$$$$$$$'
        !$$$$$$$$$7         !       '$$$$$$$'       !         V$$$$$$$$$!
         ^o$$$$$$!                   '$$$$$'                   !$$$$$$o^
           ^$$$$$"                    $$$$$                    "$$$$$^
             'o$$$`                   ^$$$'                   '$$$o'
               ~$$$.                   $$$.                  .$$$~
                 '$;.                  `$'                  .;$'
                    '.                  !                  .`
''')



print("Welcome to Treasure island.\n Your mission is to find the treasure.")
direction = input("left or right?").lower()



if direction == "left":
    actionsto = input("swim or wait?").lower()
    if actionsto == "wait":
        door = input("Which door?").lower()
        if door == "blue":
            print("Eaten by beasts. \n Game Over")
        elif door == "red":
            print("Burned by fire.\n Game Over")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\n Game Over.")
else:
    print("Fall into a hole. \n Game Over.")


    
