from MojangAPI import Client
import asyncio
import os

slim_model = True
name = input("Target to get the Skin URL from: ")

async def main():
    user = await Client.User.createUser(name)
    profile = await user.getProfile()
    print(profile.skin)
    os.system('pause')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print("Now you can copy the link above and change your skin!")
print("")
skin_url = input("Skin URL: ")
target = input("Name of your account: ")
email = input("Email: ")
password = input("Password: ")

async def main():
    user = await Client.User.createUser(target)
    await user.authenticate(email, password)
    await user.changeSkin(skin_url, slim_model) # Change skin_url to your skin URL and remove the skin_url input above if you want so you dont have to put it in everytime! (If you want to add it to your sniper)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("[SUCCESS] Skin successfully changed!")
os.system('pause')
