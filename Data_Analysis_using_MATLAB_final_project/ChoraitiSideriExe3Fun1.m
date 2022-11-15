function [stat_shm,dif] = ChoraitiSideriExe3Fun1(pr_he_table,pr_eu)

a =0.05;
m=1000;

%bootstrap method
for i=1:m
    r = unidrnd(7,7,1);
    pr_b = pr_he_table(r);
    pr_m(i) = mean(pr_b);
end

pr_m_s = sort(pr_m);

d1 = round(m*a/2);
d2 = round(m*(1-a/2));

% the confidence interval
de_min = pr_m_s(d1);
de_max = pr_m_s(d2);

stat_shm = 0;

%if we have a statisticly significant diference we give stat_dhm the value
%1
if pr_eu<=de_min || pr_eu>=de_max
    stat_shm = 1;
end

%And we calculate the differenece
if stat_shm == 1
    dif = pr_eu - mean(pr_he_table);
else
    dif = 0;
end    
    
   