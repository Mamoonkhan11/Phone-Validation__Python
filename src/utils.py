# Helper function for saving return function
def save_to_file(info, filename="results.txt"):
    with open(filename, "a") as f:
        f.write(str(info) + "\n")
