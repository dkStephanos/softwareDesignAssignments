//--------------udp fixed message length client main.cpp-----------------------------------------------------
//
//  Author:  Phil Pfeiffer
//  Date:    Fall 1999
//  Last modified:  April 2020
//
//  Illustrate operation of PISCES socket class library's support for UDP communications
//  This program's companion program is sample udp server main.cpp.
//
//   Design notes:
//   -.  servers must support same buffer size as the size that's hard-coded into this program
//       -.  suggested improvement: make buffer size a command-line parameter
//-----------------------------------------------------------------------------------------------------------

#include "udp_fixed_message_length_client.h"

#include <iostream>     // cin, cout, clog
#include <string>

#ifndef STD_H
#include "std.h"
#endif

#ifndef HOST_DATA_H
#include "host_data.h"    // TCP/IP host data class
#endif

#ifndef QUERY_CLIENT_H
#include "query_client.h"   // client query-response class
#endif

#ifndef DAYTIME_H
#include "daytime.h"    // time of day class
#endif

// *===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===
// definition of "introduce self" routine
// *===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===*===

void introductory_message(ostream& os)
{
    os << "Current time: " << /*replace*/daytimeClass() << endl << endl;

    os << "This program sends data to a server on a port of your choice." << endl
        << "You, the user, will first be asked to specify a server to contact," << endl
        << "  in the form of an IP address and a port number."
        << endl;

    os << "After any message, you will be allowed to stop communications " << endl
        << "with the current server, and stop the program. " << endl
        << endl;
}

int main(void)
{
    // *** *** maintain status variable for final exit code *** ***
       //
    const int GOOD_EXIT = 0;
    const int BAD_EXIT = 1;
    int final_status = GOOD_EXIT;    // assume all OK, for starters

    ostream& feedback_stream = clog;
    ostream& query_stream = cout;
    istream& response_stream = cin;

    const unsigned BUFFER_PAYLOAD_SIZE = 40;

    // *** *** advertise program's purpose, function *** ***
    //
    introductory_message(feedback_stream);

    try
    {
        //  *** instantiate object for dialoguing with user about stuff,
        //      including socket connection parameters
        //
        client_query_class query_object(response_stream, query_stream, feedback_stream);

        // *** display current host's name, IP address ***
        //
        //feedback_stream << endl << "current " << host_data_class() << endl;

        // *********************************************
        //   loop to communicate with multiple servers
        // *********************************************

        do
        {
            // ==== instantiate a socket for communications ====
            //
            //  must reinstantiate socket on every pass through loop:
            //  a WinSock socket, once closed, may not be reopened.
            //
            udp_fixed_message_length_client_class socket(BUFFER_PAYLOAD_SIZE);

            try
            {
                // *********************************************
                //   access one server
                // *********************************************

                // ==== ask user for port/IP adr access; connect to port ====
                //
                socket_service_access_point_class server_sap;
                query_object.get_access_point(server_sap);

                // **********************************
                //  loop to exchange multiple messages with server
                // **********************************

                do
                {
                    string client_message;
                    query_object.get_string("please enter string to send", client_message, query_class::newline_);
                    if (client_message.length() > BUFFER_PAYLOAD_SIZE)
                    {
                        feedback_stream << "?? message (" << client_message << ") exceeds maximum message (" << BUFFER_PAYLOAD_SIZE << ")" << endl;
                        continue;
                    }
                    socket.request(client_message, server_sap);

                    string server_reply;
                    socket_service_access_point_class respondant_sap;
                    socket.confirm(server_reply, respondant_sap);

                    if (server_sap != respondant_sap)
                        feedback_stream << "message from " << respondant_sap << ":";
                    else
                        feedback_stream << "reply: ";

                    feedback_stream << server_reply << endl;
                } while (query_object.yes_unless_n("continue session?"));
            }
            catch (const socket_exception& message)
            {
                feedback_stream << message << endl;
            }

            //  === end communications with current server ===

            socket.closesocket();
        } while (query_object.yes_unless_n("start another session?"));
    }
    catch (const basic_exception& message)
    {
        feedback_stream << message << endl;
        feedback_stream << "?? unexpected exception: program ending" << endl;
        final_status = BAD_EXIT;
    }
    catch (...)
    {
        feedback_stream << "?? unexpected exception: program ending" << endl;
        final_status = BAD_EXIT;
    }
    return final_status;
}