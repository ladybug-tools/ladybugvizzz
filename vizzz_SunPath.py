import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

winterAzi = datafomPySolarAzi
winterAlt = datafromPySolarAlt

# create instance of basemap, note we want a south polar projection to 90 = E
myMap = Basemap(projection='spstere',boundinglat=0,lon_0=180,resolution='l',round=True,suppress_ticks=True)
# set the grid up
gridX,gridY = 10.0,15.0
parallelGrid = np.arange(-90.0,90.0,gridX)
meridianGrid = np.arange(-180.0,180.0,gridY)

# draw parallel and meridian grid, not labels are off. We have to manually create these.
myMap.drawparallels(parallelGrid,labels=[False,False,False,False])
myMap.drawmeridians(meridianGrid,labels=[False,False,False,False],labelstyle='+/-',fmt='%i')

# we have to send our values through basemap to convert coordinates, note -winterAlt
winterX,winterY = myMap(winterAzi,-winterAlt)

# plot azimuth labels, with a North label.
ax = plt.gca()
ax.text(0.5,1.025,'N',transform=ax.transAxes,horizontalalignment='center',verticalalignment='bottom',size=25)
for para in np.arange(gridY,360,gridY):
    x= (1.1*0.5*np.sin(np.deg2rad(para)))+0.5
    y= (1.1*0.5*np.cos(np.deg2rad(para)))+0.5
    ax.text(x,y,u'%i\N{DEGREE SIGN}'%para,transform=ax.transAxes,horizontalalignment='center',verticalalignment='center')


# plot the winter values
myMap.plot(winterX,winterY ,'bo')