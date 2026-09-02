#recursive:
def generate_binary_strings(n):
    result = []

    def backtrack(current):

        # Base case
        if len(current) == n:
            result.append(current)
            return

        # Choice 1: Add 0
        backtrack(current + "0")

        # Choice 2: Add 1 (only if valid)
        if not current or current[-1] != "1":
            backtrack(current + "1")

    backtrack("")

    return result

#iterative
def generate_binary_strings1(n):
    result = [""]

    for _ in range(n):
        new_result = []

        for s in result:

            # We can always add 0
            new_result.append(s + "0")

            # We can add 1 only if previous char isn't 1
            if not s or s[-1] != "1":
                new_result.append(s + "1")

        result = new_result

    return result