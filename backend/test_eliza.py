import eliza

Eliza=eliza.Eliza()
Eliza.load('doctor.txt')
print(Eliza.initial())
while True:
	user_response=input('>')
	if user_response == 'Bye':
		break
	print(Eliza.respond(user_response))

