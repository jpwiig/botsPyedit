def respones(mssge: str) -> str:
    message = mssge.lower()

    if message == 'mus':
        return 'ehus'
    elif message == 'rick':
        return 'never gonna give you up, never gonna let you down'
    elif message == 'https://tenor.com/view/ruben-vareide-ruben-vareide-prebz-og-dennis-prebz-gif-26529878':
        return 'https://media1.tenor.com/images/c5d7235861884672feac3bc93f20d5da/tenor.gif?itemid=26839897'
    elif message == '!hva':
        return 'hjelpemelding din nørd'
    if message == 'faen' or message == 'fuck deg':
        return 'ikke bann!'
    else:
        return None
# return 'tulling'
