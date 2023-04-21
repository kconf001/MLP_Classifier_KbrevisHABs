# **Preliminary Classification of <em>Karenia Brevis </em> HAB conditions on the West Florida Shelf (WFS)**
# Capstone Project - Kristina Confesor, 2023
## **Background**
<p align="center">
<img src="https://images.marinespecies.org/thumbs/33875_karenia-brevis.jpg?w=700" alt="K.brevis Morphology" style="height: 200px; width:300px;"/>

<p align="center">
Figure 1: <em> K. brevis </em> morphology (Hansen, 2000).
<p> Harmful algal blooms (HABs) have devastating impacts on both marine and human health. Monitoring and predicting HAB events is crucial in improving the ability to mitigate their effects. One example of a HAB causing species is <em>Karenia brevis</em> (Figure 1), a toxic dinoflagellate contributing to red tide bloom events on the West Florida Shelf (WFS). What makes <em>K. brevis</em> of interest is the brevotoxins they produce during HAB events (Pierce & Henry, 2008). Shellfish  harvested and consumed from brevotoxin produced by <em>K. brevis</em> infested waters can result in oceanic and human mortalities (Kirkpatrick et al., 2004). Wave actions of <em>K. brevis</em> HABs around beach areas has also resulted in documented cases of brevotoxins aerosolized and  ingested via breathing (Fleming et al., 2005). The lethal toxicity of the brevotoxins produced as well as the documented prolific growth results in <em>K. brevis</em> as a designated prominent HAB species at the WFS. Creating models to predict <em>K. brevis</em> HAB events is crucial in understanding what causes 
them and where they are likely to occur.</p>

## **Purpose**

<p> This capstone project utilizes supervised machine 
learning (MLP Classifier from the <em>scikitlearn</em> toolkit) to classify <em>K. brevis</em> bloom occurences on the WFS in a 2019 cruise (Confesor et al, 2022). Cell counts will be used as a measure of bloom formation, with the target variable specifically as <em>K. brevis</em> cells counted per liter. A bloom for the purposes of this model is defined cell counts above 50 per Liter (cells/L > 50). A classifer model is necessary as <em>K. brevis</em> HAB events have changed over the past decade, and we do not have a clear hypothesis as to what causes these blooms to occur yet. </p>

