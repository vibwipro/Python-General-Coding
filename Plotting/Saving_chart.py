import matplotlib.pyplot as plt

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]

plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels,radius=1.5, autopct='%0.1f%%', explode=[0,0.1,0.1,0,0])

##### Saving file in JPG Format
plt.savefig("piechart.jpg", bbox_inches="tight", pad_inches=1, transparent=True)
plt.show()


########## Saving file in PDF format at diff location.

plt.pie(exp_vals,labels=exp_labels,radius=2, autopct='%0.1f%%', explode=[0,0.1,0.1,0,0])
plt.savefig("C:/Users/vibho/Desktop/piechart.pdf", bbox_inches="tight", pad_inches=10, transparent=True)
plt.show()