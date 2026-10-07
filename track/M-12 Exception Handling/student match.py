match = input()
req = input()
try:
    match = int(match)
    req = int(req)
    match_per = (match / req) * 100
    print(f"match: {match_per}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Required skills cannot be zero")
else:
    print(f"Match percentage: {match_per}")
finally:
    print("Match processing completed")
