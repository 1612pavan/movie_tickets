
import sys
import mini_project as bt



arg1 = sys.argv[1] # [file_name, arg1, arg2]

if len(sys.argv) >= 3:
    arg2 = sys.argv[2]

if arg1 == "movie" and arg2 == "list":
    bt.get_movie_list()

elif arg1 == "book":
    # Book Ticket for Specific Movie
    no_of_tickets = int(input("No of tickets: "))
    bk_name = input("Booking Name: ")
    bt.get_ticket(arg2, no_of_tickets, bk_name)

elif arg1 == "--help":
    # Show help menu
    print("-------------Help Menu---------------\nCommands:")
    print("1. movie list")
    print("2. book {movie_name}")
    print("----------------------------")
