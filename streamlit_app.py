# Niko Sarcevic
# github.com/nikosarcevic
# November 2022
# ------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import streamlit as st

# add streamlit app title (on the main page)
st.title("GaussApp")

# create a sidebar on the app
with st.sidebar:
  
  # add a header in the sidebar area
  st.header("Choose your distribution parameters here")
  
 # define a start number input param, default set to -50 
  start = st.number_input("start", value=-50)

  # define a stop number input param, default set to 50
  stop = st.number_input("stop", value=50)

  # define the mean of the distribution, default set to 0
  mu = st.slider("mu", value=0)

  # define the standard deviation, default set to 0
  sigma = st.slider("sigma", value=10)
  
  # add markdowns with some relevant info
  st.markdown("Niko Sarcevic")
  st.markdown("github.com/nikosarcevic")
  st.markdown("MAS2806-PHY2039 @Newcastle University")
  st.markdown("November 2022")

# set the range of x values where the function is defined  
x = np.arange(start, stop, 0.01)
# generate the gaussian using scipy norm pdf
y = sp.stats.norm.pdf(x, mu, sigma)

# define a figure
fig, ax = plt.subplots(figsize=(10, 5))

# plot the distribution
ax.plot(x, y, color="k", lw=2)
# indicate the mean of the distribution
ax.vlines(mu, ymin=0, ymax=np.max(y), color="k", lw=2, ls="--", label="mean")
# the next 3 lines define the shaded reagion on the plot
# shaded regions indicate a one sigma spread away from the mean
xfill = np.arange(mu-sigma, mu+sigma, 0.01) # define the x coordinates of the shaded region
yfill = sp.stats.norm.pdf(xfill, mu, sigma) # define the y coordinates of the shaded region
plt.fill_between(xfill, yfill, 0, alpha=0.7, color="orange") # fill between x and y
# plot the legend
plt.legend()
plt.show()

# wrap the figure in the streamlit function, display it on the app
st.pyplot(fig)
