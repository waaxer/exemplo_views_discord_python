#Exemplo com arquivo do comando separarado das views.

###########################  Código do arquivo do comando:  ###########################
import discord
from discord import app_commands
from discord import Interaction
from discord.ext import commands

#Importar o local de onde está o arquivo com as views
#from Functions.SlashCommands.teste.views import ViewExemplo

class ComandoExemplo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cog = __class__.__name__

    def cog_load(self):
        print(f"Comando: {self.cog} foi carregado!")

    @app_commands.command(name="teste", description="teste")
    @app_commands.guild_only
    async def nome_comando(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="Olá", view=ViewExemplo())
        

async def setup(bot):
    await bot.add_cog(ComandoExemplo(bot))
    
###########################  Código do arquivo da view com botões ou selects:  ###########################
import discord
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import ui

class ViewExemplo(discord.ui.View):

    @discord.ui.select(
        placeholder="What is your age?",
        options=[
            discord.SelectOption(label="16 - 17", value="16"),
            discord.SelectOption(label="18 - 23", value="18"),
            discord.SelectOption(label="24 - 30", value="24")
        ]        
    )
    async def func_menu_1(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        #print(select_item.values) para saber o valor do item do menu que o usuário clicou
        await interaction.response.edit_message(content="editada pelo menu")
        
    @discord.ui.button(
        label='Label botão 1',
        style=discord.ButtonStyle.green,
        emoji='⏰'
    )
    async def func_botao_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="editada pelo botão")
