from rflib import *

d = RfCat()
d.setFreq(433891000)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(4800)

switch = int(input("Switch Number(1-3):"))
state = int(input("Switch State(0/1):"))

if switch == 1:

	if state == 1:
		print("Transmitting...")
		d.RFxmit("\x9a\x69\xa4\x92\x69\xa6\x93\x69\x36\x80\x00"*10)	# Switch 1 ON
		print("Done!")

	elif state == 0:
		print("Transmitting")
		d.RFxmit("\x9a\x69\xa4\x92\x69\xa6\x93\x6d\xa4\x80\x00"*10)	# Switch 1 OFF
		print("Done!")

	else:
		print("Not a valid Switch State!")

elif switch == 2:

	if state == 1:
		print("Transmitting...")
		d.RFxmit("\x9a\x69\xa4\x92\x69\xa6\xda\x49\x36\x80\x00"*10)	# Switch 2 ON
		print("Done!")

	elif state == 0:
		print("Transmitting")
		d.RFxmit("\x9a\x69\xa4\x92\x69\xa6\xda\x4d\xa4\x80\x00"*10)	# Switch 2 OFF
		print("Done!")

	else:
		print("Not a valid Switch State!")

elif switch == 3:

	if state == 1:
		print("Transmitting...")
		d.RFxmit("\x9a\x69\xa4\x92\x69\xb6\x92\x49\x36\x80\x00"*10)	# Switch 3 ON
		print("Done!")

	elif state == 0:
		print("Transmitting")
		d.RFxmit("\x9a\x69\xa4\x92\x69\xb6\x92\x4d\xa4\x80\x00"*10)	# Switch 3 OFF
		print("Done!")

	else:
		print("Not a valid Switch State!")
