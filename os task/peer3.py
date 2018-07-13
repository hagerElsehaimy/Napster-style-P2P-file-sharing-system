from peer import client_server

if __name__ == "__main__":
    port_number=41568
    client=client_server(port_number)

    while True:
        print "Enter one of these numbers to get corresponding service: "
        print "1 upload file"
        print "2 Search File On Server"
        print "3 Connect With another client"
        print "4 Disconnect"
        number = raw_input()

        # print file uploaded successfully if register function returns a true value which means peer registered
        if (number == "1"):
            file_name = raw_input("Enter File Name: ")
            if (client.register(file_name)):
                print "file uploaded successfully"
            else:
                print "file unavailable"

                # calls function of search
        if (number == "2"):
            file_name = raw_input("Enter file Name: ")
            peers = client.search(file_name)

            if (len(peers) == 0):
                print "Error 404 File not found"
            else:
                print "this port have the file that you wanted", peers
                # request a peer connection
        if (number == "3"):
            port = raw_input("Enter peer's ID you want to connect to ")
            if (port != "21568" and port != "31568" and port != "41568"):
                print "unavailable peer"

            # in case of correct entry of port number or peer id
            else:
                client.runServer(int(port))
                while True:
                    print "1 download file"
                    print "2 exit"
                    selection_input = raw_input()
                    if (selection_input == "1"):
                        file_name = raw_input("Enter File Name: ")

                        if (client.download(file_name)):
                            print "File Downloaded!"
                        else:
                            print "this client doesn't own this file"
                    elif (selection_input == "2"):
                        break
                    else:
                        print "enter valid number"
        if (number == "4"):
            print "user with id =", port_number, "disconnected from server"
            break
        else:
            print "enter a valid number"