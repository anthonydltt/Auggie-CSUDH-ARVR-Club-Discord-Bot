import discord
from discord import app_commands
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

def run_Auggie():
    TOKEN = '#########'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = commands.Bot(command_prefix = '!', intents=intents)


    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type = discord.ActivityType.listening, name= "the voices in my head"))
        print(f"Hello! I'm ready to go!")
        print("------------------------")

        try:
            synced = await client.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @client.event
    async def on_member_join(member):
       channel = client.get_channel('########')
       await channel.send("Welcome " + str(member) + "!")

    @client.tree.command(name="hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.mention}! I\'m Auggie!")
    
    @client.tree.command(name="events")
    async def events(interaction: discord.Interaction):
        events = discord.Embed(title= "Next Event!", url= "https://torolink.csudh.edu/organization/csudh-ar-vr-club", description="Our next workshop is on October 12th, 2023!\nApple Engineer soandso will be joining us! RSVP TODAY on toroLink.", color=0xB7ADCF)
        events.set_author(name="Events", icon_url="https://i.imgur.com/mT6h5Mi.jpeg")
        events.set_thumbnail(url="https://cdn.discordapp.com/attachments/1121156264269983887/1158520610247422102/D8C9D567-ED65-4C56-980D-784AD9D4DD2BDark_Blue_and_Oranye_Geometric_Podcast_Special_Guest_Star_Instagram_Post.jpg?ex=651c8be5&is=651b3a65&hm=1d119aaabcdb77593bfe7f9f1d8a4a294a332c70d5d51434172e50757ee1ddde&")
        events.set_footer(text="Hope to see you there!!")
        await interaction.response.send_message(embed=events)

    @client.tree.command(name="instagram")
    async def instagram(interaction: discord.Interaction):
        instagram = discord.Embed(title = "AR/VR Club Instagram", url="https://instagram.com/csudh_arvr_club?igshid=MzRlODBiNWFlZA==", description="Click the link above to follow our Instgram!", color= 0xB7ADCF)
        instagram.set_author(name="Instagram", icon_url="https://i.imgur.com/mT6h5Mi.jpeg")
        instagram.set_thumbnail(url="https://brandlogos.net/wp-content/uploads/2022/05/instagram-2022-logo_brandlogos.net_kamyn.png")
        instagram.set_footer(text="Thank you for following!")
        await interaction.response.send_message(embed=instagram)
    
    @client.tree.command(name="torolink")
    async def torolink(interaction: discord.Interaction):
        torolink = discord.Embed(title = "AR/VR Club Toro Link", url="https://torolink.csudh.edu/organization/csudh-ar-vr-club", description="Click the link above to visit our Toro Link page!", color= 0xB7ADCF)
        torolink.set_author(name="Toro Link", icon_url="https://i.imgur.com/mT6h5Mi.jpeg")
        torolink.set_thumbnail(url="https://i.imgur.com/mT6h5Mi.jpeg")
        torolink.set_footer(text="Hope to see you at our events!")
        await interaction.response.send_message(embed=torolink)


    client.run(TOKEN)