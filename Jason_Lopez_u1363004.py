# Author: Jason Lopez
# Class: CS4480
# Assignment: PA3 Orchestrator
# Date: 4/22/25
import subprocess
import sys


# Construct the network topology
def setup_network():
    # setup files that will be needed to be called later.
    subprocess.call(["chmod", "+x", "frrsetup"])
    subprocess.call(["chmod", "+x", "ospfraise"])
    subprocess.call(["chmod", "+x", "ospflower"])

    print("Setting up network")
    ans = subprocess.call(["sudo", "docker", "compose", "up", "-d"])

    if ans == 0:
        print("Topology setup finished")
    else:
        print("Topology setup failed")

    return

# Startup the OSPF daemons, with appropriate configurations, in the routers.
def startup_ospf():
    print("Starting ospf")
    # Calls service frr restart on each router container as the appropriate configures are already in place.
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r1-1", "service", "frr", "restart"])
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r2-1", "service", "frr", "restart"])
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r3-1", "service", "frr", "restart"])
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r4-1", "service", "frr", "restart"])
    return

# Install routes on each host/endpoint connected to your routed topology
def install_routes():
    print("installing route ha to hb")
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-ha-1", "route", "add", "-net",
                     "10.0.15.0/24", "gw", "10.0.14.4"])
    print("installing route hb to ha")
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-hb-1", "route", "add", "-net",
                     "10.0.14.0/24", "gw", "10.0.15.4"])
    return

# Ability to move traffic between the "north" path (R1,R2,R3) and the "south" path (R1,R4,R3) or vice versa
def swap_traffic_north():
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r2-1", "bash", "/root/ospflower"])
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r4-1", "bash", "/root/ospfraise"])
    return

def swap_traffic_south():
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r2-1", "bash", "/root/ospfraise"])
    subprocess.call(["sudo", "docker", "exec", "-it", "jason_lopez_u1363004-r4-1", "bash", "/root/ospflower"])
    return

# Show the available commands that can be taken on the orchestrator.
def show_help():
    print("Create network topology with command:")
    print("-c setup")
    print("Startup OSPF daemons on topology:")
    print("-c startup ospf")
    print("Add endpoint routes:")
    print("-c install routes")
    print("Move traffic path from the current route to the north route:")
    print("-c swap path north")
    print("Move traffic path from the current route to the south route:")
    print("-c swap path south")
    return

total_args = len(sys.argv)

if total_args > 1:
    #input_string = input()
    input_string = sys.argv[1]
    command_string = ""

    if input_string == "-h":
        show_help()
    elif input_string == "-c":
        command_string = sys.argv[2]
        if command_string == "setup":
            setup_network()
        elif command_string == "startup":
            startup_ospf()
        elif command_string == "install":
            install_routes()
        elif command_string == "swap" and sys.argv[4] == "north":
            swap_traffic_north()
        elif command_string == "swap" and sys.argv[4] == "south":
            swap_traffic_south()
