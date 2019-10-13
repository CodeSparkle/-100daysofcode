Echo client-server program.

This is a program that runs an echo server or a client, depending on the command-line arguments:
    * client - Runs the client.
    * server - Runs the server.

the code uses four libraries:
    * msvcrt    - Get the keystrokes
    * socket    - Create the connections and send/recieve messages
    * sys       - Get the command-line arguments
    * threading - Create more threads