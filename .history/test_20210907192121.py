from pytryfi import PyTryFi

username = "adrianj98@gmail.com"
password = "Twitchy@2f"

tryfi = PyTryFi(username, password)
print(tryfi)


tryfi.updatePets()
print(tryfi.pets)

tryfi.pets[0].updateStats(tryfi.session)