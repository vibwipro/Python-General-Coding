import matplotlib.pyplot as plt
import numpy as np

##########   Simple bar chart showing revenues of major US tech companies

company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]

xpos = np.arange(len(company))
print(xpos)

plt.bar(xpos,revenue, label="Revenue")

plt.xticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
plt.show()

##########################################
############## Multiple Bars showing revenue and profit of major US tech companies

profit=[40,2,34,12]

plt.bar(xpos-0.2,revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2,profit, width=0.4,label="Profit")

plt.xticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
plt.show()


#############################################################
############## Horizontal bar chart using barh function

plt.barh(xpos,revenue, label="Revenue")

plt.yticks(xpos,company)
plt.xlabel("Revenue(Bln)")
plt.title('US Technolog Stocks')
plt.legend()
plt.show()
