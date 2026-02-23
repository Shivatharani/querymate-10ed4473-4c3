def display_events(events):
    print("\n--- Available Events ---")
    if not events:
        print("No events currently available.")
        return

    for i, event in enumerate(events):
        print(f"{i + 1}. {event['name']} - Date: {event['date']} - Time: {event['time']} - Price: ${event['price']:.2f} - Available Tickets: {event['available_tickets']}")
    print("-------------------------")

def book_tickets(events, bookings):
    display_events(events)
    if not events:
        return

    try:
        event_choice = int(input("Enter the number of the event you want to book: ")) - 1
        if not (0 <= event_choice < len(events)):
            print("Invalid event choice.")
            return

        selected_event = events[event_choice]

        num_tickets = int(input(f"How many tickets do you want for '{selected_event['name']}'? "))
        if num_tickets <= 0:
            print("Number of tickets must be positive.")
            return

        if num_tickets > selected_event['available_tickets']:
            print(f"Sorry, only {selected_event['available_tickets']} tickets are available for this event.")
            return

        total_cost = num_tickets * selected_event['price']
        print(f"Total cost for {num_tickets} tickets: ${total_cost:.2f}")

        confirm = input("Confirm booking (yes/no): ").lower()
        if confirm == 'yes':
            selected_event['available_tickets'] -= num_tickets
            booking_id = len(bookings) + 1
            bookings.append({
                'id': booking_id,
                'event_name': selected_event['name'],
                'num_tickets': num_tickets,
                'total_cost': total_cost
            })
            print(f"Booking successful! Your booking ID is {booking_id}.")
        else:
            print("Booking cancelled.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_bookings(bookings):
    print("\n--- Your Bookings ---")
    if not bookings:
        print("No bookings found.")
        return

    for booking in bookings:
        print(f"Booking ID: {booking['id']} - Event: {booking['event_name']} - Tickets: {booking['num_tickets']} - Total Cost: ${booking['total_cost']:.2f}")
    print("---------------------")

def main():
    events = [
        {'name': 'Concert in the Park', 'date': '2026-03-15', 'time': '19:00', 'price': 50.00, 'available_tickets': 100},
        {'name': 'Comedy Night Live', 'date': '2026-03-20', 'time': '20:30', 'price': 35.50, 'available_tickets': 75},
        {'name': 'Theater Play: The Great Adventure', 'date': '2026-04-01', 'time': '18:00', 'price': 60.00, 'available_tickets': 120}
    ]

    bookings = []

    while True:
        print("\n--- Ticket Booking App ---")
        print("1. View Available Events")
        print("2. Book Tickets")
        print("3. View My Bookings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_events(events)
        elif choice == '2':
            book_tickets(events, bookings)
        elif choice == '3':
            view_bookings(bookings)
        elif choice == '4':
            print("Thank you for using the Ticket Booking App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()