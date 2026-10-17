command = "delete"

match command:
    case "add":
        print("Adding a new item")

    case "delete":
        print("Deleting an item")

    case "update":
        print("Updating an item")

    case "view":
        print("Showing items")

    case _:
        print("Unknown command")