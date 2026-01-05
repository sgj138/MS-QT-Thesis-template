import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "font.size": 11,          # comparable to thesis caption/figure text
    "axes.labelsize": 11,
    "axes.titlesize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "font.family": "serif"
})

plt.figure(figsize=(6,5))
x=np.arange(0,10,0.1)
plt.plot(x,np.sin(x),color='r',lw=2,label="sin")
plt.plot(x,np.cos(x),color='g',lw=2,label="cos")
plt.legend()
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Example Figure")
# Save as vector where possible
plt.tight_layout()
plt.savefig("example_figure.pdf", bbox_inches="tight")


plt.figure(figsize=(5.5,3))
plt.subplot(1,2,1)
x=np.arange(0,10,0.1)
plt.plot(x,np.sin(x),color='r',lw=2,label="sin")
plt.plot(x,np.cos(x),color='g',lw=2,label="cos")
plt.legend(loc="lower left")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.ylim(-1.8,1.25 )
plt.text(.15, 0.95, "(a)", fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)
plt.title("Trigonometric Functions")

plt.subplot(1,2,2)
x=np.arange(0,10,0.01)
plt.plot(x,np.tanh(x),color='r',lw=2,label="tanh")
plt.plot(x,1/np.cosh(x),color='k',lw=2,label="sech")
plt.legend()
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Hyperbolic Functions")
plt.text(.15, .95, "(b)", fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)
plt.ylim(-.05,1.25 )
plt.tight_layout()

# Save as vector where possible
plt.savefig("example_figure2.pdf", bbox_inches="tight")
