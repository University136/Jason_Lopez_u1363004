# Author: Jason Lopez
# Class: CS4480
# Assignment: PA3 Orchestrator
# Date: 4/20/25
import subprocess


# Construct the network topology
def setup_network():
    # setup files that will be needed to be called later.
    subprocess.call(["chmod", "+x", "frrsetup"])
    subprocess.call(["chmod", "+x", "frrrestart"])
    subprocess.call(["chmod", "+x", "daemons"])

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
    print("Starting ospf")
    # Calls service frr restart on each router container as the appropriate configures are already in place.
    subprocess.call(["sudo", "docker", "exec", "-it", "u1363004docker-r1-1", "service", "frr", "restart"])
    subprocess.call(["sudo", "docker", "exec", "-it", "u1363004docker-r2-1", "service", "frr", "restart"])
    subprocess.call(["sudo", "docker", "exec", "-it", "u1363004docker-r3-1", "service", "frr", "restart"])
    subprocess.call(["sudo", "docker", "exec", "-it", "u1363004docker-r4-1", "service", "frr", "restart"])
    return

# Install routes on each host/endpoint connected to your routed topology
def install_routes():
    print("installing route ha to hb")
    subprocess.call(["sudo", "docker", "exec", "-it", "u1363004docker-ha-1", "route", "add", "-net",
                     "10.0.15.0/24", "gw", "10.0.14.4"])
    print("installing route hb to ha")
    subprocess.call(["sudo", "docker", "exec", "-it", "u1363004docker-hb-1", "route", "add", "-net",
                     "10.0.14.0/24", "gw", "10.0.15.4"])
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
