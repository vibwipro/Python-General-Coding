import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x,y,color='green',linewidth=5, linestyle='dotted')
plt.show()

######################################################################3
#### Another plotting


plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(x,y,'b+--')
plt.show()

######################################################################3
#### Another plotting

# Same effect as 'b+' format string
plt.plot(x,y,color='blue',marker='+',linestyle='')
plt.show()

##### markersize
plt.plot(x,y,color='blue',marker='+',linestyle='',markersize=20)
plt.show()


############### alpha property to control transparency of line chart
plt.plot(x,y,'g<',alpha=0.1) # alpha can be specified on a scale 0 to 1
plt.show()




