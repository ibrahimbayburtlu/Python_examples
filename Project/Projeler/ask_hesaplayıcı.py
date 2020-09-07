Your_name=input("What is your name?:")
Your_friend=input("What is your friend's name?:")
love=len(Your_name)+len(Your_friend)

if len(Your_name)>len(Your_friend):
    love-=5
else:
    love+=3

love*=42
love=love/(100+len(Your_friend))

love =10 if love>10 else round(love,0)
print("{} and {} score is {} out of 10".format(Your_name, Your_friend, love))