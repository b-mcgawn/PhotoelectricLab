#Imports
import numpy as np, matplotlib.pyplot as plt

#constants
h = 6.626e-34
c = 3.00e8
e_charge = 1.602e-19

#import data
wavelengths = np.array([452.,531.,650.,589.]) #nm +- 10 nm
wavelengths_unc = np.array([10.,10.,10.,10.])

voltage = np.array([0.9,0.6,0.3,0.6])
voltage_unc = np.array([.1,.1,.2,.1])

#only care about this 
current = np.array([0.08,0.05,0.06,0.08])
current_unc = np.array([0.05,0.02,0.02,0.02])

current_0 = np.array([0.11,0.18,0.1,0.05])
current_0_unc = np.array([0.02,0.02,0.05,0.02])

polarizer = np.array([90.,60.,30.,0.])
polarizer_unc = 5*np.ones(4)


#average the polarized light measurements
size = 1000

current_hists = np.array([])
pol_hists = np.array([])
current_hists_0 = np.array([])
mean_hists = np.array([])

wavelength_hists = np.array([])
voltage_hists = np.array([[],[],[],[]])

def hist(a,b,i):
    return np.random.normal(a[i],b[i],size)

for i in range(len(current)):

    hist_i = np.random.normal(current[i],current_unc[i],size)
    current_hists = np.append(current_hists,hist_i)

    pol_i = np.random.normal(polarizer[i],polarizer_unc[i],size)
    pol_hists = np.append(pol_hists,pol_i)

    '''
    hist_i_0 = np.random.normal(current_0[i],current_0_unc[i],size)
    current_hists_0 = np.append(current_hists_0,[hist_i_0])
    
    weights = [current_unc[i],current_0_unc[i]]
    values = [current[i],current_0[i]]
    
    mean_i = np.average(values, weights = weights)
    var_i = np.average((values-mean_i)**2, weights = weights)
    std_i = (var_i)**.5
    
    mean_hist_i = np.random.normal(mean_i,std_i,size)
    mean_hists = np.append(mean_hists, [mean_hist_i])
    '''
    
    wavelength_i = np.random.normal(wavelengths[i],wavelengths_unc[i],size)
    wavelength_hists = np.append(wavelength_hists, wavelength_i)

    voltage_hists = np.append(voltage_hists,hist(voltage,voltage_unc,i))

pol_hists.shape = (len(polarizer),size)
current_hists.shape = (len(current),size)
wavelength_hists.shape = (len(wavelengths),size)
voltage_hists.shape = (len(voltage),size)
# Turn microamps into number of electrons

# turn wavelength into incident energy- E=hc/lambda
Photon_e = h*c/(wavelength_hists*10**-9)

# turn voltage into joules
KE = e_charge*voltage_hists

mean_phot_es = [np.mean(Photon_e[0]),np.mean(Photon_e[1]),
                np.mean(Photon_e[2]),np.mean(Photon_e[3])]
std_phot_es = [np.std(Photon_e[0]),np.std(Photon_e[1]),
                np.std(Photon_e[2]),np.std(Photon_e[3])]

mean_KE = [np.mean(KE[0]),np.mean(KE[1]),
                np.mean(KE[2]),np.mean(KE[3])]
std_KE = [np.std(KE[0]),np.std(KE[1]),
                np.std(KE[2]),np.std(KE[3])]

plt.ion()
plt.figure(1)
plt.clf()
plt.errorbar(x = mean_phot_es, y = mean_KE, xerr = std_phot_es,
             yerr = std_KE, color = "k", fmt = "o")
plt.axvline(2.85e-19, label = "Work Function Energy")
plt.title('Photoelectron Energy as a function of  Photon Enegery')
plt.xlabel('Incident Photon Energy (J)')
plt.ylabel('Photoelectron Kinetic Energy (J)')
#line has slope 1, 2.85e-19 is the work function
plotline = np.linspace(2.85e-19, np.max(mean_phot_es)+np.max(std_phot_es), size)
plt.plot(plotline,plotline-2.85e-19,'-r')
plt.legend()

#np.sum(resid**2/uncertainties**2)/(len(data)-len(p_arr))
#Chisquared = np.sum(


######################################################################
# Intensity:

# I = I0 cos^2(theta)

# I/I0 = cos^2(theta)

'''
I_ratio = [[(np.cos(np.radians(pol_hists[0])))**2/np.mean(pol_hists[0])],
           [(np.cos(np.radians(pol_hists[1])))**2/np.mean(pol_hists[0])],
           [(np.cos(np.radians(pol_hists[2])))**2/np.mean(pol_hists[0])],
           [(np.cos(np.radians(pol_hists[3])))**2/np.mean(pol_hists[0])]]
'''
'''
I_ratio = [[(np.cos(np.radians(pol_hists[0])))**2/pol_hists[0]],
           [(np.cos(np.radians(pol_hists[1])))**2/pol_hists[0]],
           [(np.cos(np.radians(pol_hists[2])))**2/pol_hists[0]],
           [(np.cos(np.radians(pol_hists[3])))**2/pol_hists[0]]]
'''
I_ratio = [[(np.cos(np.radians(pol_hists[0])))**2],
           [(np.cos(np.radians(pol_hists[1])))**2],
           [(np.cos(np.radians(pol_hists[2])))**2],
           [(np.cos(np.radians(pol_hists[3])))**2]]


# I = n/(s*m^2)
# n phot = n e-
# I_r = n/n0 = nphot/nphot0 = ne/ne0
# current = n * e/t
# current_r = current/current0 = ne/ne0
# ne = ne0 * current/current0 = I_r *ne0

'''
current_r = [[current_hists[0]/current_hists[0]],
             [current_hists[1]/current_hists[0]],
             [current_hists[2]/current_hists[0]],
             [current_hists[3]/current_hists[0]]]
'''

current_r = [[current_hists[0]/np.mean(current_hists[0])],
             [current_hists[1]/np.mean(current_hists[0])],
             [current_hists[2]/np.mean(current_hists[0])],
             [current_hists[3]/np.mean(current_hists[0])]]

mean_Ir = [np.mean(I_ratio[0]),np.mean(I_ratio[1]),np.mean(I_ratio[2]),
           np.mean(I_ratio[3])]
std_Ir = np.mean([np.std(I_ratio[1]),np.std(I_ratio[2])])

mean_Cr = [np.mean(current_r[0]),np.mean(current_r[1]),np.mean(current_r[2]),
           np.mean(current_r[3])]
std_Cr = [np.std(current_r[0]),np.std(current_r[1]),np.std(current_r[2]),
           np.std(current_r[3])]

plt.figure(4)
plt.clf()
plt.errorbar(x = mean_Ir, y = mean_Cr, xerr = std_Ir,
             yerr = std_Cr, color = "k", fmt = "o")
plt.title("Number of Photoelectrons as a function of Number of Photons")
plt.xlabel("Intensity Ratio (I/$I_0$)")
plt.ylabel("Current Ratio (C/$C_0$)")
plt.plot(np.linspace(0,1,size),np.linspace(0,1,size))
