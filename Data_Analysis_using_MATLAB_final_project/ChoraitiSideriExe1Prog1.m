clear all;
clc;
clf;
close all
%The country we use as country A is Denmark

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

%We plot the histogramms
figure(1)
histogram(W50_2020_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('Positive rate for W50\_2020 for 22 countries')

figure(2)
histogram(W50_2021_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('Positive rate for W50\_2021 for 25 countries')    

%We test 4 different distributions on every histogramm to choose which
%one fits better. While solving he excersise we tried more distributions,
%we present here the 4 more accurate
figure(3)
histogram(W50_2020_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('probability distribution fitting-W50\_2020')
PD_2020 = fitdist(W50_2020_pr,'normal');    
x_2020 = 0:1:45;
y_2020 = pdf(PD_2020,x_2020);
plot(x_2020,y_2020)
PD_2020 = fitdist(W50_2020_pr,'exponential');
y_2020 = pdf(PD_2020,x_2020);
plot(x_2020,y_2020)
PD_2020 = fitdist(W50_2020_pr,'gamma');
y_2020 = pdf(PD_2020,x_2020);
plot(x_2020,y_2020)
PD_2020 = fitdist(W50_2020_pr,'hn');
y_2020 = pdf(PD_2020,x_2020);
plot(x_2020,y_2020)
legend('data','normal','exp','gamma','half-normal')

figure(4)
histogram(W50_2021_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('probability distribution fitting-W50\_2021')
PD_2021 = fitdist(W50_2021_pr,'normal');    
x_2021 = 0:1:25;
y_2021 = pdf(PD_2021,x_2021);
plot(x_2021,y_2021)
PD_2021 = fitdist(W50_2021_pr,'exponential');    
y_2021 = pdf(PD_2021,x_2021);
plot(x_2021,y_2021)
PD_2021 = fitdist(W50_2021_pr,'gamma');    
y_2021 = pdf(PD_2021,x_2021);
plot(x_2021,y_2021)
PD_2021 = fitdist(W50_2021_pr,'hn');    
y_2021 = pdf(PD_2021,x_2021);
plot(x_2021,y_2021)
legend('data','normal','exp','gamma','half-normal')

%We choose the exponential distribution for the week 50 of 2020 and also 
%the exponential distribution for the week 50 of 2021
%We plot the results and print the parameters of the distributions

figure(5)
histogram(W50_2020_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('Exponential Distribution-W50\_2020')
PD_2020 = fitdist(W50_2020_pr,'exponential');
y_2020 = pdf(PD_2020,x_2020);
plot(x_2020,y_2020)

figure(6)
histogram(W50_2021_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('Exponential Distribution-W50\_2021')
PD_2021 = fitdist(W50_2021_pr,'exponential');    
y_2021 = pdf(PD_2021,x_2021);
plot(x_2021,y_2021)

disp('For the 50th week of 2020 the positive rate follows:')
disp(PD_2020)


disp('For the 50th week of 2021 the positive rate follows:')
disp(PD_2021)

%To check if we can describe the 2 weeks with the same distribution we plot
%at every histogram both the distributions

figure(7)
histogram(W50_2020_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('W50\_2020')
plot(x_2020,y_2020)
plot(x_2021,y_2021)
legend('data','exponential 2020', 'exponential 2021')

figure(8)
histogram(W50_2021_pr,6,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title('W50\_2021')
plot(x_2020,y_2020)
plot(x_2021,y_2021)
legend('data','exponential 2020', 'exponential 2021')

%If we observe the results we can say that we might be able to describe 
%bot weeks with te same distribution






