#JOIN COMMAND
""" @client.command(pass_context=True, aliases=['j'],help="If you want to talk to Babu")
async def join(ctx):
    global voice
    channel=ctx.message.author.voice.channel
    voice= get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice= await channel.connect()
    await voice.disconnect() 

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice= await channel.connect()
        print(f"Babu has connected to {channel} \n")

        await ctx.send(f"Joined {channel}")
"""

#LEAVE COMMAND
"""@client.command(pass_context=True, aliases=['f'],help="Make Babu leave voice channel")
async def leave(ctx):
    channel=ctx.message.author.voice.channel
    voice= get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"Babu has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Babu was said to leave voice channel, but was not in one")
        await ctx.send("Bhai main voice channel me nahi hu!") """


#PLAY COMMAND
""" @client.command(pass_context=True, aliases=['p'],help="To play music (this feature is still under progress)")
async def play(ctx,url: str):
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q=length-1
            try:
                first_file=os.listdir(DIR)[0]
            except :
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location=os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue")+"\\"+first_file)
            if length!=0:
                print("Songs done, playing next Queued \n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path,main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file,'song.mp3')
                voice.play(discord.FFmpegPCMAudio("songs.mp3"), after=lambda e: check_queue())
                voice.source= discord.PCMVolumeTransformer(voice.source)
                voice.source.volume= 0.07
            else:
                queues.clear()
                return
        else:
            queues.clear()
            print("No songs were queued before the ending of the last song \n")
            

    song_there=os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return
    Queue_infile=os.path.isdir("./Queue")
    try:
        Queue_folder="./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients,guild=ctx.guild)

    ydl_opts={
        'format':'bestaudio/best',
        'quiet':True,
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'prefferedcodec':'mp3',
            'prefferedquality':'192'
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now \n")
        ydl.download([url])
    
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name=file
            print(f"Renamed File: {file} \n")
            os.rename(file,"song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("songs.mp3"),after=lambda e:check_queue())
    voice.source=discord.PCMVolumeTransformer(voice.source)
    voice.source.volume=0.07

    nname = name.rsplit("-",2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")
"""

#PAUSE COMMAND
"""@client.command(pass_context=True,aliases=['pa','pau'],help="Pause the song being played")
async def pause(ctx):
    voice = get(client.voice_clients,guild=ctx.guild)
    
    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing, failed pause")
"""

#RESUME COMMAND

"""@client.command(pass_context=True,aliased=['r','res'],help="Resume music")
async def resume(ctx):

    voice =get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")
"""
#SKIP COMMAND
"""@client.command(pass_context=True,aliases=['s','ski'],help="Skip current track")
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_palying():
        print("Music skipped")
        voice.stop()
        await ctx.send("Music skipped")
    else:
        print("No music playing failed to skip")
        await ctx.send("No music playing failed to skip")
"""

#Making a list named "queues" queues={}

#QUEUE COMMAND
"""@client.command(pass_context=True,aliases=['q','que'],help="Queue music")
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num=len(os.listdir(DIR))
    q_num+=1
    add_queue=True
    while add_queue:
        if q_num in queues:
            q_num +=1
        else:
            add_queue = False
            queues[q_num]=q_num
    
    queue_path = os.path.abspath(os.path.realpath("Queue"+f"\song{q_num}.%(ext)s"))

    ydl_opts={
        'format':'bestaudio/best',
        'quiet':True,
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'prefferedcodec':'mp3',
            'prefferedquality':'192'
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now \n")
        ydl.download([url])
    await ctx.send("Adding song "+str(q_num) + "to the queue")

    print("Song added to the queue \n")
    """
#END
