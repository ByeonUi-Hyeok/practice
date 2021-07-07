import funcvote as vote

votes = input("투표내용 >>>")
# print(votes)
# print(type(votes))

result = vote.str2int(votes)

print(vote.countvotes(result))
result = vote.countvotes(result)

vote.printvote(result)