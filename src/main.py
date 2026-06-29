# This is a sample Python script that prints "Hello World" five times

if __name__ == "__main__":
    # This block will only execute if the script is run directly, not imported as a module.
    print("Script executed directly.")
variable = 5
if variable == 10:
    print(f"The variable is set to {variable}.")
    for i in range(5):
        print("Hello World")
else:
    print("The variable is not set.")
