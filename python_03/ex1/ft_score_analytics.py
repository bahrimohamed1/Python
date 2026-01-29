import sys

print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No scores provided. Usage: "
          "python3 ft_score_analytics.py <score1> <score2> ...")
    exit()
args: list = []
for arg in sys.argv[1:]:
    try:
        args.append(int(arg))
    except ValueError:
        print(arg,"is not a valid score!")
if len(args) == 0:
    print("No valid arguments to process!")
    exit()
print("Scores processed:", args)
print("Total players:", len(args))
print("Total score:", sum(args))
avg_score = sum(args) / len(args)
print("Average score:", avg_score)
print("High score:", max(args))
print("Low score:", min(args))
print("Score range:", max(args) - min(args))
