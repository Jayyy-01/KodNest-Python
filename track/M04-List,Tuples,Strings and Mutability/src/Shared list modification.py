original_scores = []

for _ in range(3):
    original_scores.append(int(input()))

alias_scores = original_scores

replacement_score = int(input())
additional_score = int(input())

alias_scores[0] = replacement_score
alias_scores.append(additional_score)

print(f"Original: {original_scores}")
print(f"Alias: {alias_scores}")
print(f"Shared Object: {original_scores is alias_scores}")

#summary is if modification is done in alias_scores then the modification will be reflected in original_scores. 