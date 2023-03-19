import discord
from discord.ext import commands, tasks
import os
import psutil
import time

# Defina o caminho do jogo e o nome do jogo
game_path = "C:/Program Files (x86)/Steam/steamapps/common/Dead by Daylight/"
game_name = "DeadByDaylight.exe"

# Defina o ID do canal para onde as notificações serão enviadas
canal_id = 1086971274829508739

# Cria um bot com o prefixo "!"
bot = commands.Bot(command_prefix='!')

# Cria a task para verificar o status do jogo
@tasks.loop(seconds=5.0)
async def check_game_status():
    # Verifica se o jogo está em execução
    for proc in psutil.process_iter():
        try:
            if proc.name() == game_name and game_path in proc.exe():
                # Envia uma mensagem para o canal especificado se o jogo estiver sendo executado
                canal = bot.get_channel(canal_id)
                await canal.send("O jogo está em execução!")
                return
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass

# Evento que é executado quando o bot está pronto
@bot.event
async def on_ready():
    print("Bot online")

    # Inicia a task de verificação do status do jogo
    check_game_status.start()

# Roda o bot
bot.run(os.getenv('MTA4Njk0NjkxNTI0NzIxMDUzNw.Gk9fnZ.DDOoMTRd-FhHeyKbxsTHKNRplniDVl2crzmgMY'))



