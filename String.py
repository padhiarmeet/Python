name = "meet"

name1 = 'meetchhemeet'
#_____________________________________________________RAW_STRING

#this is raw string which treat / as /
name4 = r'hello/meet:/meet'
print("print of row string is-",name4)

#_____________________________________________________BYTE_STRING

#this is byte string which represen sequence of bytes
name5 = b'meetHotChhe'
print(name5)
print(name5[0])

#____________________________________________________FORMAL_STRING

#we can directly use variable value in this string
name6 = "meet"
print(f"meet chhe maru name su chhe.....{name6}")

#for multiline string
name2 = '''meet
            chhe maru 
            name'''

nameSort = name1[-4:-1] #it will print 0 to 1 cherecter not 2 indexed cherecter(second argument is length,for just say)
#output --- me
namesort2 = name2[1:9:2] #it will print 1 to 8 and take gp tof 2
#output --- et  
print(nameSort)
print(namesort2)
print("meet\vchhe\vho")