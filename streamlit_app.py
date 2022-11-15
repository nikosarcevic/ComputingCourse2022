import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import streamlit as st

st.title("GaussApp")

with st.sidebar:
  st.header("Choose your distribution parameters here")
  
  start = st.number_input("start",
                          value=-50.)

  stop = st.number_input("stop",
                         value=50.)

  mu = st.slider("mu",
                 value=0
                )

  sigma = st.slider("sigma",
                    value=10)
  
  st.markdown("Niko Sarcevic")
  st.markdown("github.com/nikosarcevic")
  st.markdown("MAS2806-PHY2039 @Newcastle University")
  st.markdown("November 2022")

x = np.arange(start, stop, 0.01)
y = sp.stats.norm.pdf(x, mu, sigma)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, color="k", lw=2)
ax.vlines(mu, ymin=0, ymax=np.max(y), color="k", lw=2, ls="--", label="mean")

xfill = np.arange(mu-sigma, mu+sigma, 0.01)
yfill = sp.stats.norm.pdf(xfill, mu, sigma)
plt.fill_between(xfill, yfill, 0, alpha=0.7, color="orange")
plt.legend()
plt.show()

st.pyplot(fig)


