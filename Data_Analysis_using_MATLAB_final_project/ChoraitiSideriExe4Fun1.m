function  ChoraitiSideriExe4Fun1(cw,country,positive_rate,year_week,level)
format long
%We create a function that does the check in order to be able to call it
%for many countries on the main program. Each time we give the funcion
%the name of the country (cw) and it does the check for this country

j=1;
%We take the positivity rates and the weeks for the country
for i = 1:size(country,1)
    if strcmp(country(i),cw) && strcmp(level(i),'national')
        yw_c(j,1) = year_week(i);
        pr_c(j,1) = positive_rate(i);
        j = j+1;
    end
end   

%From the tables we take the weeks we need and store the positivity rates
%in 2 arrays, one for each year, called pr_c_2020 and pr_c_2021
for i = 1:size(yw_c,1)
    if strcmp(yw_c(i),'2020-W42')
        for j=1:9
            pr_c_2020(j) = pr_c(i);
            i=i+1;
        end    
        break;    
    elseif strcmp(yw_c(i),'2020-W43') %if w42 doesn't exist we use the next
        for j=1:9
            pr_c_2020(j) = pr_c(i);
            i=i+1;
        end    
        break;    
    end
end  

for i = 1:size(yw_c,1)
    if strcmp(yw_c(i),'2021-W42')
        for j=1:9
            pr_c_2021(j) = pr_c(i);
            i=i+1;
        end    
        break;      
    end
end  

%plot of the results
x=1:size(pr_c_2020,2);
figure
subplot(1,3,1)
plot(x,pr_c_2020,'.-')
hold on
plot(x,pr_c_2021,'.-')
title(cw)
xlabel('Weeks')
ylabel('positivity rate')
legend('2020','2021','Location','Best')


%We plot the histogramms 
nbins = round(sqrt(size(pr_c_2020,2)));

subplot(1,3,2)
histogram(pr_c_2020,nbins,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title(cw)
legend('2020','Location','Best')

subplot(1,3,3)
histogram(pr_c_2021,nbins,'normalization','pdf')
hold on
xlabel('positive rate')
ylabel('pdf')
title(cw)
legend('2021','Location','Best')

%Parametric check. We calculate the confidence interval of every 
%mean(positivity rate)and check if every mean is inside the other's 
%confidence interval.

x = pr_c_2020;
y = pr_c_2021;

n = size(pr_c_2020,2);

a=0.05;

pr_2020 = mean(x);
pr_2021 = mean(y);

s_2020 = sqrt(cov(x));
s_2021 = sqrt(cov(y));

t = tinv(1-a/2,n-1);
vl_2020 = pr_2020 - t*s_2020/sqrt(n);
vu_2020 = pr_2020 + t*s_2020/sqrt(n);
vl_2021 = pr_2021 - t*s_2021/sqrt(n);
vu_2021 = pr_2021 + t*s_2021/sqrt(n);

disp(cw)

disp('Parametric check')

fprintf('For a=%f \n',a);

fprintf('mean pr_2020 = %f and its confidence interval (%f,%f)\n',pr_2020,vl_2020,vu_2020);
fprintf('mean pr_2021 = %f and its confidence interval (%f,%f)\n\n',pr_2021,vl_2021,vu_2021);

if pr_2021>=vl_2020 && pr_2021<=vu_2020 && pr_2020>=vl_2021 && pr_2020<=vu_2021 
    fprintf('mean pr_2020 = %f is inside the confidence interval of 2021 (%f,%f)\n',pr_2020,vl_2021,vu_2021);
    fprintf('mean pr_2021 = %f is inside the confidence interval of 2020 (%f,%f)\n',pr_2021,vl_2020,vu_2020);
    fprintf('We do not reject the H0 hypothesis\n');
    fprintf('The positivity rates for the 2 years do not have significant differencies\n\n');
else
    fprintf('The mean positive rates are not both inside one anothers CI\n');
    fprintf('We reject the H0 hypothesis\n');
    fprintf('The positivity rates for the 2 years have significant differencies\n\n');
end

%Randomisation check

M = 1000;

pr_rand_2020 = zeros(M,1);
pr_rand_2021 = zeros(M,1);


for i=1:M
    z = [x;y];
    r = randperm(2*n);
    z_rand = z(r);
    x = z_rand(1:n);
    y = z_rand(n+1:2*n);
    pr_2020_r = mean(x);
    pr_2021_r = mean(y);
    pr_rand_2020(i,1) = pr_2020_r;
    pr_rand_2021(i,1) = pr_2021_r;
end    
    
% We sort the pr_rand vectors in ascending order to  check if the pr 
% for each year ff the initial sample is between %M(a/2) and M(1-a/2) 
%percentage points. H0 is rejected if t isn't between those percentage 
%points 

pr_sorted_2020 = sort(pr_rand_2020);
pr_sorted_2021 = sort(pr_rand_2021);

d1 = round(M*a/2);
d2 = round(M*(1-a/2));

% the confidence intervals
de_min_2020 = pr_sorted_2020(d1);
de_max_2020 = pr_sorted_2020(d2);

de_min_2021 = pr_sorted_2021(d1);
de_max_2021 = pr_sorted_2021(d2);

disp('Randomisation check')


fprintf('confidence interval of pr_2020 (%f,%f)\n',de_min_2020,de_max_2020);
fprintf('confidence interval of pr_2021 (%f,%f)\n\n',de_min_2021,de_max_2021);


if pr_2020>=de_min_2020 && pr_2020<=de_max_2020 && pr_2021>=de_min_2021 && pr_2021<=de_max_2021
    fprintf('mean pr_2020 = %f is inside the confidence interval\n',pr_2020);
    fprintf('mean pr_2021 = %f is inside the confidence interval\n',pr_2021);
    fprintf('We do not reject the H0 hypothesis\n');
    fprintf('The positivity rates for the 2 years do not have significant differencies\n\n');
else
    fprintf('The mean positive rates are not both inside the CIs\n');
    fprintf('We reject the H0 hypothesis\n');
    fprintf('The positivity rates for the 2 years have significant differencies\n\n');
end
disp('-----------------------------------------------------------------------')
end
