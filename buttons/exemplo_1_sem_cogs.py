#View para adicionar 1 botão ou mais.

class ExemploView(discord.ui.View):
    
    @discord.ui.button(label='Label botão 1', style=discord.ButtonStyle.green, emoji='⏰')
    async def func_botao_1(self, interaction: discord.Interaction, button: discord.ui.Button):

       #..........

    @discord.ui.button(label='Label botão 2', style=discord.ButtonStyle.blurple, emoji='🏁')
    async def func_botao_2(self, interaction: discord.Interaction, button: discord.ui.Button):

       #..........
        
        
#Adicionar View ao comando usando tree de comandos:

@bot.tree.command(name="nome_comando", description="descrição comando"))
async def func_comando(interaction: discord.Interaction):

    await interaction.response.send_message("Mensagem exemplo", view=ExemploView())
        
