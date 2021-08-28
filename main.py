import os
import asyncio
import discord as d
from discord.ext import commands
from discord.utils import get
import random
from datetime import date
from urllib.request import Request, urlopen
import json

skill = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
skills = ['combat','mining', 'smithing', 'woodcutting', 'crafting', 'fishing', 'cooking','total']

guilds_combat = {}
guilds_mining = {}
guilds_smithing = {}
guilds_woodcutting = {}
guilds_crafting = {}
guilds_fishing = {}
guilds_cooking = {}

guilds_counter  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                    'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                    'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                    'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                    'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                    'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                    'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                    0, 'ST': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                    'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                    'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                    'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                    'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                    'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                    'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                    'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                    'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                    'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                    'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                    'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                    'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                    'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                    'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                    'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                    'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                    'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                    'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                    'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                    'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_total  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                        0, 'ST': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_int  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                        0, 'ST': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

def DictToList (dictio,listo):
    listo.clear()
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        listo.append(test)

def DictToList_alt (dictio):
    temporal = []
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        temporal.append(test)
    return temporal

def ResetDict(diction):
    diction = diction.fromkeys(diction, 0)
    return diction

def SortDict (di):
    temp = {}
    temp.clear()
    temp = {k: v for k, v in sorted(di.items(), key=lambda item: item[1],reverse=True)}
    return temp

def rankk (rank):
    rank_text = "rank#"+str(rank)
    return rank_text

