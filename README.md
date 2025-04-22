Author: Jason Lopez
Date: 4/22/25
Class: CS4480
Assignment: PA3

The file Jason_Lopez_u1363004.py is the orchestrator that will setup the containers and change paths from north to south or vice versa.

In order to call the program, python3 needs to be called first like "python3 Jason_Lopez_u1363004.py argument1 argument2".
The help menu is invoked by calling "python3 Jason_Lopez_u1363004.py -h"

A copy of the help menu returned is:
"Create network topology with command:"
"-c setup"
"Startup OSPF daemons on topology:"
"-c startup ospf"
"Add endpoint routes:"
"-c install routes"
"Move traffic path from the current route to the north route:"
"-c swap path north"
"Move traffic path from the current route to the south route:"
"-c swap path south"

Assumptions: This program assumes that dockersetup from cs4480-2025-s/pa3/part1/
             has already been called. It also assumes that the program is being 
             called from inside the main "Jason_Lopez_u1363004" folder. I mean 
             the path should show ".../Jason_Lopez_u1363004".

Doing a tcpdump on r2, r4, or hb will show a ospfv2 hello as well as any pings that are being sent across the network.
