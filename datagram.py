datagram=5299 #this is a datagram. if your question mention data only, please add the header in this datagram.
mtu=821     #this is the max transfer unit .
header=37    #this is the header size . it is included in datagram. by default =20

totalbyte=datagram-header  #this is the data of the datagram.
off=0     #this is the offside counter.
mtuu=mtu-header   #this is the mtu without header .
while totalbyte>=0:
  offset=(off*mtuu)/8
  off=off+1
  totalbyte=totalbyte-mtuu
  print('{}\t{}+{}\t{}\t{}'.format((off),header,mtuu,'   x',offset))
lastFragmentSize=(datagram-header)-(offset*8)
print("Last datagram size is ",lastFragmentSize)
print("Last datagram size including header is ",lastFragmentSize+header)