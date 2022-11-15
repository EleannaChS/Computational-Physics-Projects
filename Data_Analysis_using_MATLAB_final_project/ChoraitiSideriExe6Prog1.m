clear all;
clc;
clf;
close all

%The country we use as country A is Denmark
%The 2 European countries we use are 'Cyprus' and 'Czechia' as they had
%the bigest correlation coefficients with Greece as shown in excersize 5

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

%We take all the data for the year_week and the positivity rate for the 2
%countries we want
n=1;
for k = 5:6
    
    for i = 1:size(country,1)
        if strcmp(country(i),c_w(k)) && strcmp(level(i),'national')
            pr_countries(j,n) = positive_rate(i);
            yw_countries(j,n) = year_week(i);
            j = j+1; 
        end   
    end
    j = 1;
    n = n+1;
end

n=1;
%From the data we take only the weeks from 2021-W38 to 2021-W50
for k = 1:2
    for i = 1:size(yw_countries,1)
        if strcmp(yw_countries(i,k),'2021-W38')
            for j=1:13
                pr_c(j,n) = pr_countries(i,k);
                i=i+1;
            end    
        break;    
        end
    end
    n=n+1;
end
   
%we take the positivity rates of greece
j=1;
for i = 1:size(country,1)
    if strcmp(country(i),'Greece') && strcmp(level(i),'national')
        pr_gr(j) = positive_rate(i);
        yw_gr(j) = year_week(i);
        j = j+1; 
    end   
end

%from the data we take only those for weeks 2021-W38 to 2021-W50
for i = 1:size(yw_gr,2)
    if strcmp(yw_gr(i),'2021-W38')
        for j=1:13
            pr_g(j) = pr_gr(i);
            i=i+1;
        end    
    break;    
    end
end

%we calculate the correlation coefficient matrix for every country with
%greece. Then we store the correlation coefficient Pearson for every 
%country in a vector r_c.
for i=1:2
    r = corrcoef(pr_c(:,i),pr_g);
    r_c(1,i) = r(1,2);
end 

A = pr_g';
B = pr_c(:,2);
C = pr_c(:,1);

AB = [A B];
AC = [A C];

%We unite and randomize the sample and then we take n elements randomly
%We repeat this M times and plot a histogam. 

n = size(B,1);
M = 1000;

rc_rand = zeros(M,1);


for i=1:M
    z = [AB;AC];
    r = randperm(2*n,n)';
    z_rand(:,1) = z(r,1);
    z_rand(:,2) = z(r,2);
    x(:,1) = z_rand(1:n,1);
    x(:,2) = z_rand(1:n,2);
    r = corrcoef(x(:,1),x(:,2));
    rc_rand(i,1) = r(1,2);
end 
     
% We sort he coreletion coefficients vector in ascending order to 
%check if the rhos of the sample are between %M(a/2) and M(1-a/2) 
%percentage points. 

rc_sorted = sort(rc_rand(:,1));


a=0.05;
d1 = round(M*a/2);
d2 = round(M*(1-a/2));

% the confidence intervals
de_minAB = rc_sorted(d1);
de_maxAB = rc_sorted(d2);

figure 
histogram(rc_rand,'Normalization','pdf')
title('Randomized correlation coefficients')
hold on;
line([r_c(1), r_c(1)], ylim, 'LineWidth', 1, 'Color', 'r');
line([r_c(2), r_c(2)], ylim, 'LineWidth', 1, 'Color', 'g');
line([de_minAB, de_minAB], ylim, 'LineWidth', 2, 'Color', 'm');
line([de_maxAB, de_maxAB], ylim, 'LineWidth', 2, 'Color', 'm');
legend('rand rc', 'rcAC', 'rcAB', 'CI', 'CI')


