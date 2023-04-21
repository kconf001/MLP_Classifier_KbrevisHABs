# Downloading CSV Function
def DownloadCSV(file,data):
    import pandas as pd
    data=pd.read_csv(file, sep= ',', low_memory=False)
    return(data)

# Bloom Classification Function (0=no bloom, 1=bloom)
def BloomClassification(data):
    if data.Kbrevis < 50:
        val = 0
    elif data.Kbrevis == 50:
        val = 1
    elif data.Kbrevis > 50:
        val = 1
    return val

# Define Variable Function for csv file
def VariableCSV(file,v,name):
    name=file[v]
    return(name)
    
   
# Variable to Array Function
def Array(name,variable):
    import numpy as np
    name=np.array(variable)
    return(name)
    
# Saving to CSV file Function
def SaveCSV(file,name):
    file.to_csv(name,sep=',')
    
# Downloading nc file Function
def DownloadNETCDF(file,data):
    import xarray as xr
    data= xr.open_dataset(file)
    return(data)
    
# Match FWRI Data to CMEMs Function (approximation with method=nearest) 
def Matchup(newname,df,a,b,c,d):
    import xarray as xr
    newname=df.sel(longitude=a,latitude=b,time=c,depth=d,method='nearest')
    return(newname)

# Get Variables from NETCDF File Function
def VariableNETCDF(file,v,name):
    name=file.variables[v][:]
    return(name)
    
# NETCDF to DataFrame Function
def NETCDFtoDataframe(Array,Count,Variable,df,a,b,name,Name):
    import xarray as xr
    import numpy as np
    import pandas as pd
    Array = []                                                                                         
    for i in range(Count): 
        Array.append((np.array(Variable[i,i,i,i].values), np.float32))
    df=pd.DataFrame(Array, columns=[a,b]) 
    name=df[a]
    Name=pd.DataFrame(name)
    return(Name)

# Add Nutrient Column Function
def AddNutrient(Dataframe,Name,Variable):
    Dataframe[Name]=Variable
    Dataframe[Name]=Dataframe[Name].astype(float)
    return(Dataframe[Name])

#Replace NaN with CMEM Function
def Replace(dataframe,v1,CMEM,v2):
    dataframe[v1] = dataframe[v1].fillna(CMEM[v2])
    dataframe[v1] = dataframe[v1].astype(float)
    return(dataframe[v1])
    
# Drop NaN Rows and Export to .csv File Function
def DropNaN(newdf,olddf,name):
    newdf=olddf.dropna()
    newdf.to_csv(name, sep=',')
    
# Plot Parameters on WFS Function
def FigurePlot(fig,ax,plottitle,nn,Lon,Lat,parameter,color,gl,ylabel,plotname):
    #Graphing & Plotting
    import cartopy as cp
    import cartopy.crs as ccrs
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
    from cartopy.io import shapereader
    from matplotlib import rcParams, rc
    from matplotlib import gridspec
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    #Color options for plots
    import seaborn as sb
    import cmocean as cmo

    fig = plt.figure(figsize = (10,8), dpi = 300)
    ax = fig.add_subplot(1,1,1, projection = ccrs.Mercator(central_longitude = 0.0, min_latitude = 24, max_latitude = 31))

    # ax.set_extent(east, west, south, north)
    ax.set_extent([-87.5, -79.9, 24.4, 49])
    ax.coastlines(linewidth=0.75, color='black',zorder=0)
    ax.set_title(plottitle)#, color = 'red', weight = 'bold')
    nn = ax.scatter(Lon, Lat,s=15,c=parameter,cmap = color,vmin=parameter.min(), vmax=parameter.max(),zorder=1,edgecolors='black',linewidths=0.2,
               transform=ccrs.PlateCarree())
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=1, color='k',linestyle='--',alpha=0.5)
    gl.xlabels_top = False
    gl.ylabels_left = True
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    cbar=plt.colorbar(nn)
    cbar.ax.set_ylabel(ylabel, rotation=270)
    plt.show()
    fig.savefig(plotname,format='png',dpi=600,transparent=False)
    return(fig)
    
def TS(dataset,temp,sal,plotname):
    import numpy as np
    import gsw
    import matplotlib.pyplot as plt
    #TS Diagram-working on turning this into a function this weekend
    TS=dataset[[temp, sal]]
    TS_df=TS.sort_values(temp,ascending=True)
    mint=np.min(TS_df[temp])
    maxt=np.max(TS_df[temp])
    mins=np.min(TS_df[sal])
    maxs=np.max(TS_df[sal])
    tempL=np.linspace(mint-1.25, maxt+1.25,10064)
    salL=np.linspace(mins-1.25,maxs+1.25,10064)
    Tg, Sg = np.meshgrid(tempL,salL)
    sigmatheta = gsw.sigma0(Sg,Tg)
    cnt = np.linspace(sigmatheta.min(), sigmatheta.max(),10064)
    fig,ax=plt.subplots(figsize=(8,6),dpi=300)
    cs = ax.contour(Sg, Tg, sigmatheta, colors='grey', zorder=1)
    #manual_locations = [(-60, 70)]
    cl=plt.clabel(cs,fontsize=9,inline=True)
    sc=plt.scatter(TS_df[sal], TS_df[temp],c=cnt,s=14)
    cb=plt.colorbar(sc,shrink=0.8)
    ax.set_xlabel('Salinity',fontsize=14)
    ax.set_ylabel('Temperature ($^\circ$C)',fontsize=14)
    ax.set_title('T-S Diagram',fontsize=14)
    ax.tick_params(direction='out')
    cb.ax.tick_params(direction='out')
    cb.set_label('Density (kg m$^{-3}$)')
    #plt.tight_layout()
    fig.savefig(plotname,format='png',dpi=600,transparent=False)
    plt.show()