clear all;
clc;
clf;
close all

%The country we use as country A is Denmark

% we follow the same steps as in the excersize 1 to import the data

%we import the data
data = readtable('ECDC-7Days-Testing.xlsx');
countries_wanted = readtable('EuropeanCountries.xlsx');

%from the imported table we take the data we need
j = 1;
country = data.country;
positive_rate = data.positivity_rate;
year_week = data.year_week;
level = data.level;
c_w = countries_wanted.Country;

%We take the 2020-week50 data for all the countries that have them
for i = 1:11755
    if strcmp(year_week(i),'2020-W50') && strcmp(level(i),'national')
        W50_2020_c(j,1) = country(i);
        W50_2020_pr(j,1) = positive_rate(i);
        j = j+1;
    end
end    

j=1;
%We take the 2020-week50 data for all the countries that have them
for i = 1:11755
    if strcmp(year_week(i),'2021-W50') && strcmp(level(i),'national')
        W50_2021_c(j,1) = country(i);
        W50_2021_pr(j,1) = positive_rate(i);
        j = j+1;
    end
end   

%we remove the countries we don't want to take into account
test_1 = ismember(W50_2020_c,c_w);
test_2 = ismember(W50_2021_c,c_w);

for i=1:size(test_1,1)
    if test_1(i)==0
        W50_2020_c(i) = [];
        W50_2020_pr(i) = [];
    end
end
%for the week50 of 2020 three of the countries we need don't have data
%so we overlook these values from the histogram

for i=1:size(test_2,1)
    if test_2(i)==0
        W50_2021_c(i) = [];
        W50_2021_pr(i) = [];
    end
end
%for the week50 pg 2021 all 25 countries present data

% We calculate the Kolmogorov-Smirnov statistic and the h value. The null
% hypothesis is that the 2 samples are from the same distribution. I h=0 we
% do not reject the null hypothesis. We calculate the K-S statistic firt
% for the initial sample and store the values in 2 variables called
% h_sample and ks_sample. then we do the ransomisation M times and
% calculate the values in 2 vectors called h_rand and ks_rand

[h_sample,p_sample,ks_sample] = kstest2(W50_2020_pr,W50_2021_pr);

% we import hte data in 2 new vectors for simplicity
x = W50_2020_pr;
y = W50_2021_pr;

n = size(W50_2020_pr,1);
m = size(W50_2021_pr,1);
M = 1000;

h_rand = zeros(M,1);
ks_rand = zeros(M,1);

for i=1:M
    z = [x;y];
    r = randperm(n+m);
    z_rand = z(r);
    x = z_rand(1:n);
    y = z_rand(n+1:n+m);
    [h,p,ks] = kstest2(x,y);
    h_rand(i,1) = h;
    ks_rand(i,1) = ks;
end    
    
% We sort he ks statistic vector in ascending order to  check if the ks 
% statiscit of the initial sample is between %M(a/2) and M(1-a/2) 
%percentage points. H0 is rejected if t isn't between those percentage 
%points 

ks_sorted = sort(ks_rand);

a=0.05;
d1 = round(M*a/2);
d2 = round(M*(1-a/2));

% the confidence interval
de_min = ks_sorted(d1);
de_max = ks_sorted(d2);

disp('Kolmogorov-Smirnov statistic check')

if ks_sample>=de_min && ks_sample<=de_max
    fprintf('For a=%f \n',a);
    fprintf('ks statistic = %f is inside the confidence interval (%f,%f)\n',ks_sample,de_min,de_max);
    fprintf('We do not reject the H0 hypothesis\n');
    fprintf('The positivity rates for the 2 years could be from the same distribution');
else
    fprintf('For a=%f \n',a);
    fprintf('ks statistic = %f is not inside the confidence interval (%f,%f)\n',ks_sample,de_min,de_max);
    fprintf('We reject the H0 hypothesis\n');
    fprintf('The positivity rates for the 2 years could not be from the same distribution');
end

   











