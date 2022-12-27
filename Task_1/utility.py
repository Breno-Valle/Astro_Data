from astropy.io import fits
import matplotlib.pyplot as plt
import numpy

hdulist0 = fits.open('C:/Users/breno/OneDrive/Documentos/Python/Astronomy_Coursera/Task_1/image0.fits')
data0 = hdulist0[0].data

hdulist1 = fits.open('C:/Users/breno/OneDrive/Documentos/Python/Astronomy_Coursera/Task_1/image1.fits')
data1 = hdulist1[0].data

hdulist2 = fits.open('C:/Users/breno/OneDrive/Documentos/Python/Astronomy_Coursera/Task_1/image2.fits')
data2 = hdulist2[0].data

hdulist3 = fits.open('C:/Users/breno/OneDrive/Documentos/Python/Astronomy_Coursera/Task_1/image3.fits')
data3 = hdulist3[0].data

hdulist4 = fits.open('C:/Users/breno/OneDrive/Documentos/Python/Astronomy_Coursera/Task_1/image4.fits')
data4 = hdulist4[0].data

fig, ax = plt.subplots(ncols=2, nrows=2) 
ax[0,0].imshow(data0, cmap = plt.cm.viridis)
ax[0,1].imshow(data1, cmap = plt.cm.inferno)
ax[1,0].imshow(data2, cmap = plt.cm.magma)
ax[1,1].imshow(data3, cmap = plt.cm.cividis)

ax[0,0].set_title('Data 0')
ax[0,1].set_title('Data 1')
ax[1,0].set_title('Data 2')
ax[1,1].set_title('Data 3')

plt.title('All Datas with Noise')
plt.show()

def mean_fits(list_fits):
    sum = numpy.empty((200,200), dtype = float)
    
    for item in list_fits:
        sum += item
    
    mean = sum / len(list_fits)
    
    plt.imshow(mean, cmap=plt.cm.viridis)
    plt.title('Sum of Datas, Noises canceled')
    plt.show()
    print(mean[100,100])

mean_fits([data0, data1, data2, data3, data4])