## **Data Access**
* See [Confesor_DataAccess.md](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_DataAccess.md) for access & more details.

 * The target variable consists of <em>K. brevis</em> cell counts taken by the Fish and Wildlife Research Institute (FWRI) over 2015-2023 around the coasts of Florida. This dataset contains DateTime, Latitude, Longitude, Temperature, Salinity, and cell count data for each sample taken, with some samples having incomplete parameters. Currently, it has over 60,000 samples that span from 2015 through 2020 with some salinity and temperature data missing, as well as no nutrient data available to the public. 
 * Instead, other dataset variables such as nitrate, phosphate, and silica were accessed from the GLORYS12V1 (https://tinyurl.com/uvcxw8xt, 0.083° × 0.083° spatial resolution) as well as the Global ocean biogeochemistry hindcast
(https://tinyurl.com/yc79ycck, 0.25° × 0.25° spatial resolution) to replace missing values in the FWRI dataset. These CMEM datasets have been taken since 1993 and cover the time and geographic range that the <em>K. brevis</em> cell counts were taken up until 2020. This dataset is in the form of a NetCDF (.nc) file, where variables will  have to be extracted on the basis of the FWRI parameters. 
* The Multilayer Perceptron (MLP) Classifier from the <em> scikitlearn </em> package was used for model training and testing, where <em> K.brevis </em> bloom conditions were predicted in a 2019 WFS cruise (Confesor et al, 2022). </p>

## **Package Requirements**
*  Python v3.11.2 is required.
* Packages & versions can be accessed in the
[ConfesorCapstoneEnv.yaml](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/ConfesorCapstoneEnv.yaml) file.


## **Pipeline**

|1. Data Cleaning|                                                                             2. Exploratory Data Anlaysis                                                                              |                                                                       3. MLP Classifer Model                                                                       |                                                                                                                                                             |
|:-----------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|[Confesor_DataCleanupMerge.ipynb](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_DataCleanupMerge.ipynb)|              [Confesor_EDA.ipynb](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_EDA.ipynb)               |  [Confesor_MLPClassifier.ipynb](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_MLPClassifier.ipynb)   |


(1) Data Cleaning: [Confesor_DataCleanupMerge.ipynb](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_DataCleanupMerge.ipynb)
* FWRI & CMEM Database Access 
* Raw data collection on WFS 2019 Cruise: low-through hydrographic system, trace metal-clean nutrient protocol.
* Data Cleaning/ Indexing: Create [Confesor_Functions.py](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_Functions.py) to carry out file downloads, indexing/cleaning, assign bloom vs no bloom ID, FWRI sample match ups to CMEMs data, removing NaNs, and creating new combined FWRI & CMEMs .csv file. 

(2) Exploratory Data Analysis: [Confesor_EDA.ipynb](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_EDA.ipynb)
* On combined data set, get data types, get standard deviation, mean, min, and max, plot data parameters by sample site, T-S diagram, and Spearman's Correlation (non-parametric testing)

(3) MLP Classifier Model: [Confesor_MLPClassifier.ipynb](https://github.com/kconf001/MLP_Classifier_KbrevisHABs/blob/main/Confesor_MLPClassifier.ipynb)
* Supervised machine learning: Plot parameters,split train & test data, loop through layer and neuron combinations, choose combo with best accuracy & f1-scores, create MLP Classifier model, try on WFS2019 cruise data, classify stations as bloom/no bloom conditions, and cross-validate with Kfold package.

## **Impact**
<p>
How HAB-associated species like K. brevis are induced is important for monitoring the onset and severity of such blooms. Currently, there is no single hypothesis explaining the occurrences of <em>K. brevis</em> HABs along the WFS. My research focuses on one of the hypothesis where nitrogen (N2) fixation, as a source of bioavailable N, is a primary contributor to growth and maintenance of these blooms (Vargo, 2009). The specific N2-fixation source remains to be elucidated but I suspect that the new N input from <em>Trichodesmium</em>, a diazotrophic cyanobacteria, is what contributes to <em>K. brevis</em> HAB occurrences. In my dissertation, I hope to be able to create a model that classifies/predicts <em>K. brevis</em> blooms via the listed variables above as well as N2-fixation rates from <em>Trichodesmium</em> and/or <em>Trichodesmium</em> associated variables. </p>

## **Future Directions**

* Add PCA to EDA pipeline
* Determine accuracy/standard deviation of CMEMs matchups to FWRI data
* MLP Model with different parameters (removing PO4, add <em>Trichodesmium</em> related variables)
* Constrain georaphical boundaries (only to WFS area)
* Add seasonal categories (Spring, Summer, Fall, & Winter)

## **References**
Confesor, K. A., Selden, C. R., Powell, K. E., Donahue, L. A., Mellett, T., Caprara, S., Knapp, A. N., Buck, K. N., &amp; Chappell, P. D. (2022). Defining the realized niche of the two major clades of Trichodesmium: A Study on the west florida shelf. Frontiers in Marine Science, 9. https://doi.org/10.3389/fmars.2022.821655 

Fleming, E., Backer, C., & Baden, G. (2005). Overview of Aerosolized Florida Red Tide Toxins: Exposures and Effects. Environmental Health Perspectives, 113(5), 618-620. https://doi.org/10.1289/ehp.7501 

Hansen, N., Larsen, J., & Moestrup, Ø. (2000). Phylogeny of some of the major genera of dinoflagellates based on ultrastructure and partial LSU rDNA sequence data, including the erection of three new genera of unarmoured dinoflagellates. Phycologia, 39, 302-317. 

Kirkpatrick, B., Fleming, L. E., Squicciarini, D., Backer, L. C., Clark, R., Abraham, W., Benson, J., Cheng, Y. S., Johnson, D., Pierce, R., Zaias, J., Bossart, G. D., & Baden, D. G. (2004). Literature review of Florida red tide: implications for human health effects. Harmful Algae, 3(2), 99-115. https://doi.org/https://doi.org/10.1016/j.hal.2003.08.005 

Pierce, R. H., & Henry, M. S. (2008). Harmful algal toxins of the Florida red tide (Karenia brevis): natural chemical stressors in South Florida coastal ecosystems. Ecotoxicology, 17(7), 623-631. https://doi.org/10.1007/s10646-008-0241-x 

Vargo, G. A. (2009). A brief summary of the physiology and ecology of Karenia brevis Davis (G. Hansen and Moestrup comb. nov.) red tides on the West Florida Shelf and of hypotheses posed for their initiation, growth, maintenance, and termination. Harmful Algae, 8(4), 573-584. https://doi.org/https://doi.org/10.1016/j.hal.2008.11.002
