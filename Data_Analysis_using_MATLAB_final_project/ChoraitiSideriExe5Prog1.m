clear all;
clc;
clf;
close all
%The country we use as country A is Denmark
%The 5 European countries we use are Cyprus, Czechia, Denmark, Estonia,
%Finland
 
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

%We take all the data for the year_week and the positivity rate for the 5
%countries we want
n=1;
for k = 5:9
    
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
for k = 1:5
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
   
%plot of the results
x=1:size(pr_c,1);
figure(1)
plot(x,pr_c,'.-')
title('Positivity rate for the 5 countries')
xlabel('Weeks')
ylabel('positivity rate')
legend('Cyprus','Czechia', 'Denmark', 'Estonia', 'Finland','Location','Best')

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
for i=1:5
    r = corrcoef(pr_c(:,i),pr_g);
    r_c(i,1) = r(1,2);
end    

disp('The correlation coefficients Pearson for the coutries: ')
disp(c_w(5:9))
disp('against Greece are:')
disp(r_c)

%plot of the results
x=1:size(pr_c,1);
figure(2)
title('Positivity rate comparison')
for i=1:5
    subplot(2,3,i)
    plot(x,pr_c(:,i),'.-')
    hold on
    plot(x,pr_g,'.-')
    xlabel('Weeks')
    ylabel('positivity rate')
    title(r_c(i))
    legend('Country','Greece','Location','Best')
    text(2,max(pr_c(:,i)),c_w(4+i))
end

%Parametric Control
n = size(pr_g,2);
%We use the Fisher transformation to calculate the parametric confidence 
%interval (1-a)%

%for a =0.05
a5 = 0.05;
zV = 0.5*log((1+r_c)./(1-r_c));
zcrit_5 = norminv(1-a5/2);
zsd_5 = sqrt(1/(n-3));
zlV_5 = zV-zcrit_5*zsd_5;
zuV_5 = zV+zcrit_5*zsd_5;
rlV_5 = (exp(2*zlV_5)-1)./(exp(2*zlV_5)+1);
ruV_5 = (exp(2*zuV_5)-1)./(exp(2*zuV_5)+1);

%for a=0.01
a1 = 0.01;
zcrit_1 = norminv(1-a1/2);
zsd_1 = sqrt(1/(n-3));
zlV_1 = zV-zcrit_1*zsd_1;
zuV_1 = zV+zcrit_1*zsd_1;
rlV_1 = (exp(2*zlV_1)-1)./(exp(2*zlV_1)+1);
ruV_1 = (exp(2*zuV_1)-1)./(exp(2*zuV_1)+1);

%we calculate the t statistic for the H0 case that r=0
t=r_c.*sqrt((n-2)./(1-r_c.^2));
%We calculate the p-value. The p value is the smallest value of a giving
%a rejection of H0 
p = 2.*(1-tcdf(abs(t),n-2));

disp('PARAMETRIC CONTROL')
disp('The p-value values are:')
disp(p)

for i=1:size(p)
    if p(i) <= a5
        fprintf('For a=%f \n',a5);
        fprintf('p value=%f shows statistically significant correlation \n',p(i));
        fprintf('This is the p value for the country: \n');
        disp(c_w(4+i))
    end
    if p(i) <= a1
        fprintf('For a=%f \n',a1);
        fprintf('p value=%f shows statistically significant correlation \n',p(i));
        fprintf('This is the p value for the country: \n');
        disp(c_w(4+i))
    end
end    

%Non parametric control
%We randomize L times the positivity rate of greece and find the
%correlation coefficient which we store in the r_c_rand.Every column
%represents a differenl randomized sample
L = 100;
for k=1:L
    r_rand = randperm(n);
    pr_g_rand = pr_g(r_rand);
    for i=1:5
        rho_rand = corrcoef(pr_c(:,i),pr_g_rand);
        r_c_rand(i,k) = rho_rand(1,2);        
    end 
    %we calculate the t-statistic for the H0 case that r=0, each line
    %represents a country and each column a randomized repeat
    t_rand(:,k)=r_c_rand(:,k).*sqrt((n-2)./(1-r_c_rand(:,k).^2));
end

%We sort each line in ascending order
for i=1:5
    t_sorted(i,:) = sort(t_rand(i,:));
end    

%we need to check if the t statiscit of the initial sample is between
%L(a/2) and L(1-a/2) percentage points. H0 is rejected if t isn't between
%those percentage points

%for a = 0.05
a=0.05;
d1 = round(L*a/2);
d2 = round(L*(1-a/2));

% the confidence intervals
de_min = t_sorted(:,d1);
de_max = t_sorted(:,d2);

disp('NON PARAMETRIC CONTROL')
for i=1:size(de_min)
    if not(t(i)>de_min(i) && t(i)<de_max(i))
        fprintf('For a=%f \n',a);
        fprintf('t statistic =%f shows statistically significant correlation \n',t(i));
        fprintf('This refers to the country: \n');
        disp(c_w(4+i))
    end
end    

%for a = 0.01
a=0.01;
d1 = round(L*a/2);
d2 = round(L*(1-a/2));

% the confidence intervals
de_min = t_sorted(:,d1);
de_max = t_sorted(:,d2);

for i=1:size(de_min)
    if not(t(i)>de_min(i) && t(i)<de_max(i))
        fprintf('For a=%f \n',a);
        fprintf('t statistic =%f shows statistically significant correlation \n',t(i));
        fprintf('This refers to the country: \n');
        disp(c_w(4+i))
    end
end    

disp('We observe that statistically significant correlation exist only with Czechia')





