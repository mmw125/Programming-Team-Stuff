if __name__ == "__main__":
    num_votes = input()
    votes = {}
    for vote_num in range(int(num_votes)):
        vote = input()
        votes[vote] = votes[vote] + 1 if vote in votes else 1
    highest = 0
    values = []
    for key in votes:
        num_votes = votes[key]
        if num_votes > highest:
            highest = num_votes
            values = []
        if num_votes == highest:
            values.append(key)
    values = sorted(values)
    for key in values:
        print(key)