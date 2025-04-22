# Author: Jason Lopez
# Class: CS4480
# Assignment: PA3 Orchestrator
# Date: 4/20/25
import subprocess


# Construct the network topology
def setup_network():
    # setup files that will be needed to be called later.
    subprocess.call(["chmod", "-x", "frrsetup", "&&", "chmod", "-x", "frrrestart"])

    print("Setting up network")
    ans = subprocess.call(["sudo", "docker", "compose", "up", "-d"])

    # Call frr restart on each router container

    if ans == 0:
        print("Topology setup finished")
    else:
        print("Topology setup failed")

    return

# Startup the OSPF daemons, with appropriate configurations, in the routers.
def startup_ospf():
    return

# Install routes on each host/endpoint connected to your routed topology
def install_routes():
    return

# Ability to move traffic between the "north" path (R1,R2,R3) and the "south" path (R1,R4,R3) or vice versa
def swap_traffic_path():
    return

# Show the available commands that can be taken on the orchestrator.
def show_help():
    print("Create network topology with command:")
    print("-c setup")
    print("Startup OSPF daemons on topology:")
    print("-c startup ospf")
    print("Add endpoint routes")
    print("-c install routes")
    print("Move traffic path from the current route to the opposite route")
    print("-c swap path")
    return

input_string = input()
command_string = ""
print(input_string[3:])

if input_string == "-h":
    show_help()
elif input_string[0:2] == "-c":
    command_string = input_string[3:]
    if command_string == "setup":
        setup_network()
    elif command_string == "startup ospf":
        startup_ospf()
    elif command_string == "install routes":
        install_routes()
    elif command_string == "swap path":
        swap_traffic_path()
