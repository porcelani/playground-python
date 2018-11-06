from argparse import ArgumentParser

parser = ArgumentParser(prog="hungry")
parser.add_argument("type", type=str, choices=["view", "message"])
parser.add_argument("-id", "--user_id", type=int)
parser.add_argument("-e", "--email", type=str)

args = parser.parse_args()
print ("Hello World")
if args.type == "view":
    print (args.user_id)
    print (args.email)
