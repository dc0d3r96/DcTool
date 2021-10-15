COLORS = { \
    "rd": "\033[1;31;48m",  # red bold
    "grn": "\033[1;32;48m",  # green bold
    "yl": "\033[1;33;48m",  # yellow bold
    "bl": "\033[1;34;48m",  # blue bold
    "mg": "\033[1;35;48m",  # magenta bold
    "cyn": "\033[1;36;48m",  # Cyan bold
    "reset": "\u001b[0m",  # reset
    "br": "\033[0m",  # closeColor
    "bck": "\033[1;33;43m",  # backgraund yellow
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


the_copy = """
\033[1;32;48m
           ▒█░▒█ █▀▀█ █▀▀ █░█ █▀▀ █▀▀█ 　 ▀▀█▀▀ █▀▀█ █▀▀█ █░░ █▀▀ 
           ▒█▀▀█ █▄▄█ █░░ █▀▄ █▀▀ █▄▄▀ 　 ░▒█░░ █░░█ █░░█ █░░ ▀▀█ 
           ▒█░▒█ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀ 　 ░▒█░░ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
  ╔────────────────────────────────────────────────────────────────────────╗      
  ║                 C0d3d By: Ragif Pashayev                               ║      
  ║                 Email: Ragif.pashayev@gmail.com                        ║     
  ║                 Instagram: dc0d3r                                      ║    
  ╚────────────────────────────────────────────────────────────────────────╝         
      \033[0m
    """
header = """[[mg]]
  ╔────────────────────╗  ╔────────────────────────────────────────────────╗
  ║[[yl]] Directional Attack[[mg]] ║  ║ [[yl]]       Encoder Decoder and Other Tools      [[mg]]   ║
  ╚────────────────────╝  ╚────────────────────────────────────────────────╝      [[yl]]
  🔐[[bl]]  [1] [[yl]]Md5         🔑[[bl]] [7] [[yl]]Base64 Encode            🔑[[bl]] [13] [[yl]]Encode Hex
  🔐[[bl]]  [2] [[yl]]Sha1        🔑[[bl]] [8] [[yl]]Base64 Decode            🔑[[bl]] [14] [[yl]]Decode Hex
  🔐[[bl]]  [3] [[yl]]Sha224      🔑[[bl]] [9] [[yl]]URL Encode               🔑[[bl]] [15] [[yl]]Encode Ascii
  🔐[[bl]]  [4] [[yl]]Sha256      🔑[[bl]] [10] [[yl]]URL Decode              🔑[[bl]] [16] [[yl]]Decode Ascii
  🔐[[bl]]  [5] [[yl]]Sha384      🔑[[bl]] [11] [[yl]]Decimal to Hexdecimal   🔑[[bl]] [17] [[yl]]Wd_Calculator
  🔐[[bl]]  [6] [[yl]]Sha512      🔑[[bl]] [12] [[yl]]Hexdecimal to Decimal   ❓[[bl]] [h] [[yl]] Help                   
[[br]]                  
"""
print(the_copy)
print(colorText(header))


def helpsss():
    help_me = """
[[bl]]
  ╔────────────────────────────────────────────────────────────────────────╗
  ║   [[grn]]                HackerTools Version: 3.5             [[bl]]                ║
  ║   [[grn]]                Email: Ragif.pashayev@gmail.com      [[bl]]                ║   
  ║   [[grn]]                instagam: dc0d3r                     [[bl]]                ║
  ╚────────────────────────────────────────────────────────────────────────╝ 

  ╔────────────────────────────────────────────────────────────────────────╗
  ║[[yl]] 🔐 MD  5    [[bl]]   ___Directional Attack.___                               ║
  ║[[yl]] 🔐 SHA 1    [[bl]]  1.Enter your hash: 5d009dd44f7c195fd61d8e46a9ae0bd8      ║
  ║[[yl]] 🔐 SHA 224  [[bl]]  2.Enter your wordlist file: C:\wd.txt                    ║
  ║[[yl]] 🔐 SHA 256  [[bl]]  --------------------------------------------             ║
  ║[[yl]] 🔐 SHA 384  [[bl]]  --------------------------------------------             ║
  ║[[yl]] 🔐 SHA 512  [[bl]]  --------------------------------------------             ║
  ╚────────────────────────────────────────────────────────────────────────╝
  ╔────────────────────────────────────────────────────────────────────────╗
  ║ [[yl]]🔑 Base64 Encode  [[bl]] Enter text convert to base64                        ║
  ║ [[yl]]🔑 Base64 Decode  [[bl]] Enter base64 convert to utf-8                       ║
  ║ [[yl]]🔑 URL Encode     [[bl]] Enter text convert to Url                           ║
  ║ [[yl]]🔑 URL Decode     [[bl]] Enter Url convert to utf-8                          ║
  ║ [[yl]]🔑 Decimal to Hexdecimal  [[bl]] Enter Decimal convert to hexdecimal         ║
  ║ [[yl]]🔑 Hexdecimal to Decimal  [[bl]] Enter hexdecimal convert to  Decimal        ║
  ║ [[yl]]🔑 Encode Hex    [[bl]] Enter text convert to Hex                            ║
  ║ [[yl]]🔑 Decode Hex    [[bl]] Enter hex convert to utf-8                           ║
  ║ [[yl]]🔑 Encode Ascii  [[bl]] Enter text convert to Ascii                          ║
  ║ [[yl]]🔑 Decode Ascii  [[bl]] Enter Ascii convert to utf-8 (use a space)           ║
  ║ [[yl]] Stop pocess? write[[bl]] --exit                                             ║
  ╚────────────────────────────────────────────────────────────────────────╝
  ╔────────────────────────────────────────────────────────────────────────╗
  ║                 Wordlist Calculiator enter any value. For example:     ║
  ║                 let's look at your 16-character (abcdef0123456789)     ║
  ║                 word list if length minimum 5 and maximum 5?           ║
  ║                 Result:[[grn]] 16 ^ 5 =  1048576 [[bl]] million words               ║
  ║ [[yl]]🔑 Wd_List clc[[bl]]  Number: [[grn]]Million 10⁶[[bl]] this is a number type              ║
  ║                 Number of [[grn]]characters: 7[[bl]] shows that                     ║
  ║                 7 character have in million                            ║
  ║                 and when you making wordlist it showing you            ║
  ║                 how much storage using                                 ║
  ║                                       [[cyn]]7340032  (B)yte    [[bl]]              ║
  ║                [[grn]] 16 ^ 5 =  1048576 --> [[cyn]]7168  (Kb)yte       [[bl]]             ║
  ║                                       [[cyn]]7  (Mb)yte          [[bl]]             ║
  ╚────────────────────────────────────────────────────────────────────────╝

[[br]]  
    """
    return help_me


def crackmd5():
    import hashlib
    import time
    md_header = """[[yl]]
             ░█▀▄▀█ █▀▀▄ █▀▀ 　 ─█▀▀█ ▀▀█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █─█ 
             ░█░█░█ █──█ ▀▀▄ 　 ░█▄▄█ ──█── ──█── █▄▄█ █── █▀▄ 
             ░█──░█ ▀▀▀─ ▄▄▀ 　 ░█─░█ ──▀── ──▀── ▀──▀ ▀▀▀ ▀─▀ 
  [[yl]]──────────────────────────────────────────────────────────────────────────[[br]] 
    """
    print(colorText(md_header))
    counter = 1
    md5_pass = input(colorText("[[bl]]⇨ MD5 Enter your hash[[br]]: "))
    md5_file = input(colorText("[[bl]]⇨ Enter your Wordlist file [[br]]: "))
    try:
        md5_file = open(md5_file, "r")
    except:
        print(colorText("\n⇨[[rd]] File Not Found![[br]]"))
        quit()
    for password in md5_file:
        hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start

        if hash_obj == md5_pass:
            print(
                colorText("\n[[bl]]⇨ Congratulations! Result: Successful!..\n⇨ Password [[br]]:[[grn]] %s ") % password)
            print(colorText("[[br]][[bl]]⇨ Total Duration : [[br]]"), t_time, "second")
            break
    else:
        print(colorText("\n[[rd]]⇨ Password Not Found\n[[br]]"))
    crackmd5()


def cracksha1():
    import hashlib
    import time
    md_header = """[[yl]]
             ▒█▀▀▀█ █░░█ █▀▀█ ▄█░ 　 ░█▀▀█ ▀▀█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █░█ 
             ░▀▀▀▄▄ █▀▀█ █▄▄█ ░█░ 　 ▒█▄▄█ ░░█░░ ░░█░░ █▄▄█ █░░ █▀▄ 
             ▒█▄▄▄█ ▀░░▀ ▀░░▀ ▄█▄ 　 ▒█░▒█ ░░▀░░ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀
  [[yl]]──────────────────────────────────────────────────────────────────────────[[br]] 
        """
    print(colorText(md_header))
    counter = 1
    sha1_pass = input(colorText("[[bl]]⇨ SHA1 Enter your hash[[br]]: "))
    sha1_file = input(colorText("[[bl]]⇨ Enter your Wordlist file [[br]]: "))
    try:
        sha1_file = open(sha1_file, "r")
    except:
        print(colorText("\n⇨[[rd]] File Not Found!\n[[br]]"))
        quit()
    for password in sha1_file:
        hash_obj = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start
        if hash_obj == sha1_pass:
            print(
                colorText("\n[[bl]]⇨ Congratulations! Result: Successful!..\n⇨ Password [[br]]:[[grn]] %s ") % password)
            print(colorText("[[br]][[bl]]⇨ Total Duration : [[br]]"), t_time, "second")
            break
    else:
        print(colorText("\n[[rd]]⇨ Password Not Found!\n[[br]]"))
    cracksha1()


def cracksha224():
    import hashlib
    import time
    md_header = """[[yl]]
        ▒█▀▀▀█ █░░█ █▀▀█ █▀█ █▀█ ░█▀█░ 　 ░█▀▀█ ▀▀█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █░█ 
        ░▀▀▀▄▄ █▀▀█ █▄▄█ ░▄▀ ░▄▀ █▄▄█▄ 　 ▒█▄▄█ ░░█░░ ░░█░░ █▄▄█ █░░ █▀▄ 
        ▒█▄▄▄█ ▀░░▀ ▀░░▀ █▄▄ █▄▄ ░░░█░ 　 ▒█░▒█ ░░▀░░ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀
  [[yl]]──────────────────────────────────────────────────────────────────────────[[br]] 
            """
    print(colorText(md_header))
    counter = 1
    sha224_pass = input(colorText("[[bl]]⇨ SHA 224 Enter your hash[[br]]: "))
    sha224_file = input(colorText("[[bl]]⇨ Enter your Wordlist file[[br]]: "))
    try:
        sha224_file = open(sha224_file, "r")
    except:
        print(colorText("\n⇨[[rd]] File Not Found![[br]]"))
        quit()

    for password in sha224_file:
        hash_obj = hashlib.sha224(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start

        if hash_obj == sha224_pass:
            print(
                colorText("\n[[bl]]⇨Congratulations! Result: Successful!..\n⇨ Password [[br]]:[[grn]] %s ") % password)
            print(colorText("[[br]][[bl]]⇨ Total Duration : [[br]]"), t_time, "second")
            break
    else:
        print(colorText("\n[[rd]]⇨ Password Not Found[[br]]"))
    cracksha224()


def cracksha256():
    import hashlib
    import time
    md_header = """[[yl]]
        ▒█▀▀▀█ █░░█ █▀▀█ █▀█ █▀▀ ▄▀▀▄ 　 ░█▀▀█ ▀▀█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █░█ 
        ░▀▀▀▄▄ █▀▀█ █▄▄█ ░▄▀ ▀▀▄ █▄▄░ 　 ▒█▄▄█ ░░█░░ ░░█░░ █▄▄█ █░░ █▀▄ 
        ▒█▄▄▄█ ▀░░▀ ▀░░▀ █▄▄ ▄▄▀ ▀▄▄▀ 　 ▒█░▒█ ░░▀░░ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀
  [[yl]]──────────────────────────────────────────────────────────────────────────[[br]] 
                """
    print(colorText(md_header))
    counter = 1
    sha256_pass = input(colorText("[[bl]]⇨ SHA 256 Enter your hash[[br]]: "))
    sha256_file = input(colorText("[[bl]]⇨ Enter your Wordlist file [[br]]: "))
    try:
        sha256_file = open(sha256_file, "r")
    except:
        print(colorText("\n⇨[[rd]] File Not Found!\n[[br]]"))
        quit()
    for password in sha256_file:
        hash_obj = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start
        if hash_obj == sha256_pass:
            print(
                colorText("\n[[bl]]⇨ Congratulations! Result: Successful!..\n⇨ Password [[br]]:[[grn]] %s ") % password)
            print(colorText("[[br]][[bl]]⇨ Total Duration : [[br]]"), t_time, "second")
            break
    else:
        print(colorText("\n[[rd]]⇨ Password Not Found\n[[br]]"))
    cracksha256()


def cracksha384():
    import hashlib
    import time
    md_header = """[[yl]]
       ▒█▀▀▀█ █░░█ █▀▀█ █▀▀█ ▄▀▀▄ ░█▀█░ 　 ░█▀▀█ ▀▀█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █░█ 
       ░▀▀▀▄▄ █▀▀█ █▄▄█ ░░▀▄ ▄▀▀▄ █▄▄█▄ 　 ▒█▄▄█ ░░█░░ ░░█░░ █▄▄█ █░░ █▀▄ 
       ▒█▄▄▄█ ▀░░▀ ▀░░▀ █▄▄█ ▀▄▄▀ ░░░█░ 　 ▒█░▒█ ░░▀░░ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀
  [[yl]]──────────────────────────────────────────────────────────────────────────[[br]] 
                   """
    print(colorText(md_header))
    counter = 1
    sha384_pass = input(colorText("[[bl]]⇨ SHA 384 Enter your hash[[br]]: "))
    sha384_file = input(colorText("[[bl]]⇨ Enter your Wordlist file [[br]]: "))
    try:
        sha384_file = open(sha384_file, "r")
    except:
        print(colorText("\n⇨[[rd]] File Not Found![[br]]"))
        quit()
    for password in sha384_file:
        hash_obj = hashlib.sha384(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start
        if hash_obj == sha384_pass:
            print(
                colorText("\n[[bl]]⇨ Congratulations! Result: Successful!..\n⇨ Password [[br]]:[[grn]] %s ") % password)
            print(colorText("[[br]][[bl]]⇨ Total Duration : [[br]]"), t_time, "second")
            break
    else:
        print(colorText("\n[[rd]]⇨ Password Not Found\n[[br]]"))
    cracksha384()


def cracksha512():
    import hashlib
    import time
    md_header = """[[yl]]
         ▒█▀▀▀█ █░░█ █▀▀█ █▀▀ ▄█░ █▀█ 　 ░█▀▀█ ▀▀█▀▀ ▀▀█▀▀ █▀▀█ █▀▀ █░█ 
         ░▀▀▀▄▄ █▀▀█ █▄▄█ ▀▀▄ ░█░ ░▄▀ 　 ▒█▄▄█ ░░█░░ ░░█░░ █▄▄█ █░░ █▀▄ 
         ▒█▄▄▄█ ▀░░▀ ▀░░▀ ▄▄▀ ▄█▄ █▄▄ 　 ▒█░▒█ ░░▀░░ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀
  [[yl]]──────────────────────────────────────────────────────────────────────────[[br]] 
                       """
    print(colorText(md_header))
    counter = 1
    sha512_pass = input(colorText("[[bl]]⇨ SHA 512 Enter your hash[[br]]: "))
    sha512_file = input(colorText("[[bl]]⇨ Enter your Wordlist file [[br]]: "))
    try:
        sha512_file = open(sha512_file, "r")
    except:
        print(colorText("\n⇨[[rd]] File Not Found![[br]]"))
        quit()
    for password in sha512_file:
        hash_obj = hashlib.sha512(password.strip().encode('utf-8')).hexdigest()
        start = time.time()
        print("Trying Password %d : %s " % (counter, password.strip()))
        counter += 1
        end = time.time()
        t_time = end - start
        if hash_obj == sha512_pass:
            print(
                colorText("\n[[bl]]⇨ Congratulations! Result: Successful!..\n⇨ Password [[br]]:[[grn]] %s ") % password)
            print(colorText("[[br]][[bl]]⇨ Total Duration : [[br]]"), t_time, "Password")
            break
    else:
        print(colorText("\n[[rd]]⇨ Password Not Found\n[[br]]"))
    cracksha512()


def base64Encode():
    # base64 encode
    import base64
    while True:
        your_text = input(colorText("[[bl]]⇨ Your text: "))
        if your_text == "--exit":
            quit()
        encode_base = base64.b64encode(your_text.encode("utf-8"))
        encode_str = str(encode_base, "utf-8")
        print(colorText("⇨ Encoded Base64: [[yl]]"), encode_str, "\n")
        continue
    base64Encode()


def base64Decode():
    # base64 decode
    import base64
    while True:
        your_text = input(colorText("[[bl]]⇨ Your Encoded base64: "))
        if your_text == "--exit":
            quit()
        try:
            encode_base = base64.b64decode(your_text)
            encode_str = str(encode_base, "utf-8")
        except:
            print(colorText("\n[[rd]] ⚠ Invalid character!\n"))
            continue
        print(colorText("[[bl]]⇨ Decoded: [[yl]]"), encode_str, "\n")
        continue
    base64Decode()


def urlEncode():
    # url encode
    import urllib.parse
    while True:
        your_text = input(colorText("[[bl]]⇨ Your text: "))
        if your_text == "--exit":
            quit()
        to_url = urllib.parse.quote_plus(your_text)
        print(colorText("⇨ Encoded Url:[[yl]] "), to_url, "\n")
        continue
    urlEncode()


def urlDecode():
    # url decode
    import urllib.parse
    while True:
        your_text = input(colorText("[[bl]]⇨ Your Encoded Url: "))
        if your_text == "--exit":
            quit()
        url_to_text = urllib.parse.unquote_plus(your_text)
        print(colorText("⇨ Decoded: [[yl]]"), url_to_text, "\n")
        continue
    urlDecode()


def decHexdec():
    # Decimal to Hexdecimal
    while True:
        dec_to = input(colorText("[[bl]]⇨ Decimal: "))
        if dec_to == "--exit":
            quit()
        try:
            dec = int(dec_to)
            print(colorText("⇨ Hexdecimal:[[yl]] {0:x}").format(dec), "\n")
        except:
            print(colorText("\n ⚠ Invalid character!\n"))
            continue
    decHexdec()


def hexDec():
    # Hexdecimal to Decimal
    while True:
        hex_to_dec = input(colorText("[[bl]]⇨ Hexdecimal: "))
        if hex_to_dec == "--exit":
            break
        try:
            dec = int(hex_to_dec, 16)
            print(colorText("⇨ Decimal: [[yl]]"), dec, "\n")
        except:
            print(colorText("\n[[rd]] ⚠ Invalid character!\n"))
            continue
    decHexdec()


def encodeHex():
    # Encode Hex
    while True:
        go_encode_hex = input(colorText("[[bl]]⇨ Your text: "))
        if go_encode_hex == "--exit":
            quit()
        encode_hexx = go_encode_hex.encode('utf-8')
        print(colorText("⇨ Encoded Hex: [[yl]]"), encode_hexx.hex(), "\n")
        continue
    encodeHex()


def decodeHex():
    # Decode Hex
    while True:
        go_decode_hex = input(colorText("[[bl]]⇨ Your Encoded Hex: "))
        if go_decode_hex == "--exit":
            quit()
        try:
            decode_hexx = bytes.fromhex(go_decode_hex).decode('utf-8')
            print(colorText("⇨ Decoded: [[yl]]"), decode_hexx, "\n")
        except:
            print(colorText("\n[[rd]] ⚠ Invalid character!\n"))
        continue
    decodeHex()


def asciiEncoder():
    # Ascii encoder
    while True:
        asccii = input(colorText("[[bl]]⇨ Your text: "))
        if asccii == "--exit":
            quit()
        text_to_ascii = ''.join(str(ord(c)) for c in asccii)
        print(colorText("⇨ Encoded Ascii:[[yl]] "), text_to_ascii, "\n")
        continue
    asciiEncoder()


def asciiDecoder():
    # Ascii decoder
    while True:
        to_ascii = input(colorText("[[bl]]⇨ Your Encoded Ascii: "))
        if to_ascii == "--exit":
            quit()
        try:
            to_conv = list(map(int, to_ascii.split(' ')))
            to_string = ''.join(chr(i) for i in to_conv)
        except:
            print(colorText(
                "\n[[rd]] ⚠ Invalid character!\n Use spaces for each character \n For example: 97 115 99 105 105\n"))
            continue
        print(colorText("⇨ Decoded: [[yl]]"), to_string, "\n")
        continue
    asciiDecoder()


def wdClc():
    the_copy2 = """
    \033[1;32;48m

                         ▒█░░▒█ █▀▀▄ ▒█▀▀█ █░░ █▀▀     
                         ▒█▒█▒█ █░░█ ▒█░░░ █░░ █░░     
                         ▒█▄▀▄█ ▀▀▀░ ▒█▄▄█ ▀▀▀ ▀▀▀                                                
  ╔─────────────────────────────────────────────────────────────────────────╗
  ║                 𝄴₀d₃d By: Ragif Pashayev                                ║
  ║                 Email: Ragif.pashayev@gmail.com                         ║
  ║                 Instagram: ___dcoder___                                 ║
  ║                 WordList Calculiator V_9                                ║
  ╚─────────────────────────────────────────────────────────────────────────╝
      \033[0m
    """
    print(the_copy2)
    import time, sys
    import os

    COLORS = { \
        "mg": "\033[0;35;48m",  # magenta
        "rd": "\033[1;31;48m",  # red bold
        "grn": "\033[1;32;48m",  # green bold
        "yl": "\033[1;33;48m",  # yellow bold
        "bl": "\033[1;34;48m",  # blue bold
        "cyn": "\033[1;36;48m",  # Cyan bold
        "gry": "\033[1;37;48m",  # gray bold
        "reset": "\u001b[0m",  # reset
        "br": "\033[0m",  # closeColor
    }

    def colorText(text):
        for color in COLORS:
            text = text.replace("[[" + color + "]]", COLORS[color])
        return text

    while True:
        wd_number = input(colorText("[[cyn]]⇨ Number of character: "))
        wd_min_lenght = input(colorText("[[cyn]]⇨ Min length: "))
        wd_max_lenght = input(colorText("[[cyn]]⇨ Max length: "))
        print()
        if not wd_number:
            break
        try:
            wd_number_x = int(wd_number)
            wd_min_lenght_x = int(wd_min_lenght)
            wd_max_lenght_x = int(wd_max_lenght)
            clc_min = wd_number_x ** wd_min_lenght_x
        except ValueError:
            print(colorText(
                "[[rd]]   ⚠ Invalid Character!.\n   Only number is allowed\n   Please enter a number...[[br]]"))
            print()
            continue
        if wd_min_lenght_x == wd_max_lenght_x:
            print(colorText("[[cyn]]⇨ Result: [[rd]]"), wd_number_x, "^", wd_min_lenght_x, colorText("[[cyn]]= [[yl]]"),
                  clc_min)
            go_to_str = str(clc_min)
            show_me_length = len(go_to_str)
            print(colorText("[[cyn]]⇨ Number of characters: [[bl]]"), show_me_length)
            if show_me_length <= 1:
                print(colorText("[[cyn]]⇨ Number:[[gry]] One[[rd]] 10⁰[[cyn]]"))
            elif show_me_length <= 2:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten[[rd]] 10¹[[cyn]]"))
            elif show_me_length <= 3:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred[[rd]] 10²[[cyn]]"))
            elif show_me_length <= 4:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Thousand[[rd]] 10³[[cyn]]"))
            elif show_me_length <= 5:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten thousand[[rd]] 10⁴[[cyn]]"))
            elif show_me_length <= 6:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred thousand[[rd]] 10⁵[[cyn]]"))
            elif show_me_length <= 7:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Million[[rd]] 10⁶[[cyn]]"))
            elif show_me_length <= 8:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Million[[rd]] 10⁷[[cyn]]"))
            elif show_me_length <= 9:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Million[[rd]] 10⁸[[cyn]]"))
            elif show_me_length <= 10:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Billion 10⁹[[cyn]]"))
            elif show_me_length <= 11:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Billion[[rd]] 10¹⁰[[cyn]]"))
            elif show_me_length <= 12:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Billion[[rd]] 10¹¹[[cyn]]"))
            elif show_me_length <= 13:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Trillion[[rd]] 10¹²[[cyn]]"))
            elif show_me_length <= 13:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Trillion[[rd]] 10¹³[[cyn]]"))
            elif show_me_length <= 14:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Trillion[[rd]] 10¹⁴[[cyn]]"))
            elif show_me_length <= 15:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Quadrillion[[rd]] 10¹⁵[[cyn]]"))
            elif show_me_length <= 16:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Quadrillion[[rd]] 10¹⁶[[cyn]]"))
            elif show_me_length <= 17:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Quadrillion[[rd]] 10¹⁷[[cyn]]"))
            elif show_me_length <= 18:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Quintillion[[rd]] 10¹⁸[[cyn]]"))
            elif show_me_length <= 19:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Quintillion[[rd]] 10¹⁹[[cyn]]"))
            elif show_me_length <= 20:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Quintillion[[rd]] 10²⁰[[cyn]]"))
            elif show_me_length <= 21:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Sextillion[[rd]] 10²¹[[cyn]]"))
            elif show_me_length <= 22:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Sextillion[[rd]] 10²²[[cyn]]"))
            elif show_me_length <= 23:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Sextillion[[rd]] 10²³[[cyn]]"))
            elif show_me_length <= 24:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Septillion[[rd]] 10²⁴[[cyn]]"))
            elif show_me_length <= 25:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Septillion[[rd]] 10²⁵[[cyn]]"))
            elif show_me_length <= 26:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Septillion[[rd]] 10²⁶[[cyn]]"))
            elif show_me_length <= 27:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Octillion[[rd]] 10²⁷[[cyn]]"))
            elif show_me_length <= 28:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Octillion[[rd]] 10²⁸[[cyn]]"))
            elif show_me_length <= 29:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Octillion[[rd]] 10²⁹[[cyn]]"))
            elif show_me_length <= 30:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Nonillion[[rd]] 10³⁰[[cyn]]"))
            elif show_me_length <= 31:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Nonillion[[rd]] 10³¹[[cyn]]"))
            elif show_me_length <= 32:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Nonillion[[rd]] 10³²[[cyn]]"))
            elif show_me_length <= 32:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Decillion[[rd]] 10³³[[cyn]]"))
            elif show_me_length <= 33:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Decillion[[rd]] 10³⁴[[cyn]]"))
            elif show_me_length <= 34:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Decillion[[rd]] 10³⁵[[cyn]]"))
            elif show_me_length <= 35:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Undecillion[[rd]] 10³⁶[[cyn]]"))
            elif show_me_length <= 36:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Undecillion[[rd]] 10³⁷[[cyn]]"))
            elif show_me_length <= 37:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Undecillion[[rd]] 10³⁸[[cyn]]"))
            elif show_me_length <= 38:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Duodecillion[[rd]] 10³⁹[[cyn]]"))
            elif show_me_length <= 39:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Duodecillion[[rd]] 10⁴⁰[[cyn]]"))
            elif show_me_length <= 40:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Duodecillion[[rd]] 10⁴¹[[cyn]]"))
            elif show_me_length <= 41:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Tredecillion[[rd]] 10⁴²[[cyn]]"))
            elif show_me_length <= 42:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Tredecillion[[rd]] 10⁴³[[cyn]]"))
            elif show_me_length <= 43:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Tredecillion[[rd]] 10⁴⁴[[cyn]]"))
            elif show_me_length <= 44:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Quattuordecillion[[rd]] 10⁴⁵[[cyn]]"))
            elif show_me_length <= 45:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Quattuordecillion[[rd]] 10⁴⁶[[cyn]]"))
            elif show_me_length <= 46:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Quattuordecillion[[rd]] 10⁴⁷[[cyn]]"))
            elif show_me_length <= 47:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Quindecillion[[rd]] 10⁴⁸[[cyn]]"))
            elif show_me_length <= 48:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Quindecillion[[rd]] 10⁴⁹[[cyn]]"))
            elif show_me_length <= 49:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Quindecillion[[rd]] 10⁵⁰[[cyn]]"))
            elif show_me_length <= 50:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Sexdecillion[[rd]] 10⁵¹[[cyn]]"))
            elif show_me_length <= 51:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Sexdecillion[[rd]] 10⁵²[[cyn]]"))
            elif show_me_length <= 52:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Sexdecillion[[rd]] 10⁵³[[cyn]]"))
            elif show_me_length <= 53:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Septendecillion[[rd]] 10⁵⁴[[cyn]]"))
            elif show_me_length <= 54:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Septendecillion[[rd]] 10⁵⁵[[cyn]]"))
            elif show_me_length <= 55:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Septendecillion[[rd]] 10⁵⁶[[cyn]]"))
            elif show_me_length <= 56:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Octodecillion[[rd]] 10⁵⁷[[cyn]]"))
            elif show_me_length <= 57:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Octodecillion[[rd]] 10⁵⁸[[cyn]]"))
            elif show_me_length <= 58:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Octodecillion[[rd]] 10⁵⁹[[cyn]]"))
            elif show_me_length <= 59:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Novemdecillion[[rd]] 10⁶⁰[[cyn]]"))
            elif show_me_length <= 60:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Novemdecillion[[rd]] 10⁶¹[[cyn]]"))
            elif show_me_length <= 61:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Novemdecillion[[rd]] 10⁶²[[cyn]]"))
            elif show_me_length <= 62:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Vigintillion[[rd]] 10⁶³[[cyn]]"))
            elif show_me_length <= 63:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Vigintillion[[rd]] 10⁶⁴ [[cyn]]"))
            elif show_me_length <= 64:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Vigintillion[[rd]] 10⁶⁵[[cyn]]"))
            elif show_me_length <= 65:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Unvigintillion[[rd]] 10⁶⁶[[cyn]]"))
            elif show_me_length <= 66:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Unvigintillion[[rd]] 10⁶⁷[[cyn]]"))
            elif show_me_length <= 67:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Unvigintillion[[rd]] 10⁶⁸[[cyn]]"))
            elif show_me_length <= 68:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Duovigintillion[[rd]] 10⁶⁹[[cyn]]"))
            elif show_me_length <= 69:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Duovigintillion[[rd]] 10⁷⁰[[cyn]]"))
            elif show_me_length <= 70:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Duovigintillion[[rd]] 10⁷¹[[cyn]]"))
            elif show_me_length <= 71:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Trevigintillion[[rd]] 10⁷²[[cyn]]"))
            elif show_me_length <= 72:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Trevigintillion[[rd]] 10⁷³[[cyn]]"))
            elif show_me_length <= 73:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Trevigintillion[[rd]] 10⁷⁴[[cyn]]"))
            elif show_me_length <= 74:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Quattuorvigintillion[[rd]] 10⁷⁵[[cyn]]"))
            elif show_me_length <= 75:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Quattuorvigintillion[[rd]] 10⁷⁶[[cyn]]"))
            elif show_me_length <= 76:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Quattuorvigintillion[[rd]] 10⁷⁷[[cyn]]"))
            elif show_me_length <= 77:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Quinvigintillion[[rd]] 10⁷⁸[[cyn]]"))
            elif show_me_length <= 78:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Quinvigintillion[[rd]] 10⁷⁹[[cyn]]"))
            elif show_me_length <= 79:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Quinvigintillion[[rd]] 10⁸⁰[[cyn]]"))
            elif show_me_length <= 80:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Sexvigintillion[[rd]] 10⁸¹[[cyn]]"))
            elif show_me_length <= 81:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Hundred Sexvigintillion[[rd]] 10⁸²[[cyn]]"))
            elif show_me_length <= 82:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Sexvigintillion[[rd]] 10⁸³[[cyn]]"))
            elif show_me_length <= 83:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Septenvigintillion[[rd]] 10⁸⁴[[cyn]]"))
            elif show_me_length <= 84:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Septenvigintillion[[rd]] 10⁸⁵[[cyn]]"))
            elif show_me_length <= 85:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Septenvigintillion[[rd]] 10⁸⁶[[cyn]]"))
            elif show_me_length <= 86:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Octovigintillion[[rd]] 10⁸⁷[[cyn]]"))
            elif show_me_length <= 87:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Octovigintillion[[rd]] 10⁸⁸[[cyn]]"))
            elif show_me_length <= 88:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Octovigintillion[[rd]] 10⁸⁹[[cyn]]"))
            elif show_me_length <= 89:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Novemvigintillion[[rd]] 10⁹⁰[[cyn]]"))
            elif show_me_length <= 90:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Novemvigintillion[[rd]] 10⁹¹[[cyn]]"))
            elif show_me_length <= 91:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Novemvigintillion[[rd]] 10⁹²[[cyn]]"))
            elif show_me_length <= 92:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Trigintillion[[rd]] 10⁹³[[cyn]]"))
            elif show_me_length <= 93:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Trigintillion[[rd]] 10⁹⁴[[cyn]]"))
            elif show_me_length <= 94:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Trigintillion[[rd]] 10⁹⁵[[cyn]]"))
            elif show_me_length <= 95:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Untrigintillion[[rd]] 10⁹⁶[[cyn]]"))
            elif show_me_length <= 96:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Untrigintillion[[rd]] 10⁹⁷[[cyn]]"))
            elif show_me_length <= 97:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Untrigintillion[[rd]] 10⁹⁸[[cyn]]"))
            elif show_me_length <= 98:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Duotrigintillion[[rd]] 10⁹⁹[[cyn]]"))
            elif show_me_length <= 98:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Ten Duotrigintillion[[rd]] 10¹⁰⁰[[cyn]]"))
            elif show_me_length <= 98:
                print(colorText("[[cyn]]⇨ Number:[[gry]] Hundred Duotrigintillion[[rd]] 10¹⁰¹[[cyn]]"))
            else:
                print(colorText("[[cyn]]⇨ Number:[[gry]] ∞"))
            bayt = (wd_min_lenght_x + 2) * clc_min
            kbayt = bayt // 1024
            mbayt = kbayt // 1024
            gbayt = mbayt // 1024
            trbayt = gbayt // 1024
            petabayt = trbayt // 1024
            ekzabayt = petabayt // 1024
            zettabayt = ekzabayt // 1024
            yottabayt = zettabayt // 1024
            while (bayt >= 0):
                print(colorText("⇨[[bl]]"), bayt, colorText("[[grn]] (B)yte[[cyn]]"))
                if bayt >= 1024:
                    print(colorText("⇨[[bl]]"), kbayt, colorText("[[grn]] (Kb)yte[[cyn]]"))
                if kbayt >= 1024:
                    print(colorText("⇨[[bl]]"), mbayt, colorText("[[grn]] (Mb)yte[[cyn]]"))
                if mbayt >= 1024:
                    print(colorText("⇨[[bl]]"), gbayt, colorText("[[grn]] (Gb)yte[[cyn]]"))
                if gbayt >= 1024:
                    print(colorText("⇨[[bl]]"), trbayt, colorText("[[grn]] (Tb)yte[[cyn]]"))
                if trbayt >= 1024:
                    print(colorText("⇨[[bl]]"), petabayt, colorText("[[grn]] (Pb)yte[[cyn]]"))
                if petabayt >= 1024:
                    print(colorText("⇨[[bl]]"), ekzabayt, colorText("[[grn]] (Eb)yte[[cyn]]"))
                if ekzabayt >= 1024:
                    print(colorText("⇨[[bl]]"), zettabayt, colorText("[[grn]] (Zb)yte[[cyn]]"))
                if zettabayt >= 1024:
                    print(colorText("⇨[[bl]]"), yottabayt, colorText("[[grn]] (Yb)yte[[cyn]]"))
                break

        elif wd_min_lenght_x >= wd_max_lenght_x:
            print(colorText("[[rd]] Error!\n Minimum Number cannot be larger than maximum number![[br]]"))
            print()
            continue
        elif wd_min_lenght_x <= wd_max_lenght_x:
            i = wd_min_lenght_x - 1
            while (i < wd_max_lenght_x):
                i += 1
                clc_all = wd_number_x ** i
                go_more_str = str(clc_all)
                go_len_show = len(go_more_str)
                bayt2 = (i + 2) * clc_all
                kbayt2 = bayt2 // 1024
                mbayt2 = kbayt2 // 1024
                gbayt2 = mbayt2 // 1024
                tbayt2 = gbayt2 // 1024
                petabayt2 = tbayt2 // 1024
                ekzabayt2 = petabayt2 // 1024
                zettabayt2 = ekzabayt2 // 1024
                yottabayt2 = zettabayt2 // 1024
                print(colorText("[[cyn]]⇨ Result: [[mg]]{}^{} =[[yl]] {}\n[[cyn]]⇨ Number of characters:[[bl]] {} [[cyn]]").format(wd_number_x, i, clc_all, go_len_show))
                while (bayt2 >= 0):
                    print(colorText("⇨[[bl]]"), bayt2, colorText("[[grn]] (B)yte[[cyn]]"))
                    if bayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), kbayt2, colorText("[[grn]] (Kb)yte[[cyn]]"))
                    if kbayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), mbayt2, colorText("[[grn]] (Mb)yte[[cyn]]"))
                    if mbayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), gbayt2, colorText("[[grn]] (Gb)yte[[cyn]]"))
                    if gbayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), tbayt2, colorText("[[grn]] (Tb)yte[[cyn]]"))
                    if tbayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), petabayt2, colorText("[[grn]] (Pb)yte[[cyn]]"))
                    if petabayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), ekzabayt2, colorText("[[grn]] (Eb)yte[[cyn]]"))
                    if ekzabayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), zettabayt2, colorText("[[grn]] (Zb)yte[[cyn]]"))
                    if zettabayt2 >= 1024:
                        print(colorText("⇨[[bl]]"), yottabayt2, colorText("[[grn]] (Yb)yte[[cyn]]"))
                    break
                print("\n")
        print()
        refreshh = input(colorText("[[rd]]⇨ [[cyn]] ⟳ Do you want to refresh? (y/n): "))
        if refreshh == "y":
            print(the_copy2)
        else:
            quit()
    wdClc()


