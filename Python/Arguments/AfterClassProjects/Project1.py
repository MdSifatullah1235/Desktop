def shutdown(inp):

    if inp == "yes" or "Yes":
        return "Shutting down...."
    
    elif inp == "no" or "No":
        return "Aborting shut down..."
    
    else:
        print("Sorry")

inpu = str(input("Enter yes or no to shutdown:"))

print(shutdown(inpu))