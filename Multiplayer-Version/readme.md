# Multiplayer Version of Slither.io

## Introduction
Converting a single-player game into a multiplayer version requires careful planning and implementation
of a stable client server architecture and a proper two way communication between
a client and a server. The project aims to establish a central server , that acts as an intermediate
between two clients and essentially does the task of message forwarding between two clients. To
ensure a smooth game-play with lesser lag, the heavy lifting tasks such as collision detection of a
player with any food orbs or other player has been done in client side. However, it is generally a
better practice if this is done in the server side to prevent malicious clients from sending inaccurate
messages. This abstract outlines essential guidelines for developing a client server architecture to
convert the single player version to a multiplayer one. For efficient send/recieval of objects, it is picked into binary image. The size of this object is appended as a header, and the object is padded at the end.

## Server-Side Architecture
A broadcast function which sends a message to all clients connected.
At every instance, the server is required to send the following details :
– Braodcasting the removal of the orbs to all clients.
– The player snakes are to be sent as a list of player segments. For implementation purposes,
it is easier if even the head of the snake is included in the segment list, then we can directly
send the segment list. At the client side, it has to maintain the info of the other snakes
as dictionary otherplayerssegments of the form key : value where key is the player id and
value is a list of segments of that particular player.
–Broadcasting snake objects who have died to all the other clients

## Client Side Architecture
The client must send its coordinates at every instant, and information about eating a food particle
or death whenever needed.
• Client updates its food orbs list , and also delete the player who has died in its database
• Keeping the message in the form a tuple of 2 elements where the first element tells about the
type of message, and second element carries the message is convenient.
• Send Its current location, as well as key messages such as death updates on collision
