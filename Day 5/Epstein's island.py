print ('''  missing children:

         _          __________                              _,
     _.-(_)._     ."          ".      .--""--.          _.-{__)-._
   .'________'.   | .--------. |    .'        '.      .:-'`____`'-:.
  [____________] /` |________| `\  /   .'``'.   \    /_.-"`_  _`"-._\)
  /  / .\/. \  \|  / / .\/. \ \  ||  .'/.\/.\'.  |  /`   / .\/. \   `)
  |  \__/\__/  |\_/  \__/\__/  \_/|  : |_/\_| ;  |  |    \__/\__/    |
  \            /  \            /   \ '.\    /.' / .-\                /-.
  /'._ ,--, _.'\  /'._ ,--, _.'\   /'. `'--'` .'\/   '._-.__--__.-_.'   )
 /_   `""""`   _\/_   `""""`   _\ /_  `-./\.-'  _\'.    `""""""""`    .'`)
(__/    '|    \ _)_|           |_)_/            \__)|        '       |   |
  |_____'|_____|   \__________/   |              | `_________'________`;-'
   '----------'    '----------'   '--------------'`--------------------`

   ''')
print ("Welcome to Epstein's island!")
print ("Your mission is to find the missing children!\n")

start = input ("press 1 to start your mission or 2 to puss out: \n")

if start == "1":
    print ('''           
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
    =- =- -=.--"       ''')
    print ("You've found yourself on the shore of the island of Epstein. On your left you see a barrow of drugs and on your right an open path to the mainland.")
    move1 = input ("type 'left' to check the barrow or type 'right' to make a run for the inland: \n").lower()
    if move1 == "right":
        print ('''             ____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''          ''          ''          '''  ''  ''')
        print ("It looks like the billionaires were distracted and didn't see you.\n")
        print ("You're now outside their mansion, but the day is bright and you risk being caught.")
        move2 = input ("type 'risk' to take a risk and go inside, or type 'wait' to wait for nightfall: \n").lower()
        if move2 == "wait":
            print(''' 
            ''')
            print ("You decided to play it safe and wait for nightfall, smart choice.\n")
            print ("As you walk through the mansion you come across 3 doors:")
            print ("a 'red' door, a 'blue' door and a 'yellow' door\n")
            print (''' 
    RED           BLUE         YELLOW
 __________    __________    __________
|  __  __  |  |  __  __  |  |  __  __  |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|  __  __()|  |  __  __()|  |  __  __()|
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|__________|  |__________|  |__________|

 ''')
            move3 = input ("Which color do you choose?: \n").lower()
            if move3 == "blue":
                print (" ")
                print ("As you open the blue door you see all the faces of the missing children!")
                print ('''  

         _          __________                              _,
     _.-(_)._     ."          ".      .--""--.          _.-{__)-._
   .'________'.   | .--------. |    .'        '.      .:-'`____`'-:.
  [____________] /` |________| `\  /   .'``'.   \    /_.-"`_  _`"-._\)
  /  / .\/. \  \|  / / .\/. \ \  ||  .'/.\/.\'.  |  /`   / .\/. \   `)
  |  \__/\__/  |\_/  \__/\__/  \_/|  : |_/\_| ;  |  |    \__/\__/    |
  \            /  \            /   \ '.\    /.' / .-\                /-.
  /'._ '--'  _.'\  /'._'--' _.'\   /'.` '--'` .'\/   '._-._'--'_.-_.'   )
 /_   `""""`   _\/_   `""""`   _\ /_  `-./\.-'  _\'.    `""""""""`    .'`)
(__/    '|    \ _)_|           |_)_/            \__)|        '       |   |
  |_____'|_____|   \__________/   |              | `_________'________`;-'
   '----------'    '----------'   '--------------'`--------------------`

   ''')
                print ("Congradulations you win!\n")
            elif move3 == "yellow":
                print (" ")
                print ("Uh-oh, it seems the yellow door was a bathroom.\n")
                print ("You've just walked in on a billianaires-only orgy and have been caught.\n")
                print ("GAME OVER\n")
            elif move3 == "red":
                print (" ")
                print ("Uh-oh, it appears the red door was a slaughter room.")
                print ("From the cornor of the room you hear a voice: 'If their age is off the clock.. they no longer can get the cock.'\n")
                print ("You've been caught. GAME OVER\n")
            else:
                print (" ")
                print ("bro that ain't even a room\n")
                print ("GAME OVER\n")
        else:
            print (" ")
            print ("Uh-oh, you ran into Michelle Obama!!!")
            print ("Michelle Obama whipped out her pecker and got you.\n")
            print ("GAME OVER\n")

    else:
        print (" ")
        print ("Uh-oh, it looks like Hilary Clinton was sleeping in the barrow of drugs and is now awake. You've been caught\n") 
        print ("GAME OVER\n")
else:
    print (" ")
    print ("Huh? Wow, you must hate children. Odd considering you are one.\n")
    print ("You pussed out and have been caught as a result. Welcome to your new forever home.\n")
    print ("GAME OVER\n")