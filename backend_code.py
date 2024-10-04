import scratchattach as scratch3
import time

# Scratch username and project ID

PROJECT_ID = "1062488848"                                             # Replace with your Scratch project's ID
SCRATCH_USERNAME = "Scratchography"                                   # Your Scratch username
SCRATCH_PASSWORD = "bennet"                                           # Your new Scratch password
SSI = ".eJxVj0FPhDAUhP8LZxfbsqVlb-tuNDGeMMYjeW1fobK0CGWNGv-7JeGy1_nmzZv5zZYZJw8DZofsVU8QdRfaCcbuO7vLYujRJyCpMKqwRSWk2HOKkhMrKkqs4kwTTQ4qwq4-lf1yfQx0MadnOL-9qM_66V2nmEtond-5MSUJntOyyqnMKU-kgSV2zVqhcSZhWnBGmGAkMfMBvg1NdAP-BL_2Ow44OQ33Z_RXnG7PO5i7ZGElR0MVcFlZZq1EQo2RRBVEFsDMvhJAjSiLdRzOUYfQuzX6K0w9mttIBTrNX2utGvqYfkcXfL6BOa9xvGziw2b--wflam0x:1swonG:krCDI4oVNLkDk7QnN3JSd5L0dpg"



session = scratch3.Session(SSI, username=SCRATCH_USERNAME) #replace with your session_id and username
conn = session.connect_cloud(PROJECT_ID) #replace with your project id

client = scratch3.CloudRequests(conn)

@client.request
def ping(): #called when client receives request
    print("Ping request received")
    return "pong" #sends back 'pong' to the Scratch project

@client.event
def on_ready():
    print("Request handler is running")

@client.request
def foo(argument1):
    print(f"Data requested for user {argument1}")
    user = scratch3.get_user(argument1)
    stats = user.stats()

    return_data = []
    return_data.append(f"Total loves: {stats['loves']}")
    return_data.append(f"Total favorites: {stats['favorites']}")
    return_data.append(f"Total views: {stats['views']}")

    return return_data

client.run() #make sure this is ALWAYS at the bottom of your Python file
