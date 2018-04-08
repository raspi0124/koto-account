import sqlite3
import subprocess
import re
def createaccount(name):
	dbpath = '~/koto-account.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	#connection.isolation_level = None
	cursor = connection.cursor()
	cmda = "koto-cli z_getnewaddress"
	address  =  subprocess.check_output( cmda.split(" ") )
	address = address.decode()
	print(address)
	address = str(address)
	username = "'" + name + "'"
	address = "'" + address + "'"
	if "-" not in username:
		query = 'INSERT INTO accounts (username, address) VALUES (' + username + ', ' + address + ')'
		print(query)
		cursor.execute(query)
		connection.commit()
		address = address.replace("'", "")
		return address
	else:
		return "prohibited_inc_username"
def getaddress(name):
	dbpath = '~/koto-account.sqlite'
	connection = sqlite3.connect(dbpath)
	# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
	#connection.isolation_level = None
	cursor = connection.cursor()
	username = "'" + name + "'"
	query = 'select address from accounts where username = ' + username + ''
	print(query)
	cursor.execute(query)
	address = cursor.fetchall()
	print(address)
	address = address[0]
	address = str(address)
	address = address.rstrip()
	address = address.replace("'", "")
	address = address.replace("(", "")
	address = address.replace(")", "")
	address = address.replace(",", "")
	address = address.replace("\\n", "")
	return address
def getbalance(name):
	address = getaddress(name)
	cmda = "koto-cli z_getbalance " + address + ""
	ruta =  subprocess.check_output( cmda.split(" ") )
	ruta = ruta.decode()
	ruta = str(ruta)
	return ruta
def withdraw(fromaddress, to, amount):
	fromaddress = getaddress(fromaddress)
	toaddress = to
	fromaddress = str(fromaddress)
	toaddress = str(toaddress)
	amount = str(amount)
	fromaddress = '"' + fromaddress + '"'
	cmd1 = 'koto-cli z_sendmany ' + fromaddress + ' '
	cmd2 = '[{"address": "' + toaddress + '" ,"amount": ' + amount + '}]'
	cmd2_2 = "'" + cmd2 + "'"
	cmda = cmd1 + cmd2_2
	cmda = str(cmda)
	print(cmda)
	ruta = subprocess.getoutput(cmda)
	print("--ruta--")
	print()
	return ruta
def move(fromaddress, to, amount):
	fromaddress = getaddress(fromaddress)
	toaddress = getaddress(to)
	fromaddress = str(fromaddress)
	toaddress = str(toaddress)
	amount = str(amount)
	cmd1 = 'koto-cli z_sendmany ' + fromaddress + ' '
	cmd2 = '[{"address": "' + toaddress + '" ,"amount": ' + amount + '}]'
	cmd2_2 = "'" + cmd2 + "'"
	cmda = cmd1 + cmd2_2
	cmda = str(cmda)
	print(cmda)
	ruta = subprocess.getoutput(cmda)
	print("--ruta--")
	print()
	return ruta
