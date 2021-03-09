from PIL import Image
import numpy

ctf_file="ctf.tiff" # CTF file name
# START READING THE 256 BYTES KEY  FROM THE TAIL OF FILE
f= open(ctf_file,"rb")
f.seek(-256,2)
key=f.read()
f.close()
key=list(key)
# END ###,
im = Image.open(ctf_file) # open CTF file image
imarray = numpy.array(im)
# START DE SCRAMBLING THE IMAGE
imarray[:,:]=imarray[key,:]
imarray[:,:]=imarray[:,key]
# END ###,
im=Image.fromarray(imarray) 
im.save("ctf_de.tiff") # saving the descrambled image: check the flag 
##END####,