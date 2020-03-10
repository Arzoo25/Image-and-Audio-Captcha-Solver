#!/usr/bin/env python3
from gtts import gTTS 
import os
import random
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', help='Length of captchas in characters', type=int)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()
    
    if args.length is None:
        print("Please specify the captcha length")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.output_dir is None:
        print("Please specify the captcha output directory")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(args.output_dir):
        print("Creating output directory " + args.output_dir)
        os.makedirs(args.output_dir)

# Creating audio files for training purpose with the help of google text to speech
    for i in range(args.count):
            #taking random strings
        captcha_text = ''.join([random.choice(captcha_symbols) for j in range(args.length)])
        #generating mp3 audio files
        audio_path = os.path.join(args.output_dir, captcha_text+'.mp3')
        myobj = gTTS(text=captcha_text, lang='en', slow=False) 
        myobj.save(audio_path) 
        print(audio_path)

if __name__ == '__main__':
    main()