while True:
    in_put = input(colorText("[[bl]]⇨ Choose your Process: [[br]]"))
    if (in_put == "h"):
        print(colorText(helpsss()))
        continue
    elif (in_put == "--exit"):
        quit()
    elif (in_put == "1"):
        print(crackmd5())
        break
    elif (in_put == "2"):
        print(cracksha1())
        break
    elif (in_put == "3"):
        print(cracksha224())
        break
    elif (in_put == "4"):
        print(cracksha256())
        break
    elif (in_put == "5"):
        print(cracksha384())
        break
    elif (in_put == "6"):
        print(cracksha512())
        break
    elif (in_put == "7"):
        print(base64Encode())
        break
    elif (in_put == "8"):
        print(base64Decode())
        break
    elif (in_put == "9"):
        print(urlEncode())
        break
    elif (in_put == "10"):
        print(urlDecode())
        break
    elif (in_put == "11"):
        print(decHexdec())
        break
    elif (in_put == "12"):
        print(hexDec())
        break
    elif (in_put == "13"):
        print(encodeHex())
        break
    elif (in_put == "14"):
        print(decodeHex())
        break
    elif (in_put == "15"):
        print(asciiEncoder())
        break
    elif (in_put == "16"):
        print(asciiDecoder())
        break
    elif (in_put == "17"):
        print(wdClc())
        break
    else:
        print(colorText("[[rd]]  ⚠️Invalid Character!.[[br]]\n"))
    continue
