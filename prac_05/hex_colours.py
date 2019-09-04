HEX_COLOURS = {"aquamarine1": "#7fffd4", "blue1": "	#0000ff", "chartreuse1": "#7fff00", "CornflowerBlue": "#6495ed",
               "brown1": "#ff4040", "cyan1": "#00ffff", "DarkGoldenrod1": "#ffb90f", "DarkOliveGreen1": "#caff70",
               "DarkOrange": "#ff8c00", "DarkOrchid1": "#bf3eff"}


colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("{} not in colours".format(colour))
    colour = input("Enter colour: ")