def search(skill_name):
    list_guilds_stred = []
    
    d_test = ResetDict(guilds_counter_int)
    for k in range(0,49):  
        url='https://www.curseofaros.com/highscores'
        headers = {'User-Agent': 'Mozilla/5.0'}        
        request = Request(url+skill_name+'.json?p='+str(k), headers=headers)
        html = urlopen(request).read()       
        data = html.decode("utf-8")        
        fdata = json.loads(data)
        for i in range(0,20): 
            #check names get rank
            player_name = fdata[i]["name"]
            xp = fdata[i]["xp"]
            tag = player_name.split()[0]
            tag = tag.upper()
            
            if tag in d_test :
                d_test[tag] += xp
            elif "Immortal" in player_name :
                d_test["IMMORTAL"] += xp
            else :                
                continue
        
    temp_guilds = {k: v for k, v in sorted(d_test.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_guilds,list_guilds_stred)
    
    mini_list = []
    for i in range(len(list_guilds_stred)):
        mini_list.append(list_guilds_stred[i])
    list_guilds_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    return mini_list
  
def searchtag(skill_name,guildtag):
    members_sorted = []
    guildreg = {}
    
    for k in range(0,49):  
        url='https://www.curseofaros.com/highscores'
        headers = {'User-Agent': 'Mozilla/5.0'}        
        request = Request(url+skill_name+'.json?p='+str(k), headers=headers)
        html = urlopen(request).read()       
        data = html.decode("utf-8")        
        fdata = json.loads(data)
        for i in range(0,20): 
            #check names get rank
            player_rank = 20 * k + i + 1
            player_name = fdata[i]["name"]
            xp = fdata[i]["xp"]
            tag = player_name.split()[0]
            tag = tag.upper()
            
            if tag == guildtag.upper():
                if player_name in guildreg :
                    continue
                else:
                    guildreg[player_name]=xp
                    continue
        
    temp_dic = {k: v for k, v in sorted(guildreg.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_dic,members_sorted)
    
    mini_list = []
    for i in range(len(members_sorted)):
        mini_list.append(members_sorted[i])
    members_sorted.clear()
    temp_dic = {}
    return mini_list  

def searchTotal():
    list_guilds_total_stred = []
    dd_test = ResetDict(guilds_counter_int)
    for m in range(0,7):
        for k in range(0,49):  
            url='https://www.curseofaros.com/highscores'
            headers = {'User-Agent': 'Mozilla/5.0'}        
            request = Request(url+skill[m]+'.json?p='+str(k), headers=headers)
            html = urlopen(request).read()       
            data = html.decode("utf-8")        
            fdata = json.loads(data)
            for i in range(0,20): 
                #check names get rank
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                
                if tag in dd_test :
                    dd_test[tag] += xp
                elif "Immortal" in player_name :
                    dd_test["IMMORTAL"] += xp
                else :                
                    continue
            
    temp_guilds = {k: v for k, v in sorted(dd_test.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_guilds,list_guilds_total_stred)
        
    mini_list = []
    for i in range(list_guilds_total_stred):
            mini_list.append(list_guilds_total_stred[i])
    list_guilds_total_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    return mini_list



def LeaderBoard():
    all_xp = ResetDict(guilds_counter_int)
    skill_0 = ResetDict(guilds_counter_int)
    skill_1 = ResetDict(guilds_counter_int)
    skill_2 = ResetDict(guilds_counter_int)
    skill_3 = ResetDict(guilds_counter_int)
    skill_4 = ResetDict(guilds_counter_int)
    skill_5 = ResetDict(guilds_counter_int)
    skill_6 = ResetDict(guilds_counter_int)
    skills_dict_list = [skill_0,skill_1,skill_2,skill_3,skill_4,skill_5,skill_6,all_xp]

    list_empty = []
    list_empty.clear()
    list_0 = list_empty
    list_1 = list_empty
    list_2 = list_empty
    list_3 = list_empty
    list_4 = list_empty
    list_5 = list_empty
    list_6 = list_empty
    list_all = list_empty
    list_lists = [list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_all ]
    
    for m in range(0,7):
        for k in range(0,49):  
            url='https://www.curseofaros.com/highscores'
            headers = {'User-Agent': 'Mozilla/5.0'}        
            request = Request(url+skill[m]+'.json?p='+str(k), headers=headers)
            html = urlopen(request).read()       
            data = html.decode("utf-8")        
            fdata = json.loads(data)
            for i in range(0,20): 
                #check names get rank
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                n = player_name.lower()
                
                if tag in skills_dict_list[m] :
                    skills_dict_list[m][tag] += xp
                    all_xp[tag] += xp
                elif "immortal" in n :
                    skills_dict_list[m]["IMMORTAL"] += xp
                    all_xp["IMMORTAL"] += xp
                else :                
                    continue
    for j in range(0,8):
        tempo = SortDict(skills_dict_list[j])
        #skills_dict_list[m] = tempo
        list_lists[j] = DictToList_alt(tempo)
        tempo.clear()
            
    return list_lists

############################################################################

client = d.Client()
client = commands.Bot(command_prefix='!')
@client.event
async def on_ready():
    print('2nd logging in as {0.user}'.format(client))
    await client.change_presence(activity=d.Activity(type=d.ActivityType.playing, name="Dumb Tests"))

#@client.event
#async def on_message(ctx):
#    username = str(ctx.author).split('#')[0]
#    user_message = str(ctx.content)
#    channel = str(ctx.channel)
#    print(f'{username}: {user_message} ({channel})')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def hello(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Hello {username}!")

@client.command()
async def wussup(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Nothing much, hbu {username} ?")

@client.command()
async def bye(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"See you later {username}!")

@client.command()
async def bestguild(ctx):
    await ctx.send(f"OwO Numba Wan !")

@client.command()
async def RandomNumber(ctx,user_number):
    await ctx.send(f'{random.randrange(int(user_number))}')

@client.command(name='dc',aliases=['disconnect','logout'])
async def dc(ctx):
    await client.logout()

@client.command()
async def today(ctx):
    d1 = date.today().strftime("%d/%m/%Y")
    await ctx.send(f'Today is : {d1}')


@client.command(name='combat',aliases=['melee','sw'])
async def combat(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Combat Data ... ")
    test_list_1 = search("")
    embedVar1 = d.Embed(title="Top Guilds: Combat", color=0x669999)
    for i in range(int(rank)):
        embedVar1.add_field(name=rankk(i+1), value= test_list_1[i] , inline=False)
    await ctx.send(embed=embedVar1)
    test_list_1.clear()

@client.command(name='mining',aliases=['mine','rocky','pick'])
async def mining(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Mining Data ... ")
        test_list_2 = search("-mining")
        embedVar2 = d.Embed(title="Top Guilds: Mining", color=0x333300)
        for i in range(int(rank)):
            embedVar2.add_field(name=rankk(i+1), value= test_list_2[i] , inline=False)
        await ctx.send(embed=embedVar2)
        test_list_2.clear()

@client.command(name='smithing',aliases=['smith','ember','hammer','kreiger'])
async def smithing(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Smithing Data ... ")
        test_list_3 = search("-smithing")
        embedVar3 = d.Embed(title="Top Guilds: Smithing", color=0xff0000)
        for i in range(int(rank)):
            embedVar3.add_field(name=rankk(i+1), value= test_list_3[i] , inline=False)
        await ctx.send(embed=embedVar3)
        test_list_3.clear()

@client.command(name='woodcutting',aliases=['wc','pecker','axe','matt'])
async def woodcutting(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Woodcutting Data ... ")
        test_list_4 = search("-woodcutting")
        embedVar4 = d.Embed(title="Top Guilds: Woodcutting", color=0x00cc00)
        for i in range(int(rank)):
            embedVar4.add_field(name=rankk(i+1), value= test_list_4[i] , inline=False)
        await ctx.send(embed=embedVar4)
        test_list_4.clear()

@client.command(name='crafting',aliases=['craft','woody','yekzer'])
async def crafting(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Crafting Data ... ")
        test_list_5 = search("-crafting")
        embedVar5 = d.Embed(title="Top Guilds: Crafting", color=0x996633)
        for i in range(int(rank)):
            embedVar5.add_field(name=rankk(i+1), value= test_list_5[i] , inline=False)
        await ctx.send(embed=embedVar5)
        test_list_5.clear()

@client.command(name='fishing',aliases=['fish','tantrid','tant'])
async def fishing(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Fishing Data ... ")
        test_list_6 = search("-fishing")
        embedVar6 = d.Embed(title="Top Guilds: Fishing", color=0x0066ff)
        for i in range(int(rank)):
            embedVar6.add_field(name=rankk(i+1), value= test_list_6[i] , inline=False)
        await ctx.send(embed=embedVar6)
        test_list_6.clear()

@client.command(name='cooking',aliases=['cook','food'])
async def cooking(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Cooking Data ... ")
        test_list_7 = search("-cooking")
        embedVar7 = d.Embed(title="Top Guilds: Cooking", color=0x800000)
        for i in range(int(rank)):
            embedVar7.add_field(name=rankk(i+1), value= test_list_7[i] , inline=False)
        await ctx.send(embed=embedVar7)
        test_list_7.clear()

@client.command(name='total',aliases=['totalxp'])
async def total(ctx,rank):
    if ((int(rank)<=0) or (int(rank)>75)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Data ... ")
        test_list_0 = searchTotal()
        embedVar0 = d.Embed(title="Top Guilds: Total XP", color=0x6600ff)
        for i in range(int(rank)):
            embedVar0.add_field(name=rankk(i+1), value= test_list_0[i] , inline=False)
        await ctx.send(embed=embedVar0)
        test_list_0.clear()

@client.command(name='all',aliases=['overview','ranking'])
async def all(ctx,rank):
    mining = get(ctx.guild.emojis, name="mining")
    wc = get(ctx.guild.emojis, name="woodcutting")
    fishing = get(ctx.guild.emojis, name="fishing")
    smithing = get(ctx.guild.emojis, name="smithing")
    crafting = get(ctx.guild.emojis, name="crafting")
    cooking = get(ctx.guild.emojis, name="cooking")
    combat = get(ctx.guild.emojis, name="combat")
    #fourth = get(ctx.guild.emojis, name="fourth_place")
    #fifth = get(ctx.guild.emojis, name="fifth_place") 
    
    field_header = [f' {mining} Top Guilds Mining \n',f' {wc} Top Guilds Woodcutting\n',f' {fishing} Top Guilds Fishing\n',f' {smithing} Top Guilds Smithing\n',
                        f' {crafting} Top Guilds Crafting\n',f' {cooking} Top Guilds Cooking\n',f' {combat} Top Guilds Combat\n',"Top Guilds Total XP\n"]
    
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Data ... ")
        embedVar1 = d.Embed(title="Top Guilds", color=0x669999)
        listed = LeaderBoard()
        wierd_order = [1,3,5,2,4,6,0,7]
        for i in range(8) :
            msg = ""
            for j in range(int(rank)):
                msg = msg + rankk(j+1) + ' ' + listed[wierd_order[i]][j]+'\n'
            embedVar1.add_field(name= field_header[i], value= msg , inline=True)
        await ctx.send(embed=embedVar1)
        
@client.command(name='guildlb',aliases=['guildleaderboard','skillleaderboard'])
async def guildlb(ctx,skill_name,guildtag,rank):
    guild_name = guildtag.upper()
    await ctx.send(f"Getting {guild_name}'s {skill_name} Leaderboard ... ")
    x = skills.index(skill_name.lower())
    test_list_8 = searchtag(skill[x],guildtag)
    tag = guildtag.upper()
    guildlb_msg = f"Top "+tag+": "+skill_name.capitalize()
    embedVar8 = d.Embed(title= guildlb_msg , color=0x0066ff)
    if int(rank) > int(len(test_list_8)):
        r = int(len(test_list_8))
    else:
        r = int(rank)
    for i in range(r):
        embedVar8.add_field(name=rankk(i+1), value= test_list_8[i] , inline=False)
    await ctx.send(embed=embedVar8)
    test_list_8.clear()


@client.command(name='helpme',aliases=['commands?','command?','cmd'])
async def helpme(ctx):
    embedVar9 = d.Embed(title="Guilds Commands", color=0x669999)
    embedVar9.add_field(name="skills ranking", value= "!{skill name} {how much ranks you wanna see}" , inline=False)
    embedVar9.add_field(name="!combat or !melee or !sw", value= "Show Top Guilds in Combat" , inline=False)
    embedVar9.add_field(name="!mining or !mine or !pick or !rocky or !kreiger", value= "Show Top Guilds in Mining" , inline=False)
    embedVar9.add_field(name="!smithing or !smith or !hammer or !ember", value= "Show Top Guilds in Smithing" , inline=False)
    embedVar9.add_field(name="!woodcutting or !wc or !pecker or !matt", value= "Show Top Guilds in Woodcutting" , inline=False)
    embedVar9.add_field(name="!crafting or !craft or !woody or !yekzer", value= "Show Top Guilds in Crafting" , inline=False)
    embedVar9.add_field(name="!fishing or !fish or !tantrid or !tant", value= "Show Top Guilds in Fishing" , inline=False)
    embedVar9.add_field(name="!cooking or !cook or !food", value= "Show Top Guilds in Cooking" , inline=False)
    embedVar9.add_field(name="!total or !totalxp", value= "Show Top Guilds in Total XP" , inline=False)
    embedVar9.add_field(name="!all or !overview or !ranking", value= "Show an Overall Leaderboard" , inline=False)
    embedVar9.add_field(name="!guildlb or guildleaderboard or !skillleaderboard", value= "Show The Leaderboard of a Guild in a Skill \n should be like !guildlb {skill name} {guild tag} {howmuch guildmemebers to show} " , inline=False)
    embedVar9.add_field(name="!RandomNumber [number]", value= "Show random number between 1 and the user input" , inline=False)
    embedVar9.add_field(name="!today", value= "Show Today Date" , inline=False)
    embedVar9.add_field(name="!test", value= "test The Current Command In developement" , inline=False)
    embedVar9.add_field(name="!dc or !disconnect or !logout", value= "Disconnect The Bot For a While To Reset Himself" , inline=False)
    embedVar9.add_field(name="!hello , !wussup , !bye", value= "Interract With The Bot" , inline=False)
    await ctx.send(embed=embedVar9)   

    

client.run(os.getenv('TOKEN'))