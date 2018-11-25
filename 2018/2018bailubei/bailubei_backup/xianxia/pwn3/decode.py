#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import DES


def key():
  f = open('key.txt', 'r')
  key_hex = f.readline()[:-1]
  f.close()
  return key_hex.decode("hex")

def plaintext():
  f = open('plaintext.txt', 'r')
  plain_text = f.read()
  f.close()
  return plain_text

def main():
  KEY = "a"*8
  cipher = DES.new(KEY, DES.MODE_ECB)
  info = "a"*16
  print cipher.encrypt(info).encode("hex")

if __name__ == '__main__':
  main()