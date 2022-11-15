clear all;
clc;
clf;
close all
%The country we use as country A is Denmark

%Calculation of the European positivity rate
%we import the data
data = readtable('ECDC-7Days-Testing.xlsx');
countries_wanted = readtable('EuropeanCountries.xlsx');

%from the imported table we take the data we need
country = data.country;
positive_rate = data.positivity_rate;
year_week = data.year_week;
level = data.level;
c_w = countries_wanted.Country;

%We create a table containing all the weeks for whivh we will calculate
%the European weekly positive rate. We take the weeks that contain data 
%of Greece because we will compare with the Greece's positive rate later
j=1;
for i=1:size(country,1)
    if strcmp(country(i),'Greece') && strcmp(level(i),'national')
    all_weeks(j,1) = year_week(i);
    j=j+1;
    end
end 

%We calculate the positivity rate for each week of the array all_weeks
j=1;
for k=1:size(all_weeks,1)
    pr_eu=0;
    l=0;
    for i=1:size(country,1)
        %for an element of the array all_weeks (i.e. for a week) we take 
        %the national level positivity rate and after we sum all the values
        %we devide with the number of values to calculate the mean
        %positivity rate
        if strcmp(year_week(i),all_weeks(k)) && strcmp(level(i),'national')
            if not(isnan(positive_rate(i))) 
            pr_eu = pr_eu + positive_rate(i);
            l=l+1;
            end
        end
    end   
%we store the results in a table called pr_eu_table
pr_eu_table(j,1) = pr_eu/l;   
j=j+1;  
end 

%%Calculation of the Greek positivity rate for a given week
%we import the data for greece
greece = readtable('FullEodyData.xlsx');

%from the imported table we take the data we need
new_cases = greece.NewCases;
pcr_tests = greece.PCR_Tests;
rapid_tests = greece.Rapid_Tests;
weeks = greece.Week;

%we convert the nan values with zeros
new_cases(isnan(new_cases))=0;
pcr_tests(isnan(pcr_tests))=0;
rapid_tests(isnan(rapid_tests))=0;

c = 1;
%we choose 12 weeks based on the positivity rate of the country A. In our
%case we didn't choose the last week of the biggest positivity rate because
%the results had only significaly statistical differencies. To be able to
%observe all the cases we chose the third to last peak week of the
%positivity rate and backward. Fist week is 2021-W33 and last is 2021-W44
for e=78:89
    j = 1;
    %we chose a week and make a table of the positions of the 7 days on the
    %table with all the weeks
    for i=1:size(weeks)
        if strcmp(weeks(i),all_weeks(e))
            i_table(j,1) = i;
            j=j+1;
        end
    end 

    %we calculate the positivity rates for the 7 days of the week
    j=1;    
    for l=i_table(1):i_table(size(i_table))
        pcr = pcr_tests(l) - pcr_tests(l-1);
        rapid = rapid_tests(l) - rapid_tests(l-1);
        pr_he_table(j) = new_cases(l)*100/(rapid + pcr);  
        j=j+1;
    end  
    pr_he_week(c) = mean(pr_he_table);
    pr_eu_week(c) = pr_eu_table(e);
    % main programm
    % we call the function and store the 
    [stat_shm,dif] = ChoraitiSideriExe3Fun1(pr_he_table,pr_eu_table(e));
    stat_shm_table(c) = stat_shm;
    dif_table(c) = dif;
    c = c+1;
end    

%plot of the results
x=1:12;
figure(1)
plot(x,pr_he_week,'.-')
hold on
plot(x,pr_eu_week,'.-')
title('Weekly positivity rate for 12 weeks')
xlabel('Weeks')
ylabel('positivity rate')
xlim([0 13])

%The way we chose to show the statistically significant differencies is by
%ussing errobars. We represent the statistically significant differencies
%with vertical lines cinecting the two lines of the positivity rates
for i=1:size(dif_table,2)
    if dif_table(i)<0
        dif_table_neg(i) = dif_table(i);
        dif_table_pos(i) = 0;
    elseif dif_table(i)>0
        dif_table_neg(i) = 0;
        dif_table_pos(i) = dif_table(i);
    else
        dif_table_neg(i) = 0;
        dif_table_pos(i) = 0;
    end    
end        
errorbar(x,pr_eu_week,dif_table_pos,dif_table_neg)
legend('Greece','EU','statistically significant differencies','Location','Best')
