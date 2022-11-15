clear all;
clc;
clf;
close all;

format long
%The country we use as country A is Denmark

%we import the data
data = readtable('ECDC-7Days-Testing.xlsx');

%from the imported table we take the data we need
country = data.country;
positive_rate = data.positivity_rate;
year_week = data.year_week;
level = data.level;

%we call the functions for the 5 countries,  the 5 countries we use are
%Cyprus, Czechia, Denmark, Estonia, Finland
ChoraitiSideriExe4Fun1('Cyprus',country,positive_rate,year_week,level)
ChoraitiSideriExe4Fun1('Czechia',country,positive_rate,year_week,level)
ChoraitiSideriExe4Fun1('Denmark',country,positive_rate,year_week,level)
ChoraitiSideriExe4Fun1('Estonia',country,positive_rate,year_week,level)
ChoraitiSideriExe4Fun1('Finland',country,positive_rate,year_week,level)

disp('We see that the positivity rates fo the last 2 months of 2020 and 2020')
disp('do differ significally for Cyprus, Czechia, Estonia and Finland, as a')
disp('result of both checks, parametric and non parametric')
disp('For Denmark we see that the parametric check shows significant difference')
disp('but the non parametric shows non significant, something we can observe')
disp('also in the plots of Denmark')
disp('The non parametric check shows the correct result because we do not make')
disp('any assumptions for the distribution of the data, it works for every distribution')
disp('To do the parametic control we assumed that the data follow a normal distribution')
